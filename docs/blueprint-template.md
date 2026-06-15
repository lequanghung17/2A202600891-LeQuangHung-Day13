# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Individual - Le Quang Hung - Day 13 Observability Lab
- [REPO_URL]: Local workspace `C:\Users\PC\Downloads\2A202600891-LeQuangHung-Day13`
- [MEMBERS]:
  - Member A: Le Quang Hung | Role: Logging & PII
  - Member B: Le Quang Hung | Role: Tracing & Enrichment
  - Member C: Le Quang Hung | Role: SLO & Alerts
  - Member D: Le Quang Hung | Role: Load Test & Dashboard
  - Member E: Le Quang Hung | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 50 Langfuse `run` traces visible through the Langfuse API; screenshot evidence shows >= 10 traces.
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: `screenshots/correlation_id.png`
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: `screenshots/PII_redaction.png`
- [EVIDENCE_TRACE_LIST_SCREENSHOT]: `screenshots/tracing.png`
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: `screenshots/trace_detail.png`
- [VALIDATE_LOGS_SCREENSHOT]: `screenshots/validate_logs.png`
- [TRACE_WATERFALL_EXPLANATION]: The Langfuse trace shows the `run` span for the agent pipeline. It links the request to hashed user/session metadata, feature tags, model tag, token usage metadata, and the same request window as the JSON logs. This makes it possible to move from a slow request in metrics to the trace detail and then to logs by correlation/request context.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: `screenshots/6_panels.png`
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 2651ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.1034 observed total |
| Quality Score Avg | > 0.75 | 28d | 0.88 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: `screenshots/alert_rule.png`
- [SAMPLE_RUNBOOK_LINK]: `docs/alerts.md#1-high-latency-p95`

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: When `rag_slow` was enabled, load-test latency increased sharply. The incident run showed requests such as `req-527be54b` at 13437.9ms, `req-f683c70b` at 16697.5ms, and `req-2571555c` at 26356.8ms. This was much slower than the normal request path after the incident was disabled.
- [ROOT_CAUSE_PROVED_BY]: `screenshots/enable_rag_slow.png` shows the incident toggle set to `rag_slow=True`. `screenshots/trace_detail.png` and `screenshots/tracing.png` show Langfuse traces during the same lab run. The load-test output proves the latency spike while the toggle was enabled.
- [FIX_ACTION]: Disabled the incident with `scripts/inject_incident.py --scenario rag_slow --disable --base-url http://127.0.0.1:8001`; evidence is in `screenshots/disable_rag_slow.png`.
- [PREVENTIVE_MEASURE]: Keep the high latency P95 alert active, inspect slow Langfuse traces when it fires, add timeout/fallback behavior for slow retrieval, and use the runbook in `docs/alerts.md#1-high-latency-p95`.

---

## 5. Individual Contributions & Evidence

### [MEMBER_A_NAME]: Le Quang Hung - Logging & PII
- [TASKS_COMPLETED]: Implemented correlation IDs, JSON log enrichment, recursive PII scrubbing, and validated logs at 100/100.
- [EVIDENCE_LINK]: `app/middleware.py`, `app/main.py`, `app/logging_config.py`, `app/pii.py`, `screenshots/validate_logs.png`

### [MEMBER_B_NAME]: Le Quang Hung - Tracing & Enrichment
- [TASKS_COMPLETED]: Enabled Langfuse tracing with the v3 SDK, flushed traces after requests, and verified visible traces in Langfuse.
- [EVIDENCE_LINK]: `app/tracing.py`, `app/main.py`, `screenshots/tracing.png`, `screenshots/trace_detail.png`

### [MEMBER_C_NAME]: Le Quang Hung - SLO & Alerts
- [TASKS_COMPLETED]: Reviewed SLO targets and alert rules for latency, error rate, and cost spike. Linked alert evidence to the runbook.
- [EVIDENCE_LINK]: `config/slo.yaml`, `config/alert_rules.yaml`, `docs/alerts.md`, `screenshots/alert_rule.png`

### [MEMBER_D_NAME]: Le Quang Hung - Load Test & Dashboard
- [TASKS_COMPLETED]: Ran load tests, added configurable `--base-url` support, collected `/metrics`, and prepared the 6-panel dashboard evidence.
- [EVIDENCE_LINK]: `scripts/load_test.py`, `scripts/inject_incident.py`, `screenshots/6_panels.png`

### [MEMBER_E_NAME]: Le Quang Hung - Demo & Report
- [TASKS_COMPLETED]: Tested the `rag_slow` incident, collected evidence screenshots, and completed the lab report.
- [EVIDENCE_LINK]: `screenshots/enable_rag_slow.png`, `screenshots/disable_rag_slow.png`, `docs/blueprint-template.md`

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Not claimed.
- [BONUS_AUDIT_LOGS]: Not claimed.
- [BONUS_CUSTOM_METRIC]: Not claimed.
