# Flow Telemetry

Log flow data so we can answer: "Are review phases still worth running?" and "Do Quick Fix flows stay quick?"

## When to Log

Append one JSONL line to `~/.claude/skills/kin-vibe-coding/data/flow-history.jsonl` at each of these events:

1. **Flow start** — After Phase -1 classification
2. **Phase transition** — When any phase gate passes (or phase is skipped)
3. **Review finding** — When a review phase surfaces Critical or Important findings
4. **Flow end** — When Phase 9 completes or the flow is abandoned

## Schema

```jsonl
{"ts":"2026-04-07T14:30:00Z","project":"pace-pipeline","feature":"ooo-toggle","event":"flow_start","complexity":"standard","notes":null}
{"ts":"2026-04-07T14:35:00Z","project":"pace-pipeline","feature":"ooo-toggle","event":"phase_complete","phase":"0_research","skipped":false,"notes":null}
{"ts":"2026-04-07T15:10:00Z","project":"pace-pipeline","feature":"ooo-toggle","event":"phase_complete","phase":"3_design_review","skipped":false,"notes":"2 Critical findings"}
{"ts":"2026-04-07T18:00:00Z","project":"pace-pipeline","feature":"ooo-toggle","event":"flow_end","outcome":"merged","phases_used":7,"phases_skipped":3,"notes":null}
```

## Fields

| Field | Type | Description |
|---|---|---|
| `ts` | ISO 8601 | When the event occurred |
| `project` | string | Repository/project name |
| `feature` | string | Feature name from FLOW-STATUS.md |
| `event` | enum | `flow_start`, `phase_complete`, `review_finding`, `flow_end` |
| `complexity` | enum | `quick_fix`, `standard`, `complex` (flow_start only) |
| `phase` | string | Phase identifier, e.g. `0_research`, `3_design_review` (phase events only) |
| `skipped` | bool | Whether the phase was skipped (phase events only) |
| `outcome` | enum | `merged`, `pr_created`, `parked`, `abandoned` (flow_end only) |
| `phases_used` | int | Count of non-skipped phases (flow_end only) |
| `phases_skipped` | int | Count of skipped phases (flow_end only) |
| `notes` | string | Freeform — finding counts, blockers, surprises |

## How to Log

Use a single Bash call. The orchestrator appends directly:

```bash
echo '{"ts":"...","project":"...","feature":"...","event":"..."}' >> ~/.claude/skills/kin-vibe-coding/data/flow-history.jsonl
```

Create the data directory on first use if it doesn't exist.

## Analysis

After 10+ flows, the telemetry answers:
- **Are plan reviews load-bearing?** Compare `review_finding` events at Phase 5 vs Phase 3. If Phase 5 rarely surfaces Critical findings, it's ceremony.
- **Does complexity classification hold?** Compare actual `phases_used` against the class default. If Quick Fix flows consistently use more phases, the heuristics need tuning.
- **Where does time go?** Phase durations (inferred from `ts` gaps) show which phases are expensive.
