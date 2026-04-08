#!/usr/bin/env bash
# Build-phase guard hook for kin-vibe-coding Phase 6.
#
# Checks a state file to enforce "debug before fixing" discipline.
# State file: /tmp/vibe-build-state.json
#
# The orchestrator creates this file when Phase 6 starts and removes it
# when Phase 6 ends. The hook reads it on every Edit/Write tool call
# to warn if a test failure occurred without systematic-debugging.
#
# State file schema:
#   {"phase":"build","test_failed":false,"debug_invoked":false,"fix_attempts":0}
#
# Exit codes:
#   0 = allow (no state file, or no violation)
#   Non-zero output to stderr = block with message

STATE_FILE="/tmp/vibe-build-state.json"

# No state file = not in build phase, allow everything
if [ ! -f "$STATE_FILE" ]; then
  exit 0
fi

# Read state
test_failed=$(python3 -c "import json; print(json.load(open('$STATE_FILE'))['test_failed'])" 2>/dev/null)
debug_invoked=$(python3 -c "import json; print(json.load(open('$STATE_FILE'))['debug_invoked'])" 2>/dev/null)
fix_attempts=$(python3 -c "import json; print(json.load(open('$STATE_FILE'))['fix_attempts'])" 2>/dev/null)

# If a test failed and debugging hasn't been invoked, warn
if [ "$test_failed" = "True" ] && [ "$debug_invoked" = "False" ]; then
  echo "VIBE GUARD: A test is failing but /systematic-debugging hasn't been invoked yet. Investigate root cause before editing code to fix it."
  exit 0  # Warn, don't block — the orchestrator enforces, the hook reminds
fi

# If 3+ fix attempts, warn
if [ "$fix_attempts" -ge 3 ] 2>/dev/null; then
  echo "VIBE GUARD: 3+ fix attempts on the same issue. Stop and ask the user before continuing."
  exit 0
fi

exit 0
