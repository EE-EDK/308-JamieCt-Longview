"""
Project: 308-Jamie-Ct-3b d-house
File: verify_project_state.py
Copyright (c) 2026 Ethan Kunz
License: Proprietary
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def verify():
    """Check that critical project files and directories exist."""
    errors = []

    critical_files = [
    "README.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".gitignore",
    "docs/active/STATUS.md",
    "docs/active/TECHNICAL_JOURNAL.md",
    "tests/README.md",
    "scripts/setup_env.ps1",
    "scripts/verify_project_state.py",
    "package.json",
    "dashboard.html",
    "config/config.yaml",
    "config/config.example.yaml",
    "data/.gitignore",
    "LICENSE",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    ]

    for rel_path in critical_files:
        full = PROJECT_ROOT / rel_path
        if not full.exists():
            errors.append(f"MISSING: {rel_path}")

    # Check mandatory documentation triad
    for doc in ["README.md", "CLAUDE.md", "GEMINI.md"]:
        path = PROJECT_ROOT / doc
        if path.exists() and path.stat().st_size == 0:
            errors.append(f"EMPTY: {doc} (must have content)")

    return errors


if __name__ == "__main__":
    errors = verify()
    if errors:
        print(f"FAIL: {len(errors)} issue(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK: All critical files present.")
        sys.exit(0)
