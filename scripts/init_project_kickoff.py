#!/usr/bin/env python3
"""Initialize a md-project-kickoff scaffold in a target project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "md-project-kickoff-template"

COPY_FILES = {
    "PROJECT_INDEX.template.md": "PROJECT_INDEX.md",
    "AGENTS.template.md": "AGENTS.md",
    ".gitignore.template": ".gitignore",
    "docs/definitions.template.md": "docs/definitions.md",
    "docs/method_registry.template.md": "docs/method_registry.md",
    "docs/literature/reference_manifest.template.csv": "docs/literature/reference_manifest.csv",
    "docs/codex/analysis_contract_template.md": "docs/codex/analysis_contract_template.md",
    "docs/codex/git_remote_workflow.md": "docs/codex/git_remote_workflow.md",
    "docs/codex/literature_review_workflow.md": "docs/codex/literature_review_workflow.md",
    "docs/codex/migration_checklist.template.md": "docs/codex/migration_checklist.md",
    "docs/codex/output_manifest_schema.md": "docs/codex/output_manifest_schema.md",
    "docs/codex/project_scaffold_checklist.md": "docs/codex/project_scaffold_checklist.md",
    "docs/codex/remote_sbatch_task_protocol.md": "docs/codex/remote_sbatch_task_protocol.md",
}

CREATE_DIRS = [
    "configs",
    "scripts",
    "src",
    "tests",
    "notebooks/exploratory",
    "notebooks/summaries",
    "docs/literature",
    "results",
    "logs",
    "review",
    "outputs",
]

PLACEHOLDERS = {
    "docs/literature/literature_review.md": "# Literature Review\n\nStatus: placeholder. Add seed references before method design.\n",
    "docs/literature/method_implications.md": "# Method Implications\n\n| Method idea | Literature basis | Inputs needed | Outputs | Risks | Project action |\n|---|---|---|---|---|---|\n",
}


def copy_file(src_rel: str, dst_rel: str, target: Path, force: bool, dry_run: bool) -> str:
    src = TEMPLATE_ROOT / src_rel
    dst = target / dst_rel
    if not src.exists():
        raise FileNotFoundError(f"Missing template: {src}")
    if dst.exists() and not force:
        return f"skip existing {dst_rel}"
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return f"copy {src_rel} -> {dst_rel}"


def write_placeholder(dst_rel: str, content: str, target: Path, force: bool, dry_run: bool) -> str:
    dst = target / dst_rel
    if dst.exists() and not force:
        return f"skip existing {dst_rel}"
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding="utf-8-sig")
    return f"write {dst_rel}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Project root to initialize.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing.")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    actions: list[str] = []

    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    for rel in CREATE_DIRS:
        path = target / rel
        if not args.dry_run:
            path.mkdir(parents=True, exist_ok=True)
        actions.append(f"mkdir {rel}")

    for src_rel, dst_rel in COPY_FILES.items():
        actions.append(copy_file(src_rel, dst_rel, target, args.force, args.dry_run))

    for dst_rel, content in PLACEHOLDERS.items():
        actions.append(write_placeholder(dst_rel, content, target, args.force, args.dry_run))

    for action in actions:
        print(action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

