#!/usr/bin/env python3
"""Initialize a md-project-kickoff scaffold in a target project."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "md-project-kickoff-template"

MINIMAL_COPY_FILES = {
    "PROJECT_README.template.md": "README.md",
    "PROJECT_INDEX.template.md": "PROJECT_INDEX.md",
    "AGENTS.template.md": "AGENTS.md",
    ".gitignore.template": ".gitignore",
    "docs/definitions.template.md": "docs/definitions.md",
    "docs/method_registry.template.md": "docs/method_registry.md",
    "docs/codex/analysis_contract_template.md": "docs/codex/analysis_contract_template.md",
    "docs/codex/output_manifest_schema.md": "docs/codex/output_manifest_schema.md",
    "docs/codex/outputs_manifest.template.json": "docs/codex/outputs_manifest.template.json",
    "docs/codex/project_scaffold_checklist.md": "docs/codex/project_scaffold_checklist.md",
}

FULL_COPY_FILES = {
    "docs/codex/git_remote_workflow.md": "docs/codex/git_remote_workflow.md",
    "docs/literature/reference_manifest.template.csv": "docs/literature/reference_manifest.csv",
    "docs/codex/literature_review_workflow.md": "docs/codex/literature_review_workflow.md",
    "docs/codex/migration_checklist.template.md": "docs/codex/migration_checklist.md",
    "docs/codex/remote_sbatch_task_protocol.md": "docs/codex/remote_sbatch_task_protocol.md",
}

MINIMAL_CREATE_DIRS = [
    "docs/codex",
    "outputs/test",
    "outputs/final",
    "scripts",
    "src",
    "tests",
]

FULL_CREATE_DIRS = [
    "configs",
    "notebooks/exploratory",
    "notebooks/summaries",
    "docs/literature",
    "results",
    "logs",
    "review",
    "outputs",
]

FULL_PLACEHOLDERS = {
    "docs/literature/literature_review.md": "# Literature Review\n\nStatus: placeholder. Add seed references before method design.\n",
    "docs/literature/method_implications.md": "# Method Implications\n\n| Method idea | Literature basis | Inputs needed | Outputs | Risks | Project action |\n|---|---|---|---|---|---|\n",
}

AGENT_COPY_FILES = {
    "claude": {
        "adapters/claude/CLAUDE.template.md": "CLAUDE.md",
    },
    "cursor": {
        "adapters/cursor/project-kickoff.mdc": ".cursor/rules/project-kickoff.mdc",
    },
}

AGENT_CREATE_DIRS = {
    "claude": [],
    "cursor": [".cursor/rules"],
}

LITERATURE_LIBRARY_DIRS = [
    "literature_library/pdfs",
    "literature_library/notes",
    "docs/literature",
]

LITERATURE_LIBRARY_PLACEHOLDERS = {
    "docs/literature/literature_knowledge_base.md": "# Literature Knowledge Base\n\nStatus: empty. Add PDFs to `literature_library/pdfs/`, then ask the Agent to extract method-relevant notes here.\n\n## Index\n\n| Topic | Source | Key method detail | Project implication |\n|---|---|---|---|\n",
}


def backup_file(dst: Path, target: Path, backup_root: Path, dry_run: bool) -> None:
    backup = backup_root / dst.relative_to(target)
    if not dry_run:
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dst, backup)


def copy_file(
    src_rel: str,
    dst_rel: str,
    target: Path,
    force: bool,
    dry_run: bool,
    backup_root: Path,
) -> str:
    src = TEMPLATE_ROOT / src_rel
    dst = target / dst_rel
    if not src.exists():
        raise FileNotFoundError(f"Missing template: {src}")
    if dst.exists() and not force:
        return f"skip existing {dst_rel}"
    if dst.exists():
        backup_file(dst, target, backup_root, dry_run)
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return f"copy {src_rel} -> {dst_rel}"


def write_placeholder(
    dst_rel: str,
    content: str,
    target: Path,
    force: bool,
    dry_run: bool,
    backup_root: Path,
) -> str:
    dst = target / dst_rel
    if dst.exists() and not force:
        return f"skip existing {dst_rel}"
    if dst.exists():
        backup_file(dst, target, backup_root, dry_run)
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding="utf-8-sig")
    return f"write {dst_rel}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Project root to initialize.")
    parser.add_argument(
        "--profile",
        choices=("minimal", "full"),
        default="minimal",
        help="Choose the scaffold size. Minimal is the default.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Back up, then overwrite existing scaffold files.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing.")
    parser.add_argument(
        "--with-literature-library",
        action="store_true",
        help="Create a non-Git literature_library/ folder for PDFs and a small literature knowledge-base starter.",
    )
    parser.add_argument(
        "--agent",
        choices=("neutral", "codex", "claude", "cursor", "all"),
        default="neutral",
        help="Add host-specific project instructions. Neutral/codex keep the shared AGENTS.md entry point.",
    )
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    backup_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup_root = target / ".project-kickoff-backup" / backup_stamp
    actions: list[str] = []

    copy_files = dict(MINIMAL_COPY_FILES)
    create_dirs = list(MINIMAL_CREATE_DIRS)
    placeholders = {}
    if args.profile == "full":
        copy_files.update(FULL_COPY_FILES)
        create_dirs.extend(FULL_CREATE_DIRS)
        placeholders.update(FULL_PLACEHOLDERS)
    if args.with_literature_library:
        create_dirs.extend(LITERATURE_LIBRARY_DIRS)
        placeholders.update(LITERATURE_LIBRARY_PLACEHOLDERS)

    selected_agents = {args.agent}
    if args.agent == "all":
        selected_agents = {"claude", "cursor"}
    for agent in selected_agents:
        create_dirs.extend(AGENT_CREATE_DIRS.get(agent, []))
        copy_files.update(AGENT_COPY_FILES.get(agent, {}))

    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    if not (target / ".git").exists():
        actions.append("git init --initial-branch=main")
        if not args.dry_run:
            subprocess.run(
                ["git", "init", "--initial-branch=main", str(target)],
                check=True,
                capture_output=True,
                text=True,
            )

    for rel in create_dirs:
        path = target / rel
        if not args.dry_run:
            path.mkdir(parents=True, exist_ok=True)
        actions.append(f"mkdir {rel}")

    for src_rel, dst_rel in copy_files.items():
        actions.append(
            copy_file(
                src_rel,
                dst_rel,
                target,
                args.force,
                args.dry_run,
                backup_root,
            )
        )

    for dst_rel, content in placeholders.items():
        actions.append(
            write_placeholder(
                dst_rel,
                content,
                target,
                args.force,
                args.dry_run,
                backup_root,
            )
        )

    for action in actions:
        print(action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
