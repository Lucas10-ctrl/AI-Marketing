---
name: hermes-seo-setup
description: Build, resume, or inspect a secure Hermes-based SEO operating system through a durable Kanban board. Use when setting up Hermes for Search Console, GA4, SEO-data providers, website or CMS access, reporting, content proposals, draft creation, or scheduled SEO work.
license: MIT
metadata:
  hermes:
    tags: [seo, google-search-console, google-analytics, dataforseo, kanban, automation]
---

# Hermes SEO Setup

Build the SEO system incrementally and leave a resumable record. Hermes' native Kanban database is the preferred source of truth; chat history is not.

## Start or Resume

1. Read [references/workflow.md](references/workflow.md) and [references/native-kanban.md](references/native-kanban.md).
2. Check whether the installed Hermes version provides native multi-board Kanban. If it does, create or reuse the isolated `hermes-seo` board and seed its idempotent task graph. Do not duplicate tasks on resume.
3. If native Kanban is unavailable because the skill is running in Codex, Claude Code, or an older Hermes installation, copy [assets/SEO_SETUP_KANBAN_TEMPLATE.md](assets/SEO_SETUP_KANBAN_TEMPLATE.md) into the workspace as the fallback source of truth.
4. If the next card concerns an external connection, read only the relevant section of [references/integrations.md](references/integrations.md).
5. Inspect the environment with read-only operations, reconcile task state with reality, and work only the current native task or one fallback `IN_PROGRESS` card.

If the user asks for status, report the board without mutating external systems. If the user asks to resume, continue the highest-priority actionable card rather than restarting discovery.

## Kanban Rules

With native Hermes Kanban, use its current statuses, including `triage`, `todo`, `ready`, `running`, `blocked`, `review`, `scheduled`, `done`, and `archived` where supported.

- A task stays `running` while configuration and verification are both actionable.
- Block with `kind=needs_input` when a login, secret insertion, purchase, external authorization, consequential choice, or approval is required. Put one exact requested action in the reason or comment.
- Block with the appropriate dependency, capability, or transient reason for non-user failures. Record attempted checks and the exact unblock condition.
- Use `review` only when implementation is complete and a separate reviewer is genuinely part of the chosen workflow. Use `scheduled` for time-gated cards, not user-input waits.
- Complete only after the real acceptance test succeeds. Include sanitized evidence in the structured completion handoff.
- Use task comments for decisions, failed tests, approvals, and newly discovered constraints.
- Preserve failed verification evidence; do not recreate a clean task to hide prior attempts.
- Let dependency links promote downstream work. Do not manually bypass an unmet parent.

With the Markdown fallback, map `todo` to `BACKLOG`, `ready` to `READY`, `running` to `IN_PROGRESS`, `blocked/needs_input` to `WAITING_FOR_USER`, and `done` to `DONE`. Keep at most one fallback card `IN_PROGRESS`.

## Safety and Authority

- Start every service read-only. Draft, publish, merge, deploy, delete, billing, IAM, user-management, DNS, and external-send access require separate explicit approval.
- Never ask the user to paste secrets into chat. Give the exact secret name and approved storage location, then wait while the user inserts it.
- For Hermes, keep secrets in `~/.hermes/.env` or a supported secret manager and non-secret behavior in `~/.hermes/config.yaml`. Do not commit credential files or OAuth tokens.
- Verify current commands, scopes, APIs, and configuration formats against official documentation before using them. Record the source and access date on the card.
- Inspect before editing. Preserve existing configuration and unrelated changes.
- Do not purchase services, provision paid infrastructure, install unreviewed code, broaden OAuth scopes, create schedules, or modify production without approval immediately before the action.
- Prefer native integrations, then Nous-reviewed MCP catalog entries, then official SDKs, then minimal direct API adapters.
- Inspect third-party MCP manifests and expose only necessary tools. Treat servers not controlled or reviewed by the user as untrusted.

## Execution Pattern

For the active card:

1. Restate its outcome and acceptance test.
2. Inspect existing state.
3. Present material decisions before acting.
4. Perform safe local work and create non-secret configuration.
5. Block with `kind=needs_input` when manual authorization is required, with one concise action request. Use `WAITING_FOR_USER` only in the Markdown fallback.
6. After the user acts, run the recorded acceptance test.
7. Save sanitized evidence, update the connection registry, and move the card appropriately.
8. Continue automatically to the next safe card unless new authority is required.

Configuration existence is not verification. A Google connection is complete only after a real read succeeds; a messaging gateway is complete only after an approved destination receives a test; a CMS connection is complete only after the allowed read or draft operation is confirmed.

## Required Outputs

Maintain these workspace artifacts when their cards become active:

- Native `hermes-seo` Kanban board, or `SEO_SETUP_KANBAN.md` only as a fallback.
- `SEO_SETUP_SUMMARY.md` — optional human-readable architecture and current-state snapshot; never treat it as fresher than the native board.
- `SEO_CONNECTIONS.md` — service, purpose, method, permissions, secret names, verification, and revocation. Never secret values.
- `BUSINESS_CONTEXT.md` — approved business and editorial facts; mark assumptions.
- `SEO_OPERATING_RULES.md` — approval gates and prohibited actions.
- `EDITORIAL_WORKFLOW.md` — evidence → interview → outline → approval → draft → fact-check → preview → approval → publish.
- `.env.example` or equivalent — variable names only, using names confirmed by the selected integrations.

At each pause, tell the user what changed, what was verified, which card is active, and the single next action. At completion, provide the architecture, connections, permissions, recurring costs, schedules, and exact pause/revocation instructions.

## Bootstrap Distribution

When the skill is not installed, the user can paste [assets/COPY_PASTE_BOOTSTRAP.md](assets/COPY_PASTE_BOOTSTRAP.md) into Hermes, Codex, or Claude Code to create the board and begin discovery.
