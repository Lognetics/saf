# -*- coding: utf-8 -*-
"""Home, About Us, Our Story, Leadership & Governance, Partners, Who We Serve."""

from . import data as D
from .layout import (icon, esc, chip, btn, section_head, note, table, stat_grid,
                     bullets, paras, newsletter_form, image_placeholder, breadcrumbs,
                     section_nav, cta_band)
from .components import (page_hero, status_board, pillar_card, programme_card,
                         person_card, partner_card, news_card, get_involved_grid,
                         donate_band, newsletter_band, contact_strip, programme_url,
                         pillar_url, PILLAR_INDEX, photo, photo_credit_line)

ABOUT_NAV = [
    ("Who We Are", "/about/"),
    ("Our Story", "/about/our-story/"),
    ("Leadership & Governance", "/about/leadership/"),
    ("Partners", "/about/partners/"),
    ("Who We Serve", "/who-we-serve/"),
]


# ===========================================================================
# HOME
# ===========================================================================

def home():
    pillars = "".join(pillar_card(p, PILLAR_INDEX[p["slug"]]) for p in D.PILLARS)
    news = "".join(news_card(n) for n in D.NEWS[:3])

    mottos = "".join(
        f'<span class="hero__motto">{icon(p["icon"], "", 18)}{esc(p["motto"])}</span>'
        for p in D.PILLARS)

    partner_items = "".join(
        f'<li><a href="/about/partners/#{p["slug"]}">{esc(p["name"])}</a></li>'
        for p in D.PARTNERS)

    story = D.STORIES[0]

    return f'''
<section class="hero hero--home">
  <div class="container hero__inner">
    <div class="hero__grid">
      <div>
        <span class="hero__eyebrow"><span class="dot"></span>Nigerian foundation · established 2018 · CAC registered</span>
        <h1>Dignity, opportunity and <em>a way forward</em> for displaced Nigerian families</h1>
        <p class="hero__lede">We work with internally displaced persons and indigent communities across Nigeria —
          getting children back into school, helping adults rebuild an income, and making homes safe and secure.</p>
        <div class="hero__actions btn-row">
          {btn("Donate", "/donate/", "cta")}
          {btn("See what we do", "/what-we-do/", "ghost-light", None)}
        </div>
        <div class="hero__mottos">{mottos}</div>
      </div>

      <div>
        {photo("classroom-boy-desk", "4x5", sizes="(min-width: 980px) 460px, 100vw",
               eager=True, focus="upper")}
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--surface" aria-label="Registration and legal status">
  <div class="container">
    <div class="grid grid--4" style="gap:var(--sp-4)">
      <div><p class="eyebrow" style="margin-bottom:.25em">Legal status</p>
        <p class="mb-0"><strong>Incorporated Trustees</strong>, registered with the Corporate Affairs Commission</p></div>
      <div><p class="eyebrow" style="margin-bottom:.25em">Registration</p>
        <p class="mb-0"><strong>{D.SITE["reg_number"]}</strong></p></div>
      <div><p class="eyebrow" style="margin-bottom:.25em">Head office</p>
        <p class="mb-0"><strong>Maitama, FCT</strong>, Abuja, Nigeria</p></div>
      <div><p class="eyebrow" style="margin-bottom:.25em">Who we work with</p>
        <p class="mb-0"><strong>Internally displaced persons</strong> and indigent communities</p></div>
    </div>
    <div class="btn-row mt-5">{btn("Governance, policies and reports", "/accountability/", "ghost")}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {stat_grid(D.GLANCE_STATS)}
    <p class="small text-muted mt-4">All figures are reported conservatively. See
      <a href="/accountability/how-we-measure-impact/">how we measure impact</a> for what we count,
      and what we do not yet claim.</p>
  </div>
</section>

<section class="section section--surface">
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

<section class="section">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Three programmes are running today. We will not tell you otherwise.",
                      "It would be easy to present twelve programmes and let you assume all twelve are "
                      "operating. Every programme on this site carries a status label, and we keep it current.",
                      eyebrow_text="Honest by policy")}
        <p>An organisation that presents its plans as its achievements should not be trusted with its
           achievements either. Programmes move to <strong>Running now</strong> only when they have a written
           model, a named owner, a unit cost and an indicator set.</p>
        <div class="btn-row">{btn("See the whole portfolio", "/what-we-do/", "ghost")}</div>
      </div>
      <div>{status_board()}</div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("The need we address", None, eyebrow_text="Displacement in Nigeria")}
        <p>Nigeria hosts one of the largest internally displaced populations in the world — and most displaced
           Nigerians do not live in camps. The response is weakest where displacement is least visible: in host
           communities, in cities, and among families who have been moved once already.</p>
        <p>Which is where we have chosen to concentrate.</p>
        <div class="btn-row mt-5">
          {btn("Who we serve", "/who-we-serve/", "light")}
        </div>
      </div>
      <div>
        {photo("children-community", "16x9", sizes="(min-width: 880px) 540px, 100vw",
               cls="mb-5")}
        {stat_grid(D.NEED_STATS[:4], "stat-grid--dark")}
        <p class="small mt-4" style="color:#9FBBD6">Source: IOM Displacement Tracking Matrix Nigeria,
          Round 51 (north-east) and Site Assessment Round 18 (north-central &amp; north-west), 2025.</p>
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
           and an income — and a piece of furniture made by a neighbour is a piece of furniture that gets
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

<section class="section section--surface">
  <div class="container">
    {section_head("We deliver alongside others",
                  "Almost every project in our record was delivered with someone else. We treat collaboration "
                  "as the engine of impact rather than a supporting tactic.",
                  eyebrow_text="Our partners")}
    <ul class="filters" style="list-style:none;padding:0;gap:.75rem 1.5rem;font-weight:650;color:var(--navy)">
      {partner_items}
    </ul>
    {note('<p>Partner logos are published only once we hold written permission from the partner. '
          'Until that is confirmed we name our partners in text — which is the correct order to do it in.</p>',
          "A note on logos", "info")}
    <div class="btn-row">{btn("See all partners", "/about/partners/", "ghost")}
      {btn("Partner with us", "/get-involved/partner/", "primary")}</div>
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

<section class="section">
  <div class="container">
    {section_head("Four ways to stand with the Foundation",
                  "Every contribution — of money, time or expertise — powers real education, empowerment and "
                  "relief for vulnerable communities.",
                  eyebrow_text="Get involved")}
    {get_involved_grid()}
  </div>
</section>

{newsletter_band()}
{donate_band()}
'''


# ===========================================================================
# WHO WE ARE  (/about/)
# ===========================================================================

def who_we_are():
    values = "".join(
        f'<div class="card"><p class="eyebrow" style="margin-bottom:.4em">{i+1:02d}</p>'
        f'<h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
        for i, (t, b) in enumerate(D.VALUES))

    distinctions = "".join(
        f'<div><dt>{esc(t)}</dt><dd>{esc(b)}</dd></div>' for t, b in D.DISTINCTIONS)

    facts = table(["Item", "Detail"], [[f"<strong>{esc(k)}</strong>", esc(v)] for k, v in D.AT_A_GLANCE],
                  cls="table--facts")

    return page_hero(
        title="Who we are",
        lede="A Nigerian humanitarian and development organisation working to restore hope and dignity to "
             "people pushed to the margins of society.",
        eyebrow_text="About us",
        trail=[("Home", "/"), ("About Us", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/")}</div>

<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        <p class="lede">Synia Aid Foundation works to restore hope and dignity to people pushed to the margins
          of society — above all internally displaced persons, and the wider community of indigent and
          vulnerable Nigerians whose lives have been disrupted by conflict, insecurity, disaster and poverty.</p>
        <p>The Foundation was established in December 2018 and registered with the Corporate Affairs Commission
          of the Federal Republic of Nigeria. From a first community drive in January 2019, we have grown into a
          multi-programme organisation delivering education, livelihoods, shelter and community-wellbeing work
          across several Nigerian states — always on the conviction that the people we serve are partners and
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
            <li><a href="#distinctions">What distinguishes us{icon("arrow-right", "", 18)}</a></li>
            <li><a href="#glance">At a glance{icon("arrow-right", "", 18)}</a></li>
          </ul>
        </div>
        <div class="mt-5">{photo("classroom-boy-yellow", "4x5", sizes="(min-width: 940px) 336px, 100vw", focus="upper")}</div>
        <div class="card mt-5">
          <span class="doc__icon">{icon("doc", "", 22)}</span>
          <h3>Corporate Profile 2026</h3>
          <p class="small">Edition 2, July 2026. The full picture — governance, programmes, track record,
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
    {section_head("Our core values",
                  "Values that cannot be tested are decoration. Kindness is why our conduct standards govern "
                  "tone and patience, not only outcomes. Solidarity is why community consultation opens every "
                  "intervention. Need-led service is why selection is scored against a written sheet. "
                  "Independence is why we maintain a conflicts of interest register.",
                  eyebrow_text="What governs how we work")}
    <div class="grid grid--4">{values}</div>
  </div>
</section>

<section class="section section--surface" id="distinctions">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("What distinguishes us", None, eyebrow_text="Our position")}
        {note(f'<p>{esc(D.WHAT_WE_ARE_NOT)}</p>', "What we are not", "warn", "alert")}
      </div>
      <div><dl class="definition-list">{distinctions}</dl></div>
    </div>
  </div>
</section>

<section class="section" id="glance">
  <div class="container">
    {section_head("The Foundation at a glance", None, eyebrow_text="Legal identity and footprint")}
    {facts}
  </div>
</section>

{cta_band("Read the full Corporate Profile",
          "Twenty-nine pages: our theory of change, programme portfolio, track record, monitoring framework, "
          "governance, financial stewardship, risk register and roadmap to 2029.",
          [btn("Download the profile", "/assets/documents/SAF-Corporate-Profile-2026.pdf", "cta", "download"),
           btn("See all publications", "/accountability/reports-and-publications/", "ghost-light", None)])}
'''


# ===========================================================================
# OUR STORY
# ===========================================================================

def our_story():
    items = "".join(
        f'<li class="timeline__item"><span class="timeline__year">{esc(y)}</span>'
        f'<h3 class="timeline__title">{esc(t)}</h3><p class="timeline__body">{b}</p></li>'
        for y, t, b in D.TIMELINE)

    return page_hero(
        title="Our story",
        lede="From a single charity drive to a multi-programme foundation. Early outreach built the trust and "
             "access on which our three pillars now stand.",
        eyebrow_text="About us",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Our Story", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/our-story/")}</div>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Milestones from 2018</h2>
    <div class="grid grid--sidebar">
      <div>
        <ol class="timeline">{items}</ol>
      </div>
      <aside>
        <div class="card">
          <p class="eyebrow">From the founder</p>
          <blockquote class="pullquote" style="margin-top:0">Synia Aid Foundation began with a question I could
            not put down: what happens to people who are forced from their homes but never cross a border?
            <cite>Mmaobi Nwafor-Orizu, Founder &amp; Chair</cite></blockquote>
          <p class="card__foot"><a class="card__more" href="/about/leadership/#mmaobi-nwafor-orizu-bio">
            Read the founder's biography{icon("arrow-right", "", 18)}</a></p>
        </div>
        <div class="card card--quiet mt-5">
          <h3>2026 — into programmes</h3>
          <p class="small">2026 is the year the Foundation moved from campaigns to structured programmes —
            reviewing its portfolio, writing programme models, and opening its first school partnership.</p>
          <p class="card__foot"><a class="card__more" href="/what-we-do/">
            See the programme portfolio{icon("arrow-right", "", 18)}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("How we work", None, eyebrow_text="Operating principles")}
    <div class="grid grid--3">
      {"".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(b)}</p></div>' for t, b in D.OPERATING_PRINCIPLES)}
    </div>
  </div>
</section>

{donate_band()}
'''


# ===========================================================================
# LEADERSHIP & GOVERNANCE
# ===========================================================================

def leadership():
    def bio_block(p):
        return f'''
<article class="card" id="{p["slug"]}-bio">
  <h3>{esc(p["name"])}</h3>
  <p class="person__role">{esc(p["role"])}</p>
  <p class="person__creds">{esc(p["credentials"])}</p>
  {"".join(f"<p>{x}</p>" for x in p["bio"])}
  {note(f'<p>{esc(p["remit"])}</p>', "Remit at the Foundation", "info", "target")}
</article>'''

    trustees = [p for p in D.BOARD if p["group"] == "board"]
    advisers = [p for p in D.BOARD if p["group"] == "adviser"]

    cards_board = "".join(person_card(p) for p in trustees)
    cards_adv = "".join(person_card(p) for p in advisers)
    cards_exec = "".join(person_card(p) for p in D.EXECUTIVE)

    bios = "".join(bio_block(p) for p in (D.BOARD + D.EXECUTIVE))

    bodies = table(["Body", "Responsibility"],
                   [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.GOVERNANCE_BODIES])

    commitments = table(["Commitment", "Status"],
                        [[esc(a), f'<span class="tag tag--muted">{esc(b)}</span>']
                         for a, b in D.GOVERNANCE_COMMITMENTS])

    return page_hero(
        title="Leadership &amp; governance",
        lede="The Foundation is led by a founder-chaired Board of Trustees, which draws on specialist advisers "
             "in law, human resources and media strategy sitting at Board level, and is delivered by an "
             "executive team responsible for day-to-day operations and communications.",
        eyebrow_text="About us",
        trail=[("Home", "/"), ("About Us", "/about/"), ("Leadership & Governance", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/leadership/")}</div>

<section class="section section--tight">
  <div class="container">
    {note('<p>Advisers at Board level inform decisions without holding executive responsibility for delivery. '
          'Keeping the two separate is part of the governance architecture donors and regulators expect of a '
          'credible foundation, and it is why our advisers are listed here as part of the Board rather than as '
          'staff.</p>', "Why the distinction matters", "info")}
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {section_head("Board of Trustees",
                  "The Board holds strategic direction, approves programmes and policy, and carries financial "
                  "and safeguarding oversight.", eyebrow_text="Governance")}
    <div class="grid grid--3">{cards_board}</div>

    <h3 class="mt-7">Advisers to the Board</h3>
    <p class="measure">Specialist counsel at Board level in law, human resources and media strategy — informing
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
    <h3 class="mt-7">Strengthening our governance</h3>
    <p class="measure">{esc(D.GOVERNANCE_CANDOUR)}</p>
    <div class="mt-5">{commitments}</div>
    <div class="btn-row mt-6">
      {btn("Governance &amp; policies", "/accountability/governance-and-policies/", "primary")}
      {btn("Download leadership biographies", "/assets/documents/SAF-Leadership-Biographies.pdf", "ghost", "download")}
    </div>
  </div>
</section>

<section class="section section--surface" id="biographies">
  <div class="container">
    {section_head("Full biographies", None, eyebrow_text="The people behind the mission")}
    <div class="grid" style="gap:var(--sp-5)">{bios}</div>
    <p class="small text-muted mt-6">Photographs of the Board and executive team will be published once
      supplied and consent-confirmed. Biographies are drawn from the Foundation's published leadership profiles
      and are reviewed as roles change.</p>
  </div>
</section>

{contact_strip()}
'''


# ===========================================================================
# PARTNERS
# ===========================================================================

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
      <h2>{esc(heading)}</h2>
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
        trail=[("Home", "/"), ("About Us", "/about/"), ("Partners", None)],
    ) + f'''
<div class="container">{section_nav(ABOUT_NAV, "/about/partners/")}</div>
{"".join(blocks)}

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Partnerships we are pursuing",
                      "These are not current relationships. We name them because ambition stated plainly reads "
                      "as confidence — and because a prospective partner presented as a current one is the "
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
        <div class="card">
          <h3>What we offer a partner</h3>
          {bullets(D.WHAT_WE_OFFER_PARTNERS)}
        </div>
      </div>
    </div>
  </div>
</section>
'''


# ===========================================================================
# WHO WE SERVE
# ===========================================================================

def who_we_serve():
    groups = table(
        ["Group", "Definition", "Primary programmes"],
        [[f"<strong>{esc(a)}</strong>", esc(b), f'<span class="tag tag--muted">{esc(c)}</span>']
         for a, b, c in D.BENEFICIARY_GROUPS])

    steps = "".join(
        f'<li><div><h3>{esc(t)}</h3><p>{esc(b)}</p></div></li>' for t, b in D.SELECTION_STEPS)

    implications = table(
        ["The finding", "The implication for how we work"],
        [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.NEED_IMPLICATIONS])

    locations = table(
        ["Location", "Role", "Work delivered or planned"],
        [[f"<strong>{esc(a)}</strong>" + (f'<br><span class="small text-muted">{esc(b)}</span>' if b else ""),
          esc(c), esc(d)] for a, b, c, d in D.LOCATIONS])

    return page_hero(
        title="Who we serve",
        lede="The Foundation exists first and foremost for internally displaced persons — Nigerians forced from "
             "their homes who, unlike refugees, remain inside their own country and often fall through the gaps "
             "in formal protection.",
        eyebrow_text="The people our work is for",
        trail=[("Home", "/"), ("What We Do", "/what-we-do/"), ("Who We Serve", None)],
    ) + f'''
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

<section class="section section--navy">
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
    {section_head("How we select", "We act according to need — not status, ethnicity, gender, religion, "
                  "politics or any other interest. Selection follows a consistent process across every "
                  "programme.", eyebrow_text="Selection")}
    <ol class="steps">{steps}</ol>
    {note(f'<p>{esc(D.CONDUCT_COMMITMENT)}</p>', "A commitment on conduct", "good", "shield")}
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Where we work", None, eyebrow_text="Our footprint")}
    {locations}
    <div class="grid grid--split mt-7">
      <div>{paras([esc(p) for p in D.FOOTPRINT_NOTE])}</div>
      <div>
        <blockquote class="pullquote">Most displaced Nigerians do not live in camps. The response is weakest
          where displacement is least visible — in host communities, in cities, and among families who have
          been moved once already.<cite>Corporate Profile 2026, Section 13</cite></blockquote>
      </div>
    </div>
  </div>
</section>

{donate_band()}
'''
