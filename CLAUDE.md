# CLAUDE.md — 308-Jamie-Ct-3b d-house

## What This Is

A single place to store all information for the property management of 308
Current state: Skeleton, freshly scaffolded.
Owner: Ethan Kunz.

## Repository Structure

```
308-jamie-ct-3b-d-house/
    |-- workflows
        |-- ci.yml
|-- .gitignore
|-- CLAUDE.md
|-- GEMINI.md
|-- LICENSE
|-- README.md
|-- SECURITY.md
|-- archive
|-- config
    |-- config.example.yaml
    |-- config.yaml
|-- dashboard.html
|-- data
    |-- .gitignore
        |-- Audits-Reviews
        |-- Diagrams
        |-- Guides
        |-- Project-Management
        |-- Reference
        |-- Testing
    |-- active
        |-- STATUS.md
        |-- TECHNICAL_JOURNAL.md
|-- package.json
|-- scripts
    |-- setup_env.ps1
    |-- verify_project_state.py
    |-- core
    |-- entities
    |-- systems
    |-- ui
    |-- utils
|-- tests
    +-- README.md
```

## Session Workflow

### At Session Start
1. Read this file
2. Read `docs/active/TECHNICAL_JOURNAL.md` (last ~100 lines)
3. Check `docs/active/STATUS.md` for current blockers
4. Check milestone checklists if applicable

### During the Session
- Track work: files changed, bugs fixed, decisions made
- Follow verification standards before committing

### END SESSION — Trigger Phrase
1. Run the project-specific test suite
2. Run `python scripts/verify_project_state.py`
3. Self-correct any test failures (max 1 attempt)
4. Append entry to `docs/active/TECHNICAL_JOURNAL.md`
5. Update `docs/active/STATUS.md`
6. Rebuild documentation if `docs/build_all_docs.py` exists
7. Single descriptive commit

## Coding Standards

<!-- Add project-specific coding standards here -->

## Verification Commands

```bash
python scripts/verify_project_state.py
```

## Key Technical Context

<!-- Architecture decisions, data flow, constraints -->

## What NOT to Do

- Do not commit secrets or API keys
- Do not edit generated files (`docs/index.html`) directly
- Do not skip END SESSION protocol for firmware/active projects
- Do not use magic numbers — put constants in config
- Do not duplicate values — alias to canonical source
