# Integration Playbook

Read only the section needed for the active connection card. Verify all commands and scopes against current official documentation; this file defines behavior, not frozen vendor syntax.

## Hermes Base

- Get one clean model-backed conversation working before gateway, MCP, skills, cron, or routing work.
- Check the installed CLI's diagnostics and configuration paths.
- Secrets belong in `~/.hermes/.env` or a supported secret manager. Non-secret behavior belongs in `~/.hermes/config.yaml`.
- Keep secret redaction and dangerous-command approvals enabled. Do not enable YOLO or disable approvals.
- For an always-on system, explain local versus isolated VPS tradeoffs and costs; provisioning requires approval.

Verification: one inexpensive conversation succeeds, configuration diagnostics are healthy or warnings are documented, and safety settings are recorded.

## Messaging

- Use the current Hermes gateway setup for the selected platform.
- Use a dedicated bot/app when supported and pair or allowlist only approved identities.
- Do not place bot tokens in chat or ordinary config.
- Test with a non-sensitive status message. Record how to revoke the pairing and rotate the bot token.

Verification: the approved destination receives a message from the intended Hermes profile and model.

## Google Search Console and GA4

- Use a dedicated, recognizable Google Cloud project.
- Determine which APIs and OAuth scopes the chosen adapter actually requires; do not automatically enable every similarly named Analytics API.
- Begin with read-only scopes and no Google Cloud billing or IAM administration.
- Transfer OAuth client files to the host securely, restrict file permissions where supported, and exclude them from version control.
- Interactive browser authorization is a user action. Pause and provide one clear instruction.

GSC verification: list properties, select one with the user, then retrieve a 28-day search-performance summary. Do not change users, sitemaps, or indexing state.

GA4 verification: list properties, select one with the user, then retrieve a 28-day organic landing-page and engagement summary. Do not alter events, audiences, attribution, streams, or users.

## SEO-Data Provider

- Check native tools, the Nous-reviewed MCP catalog, official SDKs, and minimal API access in that order.
- Inspect installation and runtime commands before adding an MCP server; enable only needed tools.
- Use a dedicated credential, spending alert or cap, rate limit, and small initial result limit where supported.
- Store login and password or API key outside chat.

Verification: query no more than ten results for one domain, country, and language; record request cost or count when the provider exposes it.

## Website, CMS, or Repository

- Begin read-only with a dedicated service identity and the narrowest resource scope.
- GitHub: prefer a fine-grained credential restricted to the required repository; exclude organization, workflow, secrets, and administration permissions.
- CMS: use the lowest role able to read content. Do not grant publishing, plugins, users, billing, domain, or production settings.
- Custom API: document endpoints and authentication, and write a minimal adapter only after design approval.

Verification: read one known page title/modification date or one known non-sensitive repository file.

Draft-only access is a later, separately approved card. A draft test must remain private, unmerged, unpublished, and undeployed.

## Scheduled Work

- Scheduled prompts must be self-contained because runs may start in fresh sessions.
- Separate the read-only health report from the content-opportunity proposal.
- Pin or document the model and cost behavior where the scheduler supports it.
- Use an explicit approved delivery target.
- Show the complete schedule and prompt before creation.
- Never give a scheduled job authority to publish, deploy, submit URLs, change analytics, or recursively create schedules.

Verification: list the jobs, show next run times, then perform one user-approved manual run and confirm delivery.

## Current Official References

- Hermes quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Hermes configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- Hermes security: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Hermes secrets: https://hermes-agent.nousresearch.com/docs/user-guide/secrets
- Hermes MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Hermes cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- Google Search Console API: https://developers.google.com/webmaster-tools
- Google Analytics Data API: https://developers.google.com/analytics/devguides/reporting/data/v1

Treat these as starting points and confirm that the relevant page is current before acting.
