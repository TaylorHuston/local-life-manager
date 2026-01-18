---
name: workflows:new-project
description: "Workflow: New Project (Concept → First Commit)"
---

# Workflow: New Project

Take an idea from concept to first working implementation.

## Phase 1: Foundation (30-60 minutes)

### Step 1: Create Project Brief
```bash
/brief
```
Output: `ideas/[project]/README.md` + `project-brief.md`

### Step 2: Validate Documentation
```bash
/validate-idea
```

### Step 3: Get Critical Evaluation
```bash
/critique
```
**Decision point**:
- STRONG/PROMISING → Proceed
- NEEDS WORK → Address concerns
- RECONSIDER → Pivot or shelve

## Phase 2: Address Concerns (Variable)

### Step 4: Research Key Questions
```bash
/research "[concern from critique]"
```

## Phase 3: Planning (1-4 hours)

### Step 5: Define First Feature
```bash
/spec "MVP feature set"
```

### Step 6: Document Tech Stack Decision
```bash
/adr
```

### Step 7 (Optional): Create UI Mockups
```bash
/ui-design
```

## Phase 4: Implementation (Variable)

### Step 8: Create Work Item
```bash
/issue "Build MVP"
```

### Step 9: Plan Implementation Phases
```bash
/plan
```

### Step 10: Choose Implementation Mode

**Option A**: AI writes code (fastest)
```bash
/implement
```

**Option B**: You write with guidance
```bash
/advise
```

**Option C**: Learn while building
```bash
/teach
```

### Step 11: Track Progress
```bash
/worklog
```

## Phase 5: Quality & Completion (30-60 minutes)

### Step 12: Code Quality Check
```bash
/quality
```

### Step 13: Security Audit
```bash
/security-audit
```

### Step 14 (Optional): Verify Spec Implemented
```bash
/validate-spec
```

### Step 15: Complete and Merge
```bash
/complete
```

## Variations

### Lean Startup (Skip Some Steps)
```bash
/brief → /spec → /issue → /implement → /commit
```

### Research-Heavy (More Analysis)
```bash
/brief → /critique → /research → /research → /spec → /adr → /implement
```

### Learning-Focused (You Write Code)
```bash
/brief → /spec → /issue → /plan → /teach → /worklog → /quality
```
