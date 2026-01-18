# Proficiency Guidelines

## Scale

| Level | Description |
|-------|-------------|
| `none` | No exposure |
| `basic` | Aware of concept, minimal hands-on |
| `familiar` | Used it, understand basics |
| `solid` | Comfortable, can troubleshoot |
| `expert` | Deep knowledge, can teach others |

## Review Intervals

| Proficiency | Review After |
|-------------|--------------|
| `none` | N/A |
| `basic` | 7 days |
| `familiar` | 14 days |
| `solid` | 30 days |
| `expert` | 90 days |

## When to Upgrade (Teaching Sessions)

- `none` → `basic`: First exposure, understands the concept
- `basic` → `familiar`: Can explain it, has seen examples
- `familiar` → `solid`: Can apply it, troubleshoot issues
- `solid` → `expert`: Deep knowledge, can teach others, knows edge cases

## When to Upgrade (Review Sessions)

- Retention score >= 80% AND current proficiency held for 2+ sessions → consider upgrade

## When to Downgrade

- Retention score < 50% on review → consider downgrade
- `struggled: true` twice in a row → downgrade one level

## Struggle Handling

If review session retention < 50%:
1. Set `struggled: true` on the topic
2. Set `struggle_date` to today
3. Halve the review interval (multiply by `struggle_multiplier: 0.5`)

## Retention Score Calculation

- Full correct = 1 point
- Partial = 0.5 points
- Wrong = 0 points
- Score = (points / total questions) × 100%

## Confidence Calibration

Track across all retrieval attempts:
- Average confidence: `total_confidence / attempts`
- Average accuracy: `total_accuracy / attempts`
- Calibration gap: `confidence - accuracy`
  - Positive = overconfident
  - Negative = underconfident
  - Near zero = well-calibrated

## General Principle

Be conservative - one session rarely jumps more than one level.
