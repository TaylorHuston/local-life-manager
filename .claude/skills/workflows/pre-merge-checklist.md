---
name: workflows:pre-merge-checklist
description: "Workflow: Pre-Merge Checklist"
---

# Workflow: Pre-Merge Checklist

Ensure code is ready to merge with confidence.

## Quick Reference

**Run in parallel for speed:**
```bash
/quality
/security-audit
/docs
/validate-spec
```

Then:
```bash
/complete
```

## Parallel Checks

### Check 1: Code Quality
```bash
/quality
```
- Code patterns and best practices
- Complexity and maintainability
- Test coverage adequacy

### Check 2: Security Audit
```bash
/security-audit
```
- OWASP Top 10
- Secrets in code
- Input validation
- Auth/authz issues

**If fails**: MUST FIX before merging

### Check 3: Documentation Health
```bash
/docs
```
- README accuracy
- API documentation
- ADRs for decisions
- Change logs updated

### Check 4: Spec Compliance
```bash
/validate-spec
```
- Implementation matches spec
- Acceptance criteria satisfied

## Final Step

### Complete & Merge
```bash
/complete
```
1. Re-validates all checks
2. Updates documentation
3. Runs code review
4. Creates commit
5. Merges to develop

## Fix Priorities

### Critical (Must fix)
- Security vulnerabilities
- Data loss risks
- Breaking changes without migration
- Critical bugs

### High (Should fix)
- Test failures
- High complexity code
- Missing error handling

### Medium (Can fix after merge)
- Minor code smells
- Documentation improvements
- Refactoring opportunities

## Red Flags (Don't Merge)

- Security vulnerabilities present
- Tests failing
- Critical bugs
- Breaking changes undocumented
- You don't understand what the code does

## Green Lights (Safe to Merge)

- All automated checks pass
- Manual testing successful
- Documentation updated
- Spec requirements met
- No security issues
- You're confident in the code
