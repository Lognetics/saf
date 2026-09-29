# -*- coding: utf-8 -*-
"""What We Do, pillar pages, programme pages, Our Impact, Stories, Projects, News."""

from . import data as D
from .layout import (icon, esc, chip, btn, section_head, note, table, stat_grid,
                     bullets, paras, image_placeholder, section_nav, cta_band)
from .components import (page_hero, pillar_card, programme_card, pillar_badge,
                         news_card, story_card, donate_band, newsletter_band,
                         programme_url, pillar_url, pillar_name, PILLAR_INDEX,
                         PILLAR_BY_SLUG, PROGRAMME_BY_SLUG, PARTNER_BY_SLUG,
                         photo, photo_credit_line)
from .graphics import checklist_graphic

IMPACT_NAV = [
    ("Overview & How We Measure Impact", "/impact/"),
    ("Stories", "/impact/stories/"),
    ("Projects", "/impact/projects/"),
]


# ===========================================================================
# WHAT WE DO — overview
# ===========================================================================

def what_we_do():
    pillars = "".join(pillar_card(p, PILLAR_INDEX[p["slug"]]) for p in D.PILLARS)
    cross = "".join(programme_card(x) for x in D.PROGRAMMES if x["pillar"] == "across-all-pillars")

    flow = "".join(
        f'<div class="flow__col"><p class="flow__h">{esc(h)}</p><ul>'
        + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul></div>"
        for h, items in D.THEORY_OF_CHANGE)

    assumptions = "".join(
        f'<details class="value"><summary><span class="value__n">{i+1:02d}</span>{esc(a)}</summary>'
        f'<p>{esc(b)}</p></details>' for i, (a, b) in enumerate(D.TOC_ASSUMPTIONS))

    return page_hero(
        title="What we do",
        lede="Our work rests on three pillars, represented in the Foundation's logo by the open book, the "
             "lightbulb and the house. Together they form a continuum of care: educate the mind, equip the "
             "hands, secure the home.",
        eyebrow_text="Three pillars · twelve programmes",
        image="classroom-desks",
        trail=[("Home", "/"), ("What We Do", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Our three pillars</h2>
    <div class="grid grid--3">{pillars}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("One road out, not three services", None, eyebrow_text="How the pillars work together")}
        <p>A family that has been displaced does not have one problem. The children are out of school, the
           adults have lost their trade, and the home is gone. Our three pillars are designed to be used
           together, and a household may be supported by more than one at the same time.</p>
        <p>We have deliberately kept the structure small. It is easier to do a few things properly, and to
           prove that they worked, than to do many things and prove nothing.</p>
      </div>
      <div>
        {photo("classroom-friends", "16x9", sizes="(min-width: 880px) 540px, 100vw")}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head(esc(D.CROSS_CUTTING["name"]), esc(D.CROSS_CUTTING["lede"]),
                  eyebrow_text="Running through everything")}
    <div class="grid grid--2">{cross}</div>
    {note('<p>Every person delivering our work is vetted and bound by a code of conduct, and no child is ever '
          'met alone. A plain-language route to raise a concern is displayed wherever we work.</p>'
          '<p><a href="/safeguarding/">Read our safeguarding statement</a></p>',
          "Safeguarding runs through everything", "good", "shield")}
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Our theory of change",
                  "We follow a simple, repeatable method: identify needs, provide support, and create lasting "
                  "impact. Open a section to read more.",
                  eyebrow_text="Our logic")}
    <div class="accordion">
      <details>
        <summary>The method, from inputs to impact</summary>
        <div class="accordion__body"><div class="flow">{flow}</div></div>
      </details>
      <details>
        <summary>From outputs to outcomes</summary>
        <div class="accordion__body">
          <p>An output is what we did: a fee paid, a grant disbursed, a roof repaired. An outcome is what
             changed: a child still in school at the end of the year, a business still trading twelve months
             later, a family still housed and secure. We are building our monitoring framework to capture
             outcomes. <a href="/impact/#how-we-measure-impact">How we measure impact</a>.</p>
        </div>
      </details>
      <details>
        <summary>The assumptions we test</summary>
        <div class="accordion__body">
          <p>A theory of change that carries no assumptions is not a theory; it is a wish. Ours rests on four,
             each of which we test rather than presume.</p>
          <div class="values values--single">{assumptions}</div>
        </div>
      </details>
    </div>
  </div>
</section>

{cta_band("Every programme has a written model behind it",
          "Who it serves, what the standard package contains, what it costs per person, how it is measured and "
          "when support ends. We are glad to share the relevant model.",
          [btn("Talk to us about funding", "/contact/?subject=funding", "cta"),
           btn("Download the programme guide", "/assets/documents/SAF-Our-Programmes-Structure-Guide.pdf",
               "ghost-light", "download")])}
'''


# ===========================================================================
# PILLAR PAGES
# ===========================================================================

def pillar_page(p):
    idx = PILLAR_INDEX[p["slug"]]
    progs = [x for x in D.PROGRAMMES if x["pillar"] == p["slug"]]
    cards = "".join(programme_card(x) for x in progs)
    others = "".join(
        f'<li><a href="{pillar_url(o["slug"])}"><span><strong>{esc(o["name"])}</strong>'
        f'<small>{esc(o["motto"])}</small></span>{icon("arrow-right", "", 18)}</a></li>'
        for o in D.PILLARS if o["slug"] != p["slug"])

    meta = (f'<span class="hero__motto">{icon(p["icon"], "", 18)}{esc(p["motto"])}</span>'
            f'<span class="hero__motto">Pillar {idx} of 3</span>')

    return page_hero(
        title=esc(p["name"]),
        lede=esc(p["lede"]),
        eyebrow_text="What we do",
        meta=meta,
        variant="page-hero--pillar",
        image=D.PILLAR_PHOTOS[p["slug"]],
        trail=[("Home", "/"), ("What We Do", "/what-we-do/"), (p["name"], None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">About this pillar</h2>
    <div class="grid grid--sidebar">
      <div class="prose">
        {paras([esc(x) for x in p["intro"]])}
      </div>
      <aside>
        <div class="card card--quiet">
          <h3>The other pillars</h3>
          <ul class="linklist mt-4">{others}</ul>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head(f"Programmes in this pillar",
                  f"{len(progs)} programmes sit within this pillar.",
                  eyebrow_text="The work")}
    <div class="grid grid--3">{cards}</div>
    <div class="photo-band mt-7">
      {photo("classroom-friends", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-laughing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <p class="small text-muted mt-4">{photo_credit_line()}</p>
  </div>
</section>

{donate_band()}
'''


# ===========================================================================
# PROGRAMME PAGES
# ===========================================================================

def programme_page(p):
    pil_slug = p["pillar"]
    pil = PILLAR_BY_SLUG.get(pil_slug)
    pil_label = pillar_name(pil_slug)
    pil_href = pillar_url(pil_slug) if pil else "/what-we-do/"

    extra = "".join(
        f'<h2>{esc(h)}</h2>{paras(items)}' for h, items in p.get("extra", []))

    partners = [PARTNER_BY_SLUG[s] for s in p.get("partners", []) if s in PARTNER_BY_SLUG]
    if partners:
        plist = "".join(
            f'<li><a href="/about/partners/#{x["slug"]}"><span><strong>{esc(x["name"])}</strong>'
            f'<small>{esc(x["description"])}</small></span>{icon("arrow-right", "", 18)}</a></li>'
            for x in partners)
        partners_html = f'<h3>Delivery partners</h3><ul class="linklist mt-4">{plist}</ul>'
    else:
        partners_html = ('<h3>Delivery partners</h3><p class="small text-muted">No delivery partner is named '
                         'for this programme yet. Where technical delivery is required we say who our partner '
                         'is — and where we have not yet appointed one, we say that too.</p>')

    related = [n for n in D.NEWS if n.get("pillar") == pil_slug][:2]
    related_stories = [s for s in D.STORIES if s.get("pillar") == pil_slug][:2]
    rel_html = ""
    if related or related_stories:
        cards = "".join(news_card(n) for n in related) + "".join(story_card(s) for s in related_stories)
        rel_html = f'''
<section class="section section--surface">
  <div class="container">
    {section_head("Related stories and news", None, eyebrow_text="From the work")}
    <div class="grid grid--3">{cards}</div>
  </div>
</section>'''

    siblings = [x for x in D.PROGRAMMES if x["pillar"] == pil_slug and x["slug"] != p["slug"]]
    sib_html = ""
    if siblings:
        items = "".join(
            f'<li><a href="{programme_url(x["slug"])}"><span><strong>{esc(x["short_name"])}</strong>'
            f'<small>{esc(x["one_line"])}</small></span>{icon("arrow-right", "", 18)}</a></li>'
            for x in siblings)
        sib_html = (f'<div class="card card--quiet mt-5"><h3>Also in {esc(pil_label)}</h3>'
                    f'<ul class="linklist mt-4">{items}</ul></div>')

    mindcheck = ""
    if p.get("mindcheck"):
        mindcheck = note(
            '<p>MindCheck is a free and confidential way to check how you are doing and reach support early, '
            'without stigma. It is delivered with SpeakOut Mental Health Outreach.</p>'
            '<p><a href="/contact/?subject=general">Ask us how to access MindCheck</a></p>',
            "MindCheck", "good", "shield")

    pub = (f'<span class="hero__motto">Known publicly as {esc(p["public_name"])}</span>'
           if p.get("public_name") else "")
    flag = f'<span class="hero__motto">{esc(p["flagship"])}</span>' if p.get("flagship") else ""
    meta = f'{pub}{flag}'

    return page_hero(
        title=esc(p["name"]),
        lede=esc(p["one_line"]),
        eyebrow_text=pil_label,
        meta=meta,
        badge=pillar_badge(pil_slug, "hero"),
        image=D.PROGRAMME_PHOTOS[p["slug"]],
        trail=[("Home", "/"), ("What We Do", "/what-we-do/"),
               (pil_label, pil_href if pil else None), (p["short_name"], None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        <h2>What it does</h2>
        {paras([esc(x) for x in p["what_it_does"]])}

        <h2>Who it is for</h2>
        {paras([esc(x) for x in p["who_for"]])}

        <h2>What success looks like</h2>
        <blockquote class="pullquote" style="margin-top:0">{esc(p["success"])}</blockquote>

        <h2>Where it operates</h2>
        <p>{esc(p["where"])}</p>

        <h2>How it is delivered</h2>
        <p>{esc(p["delivery"])}</p>

        {extra}
        {mindcheck}
      </div>

      <aside>
        <div class="card">
          <h3>Support this programme</h3>
          <p class="small">{esc(p["support_line"])}</p>
          <div class="btn-row mt-4">
            {btn("Donate", "/donate/?designation=" + p["slug"], "cta")}
          </div>
          <p class="small text-muted mt-4">You can direct your gift to this programme, to a pillar, or to
            wherever it is most needed.</p>
        </div>
        {photo("children-community", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mt-5", max_width=640)}
        <div class="card mt-5">{partners_html}</div>
        {sib_html}
      </aside>
    </div>
  </div>
</section>

{rel_html}
{donate_band()}
'''


# ===========================================================================
# OUR IMPACT
# ===========================================================================

def impact():
    latest = "".join(story_card(s) for s in D.STORIES[:3])
    recent_projects = table(
        ["Year", "Project", "Partner", "Delivered"],
        [[f"<strong>{y}</strong>", esc(n), esc(pr), esc(d)]
         for y, n, pr, _t, d, _loc, _pil in reversed(D.PROJECTS[-5:])])

    prelaunch = checklist_graphic(D.PROGRAMME_PRELAUNCH)

    pillar_icon = {pl["name"]: pl["icon"] for pl in D.PILLARS}
    ind_rows = []
    for a_, b_, c_ in D.INDICATORS:
        ic = pillar_icon.get(a_.replace("&amp;", "&"))
        badge = f'<span class="group-icon">{icon(ic, "", 18)}</span>' if ic else ""
        ind_rows.append([f'<span class="group-name">{badge}<strong>{esc(a_)}</strong></span>',
                         esc(b_), esc(c_)])
    indicators = table(["Pillar", "Output: what we did", "Outcome: what changed"], ind_rows)

    ig = next(x for x in D.SITE["social"] if x["name"] == "Instagram")

    return page_hero(
        title="Our impact",
        lede="Since 2018 we have moved from family-and-friends donations to structured, partner-led delivery. "
             "Our early projects built the relationships and credibility on which our larger programmes are "
             "now being designed.",
        eyebrow_text="What we have delivered",
        image="children-yard",
        trail=[("Home", "/"), ("Our Impact", None)],
    ) + f'''
<div class="container">{section_nav(IMPACT_NAV, "/impact/")}</div>

<section class="section section--tight">
  <div class="container">
    {note(f'<p>{esc(D.TRACK_RECORD_NOTE)}</p>', "How to read this record", "info")}
    {stat_grid(D.GLANCE_STATS)}
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("The work in pictures", "Photographs from our outreaches, classrooms and communities. "
                  "Films and more of the people's own stories are added as they are cleared for publication.",
                  eyebrow_text="Photos and films")}
    <div class="mosaic">
      {photo("classroom-lesson", "4x3", sizes="(min-width: 700px) 33vw, 50vw", max_width=960)}
      {photo("children-outside", "4x3", sizes="(min-width: 700px) 33vw, 50vw", focus="upper", max_width=960)}
      {photo("women-gathering", "4x3", sizes="(min-width: 700px) 33vw, 50vw", max_width=960)}
      {photo("children-playing", "4x3", sizes="(min-width: 700px) 33vw, 50vw", max_width=960)}
      {photo("wheelchair-crossing", "4x3", sizes="(min-width: 700px) 33vw, 50vw", max_width=960)}
      {photo("classroom-group", "4x3", sizes="(min-width: 700px) 33vw, 50vw", max_width=960)}
    </div>
    <p class="small text-muted mt-4">{photo_credit_line()}</p>
    <div class="card card--quiet mt-6">
      <h3>Follow the work on Instagram</h3>
      <p class="small">More of our projects and the stories of the people we work with are shared on Instagram
        as {esc(ig["handle"])}.</p>
      <p class="card__foot"><a class="card__more" href="{ig["url"]}" target="_blank" rel="noopener">
        Open Instagram{icon("arrow-up-right", "", 18)}</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:1rem;max-width:none;flex-wrap:wrap">
      <div style="max-width:52ch">
        <p class="eyebrow">Stories</p>
        <h2>The work, in the words of the people in it</h2>
      </div>
      {btn("All stories", "/impact/stories/", "ghost")}
    </div>
    <div class="grid grid--3">{latest}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="section-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:1rem;max-width:none;flex-wrap:wrap">
      <div style="max-width:52ch">
        <p class="eyebrow">Projects</p>
        <h2>What we have delivered</h2>
      </div>
      {btn("All projects", "/impact/projects/", "ghost")}
    </div>
    {recent_projects}
  </div>
</section>

<section class="section" id="how-we-measure-impact">
  <div class="container">
    {section_head("How we measure impact",
                  "Monitoring, evaluation, accountability and learning is being built into the Foundation as a "
                  "system, not added as a report at the end of a grant.", eyebrow_text="Measurement")}
    <div class="grid grid--split">
      <div class="prose">
        <h3>Outputs and outcomes are not the same thing</h3>
        <p>An <strong>output</strong> is what we did: a fee paid, a grant disbursed, a roof repaired.
           An <strong>outcome</strong> is what changed: a child still in school at the end of the year, a
           business still trading twelve months later, a family still housed and secure.</p>
        {paras([esc(x) for x in D.MEASUREMENT_NOTE])}
      </div>
      <div>
        {photo("classroom-boy-yellow", "4x3", sizes="(min-width: 880px) 540px, 100vw", cls="mb-5")}
        <blockquote class="pullquote">We would rather publish a smaller number we can defend than a larger one
          we cannot.<cite>Corporate Profile 2026, Section 16</cite></blockquote>
        {note(f'<p>{esc(D.MEL_POSITION)}</p>', "Our current position, stated openly", "warn", "alert")}
      </div>
    </div>

    <h3 class="mt-7">What each programme must have before it launches</h3>
    <p class="measure">A programme without these five is not launched. Each is a gate, in order.</p>
    {prelaunch}

    <h3 class="mt-7">Illustrative indicators by pillar</h3>
    <div class="mt-4">{indicators}</div>
    <p class="small text-muted mt-5">All indicators are disaggregated by sex, displacement status, disability
      and age group. Attendance and completion are verified by physical visit at least once per term.
      Administrative records alone are not sufficient evidence for a donor report, or for us.</p>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Accountability to the people we serve", None, eyebrow_text="Not only upward")}
        <p>Measurement that reports only upward to funders is incomplete. We are establishing a beneficiary
           feedback and complaints mechanism so that the people in our programmes can tell us when something is
           wrong, in plain language, without fear and without going through the person whose conduct they may
           be questioning.</p>
        <p>Findings are reported to the Board, and we intend to publish what we learn, including where a
           programme did not work.</p>
        <div class="btn-row mt-5">{btn("How to raise a concern", "/complaints/", "light")}</div>
      </div>
      <div>
        <div class="note note--dark">
          <p class="note__title">{icon("target", "note__icon", 20)}Unit economics</p>
          <div class="note__body">
            <p>Each flagship programme carries a documented cost per participant, built up from its standard
               package and its share of programme support costs.</p>
            <p>We publish the cost per <em>outcome</em> as well as per participant, because that is the
               figure that prices what actually changed. Unit costs are re-priced at least twice a year and
               every figure is dated.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{donate_band()}
'''


def stories_index():
    cards = "".join(story_card(s) for s in D.STORIES)

    pillar_filters = "".join(
        f'<button class="filter" type="button" data-filter="{p["slug"]}" data-dimension="pillar" '
        f'aria-pressed="false">{esc(p["name"])}</button>' for p in D.PILLARS)
    format_filters = "".join(
        f'<button class="filter" type="button" data-filter="{f.lower().replace(" ", "-")}" '
        f'data-dimension="format" aria-pressed="false">{esc(f)}</button>' for f in D.STORY_FORMATS)

    return page_hero(
        title="Stories",
        lede="Films, photo essays and written pieces from the communities we work in. Filter by pillar or by "
             "format.",
        eyebrow_text="Our impact",
        trail=[("Home", "/"), ("Our Impact", "/impact/"), ("Stories", None)],
    ) + f'''
<div class="container">{section_nav(IMPACT_NAV, "/impact/stories/")}</div>

<section class="section section--tight">
  <div class="container">
    {photo("classroom-lesson", "21x9", sizes="100vw", cls="mb-6", eager=True,
           caption=photo_credit_line())}
    {note(f'<p>{esc(D.STORIES_NOTE)}</p>', "Documentary work from September 2026", "info", "film")}

    <div data-filter-group="stories">
      <div class="filters">
        <span class="filters__label">Pillar</span>
        <button class="filter" type="button" data-filter="all" data-dimension="pillar" aria-pressed="true">All</button>
        {pillar_filters}
      </div>
      <div class="filters">
        <span class="filters__label">Format</span>
        <button class="filter" type="button" data-filter="all" data-dimension="format" aria-pressed="true">All</button>
        {format_filters}
      </div>
      <p class="results-count" data-filter-count="stories" role="status"></p>
    </div>

    <h2 class="visually-hidden">All stories</h2>
    <div class="grid grid--3" data-filter-target="stories">{cards}</div>
    <div class="empty-state mt-5" data-filter-empty="stories" hidden>
      <p>No stories match that combination yet. The first documentary films arrive from September 2026.</p>
    </div>
  </div>
</section>

{newsletter_band()}
'''


def story_page(s):
    body = "".join(f"<p>{x}</p>" for x in s["body"])
    pil = s.get("pillar")
    pil_label = pillar_name(pil) if pil else ""
    return page_hero(
        title=esc(s["title"]),
        eyebrow_text=f'{s["format"]} · {pil_label}' if pil else s["format"],
        trail=[("Home", "/"), ("Our Impact", "/impact/"), ("Stories", "/impact/stories/"),
               (s["title"], None)],
    ) + f'''
<article class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        <p class="article-meta"><time datetime="{s["date_iso"]}">{esc(s["date_display"])}</time>
          <span class="tag tag--muted">{esc(s["format"])}</span>
          {f'<a class="tag" href="{pillar_url(pil)}">{esc(pil_label)}</a>' if pil else ''}</p>
        {photo(D.STORY_PHOTOS.get(s["slug"], "classroom-desks"), "16x9",
               sizes="(min-width: 940px) 720px, 100vw", eager=True,
               caption=photo_credit_line())}
        <div class="article-body mt-6">{body}</div>
        <div class="gallery mt-6">
          {photo("classroom-friends", "1x1", sizes="(min-width: 760px) 220px, 33vw", max_width=640)}
          {photo("children-laughing", "1x1", sizes="(min-width: 760px) 220px, 33vw", max_width=640)}
          {photo("classroom-doorway", "1x1", sizes="(min-width: 760px) 220px, 33vw", max_width=640)}
        </div>
        <div class="share">
          <span class="share__label">Share</span>
          <a href="https://www.facebook.com/sharer/sharer.php?u={D.SITE["base_url"]}/impact/stories/{s["slug"]}/"
             target="_blank" rel="noopener" aria-label="Share on Facebook">{icon("facebook", "", 18)}</a>
          <a href="https://www.linkedin.com/sharing/share-offsite/?url={D.SITE["base_url"]}/impact/stories/{s["slug"]}/"
             target="_blank" rel="noopener" aria-label="Share on LinkedIn">{icon("linkedin", "", 18)}</a>
          <button type="button" data-share aria-label="Share this story">{icon("arrow-up-right", "", 18)}</button>
        </div>
      </div>
      <aside>
        <h2 class="visually-hidden">Support this work, and more stories</h2>
        {photo("women-smiling", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <h3>Support this work</h3>
          <p class="small">You can direct your gift to a pillar or a programme, or give where it is most needed.</p>
          <div class="btn-row mt-4">{btn("Donate", "/donate/", "cta")}</div>
        </div>
        <div class="card card--quiet mt-5">
          <h3>More stories</h3>
          <ul class="linklist mt-4">
            {"".join(f'<li><a href="/impact/stories/{o["slug"]}/"><span>{esc(o["title"])}</span>'
                     f'{icon("arrow-right", "", 18)}</a></li>' for o in D.STORIES if o["slug"] != s["slug"])}
          </ul>
        </div>
      </aside>
    </div>
  </div>
</article>
'''


def projects():
    rows = []
    for y, name, partner, ptype, delivered, loc, pil in reversed(D.PROJECTS):
        rows.append([
            f"<strong>{y}</strong>",
            f"<strong>{esc(name)}</strong>",
            esc(partner),
            esc(loc),
            esc(delivered),
        ])
    tbl = table(["Year", "Project", "Partner", "Location", "Delivered"], rows)

    cards = "".join(
        f'<article class="card" data-facets="{pil} y{y}">'
        f'<div class="card__top" style="display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap">'
        f'<span class="tag">{y}</span><span class="tag tag--muted">{esc(ptype)}</span></div>'
        f'<h3>{esc(name)}</h3>'
        f'<p class="card__meta">{esc(loc)}{" · " + esc(partner) if partner != "—" else ""}</p>'
        f'<p>{esc(delivered)}</p></article>'
        for y, name, partner, ptype, delivered, loc, pil in reversed(D.PROJECTS))

    years = sorted({p[0] for p in D.PROJECTS}, reverse=True)
    year_filters = "".join(
        f'<button class="filter" type="button" data-filter="y{y}" data-dimension="year" '
        f'aria-pressed="false">{y}</button>' for y in years)
    pillar_filters = "".join(
        f'<button class="filter" type="button" data-filter="{p["slug"]}" data-dimension="pillar" '
        f'aria-pressed="false">{esc(p["name"])}</button>' for p in D.PILLARS)

    return page_hero(
        title="Projects",
        lede="What we have delivered since 2019, with the partner who delivered it alongside us. Filterable by "
             "year and by pillar.",
        eyebrow_text="Our impact",
        trail=[("Home", "/"), ("Our Impact", "/impact/"), ("Projects", None)],
    ) + f'''
<div class="container">{section_nav(IMPACT_NAV, "/impact/projects/")}</div>

<section class="section section--tight">
  <div class="container">
    {note(f'<p>{esc(D.TRACK_RECORD_NOTE)}</p>', "How to read this record", "info")}

    <div data-filter-group="projects">
      <div class="filters">
        <span class="filters__label">Year</span>
        <button class="filter" type="button" data-filter="all" data-dimension="year" aria-pressed="true">All</button>
        {year_filters}
      </div>
      <div class="filters">
        <span class="filters__label">Pillar</span>
        <button class="filter" type="button" data-filter="all" data-dimension="pillar" aria-pressed="true">All</button>
        {pillar_filters}
      </div>
      <p class="results-count" data-filter-count="projects" role="status"></p>
    </div>

    <h2 class="visually-hidden">All projects</h2>
    <div class="photo-band mb-6">
      {photo("classroom-group", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-gathering", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-playing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-seated", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <div class="grid grid--3" data-filter-target="projects">{cards}</div>
    <div class="empty-state mt-5" data-filter-empty="projects" hidden>
      <p>No projects match that combination.</p>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {photo("boys-lorry", "21x9", sizes="100vw", cls="mb-6", caption=photo_credit_line())}
    {section_head("The full record", None, eyebrow_text="2019 to date")}
    {tbl}
    <p class="small text-muted mt-5">Figures and descriptions are drawn from project records and reported
      conservatively. From the 2026–27 academic year our reporting shifts to what the pillar programmes deliver.</p>
  </div>
</section>

{donate_band()}
'''


# ===========================================================================
# NEWS
# ===========================================================================

def news_index():
    cards = "".join(news_card(n) for n in D.NEWS)
    cats = sorted({n["category"] for n in D.NEWS})
    cat_filters = "".join(
        f'<button class="filter" type="button" data-filter="{esc(c)}" data-dimension="category" '
        f'aria-pressed="false">{esc(c)}</button>' for c in cats)

    return page_hero(
        title="News",
        lede="Updates from the Foundation — programmes launching, outreaches delivered, and reports published.",
        eyebrow_text="Latest",
        trail=[("Home", "/"), ("News", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    {photo("children-community", "21x9", sizes="100vw", cls="mb-6", eager=True,
           caption=photo_credit_line())}
    <div data-filter-group="news">
      <div class="filters">
        <span class="filters__label">Category</span>
        <button class="filter" type="button" data-filter="all" data-dimension="category" aria-pressed="true">All</button>
        {cat_filters}
      </div>
      <p class="results-count" data-filter-count="news" role="status"></p>
    </div>
    <h2 class="visually-hidden">All news</h2>
    <div class="grid grid--3" data-filter-target="news">{cards}</div>
    <div class="empty-state mt-5" data-filter-empty="news" hidden><p>No posts in that category yet.</p></div>
  </div>
</section>

{newsletter_band()}
'''


def news_page(n, prev_item, next_item):
    body = "".join(f"<p>{x}</p>" for x in n["body"])
    pil = n.get("pillar")
    pil_link = ""
    if pil and pil != "across-all-pillars":
        pil_link = f'<a class="tag" href="{pillar_url(pil)}">{esc(pillar_name(pil))}</a>'
    elif pil:
        pil_link = f'<span class="tag tag--muted">{esc(pillar_name(pil))}</span>'

    nav_items = []
    if prev_item:
        nav_items.append(f'<li><a href="/news/{prev_item["slug"]}/"><span><small>Previous</small>'
                         f'{esc(prev_item["title"])}</span>{icon("arrow-right", "", 18)}</a></li>')
    if next_item:
        nav_items.append(f'<li><a href="/news/{next_item["slug"]}/"><span><small>Next</small>'
                         f'{esc(next_item["title"])}</span>{icon("arrow-right", "", 18)}</a></li>')
    nav_html = (f'<div class="card card--quiet mt-5"><h3>More news</h3>'
                f'<ul class="linklist mt-4">{"".join(nav_items)}</ul></div>') if nav_items else ""

    url = f'{D.SITE["base_url"]}/news/{n["slug"]}/'

    return page_hero(
        title=esc(n["title"]),
        eyebrow_text=n["category"],
        trail=[("Home", "/"), ("News", "/news/"), (n["title"], None)],
    ) + f'''
<article class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        <p class="article-meta"><time datetime="{n["date_iso"]}">{esc(n["date_display"])}</time>
          <span class="tag tag--muted">{esc(n["category"])}</span>{pil_link}</p>
        {photo(D.NEWS_PHOTOS.get(n["slug"], "classroom-group"), "16x9",
               sizes="(min-width: 940px) 720px, 100vw", eager=True,
               caption=photo_credit_line())}
        <div class="article-body mt-6">{body}</div>
        <div class="share">
          <span class="share__label">Share</span>
          <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener"
             aria-label="Share on Facebook">{icon("facebook", "", 18)}</a>
          <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener"
             aria-label="Share on LinkedIn">{icon("linkedin", "", 18)}</a>
          <button type="button" data-share aria-label="Share this post">{icon("arrow-up-right", "", 18)}</button>
        </div>
      </div>
      <aside>
        <h2 class="visually-hidden">Support the work, and more news</h2>
        {photo("children-outside", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <h3>Support the work</h3>
          <p class="small">One-off or monthly gifts, from ₦5,000 upward.</p>
          <div class="btn-row mt-4">{btn("Donate", "/donate/", "cta")}</div>
        </div>
        {nav_html}
      </aside>
    </div>
  </div>
</article>

{newsletter_band()}
'''
