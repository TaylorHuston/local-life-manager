# Journal Template

## Location

Daily journals: `my-vault/02 Calendar/YYYY-MM-DD.md`
Template: `my-vault/09 System/Templates/Daily Template.md`

## Structure

```markdown
---
class: Daily
created: YYYY-MM-DD
---

# YYYY-MM-DD

<< [[YYYY-MM-DD|Yesterday]] | [[YYYY-MM-DD|Tomorrow]] >>

## Highlight

[Main focus for the day]

## What Did I Do?

- [Personal activities: errands, social, health, appointments]

## What Did I Work On?

- [Technical work: side projects, coding, GitHub commits]

## What Did I Study?

- [Learning sessions, courses, deliberate study]
```

## Sections

| Section | Content Type |
|---------|--------------|
| Highlight | One main focus/goal for the day |
| What Did I Do? | Personal: errands, social, health, appointments |
| What Did I Work On? | Technical: side projects, coding, GitHub work |
| What Did I Study? | Learning sessions, courses, deliberate study |

## GitHub Integration

Fetch commits for a date:
```bash
gh search commits --author=TaylorHuston --committer-date=YYYY-MM-DD
```

Summarize into meaningful bullets (not raw commit messages).

## Guidelines

- Use bulleted lists
- Keep entries concise
- Link to relevant notes where appropriate
