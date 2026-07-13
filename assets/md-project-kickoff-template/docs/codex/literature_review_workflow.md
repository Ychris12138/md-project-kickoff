# Literature Review Workflow

This workflow turns reference papers into method guidance for the project.

Goal:

```text
references -> literature review -> definitions/method registry -> analysis contracts
```

The review is not only a background essay. It should directly support later analysis design.

## 1. When To Use

Use this workflow when:

- starting a new scientific project
- choosing a new metric/order parameter/analysis method
- migrating a method from another project
- comparing alternative definitions or thresholds
- writing a report, proposal, or methods section

## 2. Inputs

The user may provide:

- DOI links
- paper titles
- arXiv links
- PDFs
- BibTeX/RIS records
- notes from prior chats
- a small seed list of key papers

If no papers are provided, ask for 3-8 seed references or ask permission to search for them.

Do not fabricate citations. If a paper cannot be accessed, record it as `not_read` in the manifest.

## 3. Reference Manifest

Create or update:

```text
docs/literature/reference_manifest.csv
```

Recommended columns:

```text
id,title,authors,year,venue,doi,url,source_type,local_path,read_status,topic,method_relevance,key_definitions,key_methods,key_outputs,notes
```

Status values:

- `seed`: provided but not read
- `reading`: currently being read
- `read`: read and summarized
- `not_accessible`: citation known but source unavailable
- `background`: useful context but not method-critical
- `method_core`: important for analysis design

## 4. Reading Notes

For each method-relevant paper, extract:

- scientific question
- system/data/model studied
- method and metric definitions
- thresholds/windows/parameters
- input data requirements
- output quantities and plots
- validation or sanity checks
- limitations and assumptions
- what can be reused in this project
- what should not be copied directly

## 5. Required Outputs

### `docs/literature/literature_review.md`

Recommended structure:

```md
# Literature Review

## Scope

## Key Takeaways

## Paper-by-Paper Notes

## Cross-Paper Method Comparison

## Definitions And Thresholds

## Validation And Sanity Checks

## Risks, Gaps, And Disagreements

## Implications For This Project

## Recommended First Analyses
```

### `docs/literature/method_implications.md`

This should be shorter and directly actionable:

```md
# Method Implications

| Method idea | Literature basis | Inputs needed | Outputs | Risks | Project action |
|---|---|---|---|---|---|
```

### Optional `docs/literature/references.bib`

Use when BibTeX entries are available or needed.

## 6. Update Project Files

After the review:

Update `docs/definitions.md` with:

- definitions confirmed by literature
- thresholds/windows/units used in papers
- unresolved disagreements

Update `docs/method_registry.md` with:

- method candidates
- canonical literature basis
- methods to avoid
- validation checks to implement

Update `PROJECT_INDEX.md` with:

- key references by workstream
- next analysis suggested by literature

## 7. Quality Rules

- Separate what the paper says from what the Agent infers.
- Keep citations attached to method claims.
- Do not overstate methods from papers that were not read.
- Prefer tables for definitions, thresholds, methods, and validation checks.
- If using web/source lookup, include DOI or stable source links.
- If reading local files only, state that source scope clearly.

