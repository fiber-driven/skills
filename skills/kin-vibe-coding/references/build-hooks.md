# Build Phase Hooks

Mechanical enforcement for Phase 6 guardrails. The orchestrator manages hook lifecycle — activate on Phase 6 entry, deactivate on Phase 6 exit.

## State File

`/tmp/vibe-build-state.json` tracks build-phase discipline:

```json
{"phase": "build", "test_failed": false, "debug_invoked": false, "fix_attempts": 0}
```

### State Transitions

| Event | State Change |
|---|---|
| Phase 6 starts | Create state file with defaults |
| Test fails or unexpected behavior | Set `test_failed: true` |
| `/systematic-debugging` invoked | Set `debug_invoked: true`, reset `fix_attempts: 0` |
| Edit/Write applied as a fix attempt | Increment `fix_attempts` |
| Fix succeeds (test passes) | Reset `test_failed: false`, `debug_invoked: false`, `fix_attempts: 0` |
| Phase 6 ends | Delete state file |

### How the Orchestrator Updates State

```bash
# Create on Phase 6 start
echo '{"phase":"build","test_failed":false,"debug_invoked":false,"fix_attempts":0}' > /tmp/vibe-build-state.json

# Update a field (e.g., after test failure)
python3 -c "
import json
s = json.load(open('/tmp/vibe-build-state.json'))
s['test_failed'] = True
json.dump(s, open('/tmp/vibe-build-state.json', 'w'))
"

# Delete on Phase 6 exit
rm -f /tmp/vibe-build-state.json
```

## Hook Script

`scripts/build-guard.sh` — runs on PreToolUse for Edit and Write during build phase.

**Behavior:**
- No state file → silent pass (not in build phase)
- Test failed + no debugging → prints warning reminder
- 3+ fix attempts → prints "stop and ask the user" reminder
- All warnings are advisory (exit 0) — the orchestrator enforces, the hook reminds

## Hook Registration

The orchestrator should tell the user to add this hook when first using the skill. It only needs to be added once:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/skills/kin-vibe-coding/scripts/build-guard.sh",
            "timeout": 3
          }
        ]
      }
    ]
  }
}
```

The hook is always-on but no-ops when the state file doesn't exist (i.e., outside Phase 6). No need to register/deregister per session.
