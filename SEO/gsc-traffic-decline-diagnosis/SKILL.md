---
name: gsc-traffic-decline-diagnosis
description: Diagnose organic traffic drops with Composio GSC data.
version: 1.0.2
author: Lucas (Lucas10-ctrl), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [seo, google-search-console, traffic-decline, composio, mcp]
    category: research
    related_skills: [gsc-keyword-cannibalization-report, competitor-serp-gap-analysis]
---

# GSC Traffic Decline Diagnosis

Use Google Search Console data gathered through Composio MCP to diagnose an organic search traffic decline. Complete the four diagnostic steps, distinguish observations from causes, and write a read-only evidence report rather than changing the site or Search Console.

## When to Use

- Organic clicks, impressions, CTR, or rankings appear to have declined.
- The user wants an AI agent to compare Search Console periods and isolate affected pages or queries.
- The user needs a reproducible diagnosis before commissioning technical, content, cannibalization, or competitor analysis.

Do not use this skill for GA4-only traffic changes, live rank tracking, or implementing recovery changes. Load the dedicated cannibalization or competitor-gap skill only after this diagnosis supports that next step.

## Prerequisites

- Composio MCP is available in the AI client.
- The Composio Google Search Console toolkit is connected through OAuth with read access to the intended verified property.
- The connection exposes `GOOGLE_SEARCH_CONSOLE_LIST_SITES`, `GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY`, and, when needed, `GOOGLE_SEARCH_CONSOLE_INSPECT_URL` and `GOOGLE_SEARCH_CONSOLE_LIST_SITEMAPS`.
- Never request or store Google passwords, OAuth tokens, MCP URLs, or Composio API keys in chat or in the report.

Discover the live tool schemas before calling them. Composio versions and MCP clients may expose different parameter wrappers. Use the property string exactly as returned by `GOOGLE_SEARCH_CONSOLE_LIST_SITES`, including protocol, trailing slash, subdomain, or `sc-domain:` prefix.

## Inputs and Defaults

Establish:

- Search Console property
- affected search type, default `web`
- current and comparison periods
- optional country, device, directory, or page-group filters

Unless the user supplies dates, use the latest 28 complete days ending three days ago and the preceding 28 days. For a seasonal business, also compare the same dates one year earlier when retained data permits. State all date choices and note that recent Search Console data may be incomplete.

If more than one plausible property is connected, ask the user to select one. Never guess between domain and URL-prefix properties.

## Procedure

### 1. Confirm the organic traffic drop

1. Call `GOOGLE_SEARCH_CONSOLE_LIST_SITES` and select the exact authorized property.
2. Query Search Analytics for both periods with `date` as the dimension and the same `search_type`, filters, and aggregation settings.
3. Retrieve every available row. Follow the live schema's pagination fields until a short or empty page proves exhaustion.
4. Compute period totals and absolute and percentage changes for clicks and impressions. Report Search Console's aggregate CTR and average position without averaging row-level CTR or position values.
5. Aggregate daily data into weeks to test whether the loss is sustained rather than a single-day fluctuation. Note weekday, holiday, reporting-lag, or seasonality effects that could distort the comparison.

**Complete when:** the report states whether a sustained decline exists, the exact periods and search type, and the click and impression deltas.

### 2. Segment the decline

Run separate, comparable Search Analytics queries for useful dimensions so broad totals do not hide a concentrated loss:

- `page`
- `query`
- `page` + `query` for priority losses
- `country`
- `device`
- `searchAppearance` when supported
- `date` combined with a priority segment when trend evidence is needed

Assess each Search type separately; never combine Web, Image, Video, News, Discover, or Google News rows into one diagnosis. Use dimension filters for approved page directories, countries, devices, or queries. Validate every filter because an invalid expression can look like a legitimate zero-row result.

Group queries by searcher task only after preserving the exact-query data. Label inferred clusters as analysis rather than raw GSC dimensions.

**Complete when:** the report names the page, query, search type, device, country, or appearance segments that explain the loss and identifies segments that remained stable or improved.

### 3. Compare clicks, impressions, CTR, and average position

Classify each priority page/query segment using all four metrics:

| Evidence pattern | First hypothesis to test | Do not conclude yet |
|---|---|---|
| Clicks down; impressions and position stable | CTR, title/snippet, SERP features, AI Overviews | That rankings fell |
| Impressions and position down | Relevance, competitors, usefulness, technical changes | The specific cause of the ranking loss |
| Impressions down; position broadly stable | Demand or seasonality | That the page needs rewriting |
| Priority URL has no rows | Query volume, filters, property mismatch, or indexing | That the URL is deindexed |
| One directory or template declines | Section-level content, deployment, navigation, or canonical issue | That the whole domain was penalized |
| Several URLs appear for one exact query | Possible cannibalization requiring dedicated analysis | That overlap is harmful |

Use weighted period aggregates returned by Search Console. Never take a simple average of already aggregated CTR or position rows. Treat GSC data as directional because low-volume and anonymized queries may be omitted.

**Complete when:** every priority loss has an evidence pattern, a first hypothesis, an explicit uncertainty, and a recommended next check.

### 4. Check Search status, manual actions, and security

Composio's current Google Search Console toolkit exposes analytics, site, sitemap, and URL-inspection tools, but may not expose Manual Actions or Security Issues reports. Do not pretend those reports were checked through MCP.

1. Use `GOOGLE_SEARCH_CONSOLE_GET_SITE` or the listed-site response to confirm access and property status when available.
2. Use `GOOGLE_SEARCH_CONSOLE_INSPECT_URL` only for priority URLs whose disappearance or indexing state could explain material loss. Inspection data can lag and quotas apply.
3. Use `GOOGLE_SEARCH_CONSOLE_LIST_SITEMAPS` when a section-wide indexing or discovery issue is plausible. Treat submitted/indexed counts, errors, warnings, and pending state as supporting evidence, not proof of the traffic-loss cause.
4. Ask the user to open Search Console and verify **Manual Actions** and **Security Issues** manually if those tools are absent. Record the result as `clear`, `issue found`, or `not verified`.
5. If manual checks are not completed, keep those causes open and do not state that the site has no manual action or security issue.

**Complete when:** accessible Composio status evidence is recorded and Manual Actions and Security Issues are truthfully labeled as verified or not verified.

## Report Artifact

After completing the analysis, create a Markdown report with `write_file`. Do not stop at a chat summary.

- Save it as `reports/gsc-traffic-decline-<property-slug>-<current-period-end>.md` in the current workspace.
- Convert the property to a safe lowercase slug by removing the protocol and `sc-domain:` prefix and replacing non-alphanumeric runs with hyphens.
- Use the current comparison period's end date in `YYYY-MM-DD` format.
- If that path already exists, append a UTC timestamp to the filename rather than overwriting an earlier report.
- Keep the report self-contained. Include the inputs, evidence, calculations, limitations, and next actions needed to understand it without reading the chat.
- Do not include OAuth tokens, MCP URLs, Composio API keys, or unredacted account identifiers.

The report must contain these sections:

1. **Diagnosis summary** — property, periods, search type, sustained-drop result, and leading evidence pattern.
2. **Period comparison** — clicks, impressions, CTR, and average position for each period with absolute and percentage/percentage-point deltas.
3. **Segment findings** — query, page/query, country, device, search appearance, and search-type findings.
4. **Hypothesis matrix**:

| Priority | Segment | Evidence | Classification | First hypothesis | Evidence that would weaken it | Next check |
|---|---|---|---|---|---|---|

5. **Search status** — URL inspection and sitemap findings plus explicit Manual Actions and Security Issues verification state.
6. **Recommended next analysis** — only evidence-supported follow-ups, including the dedicated cannibalization or competitor-gap skill when appropriate.

After writing the file, return a short chat summary with the diagnosis, the report path, and any checks still marked `not verified`. The Markdown file is the primary deliverable.

## Pitfalls

- Search Console retains a limited history and omits some low-volume queries.
- Recent data can be incomplete; default to complete days.
- Zero rows can mean no impressions, an invalid filter, a property mismatch, insufficient access, or unavailable data.
- Average position is an aggregate, not a literal rank tracker.
- Search Analytics does not prove why rankings or clicks changed.
- Multiple URLs for one query are candidates for cannibalization analysis, not proof.
- Do not use mutating Composio tools such as Add Site, Delete Site, Submit Sitemap, or any indexing action during diagnosis.

## Verification

Before finishing:

- every comparison uses identical filters, dimensions, search type, and aggregation settings across periods
- pagination is exhausted or the report clearly states a row-limit constraint
- property strings and dates are preserved exactly
- CTR changes are expressed in percentage points and percentage change only when useful
- row-level CTR and position values were not naively averaged
- page/query totals are not presented as complete when GSC withheld data
- every causal statement is labeled as a hypothesis unless independently verified
- Manual Actions and Security Issues are marked `not verified` unless they were actually checked
- no site, Search Console, sitemap, or indexing setting was changed
- the Markdown report exists at the reported path and contains all six required sections
- the final response links or names the exact report path
