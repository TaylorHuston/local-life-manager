# [Project] Specification

<!--
This is a PROTOCOL SPECIFICATION - it defines WHAT the system must do.
It is the source of truth for requirements. TASKs implement sections of this spec.

For projects implementing external specs (OAuth, LEAF, OpenAPI, etc.),
import those specs instead of using this template.

Use this template for self-authored protocol specs when your project
needs to define its own standard/contract.
-->

**Version:** 0.1.0-draft
**Created:** YYYY-MM-DD
**Updated:** YYYY-MM-DD

---

## Overview

[What this system does and why it exists. 2-3 sentences.]

## Actors

[Who or what interacts with this system]

- **User** - [description]
- **Admin** - [description]
- **External System** - [description]

## Core Operations

[The fundamental things this system MUST do]

### Operation 1: [Name]

**Description:** [What it does]

**Inputs:**
- [Input 1]
- [Input 2]

**Outputs:**
- [Output 1]

**Behavior:**
- [Rule 1]
- [Rule 2]

### Operation 2: [Name]

[Same structure]

---

## API Specification

### Endpoints

#### [METHOD] /api/[resource]

**Description:** [What it does]

**Auth Required:** Yes/No

**Request:**
```json
{
  "field": "value"
}
```

**Response:** `200 OK`
```json
{
  "field": "value"
}
```

**Errors:**
- `400` - [When/why]
- `401` - [When/why]
- `404` - [When/why]

---

## Data Models

### [Entity Name]

```json
{
  "id": "string (unique identifier)",
  "field1": "string (description)",
  "field2": "number (description)",
  "createdAt": "string (ISO 8601 datetime)"
}
```

**Field Requirements:**
- `id` - Required, unique, immutable
- `field1` - Required, [constraints]
- `field2` - Optional, [defaults]

---

## Required Features

### §1 [Feature Area]

**Requirements:**
- [Requirement 1]
- [Requirement 2]

**Test Criteria:**
- [How to verify requirement 1]
- [How to verify requirement 2]

### §2 [Feature Area]

[Same structure]

---

## Out of Scope

[What this spec explicitly does NOT cover]

- [Item 1]
- [Item 2]

---

## Changelog

### [0.1.0-draft] - YYYY-MM-DD
- Initial specification draft
