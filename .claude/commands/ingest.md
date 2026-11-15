---
description: Review an Inbox note, extract topic notes, and file it in Resources
argument-hint: [note name in 00 Inbox — omit to process all]
---

Run the vault workflow from README.md on `$ARGUMENTS` (if empty, every note in `00 Inbox` with `status: inbox`).

For each note:

1. **Read** the note in `00 Inbox`. Confirm frontmatter has `status: inbox`; if frontmatter is missing, add `type`, `status`, `created` (today), `tags`, and `source` where known.
2. **Extract concepts** into atomic notes in `01 Topics`:
   - First check existing topics (`01 Topics/`) — extend a matching note rather than duplicating it.
   - New topic notes use frontmatter `type: topic` and `tags: [...]`, a `# Title`, a short definition, and `[[wikilinks]]` to related topics.
   - Keep topics atomic: one concept per note, no copy-pasted source prose.
3. **Link back**: in the source note, add `See [[Topic]]` links to every topic created or updated. Add new topics to `[[AI Engineer Skill Stack]]` or other hub notes if they fit.
4. **File**: set `status: reviewed` and move the source note to `02 Resources` (use `git mv` if tracked). Keep the filename.
5. **Report**: list topics created/updated and where the source note ended up. Do not commit unless asked.

Rules: use Obsidian `[[wikilinks]]` only (no markdown links between notes), don't delete anything from the source note, and ask before overwriting any existing topic content.
