# Copy-Paste Bootstrap Prompt

Paste the text below into Hermes, Codex, or Claude Code from the machine or VPS where Hermes should run.

```text
Set up a secure Hermes SEO operating system for me through a durable Kanban
board. Work as an implementation agent, not merely an advisor.

First check whether a skill named `hermes-seo-setup` is installed. If it is,
load and follow it.

Then check whether this Hermes installation supports the native durable
multi-board Kanban. Confirm current syntax from official Hermes documentation.
If supported, create or reuse an isolated board with slug `hermes-seo`, seed the
linked task graph below with stable idempotency keys, and use that SQLite-backed
board as the source of truth. Do not duplicate tasks when this prompt is run
again. Put the first task in `ready` and dependent tasks in `todo`; do not use
`triage`, because automatic decomposition could duplicate this deliberate
graph.

Include the complete outcome, safety constraints, acceptance test, and approval
boundary in every native task body. If the skill is installed, attach
`hermes-seo-setup` to each task so dispatcher-spawned workers load it.

If native Kanban is unavailable because you are running in Codex, Claude Code,
or an older Hermes version, create `SEO_SETUP_KANBAN.md` as a fallback with
BACKLOG, READY, IN_PROGRESS, WAITING_FOR_USER, DONE, and BLOCKED columns.

Configuration is not completion: a task moves to `done` only after a real
acceptance test succeeds and sanitized evidence is recorded in its completion
handoff. Use task comments for decisions, approvals, failed tests, and retry
conditions so another session or profile can resume the work.

Create this backlog:

FOUND-01  Discover the environment
BASE-01   Establish a healthy Hermes installation and model connection
MSG-01    Connect and verify one messaging gateway
GCP-01    Configure minimum-scope Google OAuth
GSC-01    Connect and verify Google Search Console read-only
GA4-01    Connect and verify Google Analytics 4 read-only
SEO-01    Connect and verify DataForSEO or another approved SEO-data provider
SITE-01   Connect and verify the website, CMS, or repository read-only
CTX-01    Interview me and create approved BUSINESS_CONTEXT.md
FLOW-01   Create the human-approved editorial workflow and operating rules
TEST-01   Run one evidence-backed SEO opportunity test and produce an outline
DRAFT-01  Optionally add separately approved draft-only write access
CRON-01   Optionally schedule a read-only report and separate opportunity brief
SEC-01    Complete the permission, cost, verification, and revocation review

Create dependency links in this order:

FOUND-01 -> BASE-01
BASE-01 -> MSG-01, GCP-01, SEO-01, SITE-01
GCP-01 -> GSC-01, GA4-01
GSC-01 + GA4-01 + SEO-01 + SITE-01 -> CTX-01
CTX-01 -> FLOW-01 -> TEST-01
TEST-01 -> optional DRAFT-01
TEST-01 + MSG-01 -> optional CRON-01

Create SEC-01 after I decide which optional cards are in scope, so skipped
optional features cannot block the final review.

Start every external service read-only. Never infer permission to publish,
merge, deploy, delete, change DNS, administer users, access billing, broaden
OAuth scopes, install unreviewed code, purchase services, create schedules, or
send external messages. Ask for approval immediately before those actions.

Never ask me to paste secrets into chat. Tell me the exact secret name and
secure storage location, then wait while I add it. For Hermes, keep secrets in
`~/.hermes/.env` or a supported secret manager and non-secret behavior in
`~/.hermes/config.yaml`. Keep secret redaction and dangerous-command approvals
enabled; do not use YOLO or unrestricted execution. Do not commit credential
files or tokens.

Before using commands, APIs, OAuth scopes, configuration formats, or MCP
servers, check current official documentation. Prefer native integrations,
then Nous-reviewed MCP catalog entries, then official SDKs, then minimal direct
API adapters. Inspect third-party MCP manifests and expose only necessary
tools.

For each connection, record service, purpose, method, permissions, secret
names and storage location without values, verification test and result,
write capabilities deliberately disabled, cost controls, and revocation.

Maintain these artifacts as their cards become active:

- Native `hermes-seo` Kanban board, or SEO_SETUP_KANBAN.md only as fallback
- SEO_SETUP_SUMMARY.md when a human-readable snapshot is useful
- SEO_CONNECTIONS.md
- BUSINESS_CONTEXT.md
- SEO_OPERATING_RULES.md
- EDITORIAL_WORKFLOW.md
- .env.example or an equivalent containing names only

Begin with FOUND-01. Inspect the current environment using read-only
operations. Determine the OS, shell, active harness, Hermes installation and
version, local versus VPS placement, current workspace and website stack,
existing config, gateways, MCPs, skills, schedules, and integrations. Do not
display secret-file contents.

Then show me what you discovered, the proposed architecture, security
concerns, missing information, the board location, and the first decision or
manual action you need. Continue automatically through safe, local, reversible
work. Pause only for a login, secret insertion, purchase, external
authorization, consequential choice, unreviewed install, write permission,
schedule creation, production change, or external message.
```
