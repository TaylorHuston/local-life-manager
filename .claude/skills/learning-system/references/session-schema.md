# Session Schema

## Session File Location

All session files are stored in `.claude/learning-sessions/`

## Index File

`.claude/learning-sessions/index.json` tracks all sessions:

```json
{
  "sessions": [
    { "id": "2026-01-11-001", "status": "completed" },
    { "id": "2026-01-12-001", "status": "active" }
  ]
}
```

## Session File Schema

Each session is stored as `.claude/learning-sessions/<id>.json`:

```json
{
  "id": "2026-01-12-001",
  "topic": "AWS Secrets Manager",
  "type": "teaching",
  "started": "2026-01-12T10:30:00Z",
  "ended": null,
  "status": "active",
  "entries": [],
  "summary": null
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Format: `YYYY-MM-DD-NNN` (date + sequence) |
| `topic` | string | What's being learned |
| `type` | string | `"teaching"` or `"review"` |
| `started` | ISO timestamp | When session began |
| `ended` | ISO timestamp | When session ended (null if active) |
| `status` | string | `"active"` or `"completed"` |
| `entries` | array | Learning entries (see entry-types.md) |
| `summary` | string | Brief summary when completed |

### Review Session Additional Fields

```json
{
  "type": "review",
  "retention_score": 85
}
```

## Learning Plan

`.claude/learning-sessions/learning-plan.json` tracks progress:

```json
{
  "domains": {
    "AWS": {
      "topics": {
        "RDS/Aurora": {
          "proficiency": "solid",
          "last_covered": "2026-01-11",
          "sessions": ["2026-01-11-001"]
        }
      }
    }
  },
  "queue": ["Next topic", "Another topic"],
  "review_intervals_days": {
    "basic": 7,
    "familiar": 14,
    "solid": 30,
    "expert": 90
  }
}
```

## Session ID Generation

1. Use today's date: `YYYY-MM-DD`
2. Check existing sessions for today in index.json
3. Increment sequence: `-001`, `-002`, etc.
