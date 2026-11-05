"""Saya memeriksa aset, tautan lokal, metadata, dan kontras dua tema."""

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import pytest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


@pytest.fixture
def page():
    result = Page()
    result.feed((ROOT / "index.html").read_text())
    return result


def test_document_semantics_and_metadata(page):
    assert [a for t, a in page.tags if t == "html"][0]["lang"] == "id"
    assert len([t for t, _ in page.tags if t == "h1"]) == 1
    assert len([t for t, _ in page.tags if t == "main"]) == 1
    assert not [t for t, _ in page.tags if t == "script"]
    meta = [a for t, a in page.tags if t == "meta"]
    for key in ["description", "viewport"]:
        assert any(a.get("name") == key and a.get("content") for a in meta)
    for key in ["og:title", "og:description", "og:image", "og:url"]:
        assert any(a.get("property") == key and a.get("content") for a in meta)
    ids = [a["id"] for _, a in page.tags if "id" in a]
    assert len(ids) == len(set(ids))


def test_local_links_and_fragment_targets(page):
    ids = {a["id"] for _, a in page.tags if "id" in a}
    for _, attrs in page.tags:
        for name in ["src", "href"]:
            value = attrs.get(name, "")
            target = urlsplit(value)
            if not value or target.scheme or target.netloc:
                continue
            if target.path:
                assert (ROOT / unquote(target.path)).exists(), value
            if target.fragment:
                assert target.fragment in ids, value


def test_image_dimensions_and_total_size(page):
    for tag, attrs in page.tags:
        if tag == "img":
            assert attrs.get("alt")
            with Image.open(ROOT / attrs["src"]) as image:
                assert image.width <= 800
                assert (int(attrs["width"]), int(attrs["height"])) == image.size
    published = [ROOT / "index.html", ROOT / "style.css", *(ROOT / "assets").iterdir()]
    assert sum(p.stat().st_size for p in published) < 2_000_000


def luminance(value):
    rgb = [int(value[i : i + 2], 16) / 255 for i in [1, 3, 5]]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return sum(v * w for v, w in zip(linear, [0.2126, 0.7152, 0.0722]))


def contrast(a, b):
    hi, lo = sorted([luminance(a), luminance(b)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


@pytest.mark.parametrize("theme", ["light", "dark"])
def test_text_palette_meets_wcag_aa(theme):
    css = (ROOT / "style.css").read_text()
    roots = re.findall(r":root\{([^}]+)\}", css)
    palette = dict(re.findall(r"--([a-z-]+):(#[0-9a-fA-F]{3,6})", roots[0]))
    if theme == "dark":
        palette.update(dict(re.findall(r"--([a-z-]+):(#[0-9a-fA-F]{3,6})", roots[1])))
    palette = {
        k: ("#" + v[1:] * 2 if len(v) == 4 and len(set(v[1:])) == 1 else v)
        for k, v in palette.items()
    }
    pairs = [
        ("ink", "paper"),
        ("muted", "paper"),
        ("ink", "surface"),
        ("muted", "surface"),
        ("accent", "paper"),
        ("ink", "band"),
        ("muted", "band"),
        ("ink", "soft"),
        ("button-text", "button"),
        ("contact-text", "contact"),
    ]
    for foreground, background in pairs:
        assert contrast(palette[foreground], palette[background]) >= 4.5, (
            theme,
            foreground,
            background,
        )


def test_responsive_and_motion_preferences_are_present():
    css = (ROOT / "style.css").read_text()
    assert "@media(max-width:650px)" in css
    assert "grid-template-columns:1fr" in css
    assert "prefers-color-scheme:dark" in css
    assert "prefers-reduced-motion:reduce" in css
    assert "overflow-wrap:anywhere" in css
