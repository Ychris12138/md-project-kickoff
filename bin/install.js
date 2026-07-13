#!/usr/bin/env node

"use strict";

const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { spawnSync } = require("node:child_process");

const SKILL_NAME = "md-project-kickoff";
const REPO = "Ychris12138/md-project-kickoff";
const ROOT = path.resolve(__dirname, "..");
const COPY_ENTRIES = ["SKILL.md", "agents", "assets", "scripts"];

function parseArgs(argv) {
  const options = {
    all: false,
    dryRun: false,
    home: null,
    only: null,
    uninstall: false,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--all") {
      options.all = true;
    } else if (arg === "--dry-run") {
      options.dryRun = true;
    } else if (arg === "--uninstall") {
      options.uninstall = true;
    } else if (arg === "--home") {
      options.home = argv[++index];
      if (!options.home) throw new Error("--home requires a path");
    } else if (arg === "--only") {
      options.only = argv[++index];
      if (!options.only) throw new Error("--only requires a comma-separated agent list");
    } else if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown installer option: ${arg}`);
    }
  }

  return options;
}

function printHelp() {
  console.log(`Install ${SKILL_NAME} for detected local Agents.

Usage:
  node bin/install.js [--all] [--only codex,claude,cursor,agents]
                      [--dry-run] [--uninstall]

Detection checks the standard global skill roots and Agent executables.
Use --all to create all supported roots, or --only to select exact targets.
`);
}

function commandExists(command) {
  const lookup = process.platform === "win32" ? "where" : "which";
  return spawnSync(lookup, [command], { stdio: "ignore" }).status === 0;
}

function makeTargets(options) {
  const home = options.home ? path.resolve(options.home) : os.homedir();
  const customHome = Boolean(options.home);
  const codexRoot = customHome
    ? path.join(home, ".codex")
    : process.env.CODEX_HOME || path.join(home, ".codex");

  const targets = [
    {
      id: "codex",
      label: "Codex",
      root: codexRoot,
      command: "codex",
    },
    {
      id: "claude",
      label: "Claude Code",
      root: path.join(home, ".claude"),
      command: "claude",
    },
    {
      id: "cursor",
      label: "Cursor",
      root: path.join(home, ".cursor"),
      command: "cursor-agent",
    },
    {
      id: "agents",
      label: "Agent Skills standard",
      root: path.join(home, ".agents"),
      command: null,
    },
  ].map((target) => ({
    ...target,
    skillDir: path.join(target.root, "skills", SKILL_NAME),
  }));

  if (options.only) {
    const selected = new Set(options.only.split(",").map((item) => item.trim()).filter(Boolean));
    const known = new Set(targets.map((target) => target.id));
    for (const id of selected) {
      if (!known.has(id)) throw new Error(`Unknown agent: ${id}`);
    }
    return targets.filter((target) => selected.has(target.id));
  }

  if (options.all) return targets;

  if (customHome) return targets.filter((target) => fs.existsSync(target.root));

  return targets.filter(
    (target) => fs.existsSync(target.root) || (target.command && commandExists(target.command)),
  );
}

function installTarget(target, options) {
  console.log(`${options.uninstall ? "Uninstalling" : "Installing"} ${SKILL_NAME} for ${target.label}: ${target.skillDir}`);
  if (options.dryRun) return;

  if (options.uninstall) {
    fs.rmSync(target.skillDir, { force: true, recursive: true });
    return;
  }

  fs.mkdirSync(target.skillDir, { recursive: true });
  for (const entry of COPY_ENTRIES) {
    const source = path.join(ROOT, entry);
    const destination = path.join(target.skillDir, entry);
    fs.cpSync(source, destination, { force: true, recursive: true });
  }
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  const targets = makeTargets(options);
  if (targets.length === 0) {
    throw new Error(
      "No supported Agent installation was detected. Use --all or --only codex,claude,cursor,agents.",
    );
  }

  for (const target of targets) installTarget(target, options);
  console.log(options.dryRun ? "Dry run complete." : "Installation complete.");
}

try {
  main();
} catch (error) {
  console.error(`md-project-kickoff installer: ${error.message}`);
  process.exitCode = 1;
}
