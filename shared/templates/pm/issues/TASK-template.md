---
status: open  # open | in_progress | blocked | complete
created: "YYYY-MM-DD"
implements: ""  # e.g., "docs/specs/required-features.md#user-registration"
depends_on: []
---

<!--
TASK SCOPING: One TASK = One spec requirement line item

A TASK should be:
- Atomic: implements exactly one requirement
- Shippable: can be pushed to main independently
- Clear: updates one ⏳ → ✅ marker when complete

DON'T: "Implement Authentication" (too broad)
DO: "User registration endpoint" (one requirement)
-->

# TASK-###: [Title]

## Description

[What needs to be done - should map to one spec requirement]

## Implements

**Spec Requirement:** `[requirement text from spec]`

**Location:** [docs/specs/file.md#section](../../../spaces/[project]/docs/specs/file.md#section)

## Acceptance Criteria

- [ ] Spec requirement fulfilled
- [ ] Tests passing
- [ ] Can be deployed independently

## Context

[Background, relevant decisions, technical notes]

---

**Next**: Run `/plan ###` to create implementation phases
