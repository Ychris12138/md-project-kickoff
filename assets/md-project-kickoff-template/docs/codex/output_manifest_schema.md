# Output Manifest

Every formal analysis should write one small `outputs_manifest.json` beside its outputs. The JSON template at `docs/codex/outputs_manifest.template.json` is the canonical core structure; this document only explains field intent and optional extensions.

## Required Core

Keep these fields for every analysis:

- `schema_version`: manifest format version.
- `analysis_id`: stable short analysis identifier.
- `status`: `planned`, `running`, `complete`, `partial`, or `failed`.
- `generated_at`: ISO-8601 timestamp.
- `command`: reproducible entry point or exact command.
- `outputs`: produced files and why they matter.
- `checks`: lightweight validation results.

Each output needs only:

- `path`: project-relative path when possible.
- `role`: `table`, `figure`, `report`, `log`, `data`, or `other`.
- `description`: one-line purpose.
- `sync`: whether a lightweight copy should be downloaded or archived.

## Optional Extensions

Add fields only when they help reproduce or retrieve the result:

- `git`: branch and commit.
- `inputs`: important input paths, labels, and read-only status.
- `method`: parameters, definitions, windows, thresholds, and units.
- `remote`: SSH alias, runtime checkout, job id, sbatch script, log, and remote result paths.
- `literature`: references that directly informed the method.
- `warnings`: caveats or incomplete checks.
- Per-output `size_bytes`, `remote_path`, `local_path`, and `cite_ready`.

Do not add empty remote or literature blocks to a local analysis. The manifest is an index, not a second report.

## Minimum Validation

Record at least one meaningful check, such as file existence, row count, missing-run count, unit sanity, plot generation, or server job completion.
