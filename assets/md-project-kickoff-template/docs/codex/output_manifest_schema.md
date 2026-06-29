# Output Manifest Schema

Every formal analysis should write:

```text
results/<system>/<analysis_id>/outputs_manifest.json
```

The manifest lets Codex answer:

- What files were produced?
- Which files should be synced/downloaded?
- Which outputs are cite-ready?
- Which parameters and definitions produced this result?
- Which checks passed or failed?
- Where remote files live, and which ones should be synced locally?

## Minimal JSON Schema

```json
{
  "schema_version": 1,
  "project": "<project>",
  "module": "<module>",
  "analysis_id": "<analysis_id>",
  "generated_at": "<ISO timestamp>",
  "command": "<exact command>",
  "runtime": {
    "location": "local or remote",
    "remote_ssh_alias": "<alias or null>",
    "remote_runtime_checkout": "<path or null>",
    "remote_results_root": "<path or null>",
    "remote_log_path": "<path or null>",
    "sbatch_script": "<path or null>",
    "sbatch_command": "<command or null>",
    "job_id": "<job id or null>",
    "estimated_runtime": "<estimate or null>"
  },
  "git": {
    "branch": "<branch>",
    "commit": "<commit or dirty>"
  },
  "definitions": {
    "system": "<system>",
    "run_range": "<runs>",
    "window": "<window definition>",
    "metric": "<metric definition>",
    "units": "<units>"
  },
  "literature_basis": [
    {
      "id": "<ref id>",
      "doi": "<doi or null>",
      "claim_or_method_used": "<what this output relied on>"
    }
  ],
  "files": [
    {
      "path": "results/system/analysis/tables/summary.csv",
      "kind": "table",
      "purpose": "main summary",
      "system": "<system>",
      "run": "all",
      "window": "<window>",
      "remote_path": "<remote path or null>",
      "local_path": "<local path or null>",
      "download_to_outputs": true,
      "size_bytes": 0,
      "sync": true,
      "cite_ready": true,
      "notes": ""
    }
  ],
  "checks": [
    {
      "name": "row count",
      "status": "pass",
      "details": "<details>"
    }
  ],
  "warnings": []
}
```

## File Kinds

Recommended `kind` values:

- `table`
- `figure`
- `log`
- `notebook`
- `html`
- `json`
- `readme`
- `debug`

## Sync Labels

Use:

- `sync: true` for lightweight files that should be downloaded or archived.
- `sync: false` for large intermediate files, debug outputs, or files that can be regenerated.

Use:

- `cite_ready: true` for final tables/figures that can be used downstream.
- `cite_ready: false` for exploratory/debug outputs.

## Required Checks

At minimum include one of:

- file existence check
- row count check
- missing-run count
- plot generated check
- unit/sanity check
- server job completion check
