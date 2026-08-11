# -*- coding: utf-8 -*-
"""Get Involved: hub, Donate, thank-you, Partner, Volunteer, Ambassador."""

from . import data as D
from .layout import (icon, esc, btn, section_head, note, table, bullets, paras,
                     section_nav, cta_band, newsletter_form)
from .components import (page_hero, get_involved_grid, donate_band, contact_strip,
                         programme_url, PROGRAMME_BY_SLUG, photo, photo_credit_line)

INVOLVE_NAV = [
    ("Overview", "/get-involved/"),
    ("Donate", "/donate/"),
    ("Partner with us", "/get-involved/partner/"),
    ("Volunteer", "/get-involved/volunteer/"),
    ("Become an ambassador", "/get-involved/ambassador/"),
]


def _consent_field(prefix):
    return f'''
<div class="field field--check">
  <input type="checkbox" id="{prefix}-marketing" name="marketing_consent" value="yes">
  <label for="{prefix}-marketing">Optional: I would like to receive occasional email updates about the
    Foundation's work. This is separate from your enquiry, and you can unsubscribe at any time.</label>
</div>
<p class="form__legal">We use the details you give here only to respond to you. We keep them no longer than we
  need to, we do not sell or share them, and you may ask us to correct or delete them at any time — see our
  <a href="/privacy/">Privacy Policy</a>.</p>'''


# ===========================================================================
# HUB
# ===========================================================================

def get_involved():
    return page_hero(
        title="Get involved",
        lede="Every contribution — of money, time or expertise — powers real education, empowerment and relief "
             "for vulnerable communities. There are four ways to stand with the Foundation.",
        eyebrow_text="Work with us",
        trail=[("Home", "/"), ("Get Involved", None)],
    ) + f'''
<div class="container">{section_nav(INVOLVE_NAV, "/get-involved/")}</div>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Four ways to stand with the Foundation</h2>
    <div class="grid grid--2">
      {"".join(f"""
      <article class="card card--link">
        <span class="pillar__icon">{icon(g["icon"], "", 26)}</span>
        <p class="eyebrow" style="margin-bottom:.3em">{g["num"]}</p>
        <h3><a class="stretched" href="{'/donate/' if g['slug'] == 'donate' else '/get-involved/' + g['slug'] + '/'}">{esc(g["title"])}</a></h3>
        <p class="lede" style="font-size:var(--step-0)">{esc(g["summary"])}</p>
        <p>{esc(g["detail"])}</p>
        <p class="card__foot"><span class="card__more">{esc(g["cta"])}{icon("arrow-right", "", 18)}</span></p>
      </article>""" for g in D.GET_INVOLVED)}
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("If you are considering funding us", None, eyebrow_text="For institutional funders")}
        <p>Each programme on this site has a written model behind it — who it serves, what the standard package
           contains, what it costs per person, how it is measured and when support ends. We are glad to share
           the relevant model and to talk openly about what we can and cannot yet evidence.</p>
        <p>We would rather begin a funding relationship with an accurate picture than an impressive one.</p>
        <div class="btn-row mt-5">
          {btn("Talk to us about funding", "/contact/?subject=funding", "primary")}
          {btn("See our accountability section", "/accountability/", "ghost", None)}
        </div>
      </div>
      <div>
        <div class="card">
          <h3>What a funder can expect from us</h3>
          {bullets(D.FUNDER_EXPECTATIONS)}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="photo-band">
      {photo("classroom-group", "1x1", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("woman-portrait", "1x1", sizes="(min-width: 700px) 25vw, 50vw", focus="upper", max_width=640)}
      {photo("children-yard", "1x1", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-seated", "1x1", sizes="(min-width: 700px) 25vw, 50vw", focus="upper", max_width=640)}
    </div>
    <p class="small text-muted mt-4">{photo_credit_line()}</p>
  </div>
</section>

{contact_strip()}
'''


# ===========================================================================
# DONATE
# ===========================================================================

def donate():
    amounts = "".join(f'''
    <div class="amount">
      <input type="radio" name="amount" id="amt-{t["amount"]}" value="{t["amount"]}"
             {"checked" if t["amount"] == 25000 else ""}>
      <label for="amt-{t["amount"]}">
        <span class="amount__value">{esc(t["label"])}</span>
        <span class="amount__funds">{esc(t["funds"])}</span>
      </label>
    </div>''' for t in D.DONATION_TIERS)

    designations = "".join(
        f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in D.DONATION_DESIGNATIONS)

    bank_rows = "".join(f'<div><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k, v in [
        ("Bank", f'<span class="placeholder-value">{esc(D.BANK_TRANSFER["bank"])}</span>'),
        ("Account name", esc(D.BANK_TRANSFER["account_name"])),
        ("Account number", f'<span class="placeholder-value">{esc(D.BANK_TRANSFER["account_number"])}</span>'),
        ("For international transfers", f'<span class="placeholder-value">{esc(D.BANK_TRANSFER["sort_or_swift"])}</span>'),
        ("Reference", esc(D.BANK_TRANSFER["reference"])),
    ])

    faqs = [
        ("Will I get a receipt?",
         "Yes. A receipt is emailed to you immediately, showing our registered name, our registration number "
         "CAC/IT/NO 121882, the amount and the date. If it does not arrive, check your spam folder and then "
         "email us — we will resend it."),
        ("Can I cancel a monthly gift?",
         "At any time, without giving a reason. Email info@syniafoundation.org or call us and we will cancel it "
         "and confirm in writing. You can also cancel through the payment provider directly."),
        ("Can I choose what my gift funds?",
         "Yes. You can direct your gift to a pillar, to a specific programme, or leave it where it is most "
         "needed. Whatever you choose is recorded against your donation, and a restriction you place on a gift "
         "is honoured absolutely."),
        ("Can I give anonymously?",
         "Yes. You may withhold your name from any public acknowledgement. We will still need your email "
         "address to send you a receipt, and we will not publish your name anywhere."),
        ("Is my card safe?",
         "Card details are handled entirely by the payment provider on their own secure pages. No card details "
         "are ever stored on this website. The whole site runs over HTTPS."),
        ("Can I give from outside Nigeria?",
         "Yes. Foreign cards are accepted and the currency is shown clearly before you confirm. Our diaspora "
         "supporters are a real and valued segment of our income."),
        ("How do I know the money is used well?",
         "Programme budgets are approved by the Board before expenditure is committed; payment authorisation "
         "is separated from payment requests; grants to participants are released against milestones rather "
         "than as lump sums; and no one both selects a participant and releases their funds. We publish our "
         "controls, our risks and what we have not yet achieved."),
    ]
    faq_html = "".join(
        f'<details><summary>{esc(q)}</summary><div class="accordion__body"><p>{esc(a)}</p></div></details>'
        for q, a in faqs)

    return page_hero(
        title="Donate",
        lede="Fund a child's school year, a household's shelter repair, or a trader's start in business. "
             "One-off or monthly, from ₦5,000 upward, in Naira or from abroad.",
        eyebrow_text="Get involved",
        trail=[("Home", "/"), ("Get Involved", "/get-involved/"), ("Donate", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Make your donation</h2>
    <div class="grid grid--sidebar">
      <div>
        <form class="donate-box" data-donate data-form="donation" action="/donate/checkout" method="post" novalidate>
          <fieldset>
            <legend>How often would you like to give?</legend>
            <div class="toggle">
              <input type="radio" name="frequency" id="freq-once" value="once" checked>
              <label for="freq-once">One-off gift</label>
              <input type="radio" name="frequency" id="freq-monthly" value="monthly">
              <label for="freq-monthly">Every month</label>
            </div>
            <p class="field__hint mt-4">Recurring giving matters more to us than any single total, because it
              lets us commit to a child for a full academic year. You can cancel at any time.</p>
          </fieldset>

          <fieldset>
            <legend>Choose an amount</legend>
            <div class="amounts">
              {amounts}
              <div class="amount">
                <input type="radio" name="amount" id="amt-custom" value="custom">
                <label for="amt-custom">
                  <span class="amount__value">Other</span>
                  <span class="amount__funds">Choose your own amount</span>
                </label>
              </div>
            </div>
            <div class="field mt-4">
              <label class="field__label" for="custom-amount">Other amount (₦)</label>
              <input class="field__input" type="number" inputmode="numeric" min="5000" step="500"
                     id="custom-amount" name="custom_amount" data-donate-custom placeholder="e.g. 15000">
              <p class="field__hint" data-donate-min hidden style="color:#A61B1B">The minimum gift is ₦5,000.</p>
            </div>
            <p class="field__hint">The amounts above describe what a gift of that size typically covers within
              the standard package for that programme. They are not audited unit costs — we publish cost per
              participant and cost per outcome once a full delivery cycle is complete.</p>
          </fieldset>

          <fieldset>
            <legend>Where would you like it to go?</legend>
            <div class="field">
              <label class="field__label" for="designation">Direct my gift to</label>
              <select class="field__select" id="designation" name="designation">{designations}</select>
              <p class="field__hint">Whatever you choose is recorded against your donation, and a restriction
                you place on a gift is honoured absolutely.</p>
            </div>
          </fieldset>

          <fieldset>
            <legend>Your details</legend>
            <div class="form__grid form__grid--2">
              <div class="field">
                <label class="field__label" for="donor-name">Full name <span class="req">*</span></label>
                <input class="field__input" type="text" id="donor-name" name="name" autocomplete="name" required>
              </div>
              <div class="field">
                <label class="field__label" for="donor-email">Email address <span class="req">*</span></label>
                <input class="field__input" type="email" id="donor-email" name="email" autocomplete="email" required>
                <p class="field__hint">Your receipt is sent here.</p>
              </div>
            </div>
            <div class="field field--check mt-4">
              <input type="checkbox" id="donor-anon" name="anonymous" value="yes">
              <label for="donor-anon">Keep my gift anonymous — do not include my name in any public
                acknowledgement.</label>
            </div>
            {_consent_field("donate")}
          </fieldset>

          <div class="donate-summary">
            <span><span class="donate-summary__amount" data-donate-amount>₦25,000</span>
              <span class="donate-summary__freq" data-donate-freq>one-off gift</span></span>
            <button class="btn btn--cta" type="submit" data-donate-submit>Give ₦25,000</button>
          </div>

          <p class="gateway-note">{icon("shield", "", 20)}
            <span>Payments are processed on the provider's own secure pages. No card details are stored on this
            website. Every gift is receipted with our registered name and number.</span></p>

          <div class="hp" aria-hidden="true"><label for="donate-website">Leave empty</label>
            <input type="text" id="donate-website" name="website" tabindex="-1" autocomplete="off"></div>
          <p class="form-status" role="status" data-form-status></p>
          <noscript><p class="form-status is-error">Card giving needs JavaScript. You can give by
            <a href="#bank-transfer">bank transfer</a>, or call us on
            <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a> and we will take your gift over the
            phone.</p></noscript>
        </form>
      </div>

      <aside>
        {photo("classroom-writing", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <p class="eyebrow">Why monthly matters</p>
          <h3>A school year is nine months long</h3>
          <p class="small">A one-off gift pays a term. A monthly gift lets us tell a family, in writing, that
            their child's place is covered to the end of the year — which is the difference between a child
            who returns to school and a child who stays there.</p>
        </div>

        <div class="card mt-5">
          <h3>Where your gift goes</h3>
          <ul class="linklist mt-4">
            {"".join(f'<li><a href="{programme_url(s)}"><span>{esc(PROGRAMME_BY_SLUG[s]["short_name"])}<small>{esc(PROGRAMME_BY_SLUG[s]["one_line"])}</small></span>{icon("arrow-right", "", 18)}</a></li>' for s in ["learning-access-retention", "enterprise-development", "safe-shelter"])}
          </ul>
          <p class="small text-muted mt-4">These three programmes are running today. You can also give to a
            pillar, or wherever it is most needed.</p>
        </div>

        <div class="card card--quiet mt-5">
          <h3>Other ways to give</h3>
          <p class="small">Bank transfer details are below. For corporate giving, payroll giving or a gift in
            a will, please <a href="/contact/?subject=donation">talk to us directly</a>.</p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface" id="bank-transfer">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Prefer a bank transfer?",
                      "Many of our supporters give by direct transfer. Please use the reference convention "
                      "below so we can match your gift to you and send your receipt.",
                      eyebrow_text="Bank transfer")}
        {note('<p>If you transfer without a reference we may not be able to identify you, which means we '
              'cannot send a receipt or honour a restriction you wanted to place on the gift.</p>',
              "Please use a reference", "warn", "alert")}
      </div>
      <div>
        <div class="card">
          <dl class="bank-details">{bank_rows}</dl>
          <p class="small text-muted mt-4">Account details are issued by the Foundation directly. If any detail
            on this page is shown as a placeholder, it has not yet been published — please
            <a href="/contact/?subject=donation">contact us</a> for confirmed details before transferring.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("Questions about giving", None, eyebrow_text="Before you give")}
        <p>If your question is not answered here, call us on
          <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a> or email
          <a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a>. A named person will answer you.</p>
      </div>
      <div><div class="accordion">{faq_html}</div></div>
    </div>
  </div>
</section>

{cta_band("Not ready to give? There are three other ways to help.",
          "Partner with us, volunteer your time and skills, or become an ambassador and carry the work into "
          "your own network.",
          [btn("See all four routes", "/get-involved/", "cta")], "surface")}
'''


def thank_you():
    return page_hero(
        title="Thank you",
        lede="Your gift has been received, and a receipt is on its way to your inbox.",
        eyebrow_text="Donation complete",
        trail=[("Home", "/"), ("Donate", "/donate/"), ("Thank you", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        <h2>What happens next</h2>
        <ol class="steps">
          <li><div><h3>Your receipt</h3><p>An email receipt is sent immediately, showing our registered name,
            our registration number CAC/IT/NO 121882, the amount and the date. If it has not arrived within a
            few minutes, check your spam folder and then email us.</p></div></li>
          <li><div><h3>Your gift is recorded against what you chose</h3><p>If you directed your gift to a pillar
            or a programme, that restriction is recorded and honoured absolutely.</p></div></li>
          <li><div><h3>You will hear how it was used</h3><p>We report on our programmes honestly — including
            where results disappoint. From the 2026–27 academic year our published figures are backed by
            project-level data with sources and dates.</p></div></li>
          <li><div><h3>If you gave monthly</h3><p>You may cancel at any time, without giving a reason. Email or
            call us and we will cancel it and confirm in writing.</p></div></li>
        </ol>

        <h2>One more thing that would help</h2>
        <p>Most people who support us heard about the Foundation from someone they know. If you would tell one
           person about this work, that is worth more to us than you might expect.</p>
        <div class="btn-row">
          {btn("Share on Facebook", "https://www.facebook.com/sharer/sharer.php?u=" + D.SITE["base_url"], "ghost", "facebook")}
          {btn("Share on LinkedIn", "https://www.linkedin.com/sharing/share-offsite/?url=" + D.SITE["base_url"], "ghost", "linkedin")}
        </div>
      </div>
      <aside>
        <div class="card">
          <h3>Join the newsletter</h3>
          <p class="small">A short email when there is something real to report. Separate from your donation —
            you are not signed up unless you ask to be.</p>
          <div class="mt-4">{newsletter_form(compact=True)}</div>
        </div>
        <div class="card card--quiet mt-5">
          <h3>A question about your gift?</h3>
          <p class="small"><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a><br>
            <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# PARTNER
# ===========================================================================

def partner():
    types = [
        ("Programme partners", "Organisations delivering alongside us — schools, health bodies, technical "
                               "specialists and community organisations."),
        ("Funders", "Corporate foundations, institutional donors and diaspora networks funding a programme or "
                    "a cohort."),
        ("Technical collaborators", "Engineering, WASH, legal, monitoring and evaluation capability we do not "
                                    "hold in house and do not pretend to."),
        ("Institutional allies", "Government agencies, UN bodies and networks working on displacement, "
                                 "resettlement and durable solutions."),
    ]
    type_cards = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(b)}</p></div>' for t, b in types)

    return page_hero(
        title="Partner with us",
        lede="We do not believe the change we seek can be created alone, and we do not try. Almost every "
             "project in our record was delivered alongside someone else.",
        eyebrow_text="Get involved",
        trail=[("Home", "/"), ("Get Involved", "/get-involved/"), ("Partner With Us", None)],
    ) + f'''
<div class="container">{section_nav(INVOLVE_NAV, "/get-involved/partner/")}</div>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Why we work in partnership</h2>
    <div class="grid grid--split">
      <div class="prose">
        <p class="lede">By joining forces with health bodies, schools, mental-health organisations, service
          clubs, fellow foundations, government agencies and UN civil-society focal points, we reach further,
          deliver deeper expertise and multiply the value of every naira raised.</p>
        <p>A road walk becomes a district-wide conversation; a medical outreach becomes a full clinic; a school
          visit becomes a safeguarding programme. Each partner brings capability we alone would take years to
          build — and in return we offer trusted, community-rooted access to the people who need help most.</p>
        <p>Collaboration is not a supporting tactic; it is the engine of our impact.</p>
      </div>
      <div>
        {photo("children-community", "4x3", sizes="(min-width: 880px) 540px, 100vw", cls="mb-5")}
        <div class="card">
          <h3>What we offer a partner</h3>
          {bullets(D.WHAT_WE_OFFER_PARTNERS)}
          <p class="card__foot"><a class="card__more" href="/about/partners/">
            See who we already work with{icon("arrow-right", "", 18)}</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {section_head("The kinds of partnership we seek", None, eyebrow_text="Four routes")}
    <div class="grid grid--4">{type_cards}</div>
    {note('<p>Every partner whose personnel come into contact with children is bound by our Safeguarding Policy '
          'or an equivalent standard, as a written condition of the partnership. We ask this of everyone, '
          'without exception, and we expect to be asked the same.</p>',
          "One condition we do not move on", "good", "shield")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        {section_head("Start a conversation",
                      "Tell us a little about your organisation and what you have in mind. A named person will "
                      "reply — not an autoresponder alone.", eyebrow_text="Partnership enquiry")}
        <form class="form" data-form="partnership" data-subject="Partnership enquiry from the website"
              action="/enquiry" method="post" novalidate>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="p-name">Your name <span class="req">*</span></label>
              <input class="field__input" type="text" id="p-name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label class="field__label" for="p-role">Your role</label>
              <input class="field__input" type="text" id="p-role" name="role">
            </div>
          </div>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="p-org">Organisation <span class="req">*</span></label>
              <input class="field__input" type="text" id="p-org" name="organisation" required>
            </div>
            <div class="field">
              <label class="field__label" for="p-email">Email <span class="req">*</span></label>
              <input class="field__input" type="email" id="p-email" name="email" autocomplete="email" required>
            </div>
          </div>
          <div class="field">
            <label class="field__label" for="p-type">Type of partnership</label>
            <select class="field__select" id="p-type" name="partnership_type">
              <option>Programme partner</option>
              <option>Funder</option>
              <option>Technical collaborator</option>
              <option>Institutional ally</option>
              <option>Not sure yet</option>
            </select>
          </div>
          <div class="field">
            <label class="field__label" for="p-message">What do you have in mind? <span class="req">*</span></label>
            <textarea class="field__textarea" id="p-message" name="message" required></textarea>
          </div>
          {_consent_field("p")}
          <div class="hp" aria-hidden="true"><label for="p-website">Leave empty</label>
            <input type="text" id="p-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="btn-row">
            <button class="btn btn--cta" type="submit">Send enquiry{icon("arrow-right", "btn__icon", 20)}</button>
          </div>
          <p class="form-status" role="status" data-form-status></p>
        </form>
      </div>
      <aside>
        <div class="card">
          <h3>Prefer to speak to someone?</h3>
          <p class="small"><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a><br>
            <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a><br>
            <span class="text-muted">{esc(D.SITE["hours"])}</span></p>
        </div>
        <div class="card card--quiet mt-5">
          <h3>Doing due diligence?</h3>
          <p class="small">Our governance, policies, monitoring approach and published documents are all in one
            place.</p>
          <p class="card__foot"><a class="card__more" href="/accountability/">
            Accountability{icon("arrow-right", "", 18)}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# VOLUNTEER
# ===========================================================================

def volunteer():
    roles = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
                    for t, b in D.VOLUNTEER_ROLES)

    return page_hero(
        title="Volunteer",
        lede="Give your time and skills in your own community and on our outreaches. Our volunteer network "
             "spans several Nigerian states.",
        eyebrow_text="Get involved",
        trail=[("Home", "/"), ("Get Involved", "/get-involved/"), ("Volunteer", None)],
    ) + f'''
<div class="container">{section_nav(INVOLVE_NAV, "/get-involved/volunteer/")}</div>

<section class="section section--tight">
  <div class="container">
    {note(f'<p>{esc(D.VOLUNTEER_VETTING)}</p>', "Volunteers working with children are vetted", "warn", "shield")}
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {section_head("Where we need help", "Opportunities vary through the year. Tell us what you can offer and "
                  "we will match you to something real rather than keeping you on a list.",
                  eyebrow_text="Current opportunities")}
    <div class="grid grid--4">{roles}</div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        {section_head("Apply to volunteer", "We will reply. If we cannot place you now, we will say so rather "
                      "than leave you waiting.", eyebrow_text="Application")}
        <form class="form" data-form="volunteer" data-subject="Volunteer application from the website"
              action="/enquiry" method="post" novalidate>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="v-name">Full name <span class="req">*</span></label>
              <input class="field__input" type="text" id="v-name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label class="field__label" for="v-email">Email <span class="req">*</span></label>
              <input class="field__input" type="email" id="v-email" name="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="v-phone">Phone</label>
              <input class="field__input" type="tel" id="v-phone" name="phone" autocomplete="tel">
            </div>
            <div class="field">
              <label class="field__label" for="v-location">Where are you based? <span class="req">*</span></label>
              <input class="field__input" type="text" id="v-location" name="location" required
                     placeholder="e.g. Keffi, Nasarawa">
            </div>
          </div>
          <div class="field">
            <label class="field__label" for="v-role">What would you like to help with?</label>
            <select class="field__select" id="v-role" name="role">
              {"".join(f"<option>{esc(t)}</option>" for t, _ in D.VOLUNTEER_ROLES)}
              <option>Something else — I will explain below</option>
            </select>
          </div>
          <div class="field">
            <label class="field__label" for="v-about">Tell us about yourself <span class="req">*</span></label>
            <textarea class="field__textarea" id="v-about" name="about" required
              placeholder="Your skills, your availability, and anything you have done like this before."></textarea>
          </div>
          <div class="field field--check">
            <input type="checkbox" id="v-vetting" name="vetting_understood" value="yes" required>
            <label for="v-vetting">I understand that volunteering with children requires vetting, two
              references, safeguarding induction and a signed Code of Conduct. <span class="req">*</span></label>
          </div>
          {_consent_field("v")}
          <div class="hp" aria-hidden="true"><label for="v-website">Leave empty</label>
            <input type="text" id="v-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="btn-row">
            <button class="btn btn--cta" type="submit">Send application{icon("arrow-right", "btn__icon", 20)}</button>
          </div>
          <p class="form-status" role="status" data-form-status></p>
        </form>
      </div>
      <aside>
        {photo("women-smiling", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <h3>What volunteering involves</h3>
          {bullets([
            "A safeguarding induction before your first contact with a programme, and a refresher each year.",
            "A signed Code of Conduct, held on file.",
            "The two-adult rule: no unaccompanied one-to-one contact with a child, ever.",
            "A named person at the Foundation who is responsible for you and answers your questions.",
          ])}
        </div>
        <div class="card card--quiet mt-5">
          <h3>Read the standards</h3>
          <p class="small">Our Code of Conduct and Safeguarding Policy are published in full.</p>
          <p class="card__foot"><a class="card__more" href="/accountability/governance-and-policies/">
            Governance &amp; policies{icon("arrow-right", "", 18)}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# AMBASSADOR
# ===========================================================================

def ambassador():
    return page_hero(
        title="Become an ambassador",
        lede="Champion our mission and amplify its impact beyond borders.",
        eyebrow_text="Get involved",
        trail=[("Home", "/"), ("Get Involved", "/get-involved/"), ("Become an Ambassador", None)],
    ) + f'''
<div class="container">{section_nav(INVOLVE_NAV, "/get-involved/ambassador/")}</div>

<section class="section section--tight">
  <div class="container">
    <div class="grid grid--split">
      <div>
        {section_head("What an ambassador does", None, eyebrow_text="The role")}
        {bullets(D.AMBASSADOR_WHAT)}
        <p class="mt-5">Our ambassadors are often people with a network we do not have — in the diaspora, in a
          profession, in a faith community or in business. What we ask is honesty about what we are: a growing
          Nigerian foundation with three programmes running and nine more scheduled.</p>
      </div>
      <div>
        <div class="card">
          <h3>What we give you</h3>
          {bullets([
            "A named contact at the Foundation.",
            "Our Corporate Profile, programme guide and current figures, so you never have to guess.",
            "Materials you can share, and clear guidance on what may and may not be said on our behalf.",
            "An honest answer to any difficult question, including the ones about what we cannot yet evidence.",
          ])}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        {section_head("Register your interest", None, eyebrow_text="Expression of interest")}
        <form class="form" data-form="ambassador" data-subject="Ambassador expression of interest"
              action="/enquiry" method="post" novalidate>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="a-name">Full name <span class="req">*</span></label>
              <input class="field__input" type="text" id="a-name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label class="field__label" for="a-email">Email <span class="req">*</span></label>
              <input class="field__input" type="email" id="a-email" name="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="a-location">Where are you based? <span class="req">*</span></label>
              <input class="field__input" type="text" id="a-location" name="location" required
                     placeholder="City and country">
            </div>
            <div class="field">
              <label class="field__label" for="a-network">Your network or profession</label>
              <input class="field__input" type="text" id="a-network" name="network">
            </div>
          </div>
          <div class="field">
            <label class="field__label" for="a-why">Why the Foundation? <span class="req">*</span></label>
            <textarea class="field__textarea" id="a-why" name="message" required
              placeholder="What draws you to this work, and how you think you could help."></textarea>
          </div>
          <div class="field field--check">
            <input type="checkbox" id="a-conduct" name="conduct" value="yes" required>
            <label for="a-conduct">I understand that ambassadors sign the Foundation's Code of Conduct.
              <span class="req">*</span></label>
          </div>
          {_consent_field("a")}
          <div class="hp" aria-hidden="true"><label for="a-website">Leave empty</label>
            <input type="text" id="a-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="btn-row">
            <button class="btn btn--cta" type="submit">Send{icon("arrow-right", "btn__icon", 20)}</button>
          </div>
          <p class="form-status" role="status" data-form-status></p>
        </form>
      </div>
      <aside>
        <div class="card card--quiet">
          <h3>Not quite what you had in mind?</h3>
          <p class="small">There are three other ways to stand with the Foundation.</p>
          <p class="card__foot"><a class="card__more" href="/get-involved/">
            See all four routes{icon("arrow-right", "", 18)}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
