# Log Report Harbor Task

This repository contains a repaired Terminal-Bench 2 / Harbor task in
`log-report/`.

The task asks an agent to parse `/app/access.log` and write `/app/report.json`
with:

- `total_requests`
- `unique_ips`
- `top_path`

The verifier checks the exact JSON structure and values, writes reward to
`/logs/verifier/reward.txt`, and emits `/logs/verifier/ctrf.json`.

Expected validation:

```bash
harbor run -p . -i log-report -a oracle
harbor run -p . -i log-report --agent nop
```

The oracle should receive reward `1`; the no-op agent should receive reward `0`.
