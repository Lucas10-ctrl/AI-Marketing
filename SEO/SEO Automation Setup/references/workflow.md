# Kanban Workflow

The native Hermes board makes a long, interruption-prone setup resumable. Tasks are outcomes, not instructions to grant unlimited authority.

## Native Statuses

| Column | Meaning |
|---|---|
| `triage` | Rough work awaiting specification; do not use for the seeded setup graph. |
| `todo` | In scope but dependencies or review prevent dispatch. |
| `ready` | Dependencies are met and a worker may claim it. |
| `running` | A worker owns the current attempt. Configuration and verification occur in this task. |
| `blocked` | A named input, capability, dependency, authentication fix, or transient recovery is required. |
| `review` | Implementation is complete and an explicit reviewer is evaluating it. |
| `scheduled` | Work is waiting for a future time, not human input. |
| `done` | Acceptance test passed and a structured, sanitized handoff is recorded. |
| `archived` | Historical task intentionally hidden from the active workflow. |

Do not invent a separate native `verify` column. Configuration without a passing test remains `running`, or becomes `blocked` if the next verification step needs the user.

## Default Backlog and Exit Criteria

### `FOUND-01` Discover the environment

Inspect the OS, shell, harness, Hermes installation and version, local versus VPS placement, workspace, website stack, existing config, MCPs, skills, gateways, cron jobs, and integrations without revealing secret contents.

Done when the board records discovered state, recommended architecture, security concerns, missing information, and the next decision.

### `BASE-01` Establish a healthy Hermes base

Install or repair Hermes, configure one model provider, and verify a normal conversation before adding integrations. Confirm secret redaction and dangerous-command approval are active and unrestricted execution is off.

Done when the installed version, provider, model, diagnostic result, and a successful low-cost conversation test are recorded.

### `MSG-01` Connect one messaging gateway

Configure the user's selected supported platform with pairing or allowlisting. Send only a harmless test.

Done when the approved destination receives the test, unauthorized access is constrained, and revocation instructions are recorded.

### `GCP-01` Prepare Google Cloud and OAuth

Choose the current supported authentication method, enable only required APIs, request minimum read-only scopes, transfer credentials securely, and complete interactive authorization.

Done when token storage, scopes, account, revocation, and successful authentication are recorded without exposing credentials.

### `GSC-01` Verify Google Search Console

List accessible properties, let the user choose one, and retrieve a 28-day read-only performance summary.

Done when a real query returns clicks, impressions, CTR, position, top queries, and top pages for the selected property, or the board records a precise data-availability limitation.

### `GA4-01` Verify Google Analytics 4

List properties, let the user choose one, and retrieve a 28-day organic-traffic summary.

Done when a real query returns organic sessions, landing pages, engagement, and configured key events, with unavailable fields clearly identified.

### `SEO-01` Connect an SEO-data provider

Prefer a native or reviewed integration, store secrets outside chat, set usage controls where supported, and run one inexpensive domain/market/language query.

Done when provider, market, language, cost or request count, and a sample result are recorded and agree with the provider sufficiently to establish the connection.

### `SITE-01` Connect the website, CMS, or repository read-only

Select the least-privilege integration. Do not grant draft or production writes yet.

Done when Hermes reads one known, non-sensitive page or file and the board records the exact access and revocation path.

### `CTX-01` Capture approved business context

Interview the user in small groups about audience, offer, markets, evidence, expertise, brand voice, competitors, conversions, prohibited claims, and review requirements.

Done when the user approves `BUSINESS_CONTEXT.md`; only approved durable facts may enter persistent memory.

### `FLOW-01` Establish the editorial approval workflow

Write the evidence → interview → outline → approval → draft → fact-check → private preview → approval → publish process and prohibitions against fabricated experience, quotes, cases, claims, or statistics.

Done when the user approves `EDITORIAL_WORKFLOW.md` and `SEO_OPERATING_RULES.md`.

### `TEST-01` Run one opportunity test

Use GSC, GA4, external SEO data, site content, and approved context to propose no more than three evidence-backed opportunities. The user selects one; interview them and produce an outline only.

Done when one user-approved outline exists with evidence, intent, overlap check, business relevance, and human-experience inputs. No article is required.

### `DRAFT-01` Add draft-only write access

This card remains in `BACKLOG` until the user explicitly approves it after read-only tests. Add only the capability to create a private CMS draft or isolated local/branch change.

Done when an approved test draft or isolated diff is created, remains unpublished and undeployed, and its removal process is recorded.

### `CRON-01` Schedule reporting and proposals

Prepare two self-contained jobs: a read-only weekly health report and a separate opportunity proposal. Show schedules, destinations, model/API costs, and full prompts before creation.

Done when the user approves, the jobs are created, the next run times are visible, and one approved manual test delivers correctly. Jobs must not publish or recursively schedule work.

### `SEC-01` Complete the security and permission review

Inventory every service, connection, permission, secret location, read/write capability, scheduled access, verification, and revocation process. Flag overbroad access and paid APIs without controls.

Done when the final review and pause/revocation runbook are recorded. Recommendations do not authorize permission changes.

## Dependency Order

Default dependencies:

`FOUND-01` → `BASE-01` → `MSG-01`

`BASE-01` → `GCP-01` → (`GSC-01` and `GA4-01`)

`BASE-01` → `SEO-01`

`BASE-01` → `SITE-01`

(`GSC-01`, `GA4-01`, `SEO-01`, `SITE-01`) → `CTX-01` → `FLOW-01` → `TEST-01`

`TEST-01` → optional `DRAFT-01`

(`TEST-01`, `MSG-01`) → optional `CRON-01`

All implemented cards → `SEC-01`

Independent ready cards may be performed in another order when that reduces waiting, but never create more than one `IN_PROGRESS` card.

## Evidence Format

Record compact evidence in the completion handoff or task comment:

```text
Verified: 2026-08-22T14:30:00-05:00
Method: read-only API request
Result: 3 properties listed; selected sc-domain:example.com; 28-day query succeeded
Sensitive output: redacted
Source checked: official provider documentation, accessed 2026-08-22
```

Do not store access tokens, passwords, full OAuth payloads, personal identifiers, or unnecessary analytics data on the board.
