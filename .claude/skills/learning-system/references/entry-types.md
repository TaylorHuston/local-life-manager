# Entry Types

Entries are logged in the session's `entries` array.

## Entry Schema

```json
{ "type": "<type>", "content": "Description", ...extra_fields }
```

## Types

| Type | When to Use | Extra Fields |
|------|-------------|--------------|
| `concept` | Key fact or understanding gained | - |
| `correction` | Error fixed during teaching | - |
| `misconception` | Wrong belief worth revisiting later | - |
| `question` | Important question (answered or open) | - |
| `connection` | Link to another topic | - |
| `elaboration` | User explained "why/how" themselves | `quality`: strong/partial/weak |
| `retrieval_attempt` | User recalled from memory | `confidence`: 1-5, `accurate`: bool |
| `retrieval_test` | Review session question | See below |

## Examples

```json
{ "type": "concept", "content": "RDS Multi-AZ uses synchronous replication" }

{ "type": "correction", "content": "Aurora replicas can be promoted, not just failover targets" }

{ "type": "misconception", "content": "Thought EFS was block storage, actually NFS" }

{ "type": "question", "content": "How does Secrets Manager rotation work with RDS?" }

{ "type": "connection", "content": "Secrets Manager rotation similar to certificate renewal in PKI" }

{ "type": "elaboration", "content": "Explained why connection pooling helps: reduces auth overhead", "quality": "strong" }

{ "type": "retrieval_attempt", "content": "Remembered 3 of 4 RDS instance types", "confidence": 4, "accurate": false }
```

## Review Session Entry

```json
{
  "type": "retrieval_test",
  "question": "What are the three EFS throughput modes?",
  "response_summary": "Named Bursting and Provisioned, missed Elastic",
  "confidence": 3,
  "accurate": false,
  "partial": true,
  "notes": "Forgot Elastic mode exists"
}
```

## Guidelines

- Keep entries atomic and concise
- Focus on what helps rebuild context later
- Don't duplicate existing entries
- **Capture misconceptions** - valuable for review trap questions
- **Note elaborations** - user's own explanations show deep understanding
- **Track confidence vs accuracy** - builds metacognitive awareness
