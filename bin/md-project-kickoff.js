#!/usr/bin/env node

const { spawnSync } = require("node:child_process");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const script = path.join(root, "scripts", "init_project_kickoff.py");
const args = process.argv.slice(2);

if (args[0] === "--install") {
  const installer = path.join(root, "bin", "install.js");
  const result = spawnSync(process.execPath, [installer, ...args.slice(1)], { stdio: "inherit" });
  process.exit(result.status ?? 1);
}

const pythonCandidates = process.platform === "win32" ? ["py", "python", "python3"] : ["python3", "python"];

let lastError = null;
for (const python of pythonCandidates) {
  const commandArgs = python === "py" ? ["-3", script, ...args] : [script, ...args];
  const result = spawnSync(python, commandArgs, { stdio: "inherit" });
  if (result.error && result.error.code === "ENOENT") {
    lastError = result.error;
    continue;
  }
  process.exit(result.status ?? 1);
}

console.error("md-project-kickoff requires Python 3 on PATH.");
if (lastError) {
  console.error(lastError.message);
}
process.exit(1);
