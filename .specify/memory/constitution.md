<!--
Sync Impact Report:
- Version change: 0.0.0 -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> Write tests first (TDD approach)
  - [PRINCIPLE_2_NAME] -> Use Python 3.12+ with type hints everywhere
  - [PRINCIPLE_3_NAME] -> Keep code clean and easy to read
  - [PRINCIPLE_4_NAME] -> Document important decisions with ADRs
  - [PRINCIPLE_5_NAME] -> Follow essential OOP principles: SOLID, DRY, KISS
- Added sections: Technical Stack, Quality Requirements
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/memory/constitution.md
-->
# practice_specKit Constitution

## Core Principles

### Write tests first (TDD approach)
TDD mandatory: Tests written -> User approved -> Tests fail -> Then implement; Red-Green-Refactor cycle strictly enforced

### Use Python 3.12+ with type hints everywhere
All Python code must be written in version 3.12 or higher and include type hints for all function signatures and variables.

### Keep code clean and easy to read
Code should be well-structured, commented where necessary, and follow a consistent style guide.

### Document important decisions with ADRs
Architectural Decision Records (ADRs) must be used to document significant architectural decisions and their rationale.

### Follow essential OOP principles: SOLID, DRY, KISS
Adhere to SOLID, Don't Repeat Yourself (DRY), and Keep It Simple, Stupid (KISS) principles in all code.

## Technical Stack
- Python 3.12+ with UV package manager
- pytest for testing
- Keep all project files in git

## Quality Requirements
- All tests must pass
- At least 80% code coverage
- Use dataclasses for data structures

## Governance
- All PRs/reviews must verify compliance.
- Complexity must be justified.
- Amendments require documentation, approval, and a migration plan.

**Version**: 1.0.0 | **Ratified**: 2025-11-13 | **Last Amended**: 2025-11-13