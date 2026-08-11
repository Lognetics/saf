# Response to the Website Development Brief

Answers to Section 11 of the brief, and a line-by-line record of how each
requirement in Sections 03–09 has been met.

---

## Part 1 — Questions for the developer (Section 11)

### 1. What platform do you recommend, and why that one?

**A generated static site — which is what has been built — with a lightweight
CMS layer added at handover.**

The reasoning, given an organisation of this size and technical capability:

- The brief's hardest constraint is a first-time visitor on a mid-range Android
  phone on mobile data. A static site is the fastest thing that can be served:
  no database query, no server rendering, no plugin stack. It is roughly ten
  times lighter than a typical WordPress theme doing the same job.
- The second hardest constraint is honesty at scale. Programme status labels
  must be correct in twelve places at once. Here they live in one file and
  propagate — a class of error is designed out rather than policed.
- Security and maintenance: there is no login surface, no plugin to patch, and
  no known-vulnerability treadmill. For a small team, that is the difference
  between a site that stays safe and one that quietly does not.
- Hosting cost is negligible and West African performance is good via a CDN.

**The honest trade-off:** as delivered, content is edited in a structured text
file rather than a visual editor. The brief requires the team to publish news
weekly without coming back to the developer, and to assume the editor is
comfortable with Microsoft Word and nothing more. So this needs one of:

| Option | What it gives | Rough annual cost |
|---|---|---|
| **Recommended — attach a Git-based CMS** (Decap/Netlify CMS, Sveltia, or Pages CMS) to this exact build | Browser login, form-based editing of news, stories, programmes, partners and team, with roles for Administrator / Editor / Contributor. The published site stays static and fast | £0–£150 |
| Move to WordPress | Familiar admin, huge plugin ecosystem | £250–£500, plus patching forever, plus a slower site |
| Keep as-is | Fastest, cheapest, safest | £0, but every content change is a developer job — this fails the brief |

The Git-based CMS route is the one to take. It satisfies "our team is capable
but not technical" without giving up the performance the brief demands.

### 2. Which payment gateway, at what cost, and what will it require?

**Paystack**, with Flutterwave as the alternative if the Foundation wants
multi-currency settlement.

- Both are established for Nigerian organisations and support cards, bank
  transfer, USSD and mobile money, settling in Naira. **Stripe does not operate
  for Nigerian entities and has not been scoped for.**
- Paystack is the stronger recommendation for a first gateway: simpler
  onboarding, better documentation, and a subscriptions API that handles
  recurring giving on the gateway side rather than in site code — which matters,
  because a recurring donation that depends on your website staying up is a
  fragile recurring donation.
- **Transaction fees change; confirm current rates directly with the provider
  before quoting them to the Board.** Nigerian card and transfer fees are
  typically percentage-based with a cap, and international card fees are
  materially higher. Ask specifically about the cap on local transactions and
  the rate on foreign cards, since the diaspora segment matters here.
- **Documentation the gateway will ask for:** CAC certificate of incorporation
  and CAC/IT number; the constitution or trust deed; a bank account in the
  Foundation's registered name; directors'/trustees' identification and BVN;
  proof of address; and the website itself being live with visible contact
  details, a refund position and a privacy policy — all of which this site
  already has.
- Approval typically takes days rather than weeks once documents are complete.
  **Start this now**, in parallel with content, because it is the single item
  most likely to delay launch.

**Recurring donations should be handled by the gateway, not the site.** The
donor must be able to cancel without contacting us, and the mandate must survive
any change of website.

### 3. Realistic timeline from content handover to launch

The build is done. What remains is dependencies, not development:

| Week | Work |
|---|---|
| 1 | Gateway application submitted. Domain, hosting and email (SPF, DKIM, DMARC) set up. Partner permission emails sent — the wording is already drafted in Section 07 of the Partner List |
| 2 | CMS layer attached and content models mapped. Legal adviser reviews privacy, cookie and terms |
| 3 | Gateway connected; test donations, one-off and recurring. Forms connected and inbox routing tested. Analytics with goals |
| 4 | Photography and leadership images loaded as consents come in. Testing on real devices. Admin training, recorded. Redirects confirmed against the current site. Launch |

**Four weeks is realistic** provided the gateway application goes in during week
one. If it slips, everything slips — the donation flow cannot be signed off
without a real test transaction landing in the account.

### 4. Annual running costs

| Item | Indicative annual cost |
|---|---|
| Domain (.org) | £10–£20 |
| Matching domain, if acquired and redirected | £10–£20 |
| Static hosting with CDN | £0 on a free tier; £15–£20/month if a paid tier is wanted for support and analytics |
| TLS certificate | £0 — included and auto-renewed |
| Email on the Foundation's domain | £4–£6 per mailbox per month |
| Email/newsletter platform | £0 up to a few hundred subscribers; £15–£30/month beyond |
| Git-based CMS | £0–£150 |
| Uptime monitoring | £0 on a free tier |
| Payment gateway | No standing fee — transaction-based |

**Realistic total: roughly £150–£450 a year**, driven mainly by how many
mailboxes are needed and whether a paid hosting tier is chosen. This is an order
of magnitude below a typical managed WordPress arrangement, and it is a direct
consequence of the platform choice.

### 5. Maintenance and support after launch

What a support arrangement for this site should cover, and what it should not:

- **Included:** dependency-free stack means no plugin patching; content model
  changes; new page types; bug fixes; annual accessibility re-check; help when a
  gateway or email provider changes an API.
- **Not included unless agreed:** copywriting, photography, ongoing content
  entry, or campaign page design.
- Because there is no CMS core or plugin ecosystem to patch, the ongoing burden
  is genuinely low. Budget for a defined number of support hours rather than a
  monthly retainer sized for a WordPress site.

### 6. Where will data and backups be physically hosted?

This matters under the Nigeria Data Protection Act 2023 and the General
Application and Implementation Directive 2025, and the brief is right to ask.

- **The website itself holds no personal data.** It is static files. There is no
  database and no admin login to compromise.
- Personal data lives in three places, and each must be recorded in the
  Foundation's data map: the **payment gateway** (Paystack/Flutterwave, Nigerian
  companies, data in-country), the **form/email platform**, and the **email
  provider**.
- The choice of form and email platform is therefore a data-protection decision,
  not just a convenience one. Prefer providers that offer an EU or Nigerian
  region and will sign a data processing agreement.
- **Recommendation:** keep donation data in the Nigerian gateway; choose a form
  handler that stores submissions in an EU region with a DPA in place; document
  both in the privacy policy, which already carries the cross-border transfer
  disclosure the Act requires.
- Backups: the site is fully reproducible from source, so "backup" means version
  control plus a copy of the content file. Uploaded documents and images should
  additionally be backed up daily off the web server, with a restore tested
  before launch.

### 7. Anything in the brief we would advise against, or achieve a better way?

Four things, offered as the brief invited.

1. **Do not launch the Synia Scholars Fund as a donation destination.** The
   Foundation's own governance position is that the Fund will not be promoted
   until the agreement, published criteria, panel and ring-fenced accounting
   exist. It is on the site, labelled *In set-up*, with that reasoning shown.
   Resist any pressure to add a "Give to the Scholars Fund" button before the
   architecture is real — it would contradict the credibility the rest of the
   site is built on.

2. **Reconsider "10+ programmes and campaigns delivered" as a home page
   figure.** It is accurate, but "10+" reads as a rounding-up convention on a
   site whose whole argument is that it does not round up. A dated, specific
   figure — or naming the three flagship programmes instead — would be stronger.
   It is one line in `data.py`.

3. **The site search is built, but the sitemap page does more work.** On a site
   of this size, most visitors navigate rather than search. Both exist; do not
   spend money improving search before the content library grows.

4. **Treat the "How we measure impact" page as a fundraising asset, not a
   compliance page.** The brief already says not to treat it as filler. Going
   further: it is arguably the most persuasive page on the site for an
   institutional funder, because publishing a 52/100 self-assessment and a list
   of what has not yet been done is the kind of thing only a credible
   organisation does. It has been designed accordingly.

---

## Part 2 — Requirements coverage

### Section 03 — Sitemap and navigation

| Requirement | Status |
|---|---|
| Full sitemap as specified | Built — 55 pages |
| Main menu of exactly seven items | Built — About Us · What We Do · Our Impact · Get Involved · Accountability · News · Contact |
| Persistent Donate button in header, on every page including mobile — MUST | Built, visually distinct, orange with navy text (AA contrast) |
| Programme pages within two clicks of home | Built — home → pillar card → programme, and home → What We Do → programme |
| Footer with contact, registration number, socials, four Get Involved routes, utility pages | Built |
| Nothing important lives only in a dropdown | Built — every section landing page repeats its children as cards or links; the mobile menu renders all children inline with tap-friendly disclosure buttons |

### Section 04 — Page-by-page

All MUST and SHOULD pages built. Highlights:

| Page | Status |
|---|---|
| Home — hero, three pillar cards, featured story, reach strip, latest news ×3, partners, newsletter, donate CTA, **no carousel** | Built |
| Who We Are — founding story, vision, mission, philosophy, six-plus core values (all eight are published), at-a-glance facts | Built |
| Our Story — extendable timeline from 2018 | Built, 13 milestones |
| Leadership & Governance — photo, name, role, biography, governance statement, policy links | Built; photographs pending, initials avatar used meanwhile |
| Partners — name, logo where permitted, one line, partner CTA | Built, grouped by pillar in the specified order, Education first |
| What We Do — three pillars, three mottos, cross-cutting programmes | Built |
| Pillar pages ×3 | Built |
| Programme pages ×12 — consistent template: name, public campaign name, status, what it does, who it is for, what success looks like, where it operates, delivery partners, related stories, way to support | Built |
| Who We Serve — beneficiary groups, displacement context **with sources cited** | Built, IOM DTM cited in full |
| Stories — filterable by pillar and format, ready for video | Built |
| Projects — year, location, partner, outcome, filterable | Built |
| Donate | Built — see Section 05 below |
| Partner With Us / Volunteer / Ambassador | Built, with vetting and code-of-conduct statement on the volunteer page |
| Accountability landing | Built |
| Governance & Policies — downloadable PDFs, registration details, extendable | Built, five policies published |
| Reports & Publications — document library | Built, three publications plus policies; empty sections built and labelled rather than omitted |
| How We Measure Impact | Built, treated as a credibility asset |
| News — reverse-chronological, categories, featured image, share buttons | Built |
| Contact — address, both phones with the 24/7 hotline marked, email, hours, map, subject routing, socials | Built |
| Complaints — reachable from every footer | Built |
| **Programme status labels, controlled centrally** — CRITICAL | Built, and enforced structurally |

### Section 05 — Donations and functionality

| Requirement | Priority | Status |
|---|---|---|
| Nigerian gateway (Paystack/Flutterwave), not Stripe | MUST | Recommended and scoped; one config value to connect |
| Recurring donations, donor-cancellable | MUST | Built into the flow; gateway-side subscription recommended |
| Preset tiers from ₦5,000 with a free-entry field, each labelled with what it funds | MUST | Built, five tiers plus custom, ₦5,000 minimum enforced |
| International giving, currency shown | MUST | Built into the flow and FAQs |
| Designated giving recorded against the donation | SHOULD | Built — pillar, programme or where most needed, and deep-linked from every programme page |
| Automatic receipt with name, registration number, amount | MUST | Specified in the flow and stated to the donor |
| Thank-you page that says what happens next and invites the newsletter | MUST | Built |
| Bank transfer details with a reference convention | MUST | Built; account details are marked placeholders pending the Foundation |
| Anonymous giving | SHOULD | Built |
| Gateway fee option | LATER | Not built — trivial to add |
| Campaign pages with target and progress | LATER | Not built — the content model is ready to extend |
| Admin visibility, export, reconciliation | MUST | Gateway dashboard plus the reference convention |
| Enquiry forms with spam protection, routing, acknowledgement, stored submissions | MUST | Built with honeypot protection and per-form subject routing |
| Newsletter, double opt-in, unsubscribe | MUST | Built, with a separate unticked consent |
| Document library | MUST | Built |
| Video embedding (YouTube/Vimeo, not self-hosted) | MUST | Story template ready |
| Photo galleries, lazy-loaded | SHOULD | Built — galleries and photo bands, all lazy-loaded, responsive WebP with JPEG fallback, EXIF stripped. A lightbox is not built; it adds script weight for little gain on a phone, and can be added later |
| Site search | SHOULD | Built, client-side, no third-party service |
| Social links — Facebook, LinkedIn, Instagram, **no X/Twitter** | MUST | Built, each handle correct per platform |
| MindCheck route from the wellbeing programme page | SHOULD | Built |
| Volunteer portal | LATER | Not built |
| Multi-language | LATER | Not built; no restructuring needed to add it |

### Section 07 — Design and brand

Brand colours from the brief and the logo colour sheet are reconciled in one
token block. The logo's own `#026DB3 / #1A89CA / #F18A1B` are used as the brand
blues and the call-to-action orange; the brief's navy `#0F2A47`, deep blue
`#123A63` and teal `#40B89F` carry surfaces, headings and the third accent.
The brief's `#F28A1B` and the logo sheet's `#F18A1B` differ by one hex digit and
are visually identical — the logo value is used so the site matches the mark.

Tone follows the brief: warm, plain, direct; "student", "family" or a name
rather than "beneficiary"; specific over general; and no claim of working alone
where a partner delivered the work.

### Section 08 — Technical

Every MUST met and verified. Mobile-first, no external requests bar the contact
map, WCAG 2.1 AA verified, HTTPS and security headers pre-written, clean URLs,
editable titles and meta descriptions, XML sitemap, NGO structured data, correct
social sharing previews, and a draft redirect map.

### Section 09 — Legal and data protection

Privacy policy with lawful bases, retention and cross-border disclosure; cookie
consent that genuinely blocks analytics until accepted, with a real decline
option and a way to change your mind; unticked, unbundled marketing opt-ins;
data minimisation applied to every form; no card details ever touching the site;
a working erasure route; terms of use; a safeguarding statement; and an
accessibility statement.

**All three legal pages carry a visible marker that they are pending review by
the Foundation's Nigerian-qualified legal adviser**, exactly as the brief
requires. Remove the marker after review — it is one constant in
`saf/pages_utility.py`.
