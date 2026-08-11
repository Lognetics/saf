# Synia Aid Foundation — website

A complete, production-ready website for Synia Aid Foundation, built to the
*Website Development Brief v1.0 (July 2026)* and populated entirely from the
Foundation's own documents.

**Tagline used throughout:** Hope for the Common Man
**Registration shown site-wide:** CAC/IT/NO 121882

---

## 1. What is here

```
website/
├── build.py              Static site generator — run this to produce the site
├── saf/
│   ├── data.py           ALL CONTENT. Every figure, programme, partner, policy.
│   ├── layout.py         Page shell, header, footer, navigation, icons
│   ├── components.py     Cards, heroes, status chips, CTA bands
│   ├── pages_home_about.py
│   ├── pages_programmes.py
│   ├── pages_involve.py
│   ├── pages_accountability.py
│   └── pages_utility.py
├── assets/
│   ├── css/site.css      One stylesheet. Design system + all components.
│   ├── js/config.js      ← the only file you edit to connect live services
│   ├── js/site.js        Navigation, donate widget, cookie consent, search, forms
│   └── img/              Logo derivatives, favicons, social sharing card
├── photos-src/           The 24 original photographs from the Foundation
├── source-documents/     The 8 PDFs the site publishes for download
├── vercel.json           Deployment config: output dir, headers, redirects
├── dist/                 GENERATED. This is what you upload. Never edit by hand.
├── CONTENT-NOTES.md      Every gap, assumption and source discrepancy — read this
└── BRIEF-RESPONSE.md     Answers to Section 11 of the brief, and a requirements matrix
```

## 2. Build and preview

Requires Python 3.7+ only. No npm, no build toolchain, no database.

```bash
cd website
python3 build.py            # writes ./dist
python3 build.py --serve    # writes ./dist and serves it on http://localhost:8080
```

The build prints a summary and warns loudly if any source PDF is missing.

## 3. Deploy

### Vercel (configured and ready)

`vercel.json` is committed, and so is the built `dist/` folder. Import the
repository at vercel.com and accept the defaults:

| Setting | Value | Why |
|---|---|---|
| Framework preset | **Other** | There is no JS framework here |
| Build command | **leave empty** | `dist/` is committed, so Vercel has nothing to build |
| Output directory | **dist** | Already set in `vercel.json` |
| Install command | **leave empty** | No dependencies to install |

`vercel.json` also carries the security headers, the year-long cache policy for
`/assets/*`, and the redirect map from the old site's URLs. Vercel serves
`404.html` automatically and issues and renews the TLS certificate itself.

**After every content change:** run `python3 build.py`, then commit the changed
files in `dist/`. Vercel redeploys on push. The build is committed rather than
run on Vercel deliberately — it needs Python and Pillow to regenerate the
photographs, and a deploy should never be able to fail because a build image
changed underneath it.

### Any other host

`dist/` is a plain static site — upload it anywhere. `_headers` and `_redirects`
are written for Netlify and Cloudflare Pages. Point the error handler at
`/404.html` and force HTTPS.

`robots.txt`, `sitemap.xml`, `site.webmanifest`, `news/feed.xml` and
`search-index.json` are all generated automatically.

### Domain

Once the site is live on a Vercel URL, add `syniafoundation.org` in the project's
Domains settings and point the DNS at Vercel. Set one canonical host and redirect
the other (`www` → apex or apex → `www`), then update `base_url` in
`saf/data.py` if the canonical host changes, so canonical tags, the sitemap and
the social sharing tags all agree.

## 4. Connecting the live services

Everything is wired and waiting. Open **`assets/js/config.js`** and fill in three
values. Until you do, the site degrades gracefully rather than breaking:

| Setting | What it does | Behaviour while blank |
|---|---|---|
| `formEndpoint` | POST target for contact, partnership, volunteer, ambassador and newsletter forms | Forms validate, then open a pre-filled email to `info@syniafoundation.org` — no enquiry is lost |
| `donateEndpoint` | Paystack or Flutterwave checkout URL | The donate button sends the donor to the bank-transfer panel with a clear explanation. It never pretends a payment succeeded |
| `analyticsSrc` | Privacy-respecting analytics script | No analytics loads at all |

Analytics is **only ever** loaded after the visitor accepts optional cookies.
Never add an analytics tag directly to the page — it would breach the consent
requirement in Section 09 of the brief.

## 5. Editing content

All content lives in **`saf/data.py`**, organised in labelled sections. Edit,
re-run `python3 build.py`, and the change propagates everywhere it appears.

Common jobs:

| Task | Where |
|---|---|
| Change a programme's status label | `PROGRAMMES` → `"status": "running" \| "setup" \| "planned"` |
| Add or edit a news post | `NEWS` |
| Add a story (film, photo essay, written) | `STORIES` |
| Add a partner | `PARTNERS` — see the permission rule below |
| Add or replace a photograph | drop the file in `photos-src/`, add an entry to `PHOTOS` with alt text, then point a page at it via `PROGRAMME_PHOTOS` / `PILLAR_PHOTOS` / `NEWS_PHOTOS` / `STORY_PHOTOS` |
| Take a photograph down | delete or comment out its entry in `PHOTOS` and rebuild |
| Publish a partner logo | set `"logo_permission": True` **and** put the file in `assets/img/partners/` |
| Add a team member | `BOARD` or `EXECUTIVE` |
| Add a timeline milestone | `TIMELINE` |
| Add a delivered project | `PROJECTS` |
| Update the home page reach figures | `GLANCE_STATS` |
| Add a policy or report to the library | `POLICIES` / `PUBLICATIONS`, then drop the PDF in and add it to `DOC_MAP` in `build.py` |
| Update bank transfer details | `BANK_TRANSFER` — currently placeholders, deliberately |

Changing a programme status updates the programme page, its pillar page, the
home page counter, the portfolio table, the "what is running" board on
`/what-we-do/` and `/accountability/`, and the search index — from one edit.

### The partner logo rule, enforced in code

A partner logo is published **only** where `logo_permission` is `True`. Every
partner currently sits at `None`, because the Partner List handover document
records that permission has not yet been confirmed for any of the nine —
including the four whose logos are already live on the current site. Until the
Foundation confirms, each partner renders as a text entry in the same card
layout, so the grid stays even. This is Section 01/04 of the Partner List,
implemented rather than described.

## 6. Deliberate technical decisions

The brief asked for a site that is honest, fast and easy to update, designed for
a first-time visitor on a mid-range Android phone using mobile data. That drove
every decision below.

- **No web fonts.** A system font stack renders as SF on iOS, Roboto on Android
  and Segoe on Windows. Zero bytes over the wire, no flash of unstyled text.
- **No icon fonts, no third-party scripts, no CDN.** Icons are inline SVG. The
  only external request on the whole site is the map on the contact page, which
  is lazy-loaded and has a text fallback.
- **No carousel.** Explicitly ruled out in the brief, and correctly so.
- **No `backdrop-filter` on the sticky header.** It costs frames on a mid-range
  Android device, and it silently makes the header a containing block for the
  fixed off-canvas menu.
- **Responsive images, generated at build time.** Each photograph is cropped to
  the aspect ratios the pages actually use, at up to four widths, in WebP with a
  JPEG fallback — and no wider than it is ever displayed, so a square thumbnail
  never ships a 1400 px file. **All EXIF, including GPS, is stripped.**
- **Total page weight:** roughly 12 KB of gzipped HTML plus a 12 KB stylesheet
  and a 5 KB script, both cached for a year after first visit. The home page's
  hero photograph is the only image loaded eagerly; everything else is lazy.
  Well inside the three-second target on a normal Nigerian mobile connection.
- **Progressive enhancement.** Every page works with JavaScript disabled.
  Filters, search and the donate widget degrade to plain content and clear
  instructions rather than to a blank screen.

## 7. Accessibility

Built to WCAG 2.1 Level AA and verified:

- Every foreground/background pair in the palette passes AA (lowest measured
  ratio 4.71:1; body text 16.5:1). The orange call-to-action carries navy text
  rather than white for exactly this reason.
- Heading order is unbroken on all 55 pages — verified by an automated pass.
- Every form control has an associated visible label; errors are announced via
  `role="status"`, never signalled by colour alone.
- Skip link, visible focus indicators, full keyboard operation, `Esc` closes the
  menu, and the menu traps nothing the keyboard cannot leave.
- `prefers-reduced-motion` disables all animation and smooth scrolling.
- No horizontal page scroll at 390 px — verified.
- Tables reflow to labelled stacked rows on small screens.

## 8. Before launch

The brief's own sign-off checklist, with the status of each item:

| Check | Status |
|---|---|
| Test donation completed, one-off and recurring | **Blocked** — needs the gateway account (Section 4) |
| Every form tested and arriving in the right inbox | **Blocked** — needs `formEndpoint` |
| Tested on at least three real phones including a low-end Android | Outstanding — layout verified at 390 px |
| All programme statuses correct | Done — 3 running, 1 in set-up, 8 planned, from the source documents |
| Every image consent-cleared | **Outstanding** — 21 photographs supplied by the Foundation are published, 3 withheld on safeguarding grounds. The written consent record has not been handed over. See `CONTENT-NOTES.md` §3 |
| Privacy, cookie and safeguarding pages live and lawyer-reviewed | Drafted and live; **legal review outstanding** and marked as such on each page |
| Backups running and a restore tested | Host-side |
| Redirects from old URLs in place | Draft map in `dist/_redirects` — confirm against the live site's analytics |
| Analytics recording, with goals configured | **Blocked** — needs `analyticsSrc` |
| Admin training delivered and credentials handed over | Outstanding |

Read **`CONTENT-NOTES.md`** before launch. It lists every piece of content the
Foundation still owes, every assumption made, and three discrepancies found
between the source documents.
