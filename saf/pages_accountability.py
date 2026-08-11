# -*- coding: utf-8 -*-
"""Accountability: hub, Governance & Policies, Reports & Publications, How We Measure Impact."""

from . import data as D
from .layout import (icon, esc, btn, section_head, note, table, bullets, paras,
                     section_nav, cta_band, stat_grid)
from .components import page_hero, doc_card, donate_band, contact_strip, status_board

ACC_NAV = [
    ("Overview", "/accountability/"),
    ("Governance & Policies", "/accountability/governance-and-policies/"),
    ("Reports & Publications", "/accountability/reports-and-publications/"),
    ("How We Measure Impact", "/accountability/how-we-measure-impact/"),
]


def accountability():
    return page_hero(
        title="Accountability",
        lede="Everything an institutional funder, a regulator or a careful donor needs in order to assess us — "
             "governance, policies, published documents, and how we measure what we do.",
        eyebrow_text="For institutional funders and due diligence",
        trail=[("Home", "/"), ("Accountability", None)],
    ) + f'''
<div class="container">{section_nav(ACC_NAV, "/accountability/")}</div>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Explore this section</h2>
    <div class="grid grid--3">
      <article class="card card--link">
        <span class="doc__icon">{icon("scale", "", 22)}</span>
        <h3><a class="stretched" href="/accountability/governance-and-policies/">Governance &amp; policies</a></h3>
        <p>How the Foundation is governed, who is accountable for what, and our policy suite — safeguarding,
           conduct, PSEAH, anti-fraud and conflict of interest — available to download.</p>
        <p class="card__foot"><span class="card__more">Read{icon("arrow-right", "", 18)}</span></p>
      </article>
      <article class="card card--link">
        <span class="doc__icon">{icon("doc", "", 22)}</span>
        <h3><a class="stretched" href="/accountability/reports-and-publications/">Reports &amp; publications</a></h3>
        <p>Our Corporate Profile, programme structure guide and leadership biographies. Annual report and
           audited accounts are scheduled, and we say plainly that they are not yet published.</p>
        <p class="card__foot"><span class="card__more">Browse the library{icon("arrow-right", "", 18)}</span></p>
      </article>
      <article class="card card--link">
        <span class="doc__icon">{icon("chart", "", 22)}</span>
        <h3><a class="stretched" href="/accountability/how-we-measure-impact/">How we measure impact</a></h3>
        <p>What each programme must have before it launches, the indicators we use, what we count — and what we
           do not yet claim.</p>
        <p class="card__foot"><span class="card__more">Read{icon("arrow-right", "", 18)}</span></p>
      </article>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Our current position, stated openly", None, eyebrow_text="Before you ask")}
        <p>{esc(D.MEL_POSITION)}</p>
        <p>We would rather a prospective funder read that here than discover it in due diligence.</p>
      </div>
      <div>
        <div class="note note--dark">
          <p class="note__title">{icon("alert", "note__icon", 20)}What we have not yet done</p>
          <div class="note__body">
            {bullets([
              "We have not yet published audited accounts. Target: two consecutive years by 2028.",
              "We have not yet commissioned an external evaluation. It is in Phase 3 of our roadmap.",
              "Our monitoring framework is being introduced rather than long established.",
              "Nine of our twelve programmes are not yet running, and are labelled as such throughout this site.",
            ])}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("The portfolio as it actually stands", None, eyebrow_text="No programme is presented as more than it is")}
    {status_board()}
    <p class="small text-muted mt-5">Programmes move to <strong>Running now</strong> only when they have a
      written model, a named owner, a unit cost and an indicator set.
      <a href="/what-we-do/">See the full portfolio</a>.</p>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Financial stewardship",
                  "Every naira entrusted to the Foundation belongs to the people we serve. Our financial "
                  "approach is built on three commitments: control before scale, restriction honoured, and "
                  "transparency by default.", eyebrow_text="Stewardship")}
    <div class="grid grid--split">
      <div>
        {table(["Control", "How it works"],
               [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.FINANCIAL_CONTROLS])}
      </div>
      <div>
        <div class="card">
          <h3>What we will publish</h3>
          <dl class="bank-details mt-4">
            {"".join(f"<div><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>" for a, b in D.DISCLOSURE_COMMITMENTS)}
          </dl>
        </div>
        {note(f'<p>{esc(D.FINANCIAL_CANDOUR)}</p>', "Stated plainly", "warn", "alert")}
      </div>
    </div>

    <h3 class="mt-7">Restricted funds</h3>
    <p class="measure">Where a donor gives for a specific purpose, that restriction is honoured absolutely. The
      Synia Scholars Fund will operate as a ring-fenced fund with its own agreement, published selection
      criteria, separate accounting and an annual statement to its donors. We will not promote it externally
      until that architecture exists — because the word <em>Fund</em> creates an obligation, and an obligation
      we cannot yet meet is a liability rather than an asset.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Managing risk",
                  "The Board maintains a live risk register. We publish it because an organisation that cannot "
                  "name its own risks is unlikely to be managing them.", eyebrow_text="Risk")}
    {table(["Risk", "Exposure", "Mitigation"],
           [[f"<strong>{esc(a)}</strong>", esc(b), esc(c)] for a, b, c in D.RISKS])}
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Strategic priorities to 2029",
                  "Our strategy is deliberately sequenced. We are building the institutional foundations first, "
                  "proving three flagship programmes second, and expanding the portfolio third — because a "
                  "portfolio that outruns its systems eventually fails the people it was built for.",
                  eyebrow_text="Roadmap")}
    <div class="grid grid--3">
      {"".join(f"""
      <article class="card">
        <p class="eyebrow">{esc(phase)}</p>
        <h3>{esc(period)}</h3>
        {bullets([esc(x) for x in items])}
        <div class="note note--good" style="margin-bottom:0">
          <p class="note__title">{icon("target", "note__icon", 20)}Test of completion</p>
          <div class="note__body"><p class="small">{esc(test)}</p></div>
        </div>
      </article>""" for phase, period, items, test in D.ROADMAP)}
    </div>
    {note(f'<p>{esc(D.BENCHMARK_NOTE)}</p>'
          '<p><strong>We would rather be measured against a standard we have not yet reached than describe '
          'ourselves as having already arrived.</strong></p>',
          "What we are measuring ourselves against", "info", "chart")}
  </div>
</section>

{contact_strip()}
'''


def governance_policies():
    policy_cards = "".join(
        doc_card(f'{p["num"]} · {p["title"]}', p["summary"],
                 f'{esc(p["subtitle"])} · {esc(p["status"])}',
                 f'/assets/documents/{p["file"]}')
        for p in D.POLICIES)

    controls = table(["Control", "Requirement"],
                     [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.SAFEGUARDING_CONTROLS])

    in_dev = table(["Policy", "Status", "Purpose"],
                   [[f"<strong>{esc(a)}</strong>", f'<span class="tag tag--muted">{esc(b)}</span>', esc(c)]
                    for a, b, c in D.POLICIES_IN_DEVELOPMENT])

    bodies = table(["Body", "Responsibility"],
                   [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.GOVERNANCE_BODIES])

    commitments = table(["Commitment", "Status"],
                        [[esc(a), f'<span class="tag tag--muted">{esc(b)}</span>']
                         for a, b in D.GOVERNANCE_COMMITMENTS])

    return page_hero(
        title="Governance &amp; policies",
        lede="How the Foundation is governed, who is accountable for what, and the policies that bind everyone "
             "acting in our name.",
        eyebrow_text="Accountability",
        trail=[("Home", "/"), ("Accountability", "/accountability/"), ("Governance & Policies", None)],
    ) + f'''
<div class="container">{section_nav(ACC_NAV, "/accountability/governance-and-policies/")}</div>

<section class="section section--tight">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Legal identity", None, eyebrow_text="Registration")}
        <dl class="bank-details">
          <div><dt>Registered name</dt><dd>Synia Aid Foundation</dd></div>
          <div><dt>Legal form</dt><dd>Incorporated Trustees under the Companies and Allied Matters Act</dd></div>
          <div><dt>Regulator</dt><dd>Corporate Affairs Commission, Federal Republic of Nigeria</dd></div>
          <div><dt>Registration number</dt><dd>{D.SITE["reg_number"]}</dd></div>
          <div><dt>Date of registration</dt><dd>December 2018</dd></div>
          <div><dt>Registered office</dt><dd>Maitama, Federal Capital Territory, Abuja</dd></div>
          <div><dt>Governing body</dt><dd>Board of Trustees</dd></div>
        </dl>
      </div>
      <div>
        {section_head("How decisions are made", None, eyebrow_text="Governance structure")}
        {bodies}
      </div>
    </div>
  </div>
</section>

<section class="section section--surface" id="safeguarding">
  <div class="container">
    {section_head("Safeguarding",
                  "We work with children, with displaced families and with people in circumstances of acute "
                  "vulnerability. That imposes obligations which come before programme delivery, before growth "
                  "and before fundraising.", eyebrow_text="Our obligations")}
    {note(f'<p>{esc(D.SAFEGUARDING_COMMITMENT)}</p>', "Our safeguarding commitment", "good", "shield")}
    <h3 class="mt-6">What this means in practice</h3>
    <div class="mt-5">{controls}</div>
    <div class="btn-row mt-6">
      {btn("Read our safeguarding statement", "/safeguarding/", "primary")}
      {btn("Raise a concern", "/complaints/", "ghost", "shield")}
    </div>
  </div>
</section>

<section class="section" id="policies">
  <div class="container">
    {section_head("Our policy suite",
                  "Adopted policies are published in full. Everyone acting in the Foundation's name — trustees, "
                  "staff, volunteers, consultants, ambassadors and partner personnel — is bound by them.",
                  eyebrow_text="Downloadable documents")}
    <div class="grid grid--2">{policy_cards}</div>

    <h3 class="mt-7">Policies in development</h3>
    <p class="measure">We publish what has been adopted and name what has not. These are scheduled, and this
      page is updated as each is approved by the Board.</p>
    <div class="mt-5">{in_dev}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Strengthening our governance", None, eyebrow_text="Commitments")}
        <p class="measure">{esc(D.GOVERNANCE_CANDOUR)}</p>
        <div class="btn-row mt-5">
          {btn("Meet the Board and executive team", "/about/leadership/", "primary")}
        </div>
      </div>
      <div>{commitments}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Independence", None, eyebrow_text="No donation confers influence")}
    <p class="measure lede">We partner widely but remain independent of political, economic, religious and
      social interests. The people we serve are never used to promote causes that are not their own, and no
      partnership or donation confers influence over who we select or what we say.</p>
    <p class="measure">Where a conflict of interest arises, it is disclosed and the affected person recuses
      themselves from the decision. A conflict of interest is not wrongdoing — it arises naturally in a small,
      community-rooted organisation. What matters is that it is declared, recorded and managed before it
      affects a decision.</p>
  </div>
</section>

{contact_strip()}
'''


def reports_publications():
    pubs = "".join(
        doc_card(p["title"], p["summary"],
                 f'{esc(p["category"])} · {esc(p["date"])} · {esc(p["pages"])} · PDF',
                 f'/assets/documents/{p["file"]}')
        for p in D.PUBLICATIONS)

    policies = "".join(
        doc_card(f'{p["num"]} · {p["title"]}', p["summary"],
                 f'{esc(p["category"])} · {esc(p["status"])} · PDF',
                 f'/assets/documents/{p["file"]}')
        for p in D.POLICIES)

    pending = table(["Publication", "When"],
                    [[f"<strong>{esc(a)}</strong>", f'<span class="tag tag--muted">{esc(b)}</span>']
                     for a, b in D.PUBLICATIONS_PENDING])

    return page_hero(
        title="Reports &amp; publications",
        lede="Our published documents, free to download. The library grows as documents are adopted and "
             "reports are produced.",
        eyebrow_text="Accountability",
        trail=[("Home", "/"), ("Accountability", "/accountability/"), ("Reports & Publications", None)],
    ) + f'''
<div class="container">{section_nav(ACC_NAV, "/accountability/reports-and-publications/")}</div>

<section class="section section--tight">
  <div class="container">
    {section_head("Corporate documents", None, eyebrow_text="Who we are and what we do")}
    <div class="grid grid--2">{pubs}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Policies", "Adopted policies, published in full.", eyebrow_text="Governance documents")}
    <div class="grid grid--2">{policies}</div>
    <p class="small text-muted mt-5">Further policies — financial controls and procurement, complaints and
      feedback, data protection and risk management — are in development and will be added here as they are
      adopted by the Board. See <a href="/accountability/governance-and-policies/">Governance &amp;
      policies</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Not yet published", None, eyebrow_text="Scheduled")}
        <p>We build the section and leave it empty rather than omitting it. When each document exists it will
           appear here, with its date and its source data.</p>
        {note(f'<p>{esc(D.FINANCIAL_CANDOUR)}</p>', "Audited accounts", "warn", "alert")}
      </div>
      <div>{pending}</div>
    </div>
  </div>
</section>

{cta_band("Need something that is not here?",
          "If you are conducting due diligence and need a document, a programme model or a figure with its "
          "source, ask us. A named person will answer you directly.",
          [btn("Request a document", "/contact/?subject=funding", "cta")], "surface")}
'''


def how_we_measure_impact():
    prelaunch = "".join(
        f'<li><div><h3>{esc(t)}</h3><p>{esc(b)}</p></div></li>' for t, b in D.PROGRAMME_PRELAUNCH)

    indicators = table(
        ["Pillar", "Output — what we did", "Outcome — what changed"],
        [[f"<strong>{esc(a)}</strong>", esc(b), esc(c)] for a, b, c in D.INDICATORS])

    return page_hero(
        title="How we measure impact",
        lede="Monitoring, evaluation, accountability and learning is being built into the Foundation as a "
             "system, not added as a report at the end of a grant.",
        eyebrow_text="Accountability",
        trail=[("Home", "/"), ("Accountability", "/accountability/"), ("How We Measure Impact", None)],
    ) + f'''
<div class="container">{section_nav(ACC_NAV, "/accountability/how-we-measure-impact/")}</div>

<section class="section section--tight">
  <div class="container">
    <div class="grid grid--split">
      <div class="prose">
        <h2>Outputs and outcomes are not the same thing</h2>
        <p>An <strong>output</strong> is what we did: a fee paid, a grant disbursed, a roof repaired.
           An <strong>outcome</strong> is what changed: a child still in school at the end of the year, a
           business still trading twelve months later, a family still housed and secure.</p>
        <p>Outputs are easy to count and easy to inflate. Outcomes are harder, slower and more honest — and
           they are what we are building our monitoring framework to capture.</p>
        <p>We are candid that, until recently, our reporting captured outputs rather than outcomes. That is a
           limitation, not an achievement, and it is the single thing we are working hardest to correct.</p>
      </div>
      <div>
        <blockquote class="pullquote">We measure not only how much relief was delivered, but whether children
          stayed in school, whether adults sustained an income, and whether families remained housed and
          healthy.</blockquote>
        {note(f'<p>{esc(D.MEL_POSITION)}</p>', "Our current position, stated openly", "warn", "alert")}
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("What each programme must have before it launches",
                  "A programme without these is not launched. This is what stands behind every status label on "
                  "this site.", eyebrow_text="Five conditions")}
    <ol class="steps">{prelaunch}</ol>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Illustrative indicators by pillar", None, eyebrow_text="What we count")}
    {indicators}
    <p class="small text-muted mt-5">All indicators are disaggregated by sex, displacement status, disability
      and age group. Attendance and completion are verified by physical visit at least once per term —
      administrative records alone are not sufficient evidence for a donor report, or for us.</p>
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
        <p>Findings are reported to the Board, and we intend to publish what we learn — including where a
           programme did not work.</p>
        <div class="btn-row mt-5">{btn("How to raise a concern", "/complaints/", "light")}</div>
      </div>
      <div>
        <div class="note note--dark">
          <p class="note__title">{icon("target", "note__icon", 20)}Unit economics</p>
          <div class="note__body">
            <p>Each flagship programme carries a documented cost per participant, built up from its standard
               package and its share of programme support costs.</p>
            <p>We publish the cost per <em>outcome</em> as well as per participant — the cost per child
               retained to year end, or per enterprise still trading at twelve months — because that is the
               figure that prices what actually changed.</p>
            <p>Unit costs are re-priced at least twice a year and every figure is dated, since inflation
               renders an unrevised cost misleading within a year.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{donate_band()}
'''
