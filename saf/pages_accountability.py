# -*- coding: utf-8 -*-
"""Accountability: hub, Governance & Policies, Reports & Publications, How We Measure Impact."""

from . import data as D
from .layout import (icon, esc, btn, section_head, note, table, bullets, paras,
                     section_nav, cta_band, stat_grid)
from .components import (page_hero, doc_card, donate_band, contact_strip,
                         photo, photo_credit_line)
from .graphics import roadmap_graphic

ACC_NAV = [
    ("Overview", "/accountability/"),
    ("Governance & Policies", "/accountability/governance-and-policies/"),
    ("Reports & Publications", "/accountability/reports-and-publications/"),
]


def accountability():
    risks = "".join(
        f'<details><summary>{esc(a)}</summary><div class="accordion__body">'
        f'<p><strong>Exposure.</strong> {esc(b)}</p><p><strong>Mitigation.</strong> {esc(c)}</p></div></details>'
        for a, b, c in D.RISKS)

    controls = table(["Control", "How it works"],
                     [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.FINANCIAL_CONTROLS])

    return page_hero(
        title="Accountability",
        lede="Everything an institutional funder, a regulator or a careful donor needs in order to assess us: "
             "governance, policies and published documents.",
        eyebrow_text="For institutional funders and due diligence",
        image="classroom-desks",
        trail=[("Home", "/"), ("Accountability", None)],
    ) + f'''
<div class="container">{section_nav(ACC_NAV, "/accountability/")}</div>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Explore this section</h2>
    <div class="grid grid--3">
      <article class="card card--link">
        <span class="doc__icon">{icon("scale", "", 22)}</span>
        <h3><a class="stretched" href="/accountability/governance-and-policies/">Governance &amp; Policies</a></h3>
        <p>How the Foundation is governed, who is accountable for what, and our policy suite, available to
           download.</p>
        <p class="card__foot"><span class="card__more">Read{icon("arrow-right", "", 18)}</span></p>
      </article>
      <article class="card card--link">
        <span class="doc__icon">{icon("doc", "", 22)}</span>
        <h3><a class="stretched" href="/accountability/reports-and-publications/">Reports &amp; Publications</a></h3>
        <p>Our Corporate Profile, programme structure guide and leadership biographies. Annual report and
           audited accounts are scheduled, and we say plainly that they are not yet published.</p>
        <p class="card__foot"><span class="card__more">Browse the library{icon("arrow-right", "", 18)}</span></p>
      </article>
      <article class="card card--link">
        <span class="doc__icon">{icon("chart", "", 22)}</span>
        <h3><a class="stretched" href="/impact/#how-we-measure-impact">How we measure impact</a></h3>
        <p>What each programme must have before it launches, the indicators we use, and what we do not yet
           claim. Found under Our Impact.</p>
        <p class="card__foot"><span class="card__more">Read{icon("arrow-right", "", 18)}</span></p>
      </article>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Financial stewardship",
                  "Every naira entrusted to the Foundation belongs to the people we serve. Our approach rests on "
                  "three commitments: control before scale, restriction honoured, and transparency by default.",
                  eyebrow_text="Stewardship")}
    <div class="accordion">
      <details>
        <summary>The controls we operate</summary>
        <div class="accordion__body">{controls}</div>
      </details>
      <details>
        <summary>Restricted funds</summary>
        <div class="accordion__body">
          <p>Where a donor gives for a specific purpose, that restriction is honoured absolutely. The Synia
             Scholars Fund will operate as a ring-fenced fund with its own agreement, published selection
             criteria, separate accounting and an annual statement to its donors. We will not promote it
             externally until that architecture exists.</p>
        </div>
      </details>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Managing risk",
                  "The Board maintains a live risk register. We publish it because an organisation that cannot "
                  "name its own risks is unlikely to be managing them. Open any risk to read the detail.",
                  eyebrow_text="Risk")}
    <div class="accordion">{risks}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("Strategic priorities to 2029",
                  "Our strategy is deliberately sequenced: institutional foundations first, three flagship "
                  "programmes second, and expansion third, because a portfolio that outruns its systems "
                  "eventually fails the people it was built for.",
                  eyebrow_text="Roadmap")}
    {roadmap_graphic(D.ROADMAP)}
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
        title="Governance &amp; Policies",
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
    {photo("classroom-group", "21x9", sizes="100vw", cls="mb-6",
           caption="Safeguarding is a condition of operating, not a section of the plan. "
                   + photo_credit_line())}
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
    <div class="photo-band mb-7">
      {photo("classroom-girl-bench", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-laughing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-gathering", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-seated", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
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
    {photo("classroom-writing", "21x9", sizes="100vw", cls="mb-6", eager=True,
           caption=photo_credit_line())}
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
      Policies</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {photo("children-yard", "4x3", sizes="(min-width: 880px) 540px, 100vw", cls="mb-5")}
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
