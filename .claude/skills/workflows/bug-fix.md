---
name: workflows:bug-fix
description: "Workflow: Bug Fix"
---

# Workflow: Bug Fix

Systematically debug and fix an issue.

## Quick Reference

```bash
/troubleshoot → /issue → /plan → /implement → /quality → /commit
```

## Step-by-Step

### Step 1: Systematic Debugging
```bash
/troubleshoot
```
5-step loop: Reproduce → Hypothesize → Test → Identify → Plan Fix

### Step 2: Create Bug Work Item
```bash
/issue "Fix [bug description]"
```
AI auto-detects BUG type.

### Step 3: Plan the Fix
```bash
/plan
```
Phases: Reproduce test → Fix → Verify → Regression check

### Step 4: Implement the Fix
```bash
/implement
```
Or use `/advise` to write it yourself with guidance.

### Step 5: Quality Check
```bash
/quality
```

### Step 6: Commit the Fix
```bash
/commit
```

## Variations

### Quick Fix (Known Issue)
```bash
/issue "Fix [bug]" → /implement → /commit
```

### Critical Bug (Full Process)
```bash
/troubleshoot → /issue → /plan → /implement → /quality → /security-audit → /complete
```

## When to Use /complete Instead of /commit

**Use /commit**: Simple fix, low risk, not merging yet
**Use /complete**: Complex fix, security-related, ready to merge

## Testing Best Practices

Every bug fix should include:
1. Test that reproduces the bug (fails before fix)
2. Test passes after fix
3. Regression tests for similar edge cases

## Post-Fix Checklist

- [ ] Added test that would catch this in future?
- [ ] Checked for similar bugs elsewhere?
- [ ] Documented why bug occurred (in commit)?
- [ ] Updated relevant documentation?
