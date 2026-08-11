# -*- coding: utf-8 -*-
"""Page shell, navigation and shared UI components."""

import html
import json

from .data import SITE, STATUSES

# ---------------------------------------------------------------------------
# Navigation — seven top-level items, exactly as required by the brief.
# Nothing important lives only in a dropdown: every section landing page
# repeats its children as links, and the mobile menu renders them all inline.
# ---------------------------------------------------------------------------

NAV = [
    {"label": "About Us", "url": "/about/", "children": [
        {"label": "Who We Are", "url": "/about/", "desc": "Story, vision, mission and values"},
        {"label": "Our Story", "url": "/about/our-story/", "desc": "Milestones from 2018"},
        {"label": "Leadership & Governance", "url": "/about/leadership/", "desc": "Board, advisers and executive team"},
        {"label": "Partners", "url": "/about/partners/", "desc": "Who we deliver alongside"},
    ]},
    {"label": "What We Do", "url": "/what-we-do/", "children": [
        {"label": "Overview", "url": "/what-we-do/", "desc": "Three pillars, twelve programmes"},
        {"label": "Education & Skills", "url": "/what-we-do/education-skills/", "desc": "Educate the mind"},
        {"label": "Livelihoods & Economic Inclusion", "url": "/what-we-do/livelihoods-economic-inclusion/", "desc": "Equip the hands"},
        {"label": "Shelter, WASH & Protection", "url": "/what-we-do/shelter-wash-protection/", "desc": "Secure the home"},
        {"label": "Who We Serve", "url": "/who-we-serve/", "desc": "The people our work is for"},
    ]},
    {"label": "Our Impact", "url": "/impact/", "children": [
        {"label": "Overview", "url": "/impact/", "desc": "What we have delivered, reported conservatively"},
        {"label": "Stories", "url": "/impact/stories/", "desc": "Films, photo essays and written pieces"},
        {"label": "Projects", "url": "/impact/projects/", "desc": "Delivered work, by year"},
    ]},
    {"label": "Get Involved", "url": "/get-involved/", "children": [
        {"label": "Donate", "url": "/donate/", "desc": "One-off or monthly, from ₦5,000"},
        {"label": "Partner With Us", "url": "/get-involved/partner/", "desc": "For organisations and funders"},
        {"label": "Volunteer", "url": "/get-involved/volunteer/", "desc": "Give time and skills"},
        {"label": "Become an Ambassador", "url": "/get-involved/ambassador/", "desc": "Champion the mission"},
    ]},
    {"label": "Accountability", "url": "/accountability/", "children": [
        {"label": "Overview", "url": "/accountability/", "desc": "For institutional funders"},
        {"label": "Governance & Policies", "url": "/accountability/governance-and-policies/", "desc": "How we are governed, and our policy suite"},
        {"label": "Reports & Publications", "url": "/accountability/reports-and-publications/", "desc": "Document library"},
        {"label": "How We Measure Impact", "url": "/accountability/how-we-measure-impact/", "desc": "Monitoring, evaluation and learning"},
    ]},
    {"label": "News", "url": "/news/", "children": []},
    {"label": "Contact", "url": "/contact/", "children": []},
]

FOOTER_UTILITY = [
    ("Privacy Policy", "/privacy/"),
    ("Cookie Policy", "/cookies/"),
    ("Terms of Use", "/terms/"),
    ("Safeguarding Statement", "/safeguarding/"),
    ("Accessibility", "/accessibility/"),
    ("Complaints", "/complaints/"),
    ("Sitemap", "/sitemap/"),
]

# ---------------------------------------------------------------------------
# Icons — inline SVG, no icon font, no network request.
# ---------------------------------------------------------------------------

_ICON_PATHS = {
    "book": '<path d="M3 5.5A1.5 1.5 0 0 1 4.5 4H9a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H3.5A.5.5 0 0 1 3 17z"/>'
            '<path d="M21 5.5A1.5 1.5 0 0 0 19.5 4H15a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5h6a.5.5 0 0 0 .5-.5z"/>',
    "lightbulb": '<path d="M9 18h6"/><path d="M10 21.5h4"/>'
                 '<path d="M12 2.5a6.5 6.5 0 0 0-3.9 11.7c.6.5 1 1.2 1 2h5.8c0-.8.4-1.5 1-2A6.5 6.5 0 0 0 12 2.5z"/>',
    "house": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.6V20a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1V9.6"/>'
             '<path d="M9.5 21v-6h5v6"/>',
    "heart": '<path d="M12 20.3 4.6 13a4.6 4.6 0 0 1 6.5-6.5l.9.9.9-.9A4.6 4.6 0 1 1 19.4 13z"/>',
    "handshake": '<path d="M11 6.5 8.6 4.8a2 2 0 0 0-2.3 0L2.5 7.6v7l2 1.6"/>'
                 '<path d="m13 6.5 2.4-1.7a2 2 0 0 1 2.3 0l3.8 2.8v7l-2 1.6"/>'
                 '<path d="m8 12.5 2.4 2.4a1.6 1.6 0 0 0 2.3 0"/><path d="m11 15.5 1.8 1.8"/><path d="m14 16.5 1.6 1.6"/>',
    "people": '<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/>'
              '<path d="M16 5.4a3.2 3.2 0 0 1 0 5.2"/><path d="M17.5 14.6a6.2 6.2 0 0 1 3.7 5.4"/>',
    "megaphone": '<path d="M3 10.5v3a1.5 1.5 0 0 0 1.5 1.5H7l6 4.5V5.5L7 10H4.5A1.5 1.5 0 0 0 3 11.5z"/>'
                 '<path d="M17 8.5a5 5 0 0 1 0 7"/><path d="M7 15v4.5"/>',
    "shield": '<path d="M12 2.8 4.5 6v6c0 4.6 3.1 8.2 7.5 9.2 4.4-1 7.5-4.6 7.5-9.2V6z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/>',
    "scale": '<path d="M12 3.5v17"/><path d="M6 6.8h12"/><path d="M6 6.8 3 14h6z"/><path d="M18 6.8 15 14h6z"/>'
             '<path d="M8.5 20.5h7"/>',
    "doc": '<path d="M14 3H7a1.5 1.5 0 0 0-1.5 1.5v15A1.5 1.5 0 0 0 7 21h10a1.5 1.5 0 0 0 1.5-1.5V7.5z"/>'
           '<path d="M14 3v4.5h4.5"/><path d="M9 13h6"/><path d="M9 16.5h4"/>',
    "download": '<path d="M12 3.5v11"/><path d="m7.5 10.5 4.5 4.5 4.5-4.5"/><path d="M4 19.5h16"/>',
    "arrow-right": '<path d="M4.5 12h14"/><path d="m12.5 6 6 6-6 6"/>',
    "arrow-up-right": '<path d="M7 17 17 7"/><path d="M8.5 7H17v8.5"/>',
    "check": '<path d="m4.5 12.5 5 5 10-11"/>',
    "phone": '<path d="M6.4 3.5h3l1.5 4-2 1.4a12 12 0 0 0 5.7 5.7l1.4-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.4 5.7a2 2 0 0 1 2-2.2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.6 6.5 8.4 6 8.4-6"/>',
    "pin": '<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 6.8V12l3.4 2"/>',
    "search": '<circle cx="10.8" cy="10.8" r="6.8"/><path d="m15.8 15.8 4.4 4.4"/>',
    "menu": '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/>',
    "close": '<path d="m6 6 12 12"/><path d="m18 6-12 12"/>',
    "chevron-down": '<path d="m6 9.5 6 6 6-6"/>',
    "quote": '<path d="M9.5 6.5C6.5 8 5 10.4 5 13.5V18h5.5v-5.5H8c0-2.1.8-3.6 2.4-4.5z"/>'
             '<path d="M18.5 6.5C15.5 8 14 10.4 14 13.5V18h5.5v-5.5H17c0-2.1.8-3.6 2.4-4.5z"/>',
    "facebook": '<path d="M14.5 8.5h2.2V5.4h-2.6c-2.4 0-3.8 1.5-3.8 4v1.9H8v3.1h2.3V21h3.4v-6.6h2.4l.4-3.1h-2.8V9.9c0-.9.3-1.4 1.3-1.4z" fill="currentColor" stroke="none"/>',
    "linkedin": '<path d="M6.6 9.4H3.9V21h2.7zM5.2 3.2a1.6 1.6 0 1 0 0 3.2 1.6 1.6 0 0 0 0-3.2M20.1 21h-2.7v-5.7c0-1.4-.5-2.3-1.7-2.3-.9 0-1.5.6-1.7 1.3-.1.2-.1.6-.1.9V21H11.2s0-9.7 0-10.7h2.7v1.5a2.7 2.7 0 0 1 2.4-1.4c1.8 0 3.8 1.1 3.8 4.2z" fill="currentColor" stroke="none"/>',
    "instagram": '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="5"/><circle cx="12" cy="12" r="4"/>'
                 '<circle cx="17" cy="7" r="1.1" fill="currentColor" stroke="none"/>',
    "alert": '<path d="M12 3.6 2.8 19.5h18.4z"/><path d="M12 9.5v4.4"/><circle cx="12" cy="16.8" r="1" fill="currentColor" stroke="none"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5"/><circle cx="12" cy="7.8" r="1" fill="currentColor" stroke="none"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/>',
    "chart": '<path d="M4 20V9"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M3 20h18"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/>'
             '<path d="M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18z"/>',
    "film": '<rect x="3" y="4.5" width="18" height="15" rx="2"/><path d="M8 4.5v15"/><path d="M16 4.5v15"/>'
            '<path d="M3 12h18"/>',
    "camera": '<path d="M3 8.5h3.5L8 6h8l1.5 2.5H21v10a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>'
              '<circle cx="12" cy="13.2" r="3.6"/>',
    "users-check": '<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/>'
                   '<path d="m16 12.5 1.8 1.8 3.4-3.6"/>',
}


def icon(name, cls="icon", size=24):
    path = _ICON_PATHS.get(name, "")
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{path}</svg>')


# ---------------------------------------------------------------------------
# Small components
# ---------------------------------------------------------------------------

def esc(s):
    return html.escape(str(s), quote=True)


def chip(status_key, extra_note=None):
    """Programme status label. Required on every programme page and card."""
    st = STATUSES[status_key]
    note = f'<span class="chip__note">{esc(extra_note)}</span>' if extra_note else ""
    return (f'<span class="chip chip--{st["key"]}">'
            f'<span class="chip__dot" aria-hidden="true"></span>{esc(st["label"])}</span>{note}')


def btn(label, url, kind="primary", icon_name="arrow-right", attrs=""):
    ic = icon(icon_name, "btn__icon", 20) if icon_name else ""
    return f'<a class="btn btn--{kind}" href="{url}"{attrs}>{esc(label)}{ic}</a>'


def hidden_h2(text):
    """A heading present for structure and screen readers, not for the eye.
    Keeps the heading order unbroken on pages whose first content block is a
    grid of cards."""
    return f'<h2 class="visually-hidden">{esc(text)}</h2>'


def eyebrow(text):
    return f'<p class="eyebrow">{esc(text)}</p>'


def section_head(title, lede=None, eyebrow_text=None, level=2, align=""):
    out = [f'<div class="section-head {align}">']
    if eyebrow_text:
        out.append(eyebrow(eyebrow_text))
    out.append(f'<h{level}>{title}</h{level}>')
    if lede:
        out.append(f'<p class="lede">{lede}</p>')
    out.append("</div>")
    return "".join(out)


def paras(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{p}</p>" for p in items)


def bullets(items, cls="list-check", icon_name="check"):
    li = "".join(f'<li>{icon(icon_name, "list-icon", 20)}<span>{i}</span></li>' for i in items)
    return f'<ul class="{cls}">{li}</ul>'


def note(body, title=None, tone="info", icon_name="info"):
    t = f'<p class="note__title">{icon(icon_name, "note__icon", 20)}{esc(title)}</p>' if title else ""
    return f'<aside class="note note--{tone}">{t}<div class="note__body">{body}</div></aside>'


def table(headers, rows, caption=None, cls=""):
    """Responsive table — collapses to labelled stacked rows on small screens."""
    th = "".join(f"<th scope='col'>{h}</th>" for h in headers)
    body = []
    for r in rows:
        cells = "".join(
            f'<td data-label="{esc(headers[i])}">{c}</td>' for i, c in enumerate(r)
        )
        body.append(f"<tr>{cells}</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    return (f'<div class="table-wrap"><table class="table {cls}">{cap}'
            f"<thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></div>")


def stat_grid(stats, cls=""):
    cards = []
    for s in stats:
        sub = f'<p class="stat__sub">{esc(s["sub"])}</p>' if s.get("sub") else ""
        cards.append(f'<div class="stat"><p class="stat__figure">{esc(s["figure"])}</p>'
                     f'<p class="stat__label">{esc(s["label"])}</p>{sub}</div>')
    return f'<div class="stat-grid {cls}">{"".join(cards)}</div>'


def breadcrumbs(trail):
    """trail: list of (label, url) — final item has url None."""
    items, ld = [], []
    for i, (label, url) in enumerate(trail):
        if url:
            items.append(f'<li><a href="{url}">{esc(label)}</a></li>')
        else:
            items.append(f'<li><span aria-current="page">{esc(label)}</span></li>')
        ld.append({"@type": "ListItem", "position": i + 1, "name": label,
                   "item": SITE["base_url"] + (url or "")})
    schema = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                         "itemListElement": ld}, ensure_ascii=False)
    return (f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
            f'<script type="application/ld+json">{schema}</script>')


def section_nav(items, current):
    """In-section navigation, so nothing depends on a dropdown."""
    links = []
    for label, url in items:
        cur = ' aria-current="page"' if url == current else ""
        links.append(f'<a href="{url}"{cur}>{esc(label)}</a>')
    return f'<nav class="section-nav" aria-label="Section">{"".join(links)}</nav>'


def cta_band(heading, body, buttons, tone="navy"):
    b = "".join(buttons)
    return (f'<section class="cta-band cta-band--{tone}"><div class="container cta-band__inner">'
            f'<div><h2>{heading}</h2><p>{body}</p></div>'
            f'<div class="cta-band__actions">{b}</div></div></section>')


def newsletter_form(compact=False):
    cls = "newsletter newsletter--compact" if compact else "newsletter"
    return f'''
<form class="{cls}" action="/subscribe" method="post" data-form="newsletter" novalidate>
  <div class="newsletter__row">
    <div class="field">
      <label class="field__label" for="nl-email">Email address</label>
      <input class="field__input" type="email" id="nl-email" name="email" autocomplete="email"
             required placeholder="you@example.com">
    </div>
    <button class="btn btn--cta" type="submit">Sign up{icon("arrow-right", "btn__icon", 20)}</button>
  </div>
  <div class="field field--check">
    <input type="checkbox" id="nl-consent" name="consent" value="yes" required>
    <label for="nl-consent">I agree to receive occasional email updates from Synia Aid Foundation.
      I can unsubscribe at any time. See our <a href="/privacy/">Privacy Policy</a>.</label>
  </div>
  <p class="field__hint">Double opt-in: we will email you a link to confirm. We never sell or share your details.</p>
  <div class="hp" aria-hidden="true"><label for="nl-website">Leave this field empty</label>
    <input type="text" id="nl-website" name="website" tabindex="-1" autocomplete="off"></div>
  <p class="form-status" role="status" data-form-status></p>
</form>'''


def image_placeholder(caption, ratio="16 / 9", tone="navy", icon_name="camera"):
    """Consent-cleared photography arrives from September 2026. Until it does we
    show an honest, designed placeholder rather than stock imagery."""
    return (f'<figure class="ph ph--{tone}" style="--ph-ratio:{ratio}">'
            f'<div class="ph__inner">{icon(icon_name, "ph__icon", 28)}'
            f'<p class="ph__label">Photography to come</p></div>'
            f'<figcaption class="ph__caption">{caption}</figcaption></figure>')


# ---------------------------------------------------------------------------
# Header / footer
# ---------------------------------------------------------------------------

def _nav_markup(current_url):
    out = []
    for item in NAV:
        active = current_url == item["url"] or (
            item["url"] != "/" and current_url.startswith(item["url"]))
        cls = "nav__item" + (" is-active" if active else "")
        cur = ' aria-current="page"' if active else ""
        if item["children"]:
            kids = "".join(
                f'<li><a href="{c["url"]}"><span class="dd__label">{esc(c["label"])}</span>'
                f'<span class="dd__desc">{esc(c["desc"])}</span></a></li>'
                for c in item["children"])
            out.append(f'''<li class="{cls} has-dd">
  <a class="nav__link" href="{item["url"]}"{cur}>{esc(item["label"])}</a>
  <button class="nav__toggle" type="button" aria-expanded="false"
          aria-label="Show {esc(item["label"])} menu">{icon("chevron-down", "nav__chev", 18)}</button>
  <div class="dd"><ul class="dd__list">{kids}</ul></div>
</li>''')
        else:
            out.append(f'<li class="{cls}"><a class="nav__link" href="{item["url"]}"{cur}>'
                       f'{esc(item["label"])}</a></li>')
    return "".join(out)


def header(current_url):
    socials = "".join(
        f'<a class="social" href="{s["url"]}" rel="me noopener" target="_blank" '
        f'aria-label="{esc(SITE["name"])} on {esc(s["name"])}">{icon(s["icon"], "social__icon", 18)}</a>'
        for s in SITE["social"])
    return f'''
<a class="skip-link" href="#main">Skip to main content</a>
<div class="topbar">
  <div class="container topbar__inner">
    <p class="topbar__reg">Registered with the Corporate Affairs Commission&nbsp;·&nbsp;{SITE["reg_number"]}</p>
    <div class="topbar__right">
      <a class="topbar__link" href="tel:{SITE["hotline_href"]}">{icon("phone", "topbar__icon", 16)}
        <span><strong>{SITE["hotline"]}</strong> 24/7 hotline</span></a>
      <span class="topbar__socials">{socials}</span>
    </div>
  </div>
</div>
<header class="header" data-header>
  <div class="container header__inner">
    <a class="brand" href="/">
      <img class="brand__mark" src="/assets/img/logo-mark-300.png" width="300" height="240"
           alt="" decoding="async">
      <span class="brand__text">
        <span class="brand__name">Synia Aid Foundation</span>
        <span class="brand__tag">{esc(SITE["tagline"])}</span>
      </span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav__list">{_nav_markup(current_url)}</ul>
      <div class="nav__footer">
        <a class="nav__util" href="/search/">{icon("search", "", 18)} Search</a>
        <a class="nav__util" href="/complaints/">{icon("shield", "", 18)} Raise a concern</a>
        <a class="nav__util" href="tel:{SITE["hotline_href"]}">{icon("phone", "", 18)} {SITE["hotline"]} (24/7)</a>
      </div>
    </nav>
    <div class="header__actions">
      <a class="header__search" href="/search/" aria-label="Search this site">{icon("search", "", 20)}</a>
      <a class="btn btn--cta btn--donate" href="/donate/">Donate</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="site-nav"
              aria-label="Menu" data-burger>
        <span class="burger__box" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="burger__label">Menu</span>
      </button>
    </div>
  </div>
</header>
<div class="nav-scrim" data-scrim hidden></div>'''


def footer():
    socials = "".join(
        f'<a class="social social--lg" href="{s["url"]}" rel="me noopener" target="_blank" '
        f'aria-label="{esc(SITE["name"])} on {esc(s["name"])} ({esc(s["handle"])})">'
        f'{icon(s["icon"], "social__icon", 20)}</a>'
        for s in SITE["social"])
    util = " ".join(f'<a href="{u}">{esc(l)}</a>' for l, u in FOOTER_UTILITY)
    addr = "<br>".join(esc(l) for l in SITE["address_lines"])
    return f'''
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <img class="footer__mark" src="/assets/img/logo-mark-white-300.png" width="300" height="240"
             alt="" loading="lazy" decoding="async">
        <p class="footer__name">Synia Aid Foundation</p>
        <p class="footer__tag">{esc(SITE["tagline"])}</p>
        <p class="footer__mottos">Educate the mind&nbsp;· Equip the hands&nbsp;· Secure the home</p>
        <div class="footer__socials">{socials}</div>
      </div>

      <nav class="footer__col" aria-label="Stand with us">
        <h2 class="footer__h">Stand with us</h2>
        <ul>
          <li><a href="/donate/">Donate</a></li>
          <li><a href="/get-involved/partner/">Partner with us</a></li>
          <li><a href="/get-involved/volunteer/">Volunteer</a></li>
          <li><a href="/get-involved/ambassador/">Become an ambassador</a></li>
        </ul>
      </nav>

      <nav class="footer__col" aria-label="Explore">
        <h2 class="footer__h">Explore</h2>
        <ul>
          <li><a href="/about/">Who we are</a></li>
          <li><a href="/what-we-do/">What we do</a></li>
          <li><a href="/who-we-serve/">Who we serve</a></li>
          <li><a href="/impact/">Our impact</a></li>
          <li><a href="/accountability/">Accountability</a></li>
          <li><a href="/news/">News</a></li>
        </ul>
      </nav>

      <div class="footer__col footer__contact">
        <h2 class="footer__h">Contact</h2>
        <address>
          <p>{addr}</p>
          <p><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>
          <p><a href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a></p>
          <p><a href="tel:{SITE["hotline_href"]}">{SITE["hotline"]}</a> <span class="tag-24">24/7 hotline</span></p>
          <p class="footer__hours">{esc(SITE["hours"])}</p>
        </address>
      </div>
    </div>

    <div class="footer__legal">
      <p class="footer__reg">
        <strong>Synia Aid Foundation</strong> is registered with the Corporate Affairs Commission of the
        Federal Republic of Nigeria as Incorporated Trustees.
        Registration number <strong>{SITE["reg_number"]}</strong>. Head office: {esc(SITE["address_one_line"])}.
      </p>
      <nav class="footer__util" aria-label="Legal and utility">{util}</nav>
      <p class="footer__copy">© 2026 Synia Aid Foundation. All rights reserved.
        Photography by SageView Productions, published with consent — to have an image of you removed,
        <a href="/contact/?subject=general">contact us</a>.</p>
    </div>
  </div>
</footer>

<div class="cookie" data-cookie hidden role="dialog" aria-modal="false" aria-labelledby="cookie-h">
  <div class="cookie__inner">
    <div class="cookie__text">
      <h2 class="cookie__h" id="cookie-h">Cookies on this site</h2>
      <p>We use essential cookies to make this site work. We would also like to set optional analytics
        cookies to understand how the site is used, so we can improve it. We will not set optional
        cookies unless you accept them. Read our <a href="/cookies/">Cookie Policy</a>.</p>
    </div>
    <div class="cookie__actions">
      <button class="btn btn--cta" type="button" data-cookie-accept>Accept analytics cookies</button>
      <button class="btn btn--ghost-light" type="button" data-cookie-reject>Reject optional cookies</button>
    </div>
  </div>
</div>'''


# ---------------------------------------------------------------------------
# Document shell
# ---------------------------------------------------------------------------

def render(*, url, title, description, body, page_class="", schema=None,
           og_type="website", noindex=False):
    full_title = title if title.endswith(SITE["name"]) else f"{title} | {SITE['name']}"
    canonical = SITE["base_url"] + url
    schema_blocks = ""
    if schema:
        for s in (schema if isinstance(schema, list) else [schema]):
            schema_blocks += ('<script type="application/ld+json">'
                              + json.dumps(s, ensure_ascii=False) + "</script>")
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="en-NG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="theme-color" content="#0F2A47">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(SITE["name"])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_NG">
<meta property="og:image" content="{SITE["base_url"]}/assets/img/social-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/icon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/site.css">
{schema_blocks}
</head>
<body class="{page_class}">
{header(url)}
<main id="main" tabindex="-1">
{body}
</main>
{footer()}
<script src="/assets/js/config.js" defer></script>
<script src="/assets/js/site.js" defer></script>
</body>
</html>'''
