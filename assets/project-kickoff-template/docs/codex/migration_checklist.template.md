# Migration Checklist

Use this when moving methods, scripts, or analysis logic from another project.

## 1. Migration Summary

```yaml
source_project: <path/name>
target_project: <path/name>
method: <method name>
status: planned/in_progress/done/blocked
```

## 2. Source Files

| Source file/folder | Role | Migrate? | Notes |
|---|---|---|---|
| `<path>` | `<role>` | yes/no/reference only | `<notes>` |

## 3. Target Files

| Target file/folder | Role | Status |
|---|---|---|
| `<path>` | `<role>` | planned/done |

## 4. Definitions To Copy Or Reconsider

| Definition | Source value | Target value | Same? | Notes |
|---|---|---|---|---|
| `<definition>` | `<value>` | `<value>` | yes/no/unclear | `<notes>` |

## 5. Dependencies

- Python packages:
  - `<package>`
- External tools:
  - `<tool>`
- Data files:
  - `<path>`

## 6. Validation Plan

| Check | Command | Expected result |
|---|---|---|
| `<check>` | `<command>` | `<expected>` |

## 7. Files Intentionally Ignored

| File/folder | Reason |
|---|---|
| `<path>` | `<reason>` |

## 8. Completion Criteria

- [ ] Target method has a clear entry point.
- [ ] Definitions are updated in `docs/definitions.md`.
- [ ] Method is added to `docs/method_registry.md`.
- [ ] Lightweight checks pass.
- [ ] Formal outputs write `outputs_manifest.json`.

