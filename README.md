# Knowledge Base

Personal Obsidian vault for capturing and organizing what I learn. Currently focused on AI engineering.

## Structure

| Folder | Purpose |
| --- | --- |
| `00 Inbox` | Raw captures (videos, articles, ideas) waiting for review |
| `01 Topics` | Atomic topic notes, linked to each other and to their sources |
| `02 Resources` | Reviewed source notes (`status: reviewed`), named `YYYYMMDDHHMMSS <title>.md` |
| `02 Resources/attachments` | Images and other files embedded in source notes (give them descriptive names) |

## Workflow

1. Capture a new note in `00 Inbox` with `status: inbox` in the frontmatter.
2. Review it, then pull concepts out into notes in `01 Topics` using `[[wikilinks]]`.
3. Set `status: reviewed` and move the source note to `02 Resources` with a `YYYYMMDDHHMMSS` filename prefix.

### Automate it

Run `/ingest <note name>` in Claude Code (or plain `/ingest` for everything in `00 Inbox`) to do steps 2 and 3. The command lives in `.claude/commands/ingest.md`.

## Tests

```bash
tests/test-ingest.sh            # static checks + live run of /ingest in a temp copy of the vault
tests/test-ingest.sh --static   # static checks only (no API calls)
```

## Start here

- [[AI Engineer Skill Stack]]
