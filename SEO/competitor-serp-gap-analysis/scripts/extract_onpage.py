#!/usr/bin/env python3
"""Extract comparable on-page SEO signals from HTML files using the stdlib."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


SPACE_RE = re.compile(r"\s+")


def clean(value: str) -> str:
    return SPACE_RE.sub(" ", value).strip()


class OnPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.headings: dict[str, list[str]] = {"h1": [], "h2": [], "h3": []}
        self.meta: dict[str, str] = {}
        self.canonical: str | None = None
        self.hreflang: list[dict[str, str]] = []
        self.jsonld_raw: list[str] = []
        self.link_count = 0
        self.internal_candidates = 0
        self.image_count = 0
        self.images_with_alt = 0
        self.visible_parts: list[str] = []
        self._capture: str | None = None
        self._capture_parts: list[str] = []
        self._hidden_depth = 0
        self._jsonld = False
        self._jsonld_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs = {k.lower(): (v or "") for k, v in attrs_list}
        if tag in {"script", "style", "noscript", "template"}:
            self._hidden_depth += 1
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self._jsonld = True
            self._jsonld_parts = []
        if tag == "title":
            # Capture only the document title. Inline SVGs commonly contain
            # accessibility <title> nodes that must not be appended to it.
            if not self.title_parts and self._capture is None:
                self._capture = tag
                self._capture_parts = []
        elif tag in {"h1", "h2", "h3"}:
            self._capture = tag
            self._capture_parts = []
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property") or attrs.get("http-equiv")
            content = clean(attrs.get("content", ""))
            if key and content:
                self.meta[key.lower()] = content
        if tag == "link":
            rel = {part.lower() for part in attrs.get("rel", "").split()}
            href = attrs.get("href", "")
            if "canonical" in rel and href:
                self.canonical = href
            if "alternate" in rel and attrs.get("hreflang") and href:
                self.hreflang.append({"lang": attrs["hreflang"], "href": href})
        if tag == "a" and attrs.get("href"):
            self.link_count += 1
            if attrs["href"].startswith(("/", "#")):
                self.internal_candidates += 1
        if tag == "img":
            self.image_count += 1
            if clean(attrs.get("alt", "")):
                self.images_with_alt += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._capture == tag:
            value = clean("".join(self._capture_parts))
            if value:
                if tag == "title":
                    self.title_parts.append(value)
                else:
                    self.headings[tag].append(value)
            self._capture = None
            self._capture_parts = []
        if tag == "script" and self._jsonld:
            value = "".join(self._jsonld_parts).strip()
            if value:
                self.jsonld_raw.append(value)
            self._jsonld = False
            self._jsonld_parts = []
        if tag in {"script", "style", "noscript", "template"} and self._hidden_depth:
            self._hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._capture_parts.append(data)
        if self._jsonld:
            self._jsonld_parts.append(data)
        elif not self._hidden_depth:
            value = clean(data)
            if value:
                self.visible_parts.append(value)


def jsonld_types(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        item_type = value.get("@type")
        if isinstance(item_type, str):
            found.add(item_type)
        elif isinstance(item_type, list):
            found.update(str(item) for item in item_type)
        for child in value.values():
            found.update(jsonld_types(child))
    elif isinstance(value, list):
        for child in value:
            found.update(jsonld_types(child))
    return found


def extract(path: Path) -> dict[str, Any]:
    parser = OnPageParser()
    text = path.read_text(encoding="utf-8", errors="replace")
    parser.feed(text)
    types: set[str] = set()
    invalid_jsonld = 0
    for raw in parser.jsonld_raw:
        try:
            types.update(jsonld_types(json.loads(raw)))
        except json.JSONDecodeError:
            invalid_jsonld += 1
    visible = clean(" ".join(parser.visible_parts))
    return {
        "file": path.name,
        "title": clean(" ".join(parser.title_parts)) or None,
        "meta_description": parser.meta.get("description"),
        "meta_robots": parser.meta.get("robots"),
        "canonical": parser.canonical,
        "hreflang": parser.hreflang,
        "headings": parser.headings,
        "jsonld_types": sorted(types),
        "invalid_jsonld_blocks": invalid_jsonld,
        "open_graph": {k: v for k, v in parser.meta.items() if k.startswith("og:")},
        "twitter": {k: v for k, v in parser.meta.items() if k.startswith("twitter:")},
        "visible_word_count": len(visible.split()),
        "link_count": parser.link_count,
        "relative_or_fragment_link_count": parser.internal_candidates,
        "image_count": parser.image_count,
        "images_with_nonempty_alt": parser.images_with_alt,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="HTML file or directory containing HTML files")
    ap.add_argument("-o", "--output", type=Path, help="Write JSON to this file")
    args = ap.parse_args()
    paths = sorted(args.input.glob("*.html")) if args.input.is_dir() else [args.input]
    if not paths:
        ap.error("no HTML files found")
    result = [extract(path) for path in paths]
    payload = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
