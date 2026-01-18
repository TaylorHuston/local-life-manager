---
idea: "TODO: Project Name"
document: "plan"
issue_ref: "TODO: ###"
issue_type: "task"  # task | bug | spike
status: "draft"  # draft | approved | in_progress | completed
created: "TODO: YYYY-MM-DD"
updated: "TODO: YYYY-MM-DD"
created_by: "human"  # human | ai
approved_by: ""
approved_at: ""
---

# Plan: [Issue Title]

## Overview

[Brief description of the implementation approach]

## Phases

### Phase 1: [Phase Name]

**Goal**: [What this phase achieves]

- [ ] 1.1 Step description
- [ ] 1.2 Step description
- [ ] 1.3 [CHECKPOINT] Verify [condition]

> **Commit**: "feat/fix: description"

### Phase 2: [Phase Name]

**Goal**: [What this phase achieves]

- [ ] 2.1 Step description
- [ ] 2.2 Step description
- [ ] 2.3 [CHECKPOINT] Verify [condition]

> **Commit**: "feat/fix: description"

### Phase 3: [Phase Name]

**Goal**: [What this phase achieves]

- [ ] 3.1 Step description
- [ ] 3.2 Final review
- [ ] 3.3 [CHECKPOINT] All criteria met

> **Commit**: "feat/fix: description"

## Checkpoint Legend

- `[CHECKPOINT]` - General verification point
- `[CHECKPOINT: tests_fail]` - TDD red phase (tests should fail)
- `[CHECKPOINT: tests_pass]` - TDD green phase (tests should pass)
- `[CHECKPOINT: review]` - Human review required before proceeding

## Notes

[Additional context, constraints, or decisions made during planning]

## Related

- Spec: [SPEC-###](../specs/SPEC-###-name.md)
- ADR: [docs/adr-name.md](../docs/adr-name.md)
