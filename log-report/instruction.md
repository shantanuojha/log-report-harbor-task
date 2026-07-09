Parse the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains a single JSON object.
2. The JSON object has exactly these keys: `total_requests`, `unique_ips`, and
   `top_path`.
3. The JSON values summarize `/app/access.log`: `total_requests` is `6`,
   `unique_ips` is `3`, and `top_path` is `/index.html`.
