# -*- coding: utf-8 -*-
"""Higher-level building blocks assembled from the layout primitives."""

from . import data as D
from .layout import (icon, esc, chip, btn, breadcrumbs, section_head, note,
                     newsletter_form, image_placeholder)

PILLAR_BY_SLUG = {p["slug"]: p for p in D.PILLARS}
PROGRAMME_BY_SLUG = {p["slug"]: p for p in D.PROGRAMMES}
PARTNER_BY_SLUG = {p["slug"]: p for p in D.PARTNERS}
PILLAR_INDEX = {p["slug"]: i + 1 for i, p in enumerate(D.PILLARS)}


def programme_url(slug):
    return f"/programmes/{slug}/"


def pillar_url(slug):
    return f"/what-we-do/{slug}/"


def pillar_name(slug):
    if slug == "across-all-pillars":
        return "Across all pillars"
    return PILLAR_BY_SLUG[slug]["name"]


# ---------------------------------------------------------------------------

def page_hero(*, title, lede=None, trail=None, eyebrow_text=None, meta=None,
              variant="", actions=None):
    crumbs = breadcrumbs(trail) if trail else ""
    eb = f'<p class="eyebrow">{esc(eyebrow_text)}</p>' if eyebrow_text else ""
    ld = f'<p class="lede">{lede}</p>' if lede else ""
    mt = f'<div class="page-hero__meta">{meta}</div>' if meta else ""
    ac = f'<div class="btn-row mt-5">{"".join(actions)}</div>' if actions else ""
    return f'''
<section class="page-hero {variant}">
  <div class="container">
    {crumbs}
    <div class="page-hero__inner">
      {eb}<h1>{title}</h1>{ld}{mt}{ac}
    </div>
  </div>
</section>'''


def status_board():
    counts = {"running": 0, "setup": 0, "planned": 0}
    for p in D.PROGRAMMES:
        counts[p["status"]] += 1
    items = []
    for key in ("running", "setup", "planned"):
        st = D.STATUSES[key]
        items.append(
            f'<div class="status-board__item">{chip(key)}'
            f'<p class="status-board__count">{counts[key]} '
            f'<span class="small text-muted">of {len(D.PROGRAMMES)}</span></p>'
            f'<p class="status-board__def">{esc(st["definition"])}</p></div>')
    return f'<div class="status-board">{"".join(items)}</div>'


def programme_card(p, show_pillar=False):
    st_note = p.get("status_note")
    pub = (f'<p class="card__public-name">Known publicly as {esc(p["public_name"])}</p>'
           if p.get("public_name") else "")
    pil = (f'<p class="card__meta">{esc(pillar_name(p["pillar"]))}</p>' if show_pillar else "")
    flag = f'<span class="tag tag--muted">{esc(p["flagship"])}</span>' if p.get("flagship") else ""
    key = D.PROGRAMME_PHOTOS.get(p["slug"])
    media = (photo(key, "3x2", sizes="(min-width: 940px) 360px, 100vw", max_width=640)
             if key else "")
    cls = "card card--link card--programme" + (" card--photo" if media else "")
    return f'''
<article class="{cls}" data-facets="{p["pillar"]} {p["status"]}">
  {media}
  <div class="card__body">
    <div class="card__top">{chip(p["status"])}{flag}</div>
    <h3><a class="stretched" href="{programme_url(p["slug"])}">{esc(p["short_name"])}</a></h3>
    {pub}{pil}
    <p>{esc(p["one_line"])}</p>
    {f'<p class="card__meta small">{esc(st_note)}</p>' if st_note else ''}
    <p class="card__foot"><span class="card__more">Read the programme{icon("arrow-right", "", 18)}</span></p>
  </div>
</article>'''


def pillar_card(p, index):
    progs = [x for x in D.PROGRAMMES if x["pillar"] == p["slug"]]
    lis = "".join(
        f'<li><a href="{programme_url(x["slug"])}">{esc(x["short_name"])}</a>{chip(x["status"])}</li>'
        for x in progs)
    return f'''
<article class="card card--link card--pillar p{index}">
  <span class="pillar__icon">{icon(p["icon"], "", 28)}</span>
  <p class="pillar__motto">{esc(p["motto"])}</p>
  <h3><a class="stretched" href="{pillar_url(p["slug"])}">{esc(p["name"])}</a></h3>
  <p>{esc(p["lede"])}</p>
  <ul class="pillar__list">{lis}</ul>
</article>'''


def person_card(person, url_base="/about/leadership/"):
    initials = "".join(w[0] for w in person["name"].replace("Dr ", "").split()[:2]).upper()
    return f'''
<article class="card card--person" id="{person["slug"]}">
  <span class="person__avatar" aria-hidden="true">{initials}</span>
  <h3>{esc(person["name"])}</h3>
  <p class="person__role">{esc(person["role"])}</p>
  <p class="person__creds">{esc(person["credentials"])}</p>
  <p>{esc(person["summary"])}</p>
  <p class="card__foot"><a class="card__more" href="{url_base}#{person["slug"]}-bio">
    Read full biography{icon("arrow-right", "", 18)}</a></p>
</article>'''


def partner_card(partner):
    """Logo published only where written permission is confirmed [Partner List
    §01/§04]. Until then the partner shows as a text entry in the same card
    layout, so the grid stays even."""
    if partner.get("logo_permission") and partner.get("logo"):
        slot = (f'<div class="partner__logo-slot"><img src="/assets/img/partners/{partner["logo"]}" '
                f'alt="{esc(partner["name"])}" loading="lazy" decoding="async"></div>')
    else:
        slot = ('<div class="partner__logo-slot" aria-hidden="true">'
                f'{esc(partner["name"])}</div>')
    progs = [PROGRAMME_BY_SLUG[s] for s in partner["programmes"] if s in PROGRAMME_BY_SLUG]
    links = ("".join(f'<a href="{programme_url(x["slug"])}">{esc(x["short_name"])}</a>'
                     for x in progs))
    links_html = (f'<p class="card__meta">Works with us on: {links}</p>' if progs else "")
    return f'''
<article class="card card--partner">
  {slot}
  <p class="partner__name">{esc(partner["name"])}</p>
  <p>{esc(partner["description"])}</p>
  {links_html}
</article>'''


def news_card(item, with_photo=True):
    pil = f' {item["pillar"]}' if item.get("pillar") else ""
    key = D.NEWS_PHOTOS.get(item["slug"])
    media = (photo(key, "3x2", sizes="(min-width: 940px) 360px, 100vw", max_width=640)
             if (with_photo and key) else "")
    cls = "card card--link card--news" + (" card--photo" if media else "")
    return f'''
<article class="{cls}" data-facets="{esc(item["category"])}{pil}">
  {media}
  <div class="card__body">
    <p class="card__cat">{esc(item["category"])}</p>
    <h3><a class="stretched" href="/news/{item["slug"]}/">{esc(item["title"])}</a></h3>
    <p class="card__meta">{esc(item["date_display"])}</p>
    <p>{esc(item["excerpt"])}</p>
    <p class="card__foot"><span class="card__more">Read more{icon("arrow-right", "", 18)}</span></p>
  </div>
</article>'''


def story_card(item, with_photo=True):
    pil = item.get("pillar") or ""
    fmt_icon = {"Film": "film", "Photo essay": "camera", "Written": "doc"}.get(item["format"], "doc")
    key = D.STORY_PHOTOS.get(item["slug"])
    media = (photo(key, "3x2", sizes="(min-width: 940px) 360px, 100vw", max_width=640)
             if (with_photo and key) else "")
    cls = "card card--link" + (" card--photo" if media else "")
    return f'''
<article class="{cls}" data-facets="{pil} {item["format"].lower().replace(" ", "-")}">
  {media}
  <div class="card__body">
    <p class="card__cat"><span class="tag">{icon(fmt_icon, "", 16)} {esc(item["format"])}</span></p>
    <h3><a class="stretched" href="/impact/stories/{item["slug"]}/">{esc(item["title"])}</a></h3>
    <p class="card__meta">{esc(item["date_display"])}{" · " + esc(pillar_name(pil)) if pil else ""}</p>
    <p>{esc(item["excerpt"])}</p>
    <p class="card__foot"><span class="card__more">Read the story{icon("arrow-right", "", 18)}</span></p>
  </div>
</article>'''


def doc_card(title, summary, meta, href, cta="Download PDF"):
    return f'''
<article class="card card--doc">
  <span class="doc__icon">{icon("doc", "", 22)}</span>
  <div class="doc__body">
    <h3>{esc(title)}</h3>
    <p>{esc(summary)}</p>
    <p class="doc__meta">{meta}</p>
    <p class="card__foot"><a class="card__more" href="{href}" download>
      {icon("download", "", 18)} {esc(cta)}</a></p>
  </div>
</article>'''


def get_involved_grid(exclude=None):
    cards = []
    for g in D.GET_INVOLVED:
        if g["slug"] == exclude:
            continue
        url = "/donate/" if g["slug"] == "donate" else f'/get-involved/{g["slug"]}/'
        key = D.GET_INVOLVED_PHOTOS.get(g["slug"])
        media = photo(key, "3x2", sizes="(min-width: 940px) 280px, 50vw", max_width=640) if key else ""
        cards.append(f'''
<article class="card card--link card--photo">
  {media}
  <div class="card__body">
    <span class="pillar__icon">{icon(g["icon"], "", 26)}</span>
    <h3><a class="stretched" href="{url}">{esc(g["title"])}</a></h3>
    <p>{esc(g["summary"])}</p>
    <p class="card__foot"><span class="card__more">{esc(g["cta"])}{icon("arrow-right", "", 18)}</span></p>
  </div>
</article>''')
    return f'<div class="grid grid--4">{"".join(cards)}</div>'


def donate_band():
    return f'''
<section class="cta-band cta-band--navy">
  <div class="container cta-band__inner">
    <div>
      <h2>Recurring giving lets us commit to a child for a full academic year</h2>
      <p>One-off or monthly gifts, from ₦5,000 upward, in Naira or from abroad. Every gift is receipted
         with our name and registration number.</p>
    </div>
    <div class="cta-band__actions">
      {btn("Donate", "/donate/", "cta")}
      {btn("Other ways to help", "/get-involved/", "ghost-light", None)}
    </div>
  </div>
</section>'''


def newsletter_band():
    return f'''
<section class="section section--navy">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Keep up with the work", "A short email when there is something real to report — "
                      "a programme launching, a report published, a story worth your time. "
                      "No more than we would want to receive ourselves.",
                      eyebrow_text="Newsletter")}
      </div>
      <div>{newsletter_form()}</div>
    </div>
  </div>
</section>'''


def contact_strip():
    return f'''
<section class="section section--tight section--surface">
  <div class="container">
    <div class="grid grid--3">
      <div class="card card--quiet">
        <span class="doc__icon">{icon("phone", "", 22)}</span>
        <h3>Speak to someone</h3>
        <p><a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a><br>
           <a href="tel:{D.SITE["hotline_href"]}">{D.SITE["hotline"]}</a> <span class="tag">24/7 hotline</span></p>
      </div>
      <div class="card card--quiet">
        <span class="doc__icon">{icon("mail", "", 22)}</span>
        <h3>Email us</h3>
        <p><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a><br>
           <span class="text-muted small">{esc(D.SITE["hours"])}</span></p>
      </div>
      <div class="card card--quiet">
        <span class="doc__icon">{icon("shield", "", 22)}</span>
        <h3>Raise a concern</h3>
        <p>Anyone may raise a concern about our work or the conduct of anyone acting in our name.
           <a href="/complaints/">How to raise a concern</a>.</p>
      </div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------------------
# Photography
#
# photo() records which (image, aspect ratio) pairs a page actually asks for.
# build.py then generates exactly those derivatives and nothing else — no
# unused bytes are shipped, and no crop is produced that the site never shows.
# ---------------------------------------------------------------------------

REQUESTED = set()

RATIOS = {
    "21x9": (21, 9), "16x9": (16, 9), "3x2": (3, 2), "4x3": (4, 3),
    "1x1": (1, 1), "4x5": (4, 5), "3x4": (3, 4), "2x3": (2, 3),
}

WIDTHS = [400, 640, 960, 1400]


# The widest derivative worth generating for each crop. A square tile in a
# four-across band is never displayed above ~400 CSS px, so shipping a 1400px
# version of it would be pure waste on a metered connection.
DEFAULT_MAX = {"1x1": 640, "4x5": 960, "3x4": 960, "2x3": 960, "4x3": 960}


def photo(key, ratio="16x9", *, sizes="(min-width: 940px) 620px, 100vw",
          eager=False, caption=None, cls="", focus=None, rounded=True,
          max_width=None):
    """A responsive, art-directed image. WebP first, JPEG fallback.

    The crop anchor defaults to the one recorded against the photograph, so a
    portrait frame cropped to a landscape slot keeps the subject's face rather
    than trimming the top of their head."""
    meta = D.PHOTOS.get(key)
    if not meta:
        raise KeyError(f"unknown photo: {key}")
    focus = focus or meta.get("focus", "center")
    cap_w = max_width or DEFAULT_MAX.get(ratio, 1400)
    widths = [n for n in WIDTHS if n <= cap_w] or [WIDTHS[0]]
    REQUESTED.add((key, ratio, focus, cap_w))

    w, h = RATIOS[ratio]
    base = f"/assets/img/photos/{key}-{ratio}-{focus}"
    webp = ", ".join(f"{base}-{n}.webp {n}w" for n in widths)
    jpg = ", ".join(f"{base}-{n}.jpg {n}w" for n in widths)
    fallback_w = widths[-1]
    loading = ("" if eager else ' loading="lazy"')
    priority = ' fetchpriority="high" decoding="sync"' if eager else ' decoding="async"'
    cap = (f'<figcaption class="photo__caption">{caption}</figcaption>' if caption else "")
    r = "" if rounded else " photo--square-corners"

    return f'''<figure class="photo{r} {cls}" style="--photo-ratio:{w} / {h}">
  <picture>
    <source type="image/webp" srcset="{webp}" sizes="{sizes}">
    <img src="{base}-{fallback_w}.jpg" srcset="{jpg}" sizes="{sizes}"
         width="{w * 100}" height="{h * 100}" alt="{esc(meta["alt"])}"{loading}{priority}>
  </picture>{cap}
</figure>'''


def photo_credit_line():
    return (f'Photography: {esc(D.PHOTO_CREDIT)}. Published with the consent of the people shown; '
            f'if you appear in an image here and would like it removed, '
            f'<a href="/contact/?subject=general">tell us</a> and it will come down promptly.')
