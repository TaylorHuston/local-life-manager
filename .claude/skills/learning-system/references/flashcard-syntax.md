# Flashcard Syntax

For the Obsidian Spaced Repetition plugin.

## Inline Formats

```
Question :: Answer                     (single-sided)
Term ::: Definition                    (bidirectional/reversible)
```

## Multi-line Format

Answer on following lines after `;;`:

```
What are the three Service Consumer Types? ;;
- Customer
- User
- Sponsor
```

## Cloze Deletions (Fill-in-the-blank)

```
The ==hidden text== will be blanked out
The **bolded text** becomes a cloze
The {{curly brace text}} is also hidden
```

## When to Use Each

| Format | Best For |
|--------|----------|
| `::` single-sided | Facts, definitions, one-way recall |
| `:::` bidirectional | Terminology, translations, concept ↔ example |
| `;;` multi-line | Lists, multiple points, longer answers |
| Cloze `==text==` | Port numbers, values, syntax, key facts in context |

## Guidelines

1. **Atomic cards** - one concept per card
2. **Avoid yes/no questions** - too easy
3. **Break up lists** - use multiple cards instead of memorizing a list
4. **Keep answers concise** - if too long, split into multiple cards

## Example Output

```markdown
## Flashcards

Jira's default HTTP port :: 8080
PostgreSQL default port :: 5432

What is an ASG? ::: What manages EC2 instance lifecycle in AWS?

What are the three EFS throughput modes? ;;
- Bursting (scales with storage size)
- Provisioned (you set the throughput)
- Elastic (auto-scales with workload)

RDS Multi-AZ failover takes ==60-120 seconds==, while Aurora fails over in ==~30 seconds==.
```
