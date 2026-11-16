#!/usr/bin/env bash
# Tests the /ingest command end to end in a throwaway copy of the vault.
# Usage: tests/test-ingest.sh [--static]   (--static skips the live `claude` run)
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NOTE="TEST - Prompt Caching and RAG Basics"
FIXTURE="$ROOT/tests/fixtures/$NOTE.md"
CMD="$ROOT/.claude/commands/ingest.md"
pass=0; fail=0

ok()   { echo "  ok   $1"; pass=$((pass+1)); }
bad()  { echo "  FAIL $1"; fail=$((fail+1)); }
check() { local desc="$1"; shift; if "$@" >/dev/null 2>&1; then ok "$desc"; else bad "$desc"; fi; }

echo "== static checks"
check "command file exists"            test -f "$CMD"
check "command has description"        grep -q '^description:' "$CMD"
check "command references README flow" grep -q 'README.md' "$CMD"
check "fixture exists"                 test -f "$FIXTURE"
check "fixture has status: inbox"      grep -q '^status: inbox' "$FIXTURE"
for d in "00 Inbox" "01 Topics" "02 Resources"; do
  check "folder '$d' exists" test -d "$ROOT/$d"
done

if [[ "${1:-}" == "--static" ]]; then
  echo; echo "passed=$pass failed=$fail"; [[ $fail -eq 0 ]]; exit
fi

command -v claude >/dev/null || { echo "claude CLI not found"; exit 2; }

echo "== live run in temp vault"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
rsync -a --exclude .git --exclude tests "$ROOT/" "$TMP/"
cp "$FIXTURE" "$TMP/00 Inbox/"
topics_before=$(ls "$TMP/01 Topics" | wc -l | tr -d ' ')
rag_before=$(wc -c < "$TMP/01 Topics/Retrieval-Augmented Generation (RAG).md")

( cd "$TMP" && claude -p "/ingest $NOTE" \
    --permission-mode acceptEdits \
    --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Bash(mv:*)" "Bash(ls:*)" "Bash(date:*)" ) \
  > "$TMP/.claude-output.txt" 2>&1 || bad "claude exited non-zero"

RES=$(ls "$TMP/02 Resources"/[0-9]*" $NOTE.md" 2>/dev/null | head -1)
check "note left 00 Inbox"              test ! -e "$TMP/00 Inbox/$NOTE.md"
check "note now in 02 Resources"        test -f "$RES"
check "filename has datetime prefix"    sh -c "basename \"$RES\" | grep -Eq '^[0-9]{14} '"
check "status set to reviewed"          grep -q '^status: reviewed' "$RES"
check "source note has [[wikilinks]]"   grep -q '\[\[[^]]\+\]\]' "$RES"
check "source prose preserved"          grep -q 'Prompt caching stores' "$RES"
check "new topic count increased"       test "$(ls "$TMP/01 Topics" | wc -l | tr -d ' ')" -gt "$topics_before"
check "prompt-caching topic created"    sh -c "ls \"$TMP/01 Topics\" | grep -qi 'prompt cach'"
check "new topic has type: topic"       sh -c "grep -qli '^type: topic' \"$TMP/01 Topics\"/*[Cc]ach*"
check "RAG topic extended, not replaced" test "$(wc -c < "$TMP/01 Topics/Retrieval-Augmented Generation (RAG).md")" -ge "$rag_before"
check "no duplicate RAG topic"          test "$(ls "$TMP/01 Topics" | grep -ci 'retrieval')" -eq 1

echo; echo "passed=$pass failed=$fail"
[[ $fail -eq 0 ]] || { echo "--- claude output ---"; cat "$TMP/.claude-output.txt"; exit 1; }
