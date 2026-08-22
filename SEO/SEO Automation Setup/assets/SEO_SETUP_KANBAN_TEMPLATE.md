# Hermes SEO Setup Kanban

Last updated: <timestamp>
Workspace: <absolute path>
Hermes host: <local, VPS, or unknown>
Primary domain: <domain or unknown>
Market / language: <market> / <language>
Timezone: <timezone>

## Status Definitions

`BACKLOG` · prerequisites unmet  
`READY` · actionable now  
`IN_PROGRESS` · current card; maximum one  
`WAITING_FOR_USER` · named approval or manual action required  
`DONE` · acceptance evidence recorded  
`BLOCKED` · technical impasse and unblock condition recorded

## Board

| ID | Card | Status | Depends on | Next action | Evidence / blocker |
|---|---|---|---|---|---|
| FOUND-01 | Discover environment | READY | — | Inspect read-only state | — |
| BASE-01 | Establish healthy Hermes base | BACKLOG | FOUND-01 | — | — |
| MSG-01 | Connect messaging gateway | BACKLOG | BASE-01 | — | — |
| GCP-01 | Prepare Google Cloud and OAuth | BACKLOG | BASE-01 | — | — |
| GSC-01 | Verify Search Console | BACKLOG | GCP-01 | — | — |
| GA4-01 | Verify GA4 | BACKLOG | GCP-01 | — | — |
| SEO-01 | Connect SEO-data provider | BACKLOG | BASE-01 | — | — |
| SITE-01 | Connect site/CMS/repository read-only | BACKLOG | BASE-01 | — | — |
| CTX-01 | Capture approved business context | BACKLOG | GSC-01, GA4-01, SEO-01, SITE-01 | — | — |
| FLOW-01 | Establish editorial approval workflow | BACKLOG | CTX-01 | — | — |
| TEST-01 | Run one SEO opportunity test | BACKLOG | FLOW-01 | — | — |
| DRAFT-01 | Add draft-only write access | BACKLOG | TEST-01, explicit approval | — | — |
| CRON-01 | Schedule reports and proposals | BACKLOG | TEST-01, MSG-01, explicit approval | — | — |
| SEC-01 | Complete security review | BACKLOG | Implemented cards | — | — |

## Active Card

ID: <card ID or none>
Outcome: <observable outcome>
Acceptance test: <real verification>
Current step: <step>
Authority needed: <none or exact approval/manual action>

## Connection Registry

| Service | Purpose | Method | Permissions | Secret names/location | Last verification | Revocation | Status |
|---|---|---|---|---|---|---|---|

Never record secret values.

## Decisions

| Date | Decision | Reason | User approved? |
|---|---|---|---|

## Verification Log

| Date | Card | Test | Sanitized result | Source checked |
|---|---|---|---|---|

## Failures and Retry Notes

| Date | Card | Failure | Checks performed | Exact retry/unblock condition |
|---|---|---|---|---|

## Next User Action

<One concise action, or “None — agent may continue safely.”>
