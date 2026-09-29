#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Synia Aid Foundation — static site build.

    python3 build.py            # build into ./dist
    python3 build.py --serve    # build, then serve dist on http://localhost:8080

Every page is generated from saf/data.py, so a change to a programme status, a
partner or a figure is made in one place and propagates across the whole site.
"""

import json
import os
import re
import shutil
import sys
from html import unescape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from saf import data as D                                    # noqa: E402
from saf.layout import render, NAV, FOOTER_UTILITY, ACCOUNTABILITY_LINKS   # noqa: E402
from saf import pages_home_about as PA                       # noqa: E402
from saf import pages_programmes as PB                       # noqa: E402
from saf import pages_involve as PC                          # noqa: E402
from saf import pages_accountability as PD                   # noqa: E402
from saf import pages_utility as PE                          # noqa: E402
from saf.components import programme_url, pillar_url, person_url   # noqa: E402

DIST = os.path.join(HERE, "dist")
ASSETS = os.path.join(HERE, "assets")

# The PDFs the site publishes live in the repository so that a fresh clone
# builds a complete site. The Foundation's internal working documents (the
# Website Development Brief and the Partner List handover) are deliberately
# NOT in the repository — they are working papers, not publications.
SOURCE_DOCS = os.path.join(HERE, "source-documents")
LEGACY_DOCS = os.path.dirname(HERE)          # original hand-over folder, as a fallback

PAGES = []       # (url, title, description, html_body, kind, schema, noindex)


def fit_description(text, limit=155):
    """Meta descriptions are cut off by search engines at about 155 characters, so keep the first whole
    sentence (or, failing that, the first whole clause) that fits and never end mid-word."""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    head = text[:limit + 1]
    for stop in (". ", "; ", ": "):
        i = head.rfind(stop)
        if i > 60:
            return head[:i].rstrip(".;:") + "."
    i = head.rfind(" ")
    return head[:i].rstrip(",;:. ") + "."


def add(url, title, description, body, kind="Page", schema=None, noindex=False):
    description = fit_description(description)
    PAGES.append((url, title, description, body, kind, schema, noindex))


# ---------------------------------------------------------------------------
# Structured data
# ---------------------------------------------------------------------------

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "NGO",
    "name": D.SITE["name"],
    "alternateName": "SAF",
    "url": D.SITE["base_url"] + "/",
    "logo": D.SITE["base_url"] + "/assets/img/icon-512.png",
    "slogan": D.SITE["tagline"],
    "description": ("A Nigerian humanitarian and development foundation working with internally displaced "
                    "persons and indigent communities through education, livelihoods, shelter, WASH and "
                    "protection programmes."),
    "foundingDate": "2018-12",
    "founder": {"@type": "Person", "name": D.SITE["founder"]},
    "nonprofitStatus": "NonprofitANBI",
    "identifier": {"@type": "PropertyValue", "name": "Corporate Affairs Commission registration",
                   "value": D.SITE["reg_number"]},
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "No. 34 Osun Crescent, Ancestor's Court",
        "addressLocality": "Maitama, Abuja",
        "addressRegion": "Federal Capital Territory",
        "addressCountry": "NG",
    },
    "email": D.SITE["email"],
    "telephone": D.SITE["phone"],
    "areaServed": {"@type": "Country", "name": "Nigeria"},
    "sameAs": [s["url"] for s in D.SITE["social"]],
    "contactPoint": [
        {"@type": "ContactPoint", "contactType": "customer service",
         "telephone": D.SITE["phone"], "email": D.SITE["email"],
         "areaServed": "NG", "availableLanguage": "English"},
        {"@type": "ContactPoint", "contactType": "emergency",
         "name": "24/7 hotline", "telephone": D.SITE["hotline"], "areaServed": "NG"},
    ],
}

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": D.SITE["name"],
    "url": D.SITE["base_url"] + "/",
    "inLanguage": "en-NG",
    "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": D.SITE["base_url"] + "/search/?q={search_term_string}"},
        "query-input": "required name=search_term_string",
    },
}


DONATE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in PC.DONATE_FAQS
    ],
}


def article_schema(item, path, kind="NewsArticle"):
    return {
        "@context": "https://schema.org",
        "@type": kind,
        "headline": item["title"],
        "description": item["excerpt"],
        "datePublished": item["date_iso"],
        "inLanguage": "en-NG",
        "mainEntityOfPage": D.SITE["base_url"] + path,
        "publisher": {"@type": "NGO", "name": D.SITE["name"],
                      "logo": {"@type": "ImageObject",
                               "url": D.SITE["base_url"] + "/assets/img/icon-512.png"}},
        "author": {"@type": "Organization", "name": D.SITE["name"]},
    }


# ---------------------------------------------------------------------------
# Register every page
# ---------------------------------------------------------------------------

def register_pages():
    add("/", "Synia Aid Foundation",
        "A Nigerian foundation helping displaced families and indigent communities through education, "
        "livelihoods, shelter and protection.",
        PA.home(), "Home", [ORG_SCHEMA, WEBSITE_SCHEMA])

    # --- About -------------------------------------------------------------
    add("/about/", "Who we are & our story",
        "Our vision, mission and eight core values, and the milestones from our founding in December 2018 "
        "to today.", PA.who_we_are(), "About")
    add("/about/leadership/", "Leadership & Governance",
        "The Board of Trustees, its specialist advisers in law, human resources and media strategy, and the "
        "executive team delivering our work.", PA.leadership(), "About")
    for group, people in (("board", [p for p in D.BOARD if p["group"] == "board"]),
                          ("adviser", [p for p in D.BOARD if p["group"] == "adviser"]),
                          ("executive", D.EXECUTIVE)):
        for person in people:
            add(person_url(person), person["name"],
                f'{person["role"]} at Synia Aid Foundation. {person["summary"]}'[:155].rsplit(" ", 1)[0],
                PA.leadership_bio(person, group), "About")
    add("/about/partners/", "Partners",
        "The seven organisations we deliver alongside: schools, health bodies, service organisations and "
        "fellow foundations.", PA.partners(), "About")

    # --- What we do --------------------------------------------------------
    add("/what-we-do/", "What we do",
        "Three pillars and twelve programmes: educate the mind, equip the hands, secure the home.",
        PB.what_we_do(), "Programmes")
    for p in D.PILLARS:
        add(pillar_url(p["slug"]), p["name"],
            f'{p["motto"]}. {p["lede"]}', PB.pillar_page(p), "Programmes")
    for p in D.PROGRAMMES:
        add(programme_url(p["slug"]), p["name"], p["one_line"], PB.programme_page(p), "Programme")
    add("/who-we-serve/", "Who we serve",
        "Internally displaced persons and the wider community of vulnerable Nigerians we serve, how we "
        "select, and the sources on displacement.", PA.who_we_serve(), "About")

    # --- Impact ------------------------------------------------------------
    add("/impact/", "Our impact",
        "What we have delivered since 2019, reported conservatively, and how we measure impact.",
        PB.impact(), "Impact")
    add("/impact/stories/", "Stories",
        "Films, photo essays and written pieces from the communities we work in, filterable by pillar and "
        "format.", PB.stories_index(), "Impact")
    for s in D.STORIES:
        add(f'/impact/stories/{s["slug"]}/', s["title"], s["excerpt"], PB.story_page(s), "Story",
            article_schema(s, f'/impact/stories/{s["slug"]}/', "Article"))
    add("/impact/projects/", "Projects",
        "Every project delivered since 2019 with the partner who delivered it alongside us — filterable by "
        "year and pillar.", PB.projects(), "Impact")

    # --- Get involved ------------------------------------------------------
    add("/get-involved/", "Get involved",
        "Four ways to stand with the Foundation: donate, partner with us, volunteer, or become an ambassador.",
        PC.get_involved(), "Get involved")
    add("/donate/", "Donate",
        "Fund a child's school year, a family's shelter repair or a trader's start. Give once or monthly "
        "from ₦5,000, in Naira or from abroad.",
        PC.donate(), "Get involved", DONATE_SCHEMA)
    add("/donate/thank-you/", "Thank you",
        "Your gift has been received. What happens next, and how to reach us with a question.",
        PC.thank_you(), "Get involved", None, noindex=True)
    add("/get-involved/partner/", "Partner with us",
        "What we offer a partner, the kinds of partnership we seek, and how to start a conversation.",
        PC.partner(), "Get involved")
    add("/get-involved/volunteer/", "Volunteer",
        "Volunteer with the Foundation. What volunteering involves, current opportunities, and the vetting "
        "and code of conduct that apply to anyone working with children.", PC.volunteer(), "Get involved")
    add("/get-involved/ambassador/", "Become an ambassador",
        "Champion the Foundation's mission and carry it beyond borders. What an ambassador does, and how to "
        "register your interest.", PC.ambassador(), "Get involved")

    # --- Accountability ----------------------------------------------------
    add("/accountability/", "Accountability",
        "Governance, policies, published documents, financial controls and our risk register, for "
        "institutional funders.", PD.accountability(), "Accountability")
    add("/accountability/governance-and-policies/", "Governance & Policies",
        "How the Foundation is governed, our legal identity, our safeguarding controls, and the full policy "
        "suite to download.", PD.governance_policies(), "Accountability")
    add("/accountability/reports-and-publications/", "Reports & Publications",
        "Our Corporate Profile, programme structure guide, leadership biographies and policy suite, free to "
        "download.", PD.reports_publications(), "Accountability")

    # --- News --------------------------------------------------------------
    add("/news/", "News",
        "Updates from the Foundation — programmes launching, outreaches delivered and reports published.",
        PB.news_index(), "News")
    for i, n in enumerate(D.NEWS):
        prev_item = D.NEWS[i - 1] if i > 0 else None
        next_item = D.NEWS[i + 1] if i + 1 < len(D.NEWS) else None
        add(f'/news/{n["slug"]}/', n["title"], n["excerpt"],
            PB.news_page(n, prev_item, next_item), "News",
            article_schema(n, f'/news/{n["slug"]}/'))

    # --- Contact and utility ----------------------------------------------
    add("/contact/", "Contact us",
        "Head office in Maitama, Abuja. Phone, 24/7 hotline, email, office hours, a map and a contact form "
        "with subject routing.", PE.contact(), "Contact")
    add("/complaints/", "Raise a concern or make a complaint",
        "How to raise a concern about our work or the conduct of anyone acting in our name — including a "
        "safeguarding concern — and what happens next.", PE.complaints(), "Accountability")
    add("/safeguarding/", "Safeguarding statement",
        "Our public commitment to the protection of children and adults at risk, the controls that apply to "
        "everyone acting in our name, and how to report a concern.", PE.safeguarding(), "Accountability")
    add("/privacy/", "Privacy policy",
        "How we collect, use and protect personal data, and how you exercise your rights under the Nigeria "
        "Data Protection Act 2023.", PE.privacy(), "Legal")
    add("/cookies/", "Cookie policy",
        "What cookies we set, why, and how to change your choice at any time.", PE.cookies(), "Legal")
    add("/terms/", "Terms of use",
        "The terms on which this website is made available.", PE.terms(), "Legal")
    add("/accessibility/", "Accessibility statement",
        "The standard this site is built to, the choices behind it, known limitations, and how to tell us "
        "something does not work.", PE.accessibility(), "Legal")
    add("/search/", "Search", "Search across our pages, programmes, stories, news and documents.",
        PE.search(), "Utility", None, noindex=True)

    add("/sitemap/", "Sitemap", "Every page on this website.", PE.sitemap_page(sitemap_groups()),
        "Utility")


def sitemap_groups():
    people = [(p["name"], person_url(p)) for p in D.BOARD + D.EXECUTIVE]
    return [
        ("Home", [("Home", "/")]),
        ("About us", [(c["label"], c["url"]) for c in NAV[1]["children"]] + people),
        ("What we do", [("Overview", "/what-we-do/")]
         + [(p["name"], pillar_url(p["slug"])) for p in D.PILLARS]
         + [(p["short_name"], programme_url(p["slug"])) for p in D.PROGRAMMES]),
        ("Our impact", [("Overview & How We Measure Impact", "/impact/"), ("Stories", "/impact/stories/")]
         + [(s["title"], f'/impact/stories/{s["slug"]}/') for s in D.STORIES]
         + [("Projects", "/impact/projects/")]),
        ("Get involved", [("Overview", "/get-involved/"), ("Donate", "/donate/"),
                          ("Partner with us", "/get-involved/partner/"),
                          ("Volunteer", "/get-involved/volunteer/"),
                          ("Become an ambassador", "/get-involved/ambassador/")]),
        ("Accountability", list(ACCOUNTABILITY_LINKS)
         + [("Safeguarding statement", "/safeguarding/"), ("Complaints", "/complaints/")]),
        ("News", [("All news", "/news/")] + [(n["title"], f'/news/{n["slug"]}/') for n in D.NEWS]),
        ("Contact and utility", [("Contact", "/contact/"), ("Search", "/search/")]
         + [(l, u) for l, u in FOOTER_UTILITY]),
    ]


# ---------------------------------------------------------------------------
# Search index
# ---------------------------------------------------------------------------

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def plain_text(html_str, limit=2400):
    txt = re.sub(r"<script.*?</script>", " ", html_str, flags=re.S | re.I)
    txt = re.sub(r"<style.*?</style>", " ", txt, flags=re.S | re.I)
    txt = TAG_RE.sub(" ", txt)
    txt = unescape(txt)
    txt = WS_RE.sub(" ", txt).strip()
    return txt[:limit]


def build_search_index():
    docs = []
    for url, title, description, body, kind, _schema, noindex in PAGES:
        if noindex:
            continue
        docs.append({"u": url, "t": title, "s": description, "k": kind, "b": plain_text(body)})
    return docs


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

# The Foundation asked for em dashes to be removed from the writing, because they read as machine
# generated. Spaced dashes become a comma; anything else is left alone (a lone dash in a table cell
# means "not applicable", and a numeric range such as 2026–27 is not a dash in prose).
_DASH = re.compile(r"(?<=\S)\s+(?:—|&mdash;|&#8212;)\s+(?=\S)")


def clean_prose(text):
    return _DASH.sub(", ", text)


def write(path, content, binary=False):
    full = os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    mode = "wb" if binary else "w"
    with open(full, mode, encoding=None if binary else "utf-8") as fh:
        fh.write(content)


def url_to_path(url):
    if url == "/":
        return "index.html"
    return url.strip("/") + "/index.html"


def copy_assets():
    dest = os.path.join(DIST, "assets")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(ASSETS, dest)


# Published name -> the name it may carry in the original hand-over folder.
DOC_MAP = {
    "SAF-Corporate-Profile-2026.pdf": "SAF Corporate Profile 2026 .pdf",
    "SAF-Our-Programmes-Structure-Guide.pdf": "SAF Our Programmes Structure Guide.pdf",
    "SAF-Leadership-Biographies.pdf": "SAF Leadership Biographies.pdf",
    "SAF-Policy-01-Safeguarding.pdf": "SAF Policy 01 Safeguarding.pdf",
    "SAF-Policy-02-Code-of-Conduct.pdf": "SAF Policy 02 Code of Conduct.pdf",
    "SAF-Policy-03-PSEAH.pdf": "SAF Policy 03 PSEAH.pdf",
    "SAF-Policy-04-AntiFraud-Whistleblowing.pdf": "SAF Policy 04 AntiFraud Whistleblowing.pdf",
    "SAF-Policy-05-Conflict-of-Interest.pdf": "SAF Policy 05 Conflict of Interest.pdf",
}


def copy_documents():
    dest = os.path.join(DIST, "assets", "documents")
    os.makedirs(dest, exist_ok=True)
    missing = []
    for out_name, legacy_name in DOC_MAP.items():
        for candidate in (os.path.join(SOURCE_DOCS, out_name),
                          os.path.join(LEGACY_DOCS, legacy_name)):
            if os.path.isfile(candidate):
                shutil.copy2(candidate, os.path.join(dest, out_name))
                break
        else:
            missing.append(out_name)
    return missing


PHOTO_SRC = os.path.join(HERE, "photos-src")


def build_photos():
    """Generate exactly the crops the pages asked for — nothing more.

    Every derivative is written without EXIF, which satisfies the safeguarding
    requirement that no published image carries location data.
    """
    try:
        from PIL import Image, ImageFile, ImageOps
    except ImportError:
        print("  WARNING — Pillow not installed; photographs were not generated.")
        return 0, 0

    ImageFile.LOAD_TRUNCATED_IMAGES = True
    Image.MAX_IMAGE_PIXELS = None

    from saf.components import REQUESTED, RATIOS, WIDTHS

    out_dir = os.path.join(DIST, "assets", "img", "photos")
    os.makedirs(out_dir, exist_ok=True)

    written = 0
    total_bytes = 0
    cache = {}

    for key, ratio, focus, cap_w in sorted(REQUESTED):
        meta = D.PHOTOS[key]
        src_path = os.path.join(PHOTO_SRC, meta["file"])
        if not os.path.isfile(src_path):
            print(f"  WARNING — source photograph missing: {meta['file']}")
            continue

        if src_path not in cache:
            im = Image.open(src_path)
            im = ImageOps.exif_transpose(im)      # honour rotation, then drop EXIF
            cache[src_path] = im.convert("RGB")
        src = cache[src_path]

        rw, rh = RATIOS[ratio]
        target = rw / rh
        sw, sh = src.size
        current = sw / sh

        if current > target:                      # too wide — trim the sides
            new_w = int(round(sh * target))
            left = (sw - new_w) // 2
            box = (left, 0, left + new_w, sh)
        else:                                     # too tall — trim top/bottom
            new_h = int(round(sw / target))
            if focus == "top":
                top = 0
            elif focus == "upper":
                top = int((sh - new_h) * 0.18)
            else:
                top = (sh - new_h) // 2
            box = (0, top, sw, top + new_h)

        cropped = src.crop(box)

        widths = [n for n in WIDTHS if n <= cap_w] or [WIDTHS[0]]
        for w in widths:
            if w > cropped.width * 1.15:          # never upscale beyond the source
                continue
            h = int(round(w / target))
            resized = cropped.resize((w, h), Image.LANCZOS)
            stem = os.path.join(out_dir, f"{key}-{ratio}-{focus}-{w}")
            resized.save(stem + ".jpg", "JPEG", quality=74, optimize=True,
                         progressive=True, exif=b"")
            resized.save(stem + ".webp", "WEBP", quality=72, method=6)
            written += 2
            total_bytes += os.path.getsize(stem + ".jpg") + os.path.getsize(stem + ".webp")

        # Guarantee the src= fallback exists even if the source was small.
        fb_w = widths[-1]
        fallback = os.path.join(out_dir, f"{key}-{ratio}-{focus}-{fb_w}.jpg")
        if not os.path.exists(fallback):
            h = int(round(fb_w / target))
            src_fallback = cropped.resize((fb_w, h), Image.LANCZOS)
            src_fallback.save(fallback, "JPEG", quality=74, optimize=True,
                              progressive=True, exif=b"")
            written += 1
            total_bytes += os.path.getsize(fallback)

    return written, total_bytes


def robots():
    return (f"User-agent: *\nAllow: /\nDisallow: /search/\nDisallow: /donate/thank-you/\n\n"
            f"Sitemap: {D.SITE['base_url']}/sitemap.xml\n")


def sitemap_xml():
    priority = {"/": "1.0", "/donate/": "0.9", "/what-we-do/": "0.9", "/accountability/": "0.8"}
    urls = []
    for url, _t, _d, _b, _k, _s, noindex in PAGES:
        if noindex:
            continue
        p = priority.get(url, "0.6" if url.count("/") > 3 else "0.7")
        urls.append(f"  <url>\n    <loc>{D.SITE['base_url']}{url}</loc>\n"
                    f"    <changefreq>monthly</changefreq>\n    <priority>{p}</priority>\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(urls) + "\n</urlset>\n")


def manifest():
    return json.dumps({
        "name": D.SITE["name"],
        "short_name": "Synia Aid",
        "description": D.SITE["descriptor"],
        "start_url": "/",
        "display": "standalone",
        "background_color": "#FFFFFF",
        "theme_color": "#0F2A47",
        "icons": [
            {"src": "/assets/img/icon-180.png", "sizes": "180x180", "type": "image/png"},
            {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, indent=2)


def rss():
    items = []
    for n in D.NEWS:
        link = f'{D.SITE["base_url"]}/news/{n["slug"]}/'
        items.append(
            "    <item>\n"
            f"      <title>{escape_xml(n['title'])}</title>\n"
            f"      <link>{link}</link>\n"
            f"      <guid isPermaLink=\"true\">{link}</guid>\n"
            f"      <description>{escape_xml(n['excerpt'])}</description>\n"
            f"      <pubDate>{n['date_iso']}</pubDate>\n"
            "    </item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">\n  <channel>\n'
            f"    <title>{escape_xml(D.SITE['name'])} — News</title>\n"
            f"    <link>{D.SITE['base_url']}/news/</link>\n"
            f"    <description>Updates from Synia Aid Foundation.</description>\n"
            f"    <language>en-NG</language>\n" + "\n".join(items) + "\n  </channel>\n</rss>\n")


def escape_xml(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&apos;"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    register_pages()

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    copy_assets()
    missing_docs = copy_documents()

    too_long = []
    for url, title, description, body, kind, schema, noindex in PAGES:
        if len(description) > 160:
            too_long.append((url, len(description)))
        # Organisation structured data on every page (the home page already carries it).
        blocks = schema if isinstance(schema, list) else ([schema] if schema else [])
        if ORG_SCHEMA not in blocks:
            blocks = [ORG_SCHEMA] + blocks
        html_doc = render(url=url, title=title, description=description, body=body,
                          page_class="page-" + re.sub(r"[^a-z0-9]+", "-", kind.lower()).strip("-"),
                          schema=blocks, noindex=noindex,
                          og_type="article" if kind in ("News", "Story") else "website")
        write(url_to_path(url), clean_prose(html_doc))

    # 404 — served by the host's error handler, so it lives at the root.
    write("404.html", clean_prose(render(url="/404.html", title="Page not found",
                                         description="The page you asked for could not be found.",
                                         body=PE.not_found(), page_class="page-utility", noindex=True)))

    photo_files, photo_bytes = build_photos()

    write("search-index.json", clean_prose(json.dumps(build_search_index(), ensure_ascii=False,
                                                         separators=(",", ":"))))
    write("sitemap.xml", sitemap_xml())
    write("robots.txt", robots())
    write("site.webmanifest", manifest())
    write("news/feed.xml", rss())

    # Netlify / Vercel style headers + a redirect map placeholder for old URLs.
    write("_headers", (
        "/*\n"
        "  X-Content-Type-Options: nosniff\n"
        "  X-Frame-Options: SAMEORIGIN\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  Permissions-Policy: geolocation=(), microphone=(), camera=()\n"
        "  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload\n"
        "/assets/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n"
    ))
    write("_redirects", (
        "# Old site URLs -> new equivalents. Confirm against the live site's\n"
        "# analytics and search-console coverage report before launch.\n"
        "/index.html            /                       301\n"
        "/about.html            /about/                 301\n"
        "/about-us              /about/                 301\n"
        "/programs              /what-we-do/            301\n"
        "/programmes            /what-we-do/            301\n"
        "/our-programs          /what-we-do/            301\n"
        "/team                  /about/leadership/      301\n"
        "/partners              /about/partners/        301\n"
        "/gallery               /impact/stories/        301\n"
        "/blog/*                /news/:splat            301\n"
        "/donate.html           /donate/                301\n"
        "/contact.html          /contact/               301\n"
        "/about/our-story       /about/#our-story       301\n"
        "/about/our-story/      /about/#our-story       301\n"
        "/accountability/how-we-measure-impact   /impact/#how-we-measure-impact   301\n"
        "/accountability/how-we-measure-impact/  /impact/#how-we-measure-impact   301\n"
    ))

    # Pages that moved keep a working address even where the host ignores redirect rules.
    for old, new in (("/about/our-story/", "/about/#our-story"),
                     ("/accountability/how-we-measure-impact/", "/impact/#how-we-measure-impact")):
        write(url_to_path(old), (
            '<!doctype html><html lang="en-NG"><head><meta charset="utf-8">'
            '<meta name="robots" content="noindex">'
            f'<link rel="canonical" href="{D.SITE["base_url"]}{new}">'
            f'<meta http-equiv="refresh" content="0; url={new}">'
            '<title>This page has moved</title></head><body>'
            f'<p>This page has moved. <a href="{new}">Continue to the new page</a>.</p></body></html>'))

    # ---- report -----------------------------------------------------------
    total_bytes = 0
    for root, _dirs, files in os.walk(DIST):
        for f in files:
            total_bytes += os.path.getsize(os.path.join(root, f))

    print(f"Built {len(PAGES) + 1} pages into {DIST}")
    print(f"  programmes : {len(D.PROGRAMMES)}")
    if too_long:
        print("  WARNING: meta descriptions over 160 characters:")
        for u, n in too_long:
            print(f"    {n}  {u}")
    print(f"  partners   : {len(D.PARTNERS)}")
    print(f"  news       : {len(D.NEWS)}   stories: {len(D.STORIES)}   projects: {len(D.PROJECTS)}")
    print(f"  photos     : {len(D.PHOTOS)} published, {len(D.PHOTOS_WITHHELD)} withheld → "
          f"{photo_files} derivatives, {photo_bytes / 1024:.0f} KB (EXIF stripped)")
    print(f"  total size : {total_bytes / 1024:.0f} KB")
    if missing_docs:
        print("  WARNING — source PDFs not found, download links will 404:")
        for m in missing_docs:
            print("    -", m)

    if "--serve" in sys.argv:
        import http.server
        import socketserver
        os.chdir(DIST)
        port = 8080
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"\nServing http://localhost:{port}  (Ctrl+C to stop)")
            httpd.serve_forever()


if __name__ == "__main__":
    main()
