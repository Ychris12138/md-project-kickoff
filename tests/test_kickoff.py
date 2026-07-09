import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init_project_kickoff.py"


def run_initializer(target: Path, *args: str) -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT), "--target", str(target), *args],
        check=True,
        capture_output=True,
        text=True,
    )


class SkillMetadataTests(unittest.TestCase):
    def test_skill_frontmatter_is_valid_yaml(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        frontmatter = text.split("---", 2)[1]
        metadata = yaml.safe_load(frontmatter)
        self.assertEqual(metadata["name"], "md-project-kickoff")
        self.assertIsInstance(metadata["description"], str)

    def test_root_readme_has_portable_public_installation(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        self.assertIn("gh repo clone <github-owner>/md-project-kickoff", text)
        self.assertIn("npx github:<github-owner>/md-project-kickoff --target <project_root>", text)
        self.assertIn("pull --ff-only", text)
        self.assertNotIn("private repository", text.lower())

    def test_root_readme_is_bilingual_and_starts_with_use_cases(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        opening = "\n".join(text.splitlines()[:20])

        self.assertIn("适用场景", opening)
        self.assertIn("Use cases", opening)
        self.assertIn("## 中文", text)
        self.assertIn("## English", text)

    def test_repository_text_has_no_personal_account_or_specific_research_topic(self) -> None:
        forbidden = [
            "Ychris" + "12138",
            "水模型的" + "结晶",
            "L" + "LPT",
        ]
        text_suffixes = {".md", ".py", ".yaml", ".yml", ".json", ".csv", ".template"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            if path.suffix.lower() not in text_suffixes and path.name != ".gitignore.template":
                continue
            text = path.read_text(encoding="utf-8-sig")
            for value in forbidden:
                self.assertNotIn(value, text, str(path.relative_to(ROOT)))

    def test_default_gitignore_is_domain_neutral(self) -> None:
        default = (
            ROOT / "assets/md-project-kickoff-template/.gitignore.template"
        ).read_text(encoding="utf-8-sig")
        md_profile = (
            ROOT
            / "assets/md-project-kickoff-template/gitignore-profiles/molecular-dynamics.gitignore"
        ).read_text(encoding="utf-8-sig")

        self.assertNotIn("*.xtc", default)
        self.assertNotIn("*.dcd", default)
        self.assertIn("*.xtc", md_profile)
        self.assertIn("*.dcd", md_profile)

    def test_remote_sbatch_protocol_is_the_single_detailed_source(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        agents = (
            ROOT / "assets/md-project-kickoff-template/AGENTS.template.md"
        ).read_text(encoding="utf-8-sig")
        git_remote = (
            ROOT / "assets/md-project-kickoff-template/docs/codex/git_remote_workflow.md"
        ).read_text(encoding="utf-8-sig")

        self.assertIn("remote_sbatch_task_protocol.md", skill)
        self.assertNotIn("Follow the three-stage workflow", skill)
        self.assertIn("remote_sbatch_task_protocol.md", agents)
        self.assertNotIn("### Stage 1", agents)
        self.assertIn("remote_sbatch_task_protocol.md", git_remote)
        self.assertNotIn("*.dcd", git_remote)


class InitializerTests(unittest.TestCase):
    def test_minimal_profile_initializes_git_and_stays_minimal(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target)

            self.assertTrue((target / ".git").is_dir())
            self.assertTrue((target / "README.md").is_file())
            self.assertTrue((target / "docs/codex/outputs_manifest.template.json").is_file())
            self.assertTrue((target / "outputs/test").is_dir())
            self.assertTrue((target / "outputs/final").is_dir())
            self.assertFalse((target / "docs/literature").exists())
            self.assertFalse((target / "docs/codex/remote_sbatch_task_protocol.md").exists())
            self.assertFalse((target / "docs/codex/git_remote_workflow.md").exists())

            checklist = (target / "docs/codex/project_scaffold_checklist.md").read_text(
                encoding="utf-8-sig"
            )
            self.assertIn("Optional Add-ons", checklist)

    def test_full_profile_adds_literature_and_remote_workflows(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target, "--profile", "full")

            self.assertTrue((target / "docs/literature/literature_review.md").is_file())
            self.assertTrue((target / "docs/codex/git_remote_workflow.md").is_file())
            self.assertTrue((target / "docs/codex/remote_sbatch_task_protocol.md").is_file())

    def test_literature_library_option_creates_non_git_pdf_store_and_knowledge_base(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target, "--with-literature-library")

            self.assertTrue((target / "literature_library/pdfs").is_dir())
            self.assertTrue((target / "literature_library/notes").is_dir())
            self.assertTrue((target / "docs/literature/literature_knowledge_base.md").is_file())
            gitignore = (target / ".gitignore").read_text(encoding="utf-8-sig")
            self.assertIn("literature_library/", gitignore)
            self.assertIn("outputs/", gitignore)

    def test_npx_package_exposes_initializer_bin(self) -> None:
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8-sig"))

        self.assertEqual(package["name"], "md-project-kickoff")
        self.assertEqual(package["bin"]["md-project-kickoff"], "bin/md-project-kickoff.js")
        self.assertTrue((ROOT / "bin/md-project-kickoff.js").is_file())

    def test_force_backs_up_existing_project_memory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target)
            index = target / "PROJECT_INDEX.md"
            index.write_text("SENTINEL", encoding="utf-8")

            run_initializer(target, "--force")

            backups = list((target / ".project-kickoff-backup").glob("*/PROJECT_INDEX.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "SENTINEL")

    def test_manifest_template_is_small_and_parseable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target)
            manifest = json.loads(
                (target / "docs/codex/outputs_manifest.template.json").read_text(
                    encoding="utf-8-sig"
                )
            )

            self.assertEqual(manifest["schema_version"], 1)
            self.assertIn("analysis_id", manifest)
            self.assertIn("outputs", manifest)
            self.assertIn("checks", manifest)
            self.assertLessEqual(len(manifest), 8)


if __name__ == "__main__":
    unittest.main()
