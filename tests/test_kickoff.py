import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init_project_kickoff.py"
INSTALLER = ROOT / "bin" / "install.js"
NODE_CLI = ROOT / "bin" / "md-project-kickoff.js"


def run_initializer(target: Path, *args: str) -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT), "--target", str(target), *args],
        check=True,
        capture_output=True,
        text=True,
    )


def run_installer(home: Path, *args: str) -> None:
    if shutil.which("node") is None:
        raise unittest.SkipTest("Node.js is required for installer tests")
    subprocess.run(
        ["node", str(INSTALLER), "--home", str(home), *args],
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
        self.assertIn("v1.0.2", text)
        self.assertIn("irm https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.ps1 | iex", text)
        self.assertIn("curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash", text)
        self.assertIn("npx -y github:Ychris12138/md-project-kickoff --target <project_root>", text)
        self.assertIn("Node.js 18+", text)
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
            "10.13." + "34.120",
            "/public/home/" + "yangrui/",
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

    def test_shared_templates_are_agent_neutral_and_capture_runtime_guardrails(self) -> None:
        agents = (
            ROOT / "assets/md-project-kickoff-template/AGENTS.template.md"
        ).read_text(encoding="utf-8-sig")
        index = (
            ROOT / "assets/md-project-kickoff-template/PROJECT_INDEX.template.md"
        ).read_text(encoding="utf-8-sig")
        protocol = (
            ROOT
            / "assets/md-project-kickoff-template/docs/codex/remote_sbatch_task_protocol.md"
        ).read_text(encoding="utf-8-sig")

        self.assertIn("AI coding or research agent", agents)
        self.assertNotIn("how Codex should work", agents)
        self.assertIn("Remote test-agent directory", index)
        self.assertIn("Synchronization policy", index)
        for required in (
            "system/run",
            "start time",
            "end time",
            "exit status",
            "tqdm",
            "Array tasks",
            "Aggregation tasks",
            "smoke test",
        ):
            self.assertIn(required, protocol)


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

    def test_agent_all_adds_claude_and_cursor_project_entry_points(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target, "--agent", "all")

            claude = (target / "CLAUDE.md").read_text(encoding="utf-8-sig")
            cursor = (
                target / ".cursor/rules/project-kickoff.mdc"
            ).read_text(encoding="utf-8-sig")
            self.assertIn("@PROJECT_INDEX.md", claude)
            self.assertIn("@AGENTS.md", claude)
            self.assertIn("alwaysApply: true", cursor)
            self.assertIn("AGENTS.md", cursor)

    def test_agent_specific_option_does_not_add_other_host_entry_point(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run_initializer(target, "--agent", "claude")

            self.assertTrue((target / "CLAUDE.md").is_file())
            self.assertFalse((target / ".cursor/rules/project-kickoff.mdc").exists())

    def test_npx_package_exposes_initializer_bin(self) -> None:
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8-sig"))

        self.assertEqual(package["name"], "md-project-kickoff")
        self.assertEqual(package["version"], "1.0.2")
        self.assertEqual(package["bin"]["md-project-kickoff"], "bin/md-project-kickoff.js")
        self.assertTrue((ROOT / "bin/md-project-kickoff.js").is_file())
        self.assertTrue((ROOT / "bin/install.js").is_file())
        self.assertIn("install.sh", package["files"])
        self.assertIn("install.ps1", package["files"])
        self.assertIn("split('.').shift()", (ROOT / "install.sh").read_text(encoding="utf-8-sig"))
        self.assertIn("split('.').shift()", (ROOT / "install.ps1").read_text(encoding="utf-8-sig"))

    def test_installer_installs_all_supported_skill_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "home"
            run_installer(home, "--only", "codex,claude,cursor,agents")

            for agent in (".codex", ".claude", ".cursor", ".agents"):
                skill = home / agent / "skills/md-project-kickoff/SKILL.md"
                self.assertTrue(skill.is_file(), str(skill))

    def test_installer_detects_existing_agent_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "home"
            (home / ".cursor").mkdir(parents=True)
            run_installer(home)

            self.assertTrue((home / ".cursor/skills/md-project-kickoff/SKILL.md").is_file())
            self.assertFalse((home / ".codex/skills/md-project-kickoff/SKILL.md").exists())

    def test_main_cli_routes_install_mode(self) -> None:
        if shutil.which("node") is None:
            self.skipTest("Node.js is required for installer tests")
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "home"
            subprocess.run(
                ["node", str(NODE_CLI), "--install", "--home", str(home), "--only", "agents"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertTrue((home / ".agents/skills/md-project-kickoff/SKILL.md").is_file())

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
