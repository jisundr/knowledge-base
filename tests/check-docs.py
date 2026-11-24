#!/usr/bin/env python3
"""Document checks for the vault (stdlib only, run by CI and locally).

Usage: python3 tests/check-docs.py
Exits non-zero if any check fails. Rules come from README.md and
.claude/commands/ingest.md.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["00 Inbox", "01 Topics", "02 Resources", "03 Playbooks", "04 Bots"]
TOPICS_INDEX = ROOT / "01 Topics" / "00 Index.md"
PLAYBOOKS_INDEX = ROOT / "03 Playbooks" / "00 Playbooks Index.md"
BOTS_INDEX = ROOT / "04 Bots" / "00 Bots Index.md"

WIKILINK = re.compile(r"!?\[\[([^\]]+)\]\]")
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")

errors: list[str] = []


def err(path: Path, msg: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def strip_code(text: str) -> str:
    return INLINE_CODE.sub("", FENCE.sub("", text))


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def body(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


notes = sorted(p for f in FOLDERS for p in (ROOT / f).rglob("*.md"))
all_files = [p for f in FOLDERS for p in (ROOT / f).rglob("*") if p.is_file()]
# Obsidian resolves [[Name]] by basename (notes without .md, attachments with extension)
# or by vault-relative path.
targets = set()
for p in all_files:
    rel = p.relative_to(ROOT).as_posix()
    targets |= {p.name, rel}
    if p.suffix == ".md":
        targets |= {p.stem, rel[:-3]}

seen_stems: dict[str, Path] = {}
for p in notes:
    if p.stem in seen_stems:
        err(p, f"duplicate note name (also {seen_stems[p.stem].relative_to(ROOT)}); wikilinks become ambiguous")
    seen_stems[p.stem] = p

for p in notes:
    text = p.read_text(encoding="utf-8")
    folder = p.relative_to(ROOT).parts[0]
    fm = frontmatter(text)

    # Frontmatter
    if fm is None:
        err(p, "missing YAML frontmatter")
        fm = {}
    elif "type" not in fm:
        err(p, "frontmatter has no 'type'")
    if fm and "tags" not in fm:
        err(p, "frontmatter has no 'tags'")

    kind = fm.get("type")
    if folder == "00 Inbox" and fm.get("status") != "inbox":
        err(p, "Inbox note must have 'status: inbox'")
    if folder == "01 Topics" and kind not in {"topic", "index"}:
        err(p, f"Topics note must be 'type: topic' (got {kind!r})")
    if folder == "03 Playbooks" and kind not in {"playbook", "index"}:
        err(p, f"Playbooks note must be 'type: playbook' (got {kind!r})")
    if folder == "04 Bots" and kind not in {"bot", "index"}:
        err(p, f"Bots note must be 'type: bot' (got {kind!r})")
    if folder == "02 Resources":
        if fm.get("status") != "reviewed":
            err(p, "Resource note must have 'status: reviewed'")
        if not re.match(r"^\d{14} ", p.name):
            err(p, "Resource filename must start with 'YYYYMMDDHHMMSS '")
        if not body(text).startswith("Sources:"):
            err(p, "Resource note body must start with a 'Sources:' block")

    # A heading title
    if not re.search(r"^# \S", body(text), re.M) and folder != "02 Resources":
        err(p, "missing '# Title' heading")

    # Links
    clean = strip_code(text)
    for m in WIKILINK.finditer(clean):
        target = m.group(1).split("|")[0].split("#")[0].strip()
        if target and target not in targets:
            err(p, f"broken wikilink [[{m.group(1)}]]")
    for m in MD_LINK.finditer(clean):
        url = m.group(1)
        if not re.match(r"^[a-z]+:", url) and not url.startswith("#"):
            err(p, f"markdown link to local file '{url}'; use [[wikilinks]] between notes")


def linked(index: Path) -> set[str]:
    return {
        m.group(1).split("|")[0].split("#")[0].strip().split("/")[-1]
        for m in WIKILINK.finditer(strip_code(index.read_text(encoding="utf-8")))
    }


# Every topic is listed in the Topics Index; every playbook in the Playbooks Index;
# every bot in the Bots Index.
for index, folder in [
    (TOPICS_INDEX, "01 Topics"),
    (PLAYBOOKS_INDEX, "03 Playbooks"),
    (BOTS_INDEX, "04 Bots"),
]:
    if not index.exists():
        errors.append(f"{index.relative_to(ROOT)}: index note missing")
        continue
    listed = linked(index)
    for p in (ROOT / folder).rglob("*.md"):
        if p != index and p.stem not in listed:
            err(p, f"not linked from [[{index.stem}]]")

if errors:
    print(f"{len(errors)} document check(s) failed:")
    for e in errors:
        print(f"  FAIL {e}")
    sys.exit(1)
print(f"ok   {len(notes)} notes checked, no problems")
