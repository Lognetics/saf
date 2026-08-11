# Content notes, gaps and source discrepancies

Everything on this website comes from the Foundation's own documents. Nothing
was invented to fill a space. Where a fact was not supplied, the field is either
left out or carries a visible placeholder rather than a plausible-sounding
guess.

This file records what was decided, what is still owed, and three places where
the source documents disagree with each other.

---

## 1. Three discrepancies in the source documents

### 1.1 Eight partners or nine?

The Corporate Profile "at a glance" page reports **8 named delivery partners**.
The Partner List for Publication lists **nine**, states "Nine partners in total",
and declares itself the source of record: *"If the two ever disagree, the
Corporate Profile should be corrected to match a reissued version of this
document."*

**Decision:** the site publishes **9**. The Corporate Profile's "8" appears to
be stale.
**Action for the Foundation:** confirm 9, and correct the figure when the
Corporate Profile is next reissued.

### 1.2 Two spellings of the HR Adviser's name

The Corporate Profile Section 18 gives *Chinasa Ijeruh Fabian*. The Leadership
Biographies document gives *Chinasa Fabian-Ijeruh*, twice.

**Decision:** the site uses **Chinasa Fabian-Ijeruh**, following the dedicated
biographies document.
**Action:** confirm the correct form and align both documents.

### 1.3 The Programmes Structure Guide is marked "internal"

The footer of `SAF Our Programmes Structure Guide.pdf` carries the line
**"Internal — not for external circulation"**.

The Website Development Brief, which is the later document and is addressed to
the developer, explicitly lists it for publication: *Reports & Publications —
"Annual reports, audited accounts, the Company Profile, the programme structure
guide."*

**Decision:** published, following the explicit instruction in the brief. The
"internal" line also sits next to visible template artefacts (`middot;`) in the
same footer, which suggests it is a left-over rather than a live restriction.

**Action for the Foundation: confirm this before launch.** If the guide should
not be public, remove its entry from `PUBLICATIONS` in `saf/data.py`, delete the
link on `/what-we-do/`, and delete the file from `source-documents/` and
`dist/assets/documents/`. Note that the repository is a permanent record — if
the repository is public, removing the file later does not remove it from the
git history.

### 1.4 Name and domain do not match

The Foundation is *Synia Aid Foundation*; the domain is *syniafoundation.org*.
The brief asks whether acquiring the matching domain is worthwhile.

**Recommendation:** yes — register `syniaaidfoundation.org` and 301-redirect it
to the primary domain. It is inexpensive, it protects the name, and it prevents
a supporter who types the organisation's actual name from reaching nothing. Keep
`syniafoundation.org` as the canonical address so existing links and printed
material stay valid. See `BRIEF-RESPONSE.md`.

Two further inconsistencies named in the brief are already resolved in the
build: only **Hope for the Common Man** is used as a tagline anywhere on the
site, and the three social handles are each linked to the correct platform
(`@syniaaidfoundation` on Facebook and LinkedIn, `@synia_aid_foundation` on
Instagram). There is no X/Twitter icon.

---

## 2. What the Foundation still owes before launch

| # | Item | Why it is blocking | Where it lands |
|---|---|---|---|
| 1 | **Bank account details** for donations | Shown as marked placeholders on the donate page and cannot go live as they are | `saf/data.py` → `BANK_TRANSFER` |
| 2 | **Payment gateway account** (Paystack or Flutterwave) | The donate flow is built but not connected | `assets/js/config.js` → `donateEndpoint` |
| 3 | **Form endpoint / email platform** | Forms currently fall back to a pre-filled email | `assets/js/config.js` → `formEndpoint` |
| 4 | **Partner permissions** — name and logo, for all nine | No logo is published without written permission. Section 07 of the Partner List has the request wording ready to send | `PARTNERS` → `logo_permission` |
| 5 | **Leadership photographs** | Cards currently use initials in a brand-coloured avatar, which looks deliberate rather than missing | `BOARD`, `EXECUTIVE` |
| 6 | **Written consent confirmation** for the 21 published photographs | Images are live; the consent record is not yet held by the developer. See section 3 | `PHOTOS` in `saf/data.py` |
| 7 | **Legal review** of privacy, cookie and terms pages | Each carries a visible "pending legal review" marker until this is done | `pages_utility.py` → `DRAFT_MARK` |
| 8 | **Testimonial text and consents** | See section 4 below | not yet built |
| 9 | **Old-URL map** from the current site | A draft redirect map is in `dist/_redirects`; confirm against analytics and Search Console | `build.py` |
| 10 | **Safeguarding Focal Point name** and the nominated independent Trustee | The Safeguarding Policy PDF has these fields blank. The site gives the routes but not the names | Policy PDF, then `/complaints/` |

---

## 3. Photography

**24 photographs were supplied by the Foundation** through SageView Productions,
its contracted media agency. 21 are published; 3 are withheld (see 3.2).

### 3.1 How they are handled

| Rule (from the brief and the Safeguarding Policy) | How it is implemented |
|---|---|
| No location data embedded in a published image | Every derivative is written with EXIF stripped at build time. Verified: 140 published JPEGs, 0 carrying EXIF |
| A child's full name is never published beside their image | No name appears in any alt text, caption or filename |
| Real people, dignified, natural light; never stock imagery of poverty | Every image is the Foundation's own. None was sourced elsewhere |
| People shown as capable partners, not recipients | Applied as the test for what to publish and what to withhold |
| Images must come down promptly if consent is withdrawn | A removal request line appears in the site footer and beside photo credits; removing an image is one line in `saf/data.py` |

**Alt text describes only what is visible.** No photograph is captioned as being
from a named camp, school, state or event — a caption is a factual claim, and
the Foundation did not supply that information with the files. If it can confirm
where and when each was taken, the captions can be made specific and should be.

Photographs are assigned to pages through four mappings in `saf/data.py`
(`PROGRAMME_PHOTOS`, `PILLAR_PHOTOS`, `NEWS_PHOTOS`, `STORY_PHOTOS`), so an
image can be re-pointed without touching any programme content.

Each entry also carries a crop anchor, so a portrait frame placed in a landscape
slot keeps the subject's face instead of trimming the top of their head.

### 3.2 Three photographs deliberately not published

| File | Why it is withheld |
|---|---|
| `IMG_4016.JPG` | A woman and two small children sitting on bare ground. Composed with care, but it reads as destitution rather than agency, and a small child is identifiable |
| `IMG_4017.JPG` | A man sitting at a roadside with his belongings in sacks. Same reasoning |
| `IMG_4018.JPG` | An older man on a roadside kerb. Dignified, but it shows the subject at his lowest point — the smiling portraits of older men are used instead |

The Foundation's own rule is that people are shown as capable partners and that
no image may show a person in distress. These three sit on the wrong side of
that line in our judgement. **This is an editorial call, and it is the
Foundation's to overturn** — the files are in `photos-src/` and publishing one
means moving its entry from `PHOTOS_WITHHELD` into `PHOTOS`.

### 3.3 What the Foundation still owes on photography

1. **Written consent confirmation for each published image**, and for every
   child shown, written caregiver consent. The brief states the Foundation will
   confirm consent for every image it supplies; that confirmation should be
   recorded against each entry before launch.
2. **Where and when each photograph was taken**, so captions can be specific.
3. **Leadership portraits** — none of the supplied images are staff portraits,
   so the Board and executive cards still use initials in a brand-coloured
   avatar.
4. **Shelter, WASH and enterprise imagery** — the library is strong on children,
   classrooms, women and older people, and has nothing showing shelter work,
   water points or trading. Those programme pages currently carry community
   photographs whose alt text describes exactly what is in them, which is honest
   but not illustrative.

## 4. Testimonials — deliberately not published

The Partner List records four testimonials on the current home page and asks
that they be retained, subject to two checks: written consent to quote, and
confirmation that the wording is still current.

**The quote text itself was not supplied in any handover document.** Publishing
them would have meant writing words and attributing them to real organisations
and a named individual. That is not something to guess at, so the section is not
built.

When the Foundation supplies the wording and the consents, the component should
carry fields for quote, name, organisation, role and an optional photograph —
and **Sir Paul Utebor must sit in a separate "Voices" or "Supporters" block**,
not among the partner organisations, because he is an individual endorsement
rather than an institutional partnership.

## 5. News and stories — where the content came from

The site needs a working news section at launch, and no news copy was supplied.

The seven posts in `NEWS` and the two written pieces in `STORIES` were written
**only** from events already documented in the Corporate Profile's milestone
record and track-record table — the MindCheck launch (21 January 2026), the
Community Mental Health Road Walk (19 January 2026), the Leadership Development
Summit, Love on the Street (20 May 2026), the Durumi assessment and classroom
furniture project, Pad A Girl at ECWA School (22 May 2025), and the July 2026
strategic review.

They contain **no invented quotes, no invented numbers and no invented names**.
Where the source gives only a year, the post displays only the year. The
Foundation should review, expand and correct them, and treat them as a starting
library rather than finished copy.

## 6. Content written for the site, and what it is based on

A few pages required copy that does not exist verbatim in any document. In each
case it is a restatement of documented facts, and it should be reviewed:

| Page | What was written | Based on |
|---|---|---|
| Donate — amount tiers | What ₦5,000 / ₦10,000 / ₦25,000 / ₦50,000 / ₦100,000 typically covers | The standard packages described for Train a Child, Safe Shelter and Enterprise Development. **These are not audited unit costs**, and the page says so |
| Donate — FAQs | Receipts, cancelling a monthly gift, designation, anonymity, card safety, international giving, financial controls | Brief Section 05 and Corporate Profile Section 20 |
| Programme pages — "Where it operates" | Location line for each of the twelve programmes | Corporate Profile Section 13 footprint. **Per-programme locations need Foundation confirmation** |
| Privacy policy | Data table, lawful bases, retention periods, rights | Brief Section 09, NDPA 2023, GAID 2025. **Retention periods are proposals** — confirm with the legal adviser |
| Volunteer roles | Four role descriptions | The four programme areas and the vetting requirements in the Safeguarding Policy. Confirm these are the roles actually wanted |
| Accessibility statement | Standard met, known limitations | What the build actually does |

## 7. Deliberate omissions

- **No prospective partner appears anywhere on the site as a partner.** NCFRMI,
  UN agencies, state authorities, corporate foundations and diaspora networks
  appear once, on the Partners page, under the heading "Partnerships we are
  pursuing", with the explicit line that these are not current relationships.
- **SageView Production Ltd** does not appear. It is a contracted supplier, not
  a programme partner. If the Foundation wishes to credit them, the right place
  is a site credit line.
- **The Synia Scholars Fund is not promoted for donations.** It is labelled
  *In set-up*, and its page explains that it will not be promoted externally
  until the fund agreement, published criteria, selection panel and ring-fenced
  accounting exist.
- **No aggregate beneficiary numbers are claimed anywhere** — no "10,000 lives
  changed". The Foundation's own position is that its reporting has captured
  outputs rather than outcomes, and the site says so on three separate pages.

## 8. Programme statuses as built

Controlled from one place (`saf/data.py` → `PROGRAMMES` → `status`). Correct as
at the July 2026 documents:

| Status | Count | Programmes |
|---|---|---|
| Running now | 3 | Learning Access & Retention (Train a Child), Enterprise Development, Safe Shelter |
| In set-up | 1 | Synia Scholars Fund |
| Planned | 8 | Youth Skills & Employability; Savings & Financial Inclusion; Women's Economic Empowerment; WASH; Emergency Response & Household Recovery; Protection & Rights; Community Wellbeing & Mental Health (MindCheck); Durable Solutions & Resettlement Support |

Community Wellbeing & Mental Health additionally carries the qualifier
"Formalising work already under way", exactly as the source documents describe
it.

**Change one value and every appearance updates** — programme page, pillar page,
portfolio table, home page counter, the status boards on What We Do and
Accountability, and the search index.
