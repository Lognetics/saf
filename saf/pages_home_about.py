# -*- coding: utf-8 -*-
"""Home, About Us, Our Story, Leadership & Governance, Partners, Who We Serve."""

import os

from . import data as D
from .layout import (icon, esc, chip, btn, section_head, note, table, stat_grid,
                     bullets, paras, newsletter_form, image_placeholder, breadcrumbs,
                     section_nav, cta_band)
from .components import (page_hero, pillar_card, programme_card,
                         person_card, partner_card, news_card, get_involved_grid,
                         donate_band, newsletter_band, contact_strip, programme_url,
                         pillar_url, PILLAR_INDEX, photo, photo_credit_line, person_url,
                         ROLE_ICON)
from .graphics import nigeria_map, map_legend

ABOUT_NAV = [
    ("Who We Are & Our Story", "/about/"),
    ("Leadership & Governance", "/about/leadership/"),
    ("Partners", "/about/partners/"),
    ("Who We Serve", "/who-we-serve/"),
]

HERE = os.path.dirname(os.path.abspath(__file__))
HERO_VIDEO = os.path.join(os.path.dirname(HERE), "assets", "video", "hero.mp4")


# ===========================================================================
# HOME
# ===========================================================================

def home():
    pillars = "".join(pillar_card(p, PILLAR_INDEX[p["slug"]]) for p in D.PILLARS)
    news = "".join(news_card(n) for n in D.NEWS[:3])

    mottos = "".join(
        f'<span class="hero__motto">{icon(p["icon"], "", 18)}{esc(p["motto"])}</span>'
        for p in D.PILLARS)

    story = D.STORIES[0]
    headline = D.NEED_STATS[2]

    # The hero opens with the Foundation's film once assets/video/hero.mp4 is
    # supplied. Until then it shows the photograph, so nothing is ever broken.
    if os.path.isfile(HERO_VIDEO):
        hero_visual = ""
        hero_bg = ('<div class="hero__video" aria-hidden="true"><video autoplay muted loop playsinline '
                   'preload="metadata" poster="/assets/img/photos/classroom-boy-desk-4x5-upper-960.jpg">'
                   '<source src="/assets/video/hero.mp4" type="video/mp4"></video></div>')
        hero_cls = "hero hero--home hero--video"
    else:
        hero_bg = ""
        hero_visual = f'''<div>
        {photo("classroom-boy-desk", "4x5", sizes="(min-width: 980px) 460px, 100vw",
               eager=True, focus="upper")}
      </div>'''
        hero_cls = "hero hero--home"

    return f'''
<section class="{hero_cls}">
  {hero_bg}
  <div class="container hero__inner">
    <div class="hero__grid">
      <div>
        <h1>Dignity, opportunity and <em>a way forward</em> for displaced Nigerian families</h1>
        <p class="hero__lede">We work with internally displaced persons and indigent communities across Nigeria,
          getting children back into school, helping adults rebuild an income, and making homes safe and secure.</p>
        <div class="hero__actions btn-row">
          {btn("Donate", "/donate/", "cta")}
          {btn("See what we do", "/what-we-do/", "ghost-light", None)}
        </div>
        <div class="hero__mottos">{mottos}</div>
      </div>
      {hero_visual}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Three pillars, one road out",
                  "A family that has been displaced does not have one problem. The children are out of school, "
                  "the adults have lost their trade, and the home is gone. Our three pillars are designed to be "
                  "used together.",
                  eyebrow_text="What we do")}
    <div class="grid grid--3" data-reveal>{pillars}</div>
    <div class="btn-row mt-6">{btn("How the pillars fit together", "/what-we-do/", "ghost")}</div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("The need we address", None, eyebrow_text="Displacement in Nigeria")}
        <p>Nigeria hosts one of the largest internally displaced populations in the world, and most displaced
           Nigerians do not live in camps. We serve displaced people wherever assessed need exists, including
           in formal camps, and we make a particular effort to reach the majority who don't live in one, because
           that is where the response is weakest.</p>
        <p>We concentrate on the FCT–Nasarawa–Keffi corridor, in and outside formal camps, with particular
           attention to the majority who live outside one.</p>
        <div class="btn-row mt-5">
          {btn("Who we serve", "/who-we-serve/", "light")}
        </div>
      </div>
      <div>
        <div class="headline-stat">
          <span class="stat__icon stat__icon--lg">{icon(headline["icon"], "", 30)}</span>
          <p class="stat__figure">{esc(headline["figure"])}</p>
          <p class="stat__label">{esc(headline["label"])}</p>
          <p class="stat__sub">{esc(headline["sub"])}. Source: IOM Displacement Tracking Matrix Nigeria, 2025.</p>
          <p class="mb-0 mt-4"><a class="card__more card__more--light" href="/who-we-serve/#need">
            The full figures and sources{icon("arrow-right", "", 18)}</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("A story from the work", None, eyebrow_text="Featured")}
    <div class="grid grid--split">
      <div>
        {photo("classroom-desks", "4x3", sizes="(min-width: 880px) 560px, 100vw")}
      </div>
      <div>
        <p class="card__cat" style="color:var(--blue);font-weight:750;letter-spacing:.08em;text-transform:uppercase;font-size:.74rem">
          Education &amp; Skills</p>
        <h3 style="font-size:var(--step-3)">{esc(story["title"])}</h3>
        <p class="lede">{esc(story["excerpt"])}</p>
        <p>Where a community holds the skill, we buy it there. The same expenditure creates a learning space
           and an income, and a piece of furniture made by a neighbour is a piece of furniture that gets
           repaired rather than replaced.</p>
        <div class="btn-row">{btn("Read the story", "/impact/stories/" + story["slug"] + "/", "primary")}
          {btn("All stories", "/impact/stories/", "ghost", None)}</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:1rem;max-width:none;flex-wrap:wrap">
      <div style="max-width:52ch">
        <p class="eyebrow">Latest news</p>
        <h2>What we have been doing</h2>
      </div>
      {btn("All news", "/news/", "ghost")}
    </div>
    <div class="grid grid--3">{news}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="photo-band">
      {photo("children-laughing", "1x1", sizes="(min-width: 700px) 25vw, 50vw")}
      {photo("women-gathering", "1x1", sizes="(min-width: 700px) 25vw, 50vw")}
      {photo("classroom-friends", "1x1", sizes="(min-width: 700px) 25vw, 50vw")}
      {photo("elder-smiling", "1x1", sizes="(min-width: 700px) 25vw, 50vw", focus="upper")}
    </div>
    <p class="small text-muted mt-4">{photo_credit_line()}</p>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Four ways to stand with the Foundation", None, eyebrow_text="Get involved")}
    {get_involved_grid(teaser=True)}
    <div class="btn-row mt-6">{btn("All the ways to get involved", "/get-involved/", "ghost")}</div>
  </div>
</section>

{newsletter_band()}
'''


# ===========================================================================
# WHO WE ARE & OUR STORY  (/about/)  — the two pages are merged
# ===========================================================================

TIMELINE_TYPES = {
    "foundation": ("shield", "Foundation"),
    "outreach": ("heart", "Outreach"),
    "campaign": ("megaphone", "Campaign"),
    "programme": ("target", "Programme"),
    "event": ("people", "Convening"),
}
TIMELINE_KIND = ["foundation", "outreach", "campaign", "outreach", "outreach", "campaign", "outreach",
                 "campaign", "programme", "event", "outreach", "programme", "programme"]

PRINCIPLE_ICONS = ["people", "handshake", "chart", "target", "check", "doc"]


def who_we_are():
    values = "".join(
        f'<details class="value"><summary><span class="value__n">{i+1:02d}</span>{esc(t)}</summary>'
        f'<p>{esc(b)}</p></details>'
        for i, (t, b) in enumerate(D.VALUES))

    items = []
    for i, (y, t, b) in enumerate(D.TIMELINE):
        kind = TIMELINE_KIND[i] if i < len(TIMELINE_KIND) else "programme"
        ic, label = TIMELINE_TYPES[kind]
        items.append(
            f'<li class="vtl__item vtl__item--{kind}"><span class="vtl__marker" title="{esc(label)}">'
            f'{icon(ic, "", 18)}</span><div class="vtl__card"><span class="timeline__year">{esc(y)}</span>'
            f'<h3 class="vtl__title">{esc(t)}</h3>'
            f'<details class="vtl__more"><summary>Read more</summary><p>{b}</p></details></div></li>')
    legend = "".join(
        f'<li><span class="vtl__key vtl__key--{k}">{icon(ic, "", 14)}</span>{esc(lab)}</li>'
        for k, (ic, lab) in TIMELINE_TYPES.items())

    principles = "".join(
        f'<div class="principle"><span class="principle__icon">{icon(PRINCIPLE_ICONS[i], "", 22)}</span>'
        f'<h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
        for i, (t, b) in enumerate(D.OPERATING_PRINCIPLES))

    return page_hero(
        title="Who we are &amp; our story",
        lede="A Nigerian humanitarian and development organisation working to restore hope and dignity to "
             "people pushed to the margins of society, and the road that brought us here from 2018.",
        eyebrow_text="About us",
        image="children-community",
        trail=[("Home", "/"), ("About Us", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/")}</div>

<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        <p class="lede">Synia Aid Foundation works to restore hope and dignity to people pushed to the margins
          of society, above all internally displaced persons, and the wider community of indigent and
          vulnerable Nigerians whose lives have been disrupted by conflict, insecurity, disaster and poverty.</p>
        <p>The Foundation was established in December 2018 and registered with the Corporate Affairs Commission
          of the Federal Republic of Nigeria. From a first community drive in January 2019, we have grown into a
          multi-programme organisation delivering education, livelihoods, shelter and community-wellbeing work
          across several Nigerian states, always on the conviction that the people we serve are partners and
          experts in their own recovery, not passive recipients of charity.</p>

        <h2>Our guiding philosophy</h2>
        <p>The Foundation was founded on a durable conviction inherited from the educationist
          Dr A. A. Nwafor-Orizu: <strong>to educate the mind is to liberate it</strong>. We treat education and
          skills not as acts of generosity but as the most effective and lasting route out of poverty. Relief
          meets the urgent need of today; education and empowerment break the cycle for tomorrow.</p>
        <p>Equally, we are committed to moving beyond charity. Giving is good, but it can obscure the structural
          causes of poverty and displacement. We therefore pair immediate, on-the-ground relief with a
          longer-term ambition: to understand and address the social and economic forces that keep people poor,
          and to advocate for the protective policies that displaced Nigerians urgently need.</p>

        <blockquote class="pullquote">Relief meets the need of today. Education, livelihoods and legal
          protection determine whether that need returns next year.</blockquote>
      </div>

      <aside>
        <div class="card card--quiet">
          <h3>On this page</h3>
          <ul class="linklist" style="margin-top:.5rem">
            <li><a href="#vision">Vision &amp; mission{icon("arrow-right", "", 18)}</a></li>
            <li><a href="#values">Our core values{icon("arrow-right", "", 18)}</a></li>
            <li><a href="#our-story">Our story{icon("arrow-right", "", 18)}</a></li>
            <li><a href="#how-we-work">How we work{icon("arrow-right", "", 18)}</a></li>
          </ul>
        </div>
        <div class="mt-5">{photo("classroom-boy-yellow", "4x5", sizes="(min-width: 940px) 336px, 100vw", focus="upper")}</div>
        <div class="card mt-5">
          <span class="doc__icon">{icon("doc", "", 22)}</span>
          <h3>Corporate Profile 2026</h3>
          <p class="small">Edition 2, July 2026. The full picture: governance, programmes, track record,
            risk register and roadmap.</p>
          <p class="card__foot"><a class="card__more" href="/assets/documents/SAF-Corporate-Profile-2026.pdf" download>
            {icon("download", "", 18)} Download PDF</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--navy" id="vision">
  <div class="container">
    <div class="grid grid--2">
      <div>
        <p class="eyebrow">Our vision</p>
        <p class="statement__q">{esc(D.VISION)}</p>
      </div>
      <div>
        <p class="eyebrow">Our mission</p>
        <p class="statement__q">{esc(D.MISSION)}</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="values">
  <div class="container">
    {section_head("Our core values", "Eight values govern how we work. Open any one to read what it means in practice.",
                  eyebrow_text="What governs how we work")}
    <div class="values">{values}</div>
  </div>
</section>

<section class="section section--surface" id="our-story">
  <div class="container">
    {section_head("Our story", "From a single charity drive to a multi-programme foundation. Early outreach built "
                  "the trust and access on which our three pillars now stand.", eyebrow_text="Milestones from 2018")}
    <ul class="vtl__legend" aria-label="Milestone types">{legend}</ul>
    <div class="grid grid--sidebar">
      <div>
        <ol class="vtl">{"".join(items)}</ol>
      </div>
      <aside>
        <div class="card">
          <p class="eyebrow">From the founder</p>
          <blockquote class="pullquote" style="margin-top:0">Synia Aid Foundation began with a question I could
            not put down: what happens to people who are forced from their homes but never cross a border?
            <cite>Mmaobi Nwafor-Orizu, Founder &amp; Chair</cite></blockquote>
          <p class="card__foot"><a class="card__more" href="/about/leadership/mmaobi-nwafor-orizu/">
            Read the founder's biography{icon("arrow-right", "", 18)}</a></p>
        </div>
        {photo("classroom-boy-desk", "4x5", sizes="(min-width: 940px) 336px, 100vw", cls="mt-5")}
        <p class="small text-muted mt-3">{photo_credit_line()}</p>
      </aside>
    </div>
  </div>
</section>

<section class="section" id="how-we-work">
  <div class="container">
    {section_head("How we work", None, eyebrow_text="Operating principles")}
    <div class="principles">{principles}</div>
  </div>
</section>

{cta_band("Read the full Corporate Profile",
          "Twenty-nine pages: our theory of change, programme portfolio, track record, monitoring framework, "
          "governance, financial stewardship, risk register and roadmap to 2029.",
          [btn("Download the profile", "/assets/documents/SAF-Corporate-Profile-2026.pdf", "cta", "download"),
           btn("See all publications", "/accountability/reports-and-publications/", "ghost-light", None)])}
'''


# ===========================================================================
# LEADERSHIP & GOVERNANCE
# ===========================================================================

def leadership():
    trustees = [p for p in D.BOARD if p["group"] == "board"]
    advisers = [p for p in D.BOARD if p["group"] == "adviser"]

    cards_board = "".join(person_card(p, "board") for p in trustees)
    cards_adv = "".join(person_card(p, "adviser") for p in advisers)
    cards_exec = "".join(person_card(p, "executive") for p in D.EXECUTIVE)

    bodies = table(["Body", "Responsibility"],
                   [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.GOVERNANCE_BODIES])

    key = "".join(
        f'<li><span class="lead__key lead__key--{g}">{icon(ic, "", 16)}</span>{esc(lab)}</li>'
        for g, (ic, lab) in ROLE_ICON.items())

    return page_hero(
        title="Leadership &amp; governance",
        lede="The Foundation is led by a founder-chaired Board of Trustees, which draws on specialist advisers "
             "in law, human resources and media strategy sitting at Board level, and is delivered by an "
             "executive team responsible for day-to-day operations and communications.",
        eyebrow_text="About us",
        image="women-gathering",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Leadership & Governance", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/leadership/")}</div>

<section class="section section--tight">
  <div class="container">
    <ul class="lead__legend" aria-label="Key to the icons">{key}</ul>
    {section_head("Board of Trustees",
                  "The Board holds strategic direction, approves programmes and policy, and carries financial "
                  "and safeguarding oversight.", eyebrow_text="Governance")}
    <div class="grid grid--3">{cards_board}</div>

    <h3 class="mt-7">Advisers to the Board</h3>
    <p class="measure">Specialist counsel at Board level in law, human resources and media strategy, informing
      decisions without executive responsibility for delivery.</p>
    <div class="grid grid--3 mt-5">{cards_adv}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Executive team",
                  "Responsible for day-to-day delivery, operations and communications within Board-approved "
                  "budgets and policies.", eyebrow_text="Delivery")}
    <div class="grid grid--3">{cards_exec}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("How decisions are made", None, eyebrow_text="Governance structure")}
    {bodies}
    <div class="btn-row mt-6">
      {btn("Governance &amp; Policies", "/accountability/governance-and-policies/", "primary")}
      {btn("Download leadership biographies", "/assets/documents/SAF-Leadership-Biographies.pdf", "ghost", "download")}
    </div>
  </div>
</section>

{contact_strip()}
'''


def leadership_bio(person, group):
    ic, label = ROLE_ICON[group]
    initials = "".join(w[0] for w in person["name"].replace("Dr ", "").split()[:2]).upper()
    others = [p for p in D.BOARD + D.EXECUTIVE if p["slug"] != person["slug"]]
    people = "".join(
        f'<li><a href="{person_url(o)}"><span>{esc(o["name"])}<small>{esc(o["role"])}</small></span>'
        f'{icon("arrow-right", "", 18)}</a></li>' for o in others)
    return page_hero(
        title=esc(person["name"]),
        lede=esc(person["role"]),
        eyebrow_text=label,
        image="women-gathering",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Leadership & Governance", "/about/leadership/"),
               (person["name"], None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <article class="prose">
        <div class="bio__head">
          <span class="person__avatar person__avatar--lg" aria-hidden="true">{initials}</span>
          <div>
            <p class="person__role">{esc(person["role"])}</p>
            <p class="person__creds mb-0">{esc(person["credentials"])}</p>
            <p class="person__group mt-2">{icon(ic, "", 16)}<span>{esc(label)}</span></p>
          </div>
        </div>
        {"".join(f"<p>{x}</p>" for x in person["bio"])}
        {note(f'<p>{esc(person["remit"])}</p>', "Remit at the Foundation", "info", "target")}
        <div class="btn-row mt-5">
          {btn("Back to leadership", "/about/leadership/", "primary")}
          {btn("Download all biographies", "/assets/documents/SAF-Leadership-Biographies.pdf", "ghost", "download")}
        </div>
      </article>
      <aside>
        <div class="card card--quiet">
          <h3>Others on the team</h3>
          <ul class="linklist mt-4">{people}</ul>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# PARTNERS
# ===========================================================================

PARTNER_CAT_ICON = {"education-skills": "book", "displacement-response": "house",
                    "community-outreach": "heart"}


def partners():
    blocks = []
    for slug, heading, intro in D.PARTNER_CATEGORIES:
        members = sorted([p for p in D.PARTNERS if p["category"] == slug], key=lambda x: x["order"])
        cards = "".join(f'<div id="{m["slug"]}">{partner_card(m)}</div>' for m in members)
        blocks.append(f'''
<section class="section section--tight">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{len(members)} partner{"s" if len(members) != 1 else ""}</p>
      <h2 class="cat-head"><span class="cat-head__icon">{icon(PARTNER_CAT_ICON[slug], "", 24)}</span>{esc(heading)}</h2>
      <p class="lede">{esc(intro)}</p>
    </div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>''')

    pursued = bullets([esc(x) for x in D.PARTNERSHIPS_PURSUED], icon_name="target")

    return page_hero(
        title="Partners",
        lede=D.PARTNERS_INTRO,
        eyebrow_text="About us",
        image="women-smiling",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Partners", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/partners/")}</div>
{"".join(blocks)}

<section class="section section--tight">
  <div class="container">
    <div class="photo-band">
      {photo("classroom-desks", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-outside", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <p class="small text-muted mt-4">Work delivered alongside our partners. {photo_credit_line()}</p>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="pursuing">
      <div>
        {section_head("Partnerships we are pursuing",
                      "These are not current relationships. We name them because ambition stated plainly reads "
                      "as confidence, and because a prospective partner presented as a current one is the "
                      "fastest way to lose the credibility the rest of this site is built to establish.",
                      eyebrow_text="Actively seeking")}
      </div>
      <div>{pursued}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head(esc(D.PARTNER_CTA["heading"]), esc(D.PARTNER_CTA["body"]), eyebrow_text="Work with us")}
        <div class="btn-row">
          {btn(D.PARTNER_CTA["button"], "/contact/?subject=partnership", "cta")}
          {btn("What partnership involves", "/get-involved/partner/", "ghost", None)}
        </div>
      </div>
      <div>
        {photo("classroom-boy-yellow", "4x3", sizes="(min-width: 880px) 540px, 100vw")}
      </div>
    </div>
  </div>
</section>
'''


# ===========================================================================
# WHO WE SERVE
# ===========================================================================

GROUP_ICONS = ["house", "book", "people", "heart", "users-check", "globe"]


def who_we_serve():
    groups = table(
        ["Group", "Definition", "Primary programmes"],
        [[f'<span class="group-name"><span class="group-icon">{icon(GROUP_ICONS[i], "", 20)}</span>'
          f'<strong>{esc(a)}</strong></span>', esc(b), f'<span class="tag tag--muted">{esc(c)}</span>']
         for i, (a, b, c) in enumerate(D.BENEFICIARY_GROUPS)])

    steps = "".join(
        f'<li><div><h3>{esc(t)}</h3><p>{esc(b)}</p></div></li>' for t, b in D.SELECTION_STEPS)

    implications = table(
        ["The finding", "The implication for how we work"],
        [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.NEED_IMPLICATIONS])

    return page_hero(
        title="Who we serve",
        lede="The Foundation exists first and foremost for internally displaced persons, Nigerians forced from "
             "their homes who, unlike refugees, remain inside their own country and often fall through the gaps "
             "in formal protection.",
        eyebrow_text="The people our work is for",
        image="children-outside",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Who We Serve", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/who-we-serve/")}</div>

<section class="section section--tight">
  <div class="container">
    <p class="lede measure">Around this core, we serve the wider community of indigent and vulnerable Nigerians
      whose circumstances share the same roots in poverty and exclusion.</p>
    <div class="mt-6">{groups}</div>
    <div class="gallery mt-7">
      {photo("classroom-group", "4x3", sizes="(min-width: 760px) 33vw, 50vw")}
      {photo("women-smiling", "4x3", sizes="(min-width: 760px) 33vw, 50vw")}
      {photo("elder-seated", "4x3", sizes="(min-width: 760px) 33vw, 50vw", focus="upper")}
    </div>
  </div>
</section>

<section class="section section--navy" id="need">
  <div class="container">
    {section_head("The need we address",
                  "Nigeria hosts one of the largest internally displaced populations in the world. The figures "
                  "below are drawn from the International Organization for Migration's Displacement Tracking "
                  "Matrix, the standard reference for displacement data in Nigeria.",
                  eyebrow_text="Context, with sources")}
    {stat_grid(D.NEED_STATS, "stat-grid--dark")}
    <p class="small mt-5" style="color:#9FBBD6;max-width:90ch">{esc(D.NEED_SOURCE)}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("What these numbers mean for programming", None, eyebrow_text="From data to design")}
    {implications}
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Behind the figures", None, eyebrow_text="What displacement means")}
        {paras([esc(p) for p in D.BEHIND_THE_FIGURES])}
      </div>
      <div>
        {photo("wheelchair-crossing", "3x4", sizes="(min-width: 880px) 540px, 100vw",
               caption="People we serve are shown as capable partners in their own recovery, never as "
                       "objects of pity. " + photo_credit_line())}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("How we select", "We act according to need, not status, ethnicity, gender, religion, "
                  "politics or any other interest. Selection follows a consistent process across every "
                  "programme.", eyebrow_text="Selection")}
    <ol class="steps">{steps}</ol>
    <div class="photo-band mt-6 mb-6">
      {photo("classroom-doorway", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-playing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("boys-lorry", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-gathering", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    {note(f'<p>{esc(D.CONDUCT_COMMITMENT)}</p>', "A commitment on conduct", "good", "shield")}
  </div>
</section>

<section class="section section--surface" id="footprint">
  <div class="container">
    {section_head("Where we work", None, eyebrow_text="Our footprint")}
    <div class="grid grid--split">
      <div>{nigeria_map()}{map_legend()}</div>
      <div>
        {paras([esc(p) for p in D.FOOTPRINT_NOTE])}
        <blockquote class="pullquote">Most displaced Nigerians do not live in camps. The response is weakest
          where displacement is least visible: in host communities, in cities, and among families who have
          been moved once already.<cite>Corporate Profile 2026, Section 13</cite></blockquote>
        <p>That gap is a reason for us to make extra effort outside camps, not a reason to step back from
          those inside them. We continue our work in formal camps such as Durumi and New Kuchingoro.</p>
      </div>
    </div>
  </div>
</section>

{donate_band()}
'''
