# -*- coding: utf-8 -*-
"""Contact, Complaints, legal pages, Search, Sitemap and 404."""

from . import data as D
from .layout import (icon, esc, btn, section_head, note, table, bullets, paras,
                     newsletter_form, cta_band)
from .components import (page_hero, contact_strip, programme_url, photo,
                         photo_credit_line)

DRAFT_MARK = ('<p class="small"><span class="placeholder-value">Version 1.0 · pending final review by the '
              'Foundation\'s Nigerian-qualified legal adviser before launch</span></p>')


# ===========================================================================
# CONTACT
# ===========================================================================

def contact():
    subjects = "".join(f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in D.CONTACT_SUBJECTS)
    socials = "".join(
        f'<li><a href="{s["url"]}" target="_blank" rel="me noopener">'
        f'<span><strong>{esc(s["name"])}</strong><small>{esc(s["handle"])}</small></span>'
        f'{icon("arrow-up-right", "", 18)}</a></li>' for s in D.SITE["social"])
    addr = "<br>".join(esc(l) for l in D.SITE["address_lines"])
    map_q = D.SITE["address_one_line"].replace(" ", "+").replace(",", "%2C")

    return page_hero(
        title="Contact us",
        lede="A real person answers. If your question is about a safeguarding concern, please use the "
             "complaints route so it reaches the right person immediately.",
        eyebrow_text="Get in touch",
        trail=[("Home", "/"), ("Contact", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        {section_head("Send us a message", None, eyebrow_text="Contact form")}
        <form class="form" data-form="contact" data-subject="Website contact form" action="/enquiry"
              method="post" novalidate>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="c-name">Your name <span class="req">*</span></label>
              <input class="field__input" type="text" id="c-name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label class="field__label" for="c-email">Email <span class="req">*</span></label>
              <input class="field__input" type="email" id="c-email" name="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form__grid form__grid--2">
            <div class="field">
              <label class="field__label" for="c-phone">Phone (optional)</label>
              <input class="field__input" type="tel" id="c-phone" name="phone" autocomplete="tel">
            </div>
            <div class="field">
              <label class="field__label" for="contact-subject">What is your message about?
                <span class="req">*</span></label>
              <select class="field__select" id="contact-subject" name="subject" required>{subjects}</select>
            </div>
          </div>
          <div class="field">
            <label class="field__label" for="c-message">Message <span class="req">*</span></label>
            <textarea class="field__textarea" id="c-message" name="message" required></textarea>
          </div>
          <div class="field field--check">
            <input type="checkbox" id="c-marketing" name="marketing_consent" value="yes">
            <label for="c-marketing">Optional: I would like to receive occasional email updates about the
              Foundation's work. This is separate from my message, and I can unsubscribe at any time.</label>
          </div>
          <p class="form__legal">We use the details you give here only to respond to you, and we keep them no
            longer than we need to. We do not sell or share them. See our
            <a href="/privacy/">Privacy Policy</a>.</p>
          <div class="hp" aria-hidden="true"><label for="c-website">Leave empty</label>
            <input type="text" id="c-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="btn-row">
            <button class="btn btn--cta" type="submit">Send message{icon("arrow-right", "btn__icon", 20)}</button>
          </div>
          <p class="form-status" role="status" data-form-status></p>
        </form>
      </div>

      <aside>
        {photo("women-gathering", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <h3>Head office</h3>
          <address class="mt-4">
            <p>{addr}</p>
            <p><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a></p>
            <p><a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a></p>
            <p><a href="tel:{D.SITE["hotline_href"]}">{D.SITE["hotline"]}</a>
              <span class="tag">24/7 hotline</span></p>
          </address>
          <p class="small text-muted">{icon("clock", "", 16)} {esc(D.SITE["hours"])}</p>
        </div>

        <div class="card mt-5">
          <h3>Follow the work</h3>
          <ul class="linklist mt-4">{socials}</ul>
        </div>

        <div class="card card--quiet mt-5">
          <h3>Raising a concern</h3>
          <p class="small">Anyone — a participant, a member of a community we work in, a partner, a volunteer or
            a member of staff — may raise a concern about our work or the conduct of anyone acting in our name,
            without going through the person whose conduct is in question.</p>
          <p class="card__foot"><a class="card__more" href="/complaints/">
            How to raise a concern{icon("arrow-right", "", 18)}</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="photo-band mb-7">
      {photo("classroom-friends", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-outside", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("woman-portrait", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <p class="small text-muted mb-6">{photo_credit_line()}</p>
    {section_head("Find us", None, eyebrow_text="Maitama, Abuja")}
    <div class="card" style="padding:0;overflow:hidden">
      <iframe title="Map showing the location of Synia Aid Foundation, Maitama, Abuja"
        src="https://www.google.com/maps?q={map_q}&amp;output=embed"
        width="100%" height="420" style="border:0;display:block" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <p class="small text-muted mt-4">The map is loaded from Google Maps. If you have declined optional cookies,
      you can view the location directly on
      <a href="https://www.google.com/maps/search/?api=1&amp;query={map_q}" target="_blank" rel="noopener">Google
      Maps</a> instead.</p>
  </div>
</section>
'''


# ===========================================================================
# COMPLAINTS
# ===========================================================================

def complaints():
    steps = "".join(f'<li><div><h3>{esc(t)}</h3><p>{esc(b)}</p></div></li>' for t, b in D.COMPLAINTS_STEPS)

    return page_hero(
        title="Raise a concern or make a complaint",
        lede="Anyone may raise a concern about our work, or about the conduct of anyone acting in our name. "
             "You do not need proof, you do not need to be certain, and you will not be disadvantaged for "
             "speaking up.",
        eyebrow_text="Complaints and safeguarding concerns",
        trail=[("Home", "/"), ("Complaints", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    {note('<p><strong>If someone is in immediate danger, contact the emergency services first</strong> — then '
          'tell us. Do not wait for us to respond before acting to keep someone safe.</p>',
          "In an emergency", "warn", "alert")}
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    {photo("elder-smiling", "21x9", sizes="100vw", cls="mb-7",
           caption="Anyone may raise a concern, without going through the person whose conduct is in "
                   "question. " + photo_credit_line())}
    {section_head("How to reach us", None, eyebrow_text="Three routes")}
    <div class="grid grid--3">
      <div class="card">
        <span class="doc__icon">{icon("phone", "", 22)}</span>
        <h3>By phone</h3>
        <p><a href="tel:{D.SITE["hotline_href"]}"><strong>{D.SITE["hotline"]}</strong></a>
          <span class="tag">24/7 hotline</span></p>
        <p><a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a>
          <span class="small text-muted">office hours</span></p>
      </div>
      <div class="card">
        <span class="doc__icon">{icon("mail", "", 22)}</span>
        <h3>By email</h3>
        <p><a href="mailto:{D.SITE["email"]}?subject=Concern%20or%20complaint">{D.SITE["email"]}</a></p>
        <p class="small text-muted">Mark your message “Concern” and it will be routed to the Safeguarding
          Focal Point.</p>
      </div>
      <div class="card">
        <span class="doc__icon">{icon("pin", "", 22)}</span>
        <h3>In person or in writing</h3>
        <p>{esc(D.SITE["address_one_line"])}</p>
        <p class="small text-muted">You may raise a concern anonymously.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--sidebar">
      <div>
        {section_head("What happens next", None, eyebrow_text="Our response")}
        <ol class="steps">{steps}</ol>
        {note(f'<p>{esc(D.COMPLAINTS_PROTECTION)}</p>', "You are protected", "good", "shield")}
      </div>
      <aside>
        <div class="card">
          <h3>What you can raise</h3>
          {bullets([
            "Concern about the safety or welfare of a child or an adult at risk.",
            "The conduct of any trustee, member of staff, volunteer, consultant, ambassador or partner "
            "representative acting in our name.",
            "A request for payment, a gift or a favour in exchange for support — which is never a condition "
            "of anything we do.",
            "Fraud, theft, bribery or the misuse of funds or goods.",
            "A decision about selection into a programme that you believe was wrong.",
            "The quality or conduct of any of our work.",
          ])}
        </div>
        <div class="card card--quiet mt-5">
          <h3>Read the policies</h3>
          <ul class="linklist mt-4">
            <li><a href="/assets/documents/SAF-Policy-01-Safeguarding.pdf" download>
              <span>Safeguarding Policy<small>PDF</small></span>{icon("download", "", 18)}</a></li>
            <li><a href="/assets/documents/SAF-Policy-03-PSEAH.pdf" download>
              <span>PSEAH Policy<small>PDF</small></span>{icon("download", "", 18)}</a></li>
            <li><a href="/assets/documents/SAF-Policy-04-AntiFraud-Whistleblowing.pdf" download>
              <span>Anti-Fraud &amp; Whistleblowing<small>PDF</small></span>{icon("download", "", 18)}</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    {photo("women-smiling", "21x9", sizes="100vw", cls="mb-7", caption=photo_credit_line())}
    {section_head("Four things we will never do", None, eyebrow_text="Our undertaking to you")}
    <div class="grid grid--4">
      <div class="card"><h3>Ask you to prove it first</h3><p>Concerns are acted on, not weighed. Nobody is
        required to be certain, or to hold proof, before reporting.</p></div>
      <div class="card"><h3>Make you go through the person concerned</h3><p>You may report to anyone, and a
        concern about a senior person is reported to a nominated independent Trustee instead.</p></div>
      <div class="card"><h3>Withdraw your support</h3><p>No one's access to our programmes is affected by
        raising a concern in good faith.</p></div>
      <div class="card"><h3>Handle it informally</h3><p>Concerns are recorded on the day they are received and
        are never resolved by moving someone to another role.</p></div>
    </div>
  </div>
</section>
'''


# ===========================================================================
# SAFEGUARDING STATEMENT
# ===========================================================================

def safeguarding():
    controls = table(["Control", "Requirement"],
                     [[f"<strong>{esc(a)}</strong>", esc(b)] for a, b in D.SAFEGUARDING_CONTROLS])

    return page_hero(
        title="Safeguarding statement",
        lede="Our public commitment to the protection of children, adults at risk and everyone who comes into "
             "contact with our work — and how to report a concern.",
        eyebrow_text="Our obligations",
        trail=[("Home", "/"), ("Safeguarding Statement", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        {photo("classroom-group", "3x2", sizes="(min-width: 940px) 720px, 100vw", cls="mb-6", eager=True,
               caption=photo_credit_line())}
        <p class="lede">{esc(D.SAFEGUARDING_COMMITMENT)}</p>

        <h2>Our principles</h2>
        {bullets([
          "The welfare of the child or adult at risk is paramount, and outweighs the reputation of the "
          "Foundation, the interests of any individual, and the continuation of any programme.",
          "All children have an equal right to protection, regardless of sex, disability, ethnicity, religion, "
          "displacement status or family circumstance.",
          "Concerns are acted on, not weighed. Nobody is required to be certain, or to hold proof, before "
          "reporting.",
          "Support is never conditional. No person's access to our support depends on their silence, their "
          "compliance, their appearance in our materials, or their relationship with any member of our team.",
        ])}

        <h2>Who this applies to</h2>
        <p>All trustees, staff, volunteers, interns, consultants, contractors, ambassadors, visitors and
           partner personnel acting in the Foundation's name — in all Foundation activity, whether or not on
           Foundation premises and whether or not in working hours.</p>

        <h2>Images and information</h2>
        <p>Written consent is obtained from a parent or carer before photographing or filming any child,
           including in wide shots. A child's full name is never published alongside their image. No image
           showing a person in distress, undressed, or in any way that would embarrass them in adulthood is
           published. Consent may be withdrawn at any time and the material removed.</p>
        <p>Support is never conditional on appearing in photographs, film or fundraising material, and anyone
           may decline without consequence.</p>

        <h2>Zero tolerance</h2>
        <p>The Foundation has zero tolerance of sexual exploitation, sexual abuse and sexual harassment. We
           adopt the six core principles on protection from sexual exploitation and abuse established by the
           Inter-Agency Standing Committee, and our response is survivor-centred. Sexual activity with any
           person under the age of eighteen is prohibited regardless of the local age of majority or consent,
           and a mistaken belief about age is not a defence.</p>

        <h2>How to report a concern</h2>
        <p>Concerns may be raised by telephone, by email, in person or in writing, and may be raised
           anonymously. They may be raised without going through the person whose conduct is in question.
           We will acknowledge, investigate and respond.</p>
        <p><a href="/complaints/"><strong>Read how to raise a concern, and what happens next</strong></a>.</p>
      </div>
      <aside>
        {photo("children-outside", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card">
          <h3>Report a concern now</h3>
          <p><a href="tel:{D.SITE["hotline_href"]}"><strong>{D.SITE["hotline"]}</strong></a>
            <span class="tag">24/7</span></p>
          <p><a href="mailto:{D.SITE["email"]}?subject=Safeguarding%20concern">{D.SITE["email"]}</a></p>
          <div class="btn-row mt-4">{btn("How to raise a concern", "/complaints/", "cta", "shield")}</div>
        </div>
        <div class="card card--quiet mt-5">
          <h3>Download the policies</h3>
          <ul class="linklist mt-4">
            <li><a href="/assets/documents/SAF-Policy-01-Safeguarding.pdf" download>
              <span>Safeguarding Policy<small>PDF</small></span>{icon("download", "", 18)}</a></li>
            <li><a href="/assets/documents/SAF-Policy-02-Code-of-Conduct.pdf" download>
              <span>Code of Conduct<small>PDF</small></span>{icon("download", "", 18)}</a></li>
            <li><a href="/assets/documents/SAF-Policy-03-PSEAH.pdf" download>
              <span>PSEAH Policy<small>PDF</small></span>{icon("download", "", 18)}</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="photo-band mb-7">
      {photo("classroom-girl-bench", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-laughing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("classroom-doorway", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-playing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    {section_head("What this means in practice", None, eyebrow_text="Controls")}
    {controls}
  </div>
</section>
'''


# ===========================================================================
# PRIVACY
# ===========================================================================

def privacy():
    data_table = table(
        ["What we collect", "Why", "Lawful basis", "How long we keep it"],
        [
            ["<strong>Contact and enquiry forms</strong><br>name, email, phone (optional), your message",
             "To answer you",
             "Legitimate interest in responding to a person who has contacted us",
             "24 months from our last contact with you, unless you ask us to delete it sooner"],
            ["<strong>Donations</strong><br>name, email, amount, designation, payment reference",
             "To process your gift, send your receipt, honour any restriction you placed on it, and meet our "
             "financial record-keeping obligations",
             "Performance of your request, and legal obligation for financial records",
             "Seven years, in line with financial record-keeping requirements"],
            ["<strong>Newsletter</strong><br>name (optional), email",
             "To send you the updates you asked for",
             "Your consent, given by a separate, unticked opt-in",
             "Until you unsubscribe, then removed from the mailing list"],
            ["<strong>Volunteer and ambassador applications</strong><br>name, contact details, location, "
             "background you choose to tell us",
             "To assess your application and, if you are placed, to carry out vetting",
             "Steps taken at your request, and our safeguarding obligations",
             "12 months if you are not placed; for the duration of your engagement plus six years if you are"],
            ["<strong>Complaints and safeguarding concerns</strong><br>whatever you choose to tell us",
             "To respond to the concern and protect anyone at risk",
             "Our safeguarding obligations and the vital interests of the person affected",
             "Held securely and separately, and retained for as long as safeguarding requires"],
            ["<strong>Website analytics</strong><br>pages viewed, approximate location, device type",
             "To understand how the site is used so we can improve it",
             "Your consent, given through the cookie banner",
             "Not set unless you accept optional cookies"],
        ])

    rights = [
        ("Access", "Ask us for a copy of the personal data we hold about you."),
        ("Rectification", "Ask us to correct anything that is wrong or incomplete."),
        ("Erasure", "Ask us to delete your data, where we are not required to keep it."),
        ("Restriction and objection", "Ask us to stop or limit how we use your data."),
        ("Withdraw consent", "Where we rely on consent — the newsletter, and analytics cookies — you may "
                             "withdraw it at any time, and it is as easy to withdraw as it was to give."),
        ("Portability", "Ask for the data you gave us in a machine-readable form."),
        ("Complain", "Complain to us, and to the Nigeria Data Protection Commission if you are not satisfied "
                     "with our response."),
    ]
    rights_html = "".join(f'<div><dt>{esc(t)}</dt><dd>{esc(b)}</dd></div>' for t, b in rights)

    return page_hero(
        title="Privacy policy",
        lede="How Synia Aid Foundation collects, uses and protects personal data, and how you exercise your "
             "rights under the Nigeria Data Protection Act 2023.",
        eyebrow_text="Legal",
        trail=[("Home", "/"), ("Privacy Policy", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        {DRAFT_MARK}

        <h2>Who we are</h2>
        <p>Synia Aid Foundation is the data controller for the personal data described in this policy. We are
           registered with the Corporate Affairs Commission of the Federal Republic of Nigeria as Incorporated
           Trustees, registration number {D.SITE["reg_number"]}. Our head office is
           {esc(D.SITE["address_one_line"])}.</p>
        <p>If you have any question about this policy or about how we handle your data, contact us at
           <a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a> or on
           <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a>.</p>

        <h2>What we collect, why, and for how long</h2>
        <p>We collect only what each form genuinely needs. If you think we are asking for something we do not
           need, tell us — we would rather remove a field than hold data without a reason.</p>
        {data_table}

        <h2>Children's data</h2>
        <p>This website is not directed at children and we do not knowingly collect personal data from children
           through it. Data about children in our programmes is collected offline, with the informed consent of
           a parent or carer, and is handled under our Safeguarding Policy. A child's full name is never
           published alongside their image on this site or anywhere else.</p>

        <h2>Who we share data with</h2>
        <p>We do not sell your personal data, and we do not share it for anyone else's marketing. We share it
           only with:</p>
        {bullets([
          "Our payment provider, which processes card and transfer payments on its own secure pages. Card "
          "details are never stored on this website.",
          "Our email platform, which sends the newsletter you asked for.",
          "Our website host and technical suppliers, who process data only on our written instructions.",
          "Regulators, law enforcement or other authorities, where we are legally required to do so, or where "
          "it is necessary to protect someone from harm.",
        ])}

        <h2>Where your data is held</h2>
        <p>Some of the services we use — hosting, email and payment processing — may store or process data
           outside Nigeria. Where that happens, we satisfy ourselves that an adequate level of protection is in
           place, in line with the cross-border transfer requirements of the Nigeria Data Protection Act 2023
           and the General Application and Implementation Directive 2025. You may ask us where your data is
           held at any time.</p>

        <h2>How we keep it safe</h2>
        {bullets([
          "The whole site runs over HTTPS, so data is encrypted in transit.",
          "Access to enquiry and donation records is restricted to the people who need it to do their job.",
          "Administrator accounts use strong authentication.",
          "Safeguarding records are held securely and separately from personnel and programme files.",
          "No card details are ever stored on this website.",
        ])}

        <h2>Your rights</h2>
        <p>Under the Nigeria Data Protection Act 2023 you have the following rights. To exercise any of them,
           email <a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a>. We will respond as soon as we can,
           and in any event within the period the Act requires.</p>
        <dl class="definition-list">{rights_html}</dl>

        <h2>Cookies</h2>
        <p>We use essential cookies to make the site work, and optional analytics cookies only if you accept
           them. Nothing non-essential is set before you choose. See our
           <a href="/cookies/">Cookie Policy</a>, where you can also change your choice.</p>

        <h2>Changes to this policy</h2>
        <p>If we change this policy we will update this page and change the version note at the top. Where the
           change is significant we will say so on the site.</p>
      </div>
      <aside>
        {photo("women-gathering", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card card--quiet">
          <h3>Exercise your rights</h3>
          <p class="small">Ask us for a copy of your data, ask us to correct it, or ask us to delete it.</p>
          <div class="btn-row mt-4">{btn("Contact us", "/contact/?subject=general", "primary")}</div>
        </div>
        <div class="card card--quiet mt-5">
          <h3>Related</h3>
          <ul class="linklist mt-4">
            <li><a href="/cookies/"><span>Cookie Policy</span>{icon("arrow-right", "", 18)}</a></li>
            <li><a href="/terms/"><span>Terms of Use</span>{icon("arrow-right", "", 18)}</a></li>
            <li><a href="/safeguarding/"><span>Safeguarding Statement</span>{icon("arrow-right", "", 18)}</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# COOKIES
# ===========================================================================

def cookies():
    tbl = table(
        ["Cookie or storage", "Type", "Purpose", "Set when"],
        [
            ["<strong>saf-consent</strong>", "Essential",
             "Remembers whether you accepted or declined optional cookies, so we do not ask you again.",
             "When you make a choice on the cookie banner"],
            ["<strong>Analytics</strong>", "Optional",
             "Helps us understand which pages are used and where people give up, so we can improve the site.",
             "Only if you accept optional cookies"],
        ])

    return page_hero(
        title="Cookie policy",
        lede="What we set, why, and how to change your mind at any time.",
        eyebrow_text="Legal",
        trail=[("Home", "/"), ("Cookie Policy", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="prose">
      {photo("children-community", "3x2", sizes="(min-width: 940px) 720px, 100vw", cls="mb-6",
             caption=photo_credit_line())}
      {DRAFT_MARK}
      <h2>Our approach</h2>
      <p>We set no non-essential cookie and run no analytics script until you have told us you are happy for us
         to. Declining is a genuine option and costs you nothing — the site works exactly the same either way.</p>

      <h2>What we use</h2>
      {tbl}

      <h2>Third-party content</h2>
      <p>The contact page embeds a map from Google Maps, which may set its own cookies when it loads. If you
         would rather it did not, use the plain link to Google Maps on that page instead, or view our address
         in text.</p>

      <h2>Change your choice</h2>
      <p>You can change your mind at any time.</p>
      <p><button class="btn btn--primary" type="button" data-cookie-reset>Review my cookie choice</button></p>
      <p>You can also delete cookies through your browser settings. Doing so will clear your choice, and we
         will ask you again on your next visit.</p>
    </div>
  </div>
</section>
'''


# ===========================================================================
# TERMS
# ===========================================================================

def terms():
    return page_hero(
        title="Terms of use",
        lede="The terms on which this website is made available.",
        eyebrow_text="Legal",
        trail=[("Home", "/"), ("Terms of Use", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="prose">
      {photo("classroom-desks", "3x2", sizes="(min-width: 940px) 720px, 100vw", cls="mb-6",
             caption=photo_credit_line())}
      {DRAFT_MARK}
      <h2>Who we are</h2>
      <p>This website is operated by Synia Aid Foundation, Incorporated Trustees registered with the Corporate
         Affairs Commission of the Federal Republic of Nigeria, registration number {D.SITE["reg_number"]},
         of {esc(D.SITE["address_one_line"])}.</p>

      <h2>Using this site</h2>
      <p>You may read, print and share the content of this site for personal, educational or non-commercial use,
         provided you credit Synia Aid Foundation and do not alter the material. You may not use the site in
         any way that is unlawful, that impairs its operation, or that misrepresents your relationship with the
         Foundation.</p>

      <h2>Accuracy of information</h2>
      <p>We take care that the information on this site is accurate and current. Programme status labels,
         figures and partner listings are reviewed as circumstances change. Where a figure is not yet verified
         we describe the work rather than quantify it. Nothing described on this site as <em>planned</em> or
         <em>in set-up</em> should be taken as currently operating.</p>

      <h2>Donations</h2>
      <p>Donations are processed by our payment provider on its own secure pages. A gift given for a specific
         purpose is honoured for that purpose. If a programme is oversubscribed or does not proceed, we will
         contact you before applying your gift elsewhere. Monthly gifts may be cancelled at any time without
         giving a reason.</p>

      <h2>Copyright</h2>
      <p>Unless stated otherwise, the content, design and code of this site are the property of Synia Aid
         Foundation. Partner names and logos remain the property of the partner concerned and are used with
         permission. Photography is published only where the people shown have consented, and consent may be
         withdrawn — if you appear in an image on this site and would like it removed, contact us and it will
         be taken down promptly.</p>

      <h2>Links to other sites</h2>
      <p>Where we link to another organisation's website we do so because it is useful. We are not responsible
         for the content of external sites.</p>

      <h2>Liability</h2>
      <p>This site is provided in good faith and for information. To the extent permitted by law, we do not
         accept liability for any loss arising from reliance on it. Nothing in these terms limits liability
         that cannot be limited by law.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of the Federal Republic of Nigeria.</p>

      <h2>Contact</h2>
      <p><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a> ·
         <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a></p>
    </div>
  </div>
</section>
'''


# ===========================================================================
# ACCESSIBILITY
# ===========================================================================

def accessibility():
    return page_hero(
        title="Accessibility statement",
        lede="We work with people with disabilities. Our website should not exclude them.",
        eyebrow_text="Legal",
        trail=[("Home", "/"), ("Accessibility", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="grid grid--sidebar">
      <div class="prose">
        {photo("wheelchair-crossing", "3x2", sizes="(min-width: 940px) 720px, 100vw", cls="mb-6", eager=True,
               caption="We work with people with disabilities; our site should not exclude them. "
                       + photo_credit_line())}
        <h2>The standard we aim for</h2>
        <p>This site is built to meet <strong>WCAG 2.1 Level AA</strong>. That means, among other things:</p>
        {bullets([
          "Text and interface colours meet the required contrast ratios against their backgrounds.",
          "Every meaningful image carries alternative text, and decorative images are hidden from screen "
          "readers.",
          "The whole site can be operated with a keyboard alone, and the focus indicator is always visible.",
          "Every form field has a visible, associated label, and errors are announced rather than shown by "
          "colour alone.",
          "Headings follow a sensible order, so the page can be navigated by structure.",
          "Text can be resized to 200% without loss of content or function, and the layout reflows on a narrow "
          "screen without horizontal scrolling.",
          "Animation is reduced automatically if your device asks for reduced motion.",
          "There is a skip link to the main content at the top of every page.",
        ])}

        <h2>Designed for a real connection</h2>
        <p>We design for a first-time visitor on a mid-range Android phone using mobile data. The site uses no
           web fonts, no icon fonts and no third-party scripts, because our visitors pay for their data and
           page weight is a real cost to them, not a metric.</p>

        <h2>Known limitations</h2>
        {bullets([
          "The map embedded on the contact page is provided by Google and its accessibility is outside our "
          "control. Our full address is given in text on the same page.",
          "Documents published as PDFs may not all be fully tagged for screen readers. If you need any "
          "document in an accessible format, ask us and we will provide it.",
        ])}

        <h2>Tell us if something does not work</h2>
        <p>If you have difficulty using any part of this site, please tell us what happened and what you were
           trying to do. We will fix it, and in the meantime we will give you the information another way.</p>
        <p><a href="mailto:{D.SITE["email"]}">{D.SITE["email"]}</a> ·
           <a href="tel:{D.SITE["phone_href"]}">{D.SITE["phone"]}</a></p>
      </div>
      <aside>
        {photo("elder-seated", "4x3", sizes="(min-width: 940px) 336px, 100vw", cls="mb-5", max_width=640)}
        <div class="card card--quiet">
          <h3>Need something another way?</h3>
          <p class="small">We can send any document by email, read it to you over the phone, or provide it in
            large print.</p>
          <div class="btn-row mt-4">{btn("Contact us", "/contact/?subject=general", "primary")}</div>
        </div>
      </aside>
    </div>
  </div>
</section>
'''


# ===========================================================================
# SEARCH
# ===========================================================================

def search():
    return page_hero(
        title="Search",
        lede="Search across our pages, programmes, stories, news and documents.",
        eyebrow_text="Find something",
        trail=[("Home", "/"), ("Search", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container" data-search>
    <form class="form" data-search-form role="search" style="max-width:44rem">
      <div class="newsletter__row">
        <div class="field">
          <label class="field__label" for="q">What are you looking for?</label>
          <input class="field__input" type="search" id="q" name="q" data-search-input
                 placeholder="e.g. shelter, safeguarding, Keffi, annual report" autocomplete="off">
        </div>
        <button class="btn btn--primary" type="submit">Search{icon("search", "btn__icon", 20)}</button>
      </div>
    </form>

    <p class="results-count mt-6" data-search-status role="status">Type a word or two to search the site.</p>
    <ul class="grid grid--2" style="list-style:none;padding:0" data-search-results></ul>

    <noscript>
      <div class="empty-state mt-6">
        <p>Search needs JavaScript. Please use the <a href="/sitemap/">sitemap</a> to find what you need.</p>
      </div>
    </noscript>
  </div>
</section>

<section class="section section--tight section--surface">
  <div class="container">
    <div class="photo-band">
      {photo("classroom-writing", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("women-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-outside", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("elder-smiling", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <p class="small text-muted mt-4">{photo_credit_line()}</p>
  </div>
</section>
'''


# ===========================================================================
# SITEMAP PAGE
# ===========================================================================

def sitemap_page(groups):
    blocks = []
    for heading, links in groups:
        items = "".join(f'<li><a href="{u}">{esc(l)}</a></li>' for l, u in links)
        blocks.append(f'<div class="card"><h2 class="h3" style="font-size:var(--step-1)">{esc(heading)}</h2>'
                      f'<ul style="margin-top:.75rem">{items}</ul></div>')
    return page_hero(
        title="Sitemap",
        lede="Every page on this website.",
        eyebrow_text="Navigation",
        trail=[("Home", "/"), ("Sitemap", None)],
    ) + f'''
<section class="section section--tight">
  <div class="container">
    <div class="photo-band mb-7">
      {photo("classroom-lesson", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("woman-portrait", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("children-yard", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
      {photo("classroom-boy-yellow", "4x3", sizes="(min-width: 700px) 25vw, 50vw", max_width=640)}
    </div>
    <div class="grid grid--3">{"".join(blocks)}</div>
  </div>
</section>
'''


# ===========================================================================
# 404
# ===========================================================================

def not_found():
    return f'''
<section class="page-hero">
  <div class="container">
    <div class="page-hero__inner">
      <p class="eyebrow">Error 404</p>
      <h1>We cannot find that page</h1>
      <p class="lede">The link may be out of date, or the page may have moved. Here are the places people
        usually want.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <h2 class="visually-hidden">Where to go next</h2>
    {photo("children-laughing", "21x9", sizes="100vw", cls="mb-6", eager=True)}
    <div class="grid grid--3">
      <article class="card card--link">
        <h3><a class="stretched" href="/what-we-do/">What we do</a></h3>
        <p>Three pillars and twelve programmes, each with its current status.</p>
      </article>
      <article class="card card--link">
        <h3><a class="stretched" href="/donate/">Donate</a></h3>
        <p>One-off or monthly, from ₦5,000 upward.</p>
      </article>
      <article class="card card--link">
        <h3><a class="stretched" href="/accountability/">Accountability</a></h3>
        <p>Governance, policies, reports and how we measure impact.</p>
      </article>
    </div>
    <div class="btn-row mt-6">
      {btn("Search the site", "/search/", "primary", "search")}
      {btn("See the sitemap", "/sitemap/", "ghost", None)}
      {btn("Contact us", "/contact/", "ghost", None)}
    </div>
  </div>
</section>
'''
