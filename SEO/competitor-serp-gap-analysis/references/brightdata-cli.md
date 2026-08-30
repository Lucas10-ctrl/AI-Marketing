# Bright Data CLI Notes

Load this reference when installing/authenticating the CLI, selecting exact flags, or troubleshooting a collection run.

## Runtime

- Node.js 20 or newer is required.
- Portable invocation: `npx --yes --package @brightdata/cli bdata <command>`.
- `bdata` and `brightdata` are aliases for the same CLI.

## Authentication

Interactive login:

```bash
npx --yes --package @brightdata/cli bdata login
npx --yes --package @brightdata/cli bdata budget
```

Headless environments may use `BRIGHTDATA_API_KEY`. Never echo it or display the full environment.

Credential directories:

- macOS: `~/Library/Application Support/brightdata-cli/`
- Linux: `~/.config/brightdata-cli/`
- Windows: `%APPDATA%\brightdata-cli\`

Never print `credentials.json`.

## Search

```bash
bdata search "query" --engine google --country us --language en \
  --device desktop --json -o serp.json
```

Relevant fields normally include `organic[].rank`, `organic[].title`, `organic[].link`, and `organic[].description`. Conditional feature blocks may include People Also Ask, related searches, local results, shopping, or hotels. Do not assume every key exists.

Useful flags:

- `--engine google|bing|yandex`
- `--country <two-letter-code>`
- `--language <code>`
- `--page <zero-based-number>`
- `--type web|news|images|shopping`
- `--device desktop|mobile`

## Scrape

```bash
bdata scrape "https://example.com" -f html --country us -o page.html
```

Formats: `markdown`, `html`, `json`, and `screenshot`. Raw HTML is required for this skill's metadata and structured-data comparison. Quote URLs, especially those containing `?` or `&`.

## Cost and run discipline

- Run `bdata budget` before collection.
- State the number of SERP calls and page scrapes before a large run.
- Do not retry indefinitely. After two comparable failures for one URL, report the failed target and continue with the remaining sample unless the user requests deeper troubleshooting.
- Save long-running output to a file. Do not pipe a poller into `head` or another command that can close the pipe early.

## Sources

- Official CLI repository: https://github.com/brightdata/cli
- Official CLI overview: https://docs.brightdata.com/cli/overview
- Official examples: https://docs.brightdata.com/cli/examples
- Original MIT skill: https://github.com/IncomeStreamSurfer/brightdata-scraper-studio-skill
