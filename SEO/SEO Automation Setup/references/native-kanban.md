# Native Hermes Kanban

Use Hermes' current durable multi-board Kanban when available. It stores tasks in SQLite, supports dependencies and comments, survives restarts, and appears in the Hermes dashboard.

## Board Setup

1. Confirm current syntax with `hermes kanban --help` and official documentation.
2. List boards. Reuse a board whose slug is exactly `hermes-seo`; do not create a duplicate.
3. Otherwise create `hermes-seo` with a descriptive display name and switch or target it explicitly.
4. Seed the task graph from `workflow.md` with stable idempotency keys such as `hermes-seo-setup:FOUND-01`. Put the relevant outcome, constraints, acceptance test, and approval boundary in every task body so the board remains usable even if the skill is later unavailable.
5. Use the user's chosen workspace directory for tasks that must leave durable project artifacts. Do not use an ephemeral scratch workspace for business context, operating rules, adapters, or configuration deliverables unless those artifacts are explicitly attached on completion.
6. Assign tasks to the selected Hermes profile only after confirming that profile exists. Do not invent an assignee. Attach `--skill hermes-seo-setup` when the installed version supports task skills.

Useful human surfaces, subject to current CLI confirmation:

```text
hermes kanban boards list
hermes kanban boards create hermes-seo --name "Hermes SEO Setup"
hermes kanban --board hermes-seo list
hermes kanban --board hermes-seo watch
hermes dashboard
```

Agents spawned by the dispatcher use `kanban_*` tools rather than shelling out to the CLI. An orchestrator profile needs the `kanban` toolset to list, create, link, comment on, and unblock work outside a spawned task.

## Seeded Task Graph

Create these tasks with the complete outcome, constraints, acceptance criteria, and relevant skill attached:

| Key | Title | Parents |
|---|---|---|
| `FOUND-01` | Discover SEO-agent environment | — |
| `BASE-01` | Establish healthy Hermes base | `FOUND-01` |
| `MSG-01` | Connect messaging gateway | `BASE-01` |
| `GCP-01` | Prepare Google Cloud and OAuth | `BASE-01` |
| `GSC-01` | Verify Search Console read-only | `GCP-01` |
| `GA4-01` | Verify GA4 read-only | `GCP-01` |
| `SEO-01` | Connect SEO-data provider | `BASE-01` |
| `SITE-01` | Connect site or repository read-only | `BASE-01` |
| `CTX-01` | Capture approved business context | `GSC-01`, `GA4-01`, `SEO-01`, `SITE-01` |
| `FLOW-01` | Establish editorial approval workflow | `CTX-01` |
| `TEST-01` | Run one SEO opportunity test | `FLOW-01` |
| `DRAFT-01` | Add optional draft-only write access | `TEST-01` plus explicit approval |
| `CRON-01` | Add optional reports and proposal schedules | `TEST-01`, `MSG-01` plus explicit approval |
| `SEC-01` | Complete security and revocation review | Create when the user confirms which optional cards are in scope |

Do not make optional `DRAFT-01` or `CRON-01` hard parents of the final security review. An intentionally skipped optional feature must not prevent completion.

Create the first task in `ready`; dependent tasks remain `todo` until their parents complete. Do not put seeded tasks in `triage`, because automatic decomposition could duplicate the deliberate graph.

## Worker Lifecycle

At the beginning of a dispatched task, call `kanban_show` and read the full context and comment history. During long work, send heartbeats. Add comments for decisions or evidence that a later attempt needs.

On success, call `kanban_complete` with:

- concise result;
- verification method and timestamp;
- sanitized evidence;
- artifacts and their durable paths;
- permissions enabled and deliberately withheld;
- cost or usage controls;
- revocation path;
- recommended follow-up.

When user action is required, call `kanban_block` with `kind=needs_input`, a single exact requested action, and a statement of what will be verified afterward. Resume by commenting with the user's response and unblocking the task through the orchestrator or human surface.

Never mark a task done because a configuration file exists. Verification belongs in the same task unless a separate verification task is explicitly useful.

## Dashboard

When native Kanban is initialized, tell the user they can view the visual board with `hermes dashboard` and open the Kanban tab. Do not expose the dashboard publicly or weaken authentication merely for convenience.

Official reference: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
