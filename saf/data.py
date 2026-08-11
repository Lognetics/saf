# -*- coding: utf-8 -*-
"""
Synia Aid Foundation — website content source.

EVERY fact in this file is taken from one of the Foundation's own documents:

  [CP]  SAF Corporate Profile 2026 (Edition 2, July 2026)
  [PG]  SAF Our Programmes Structure Guide (July 2026)
  [LB]  SAF Leadership Biographies (July 2026)
  [PL]  SAF Partner List for Website (Version 1.0, July 2026)
  [WB]  SAF Website Development Brief (Version 1.0, July 2026)
  [PO]  SAF Policies 01-05 (Safeguarding, Code of Conduct, PSEAH,
        Anti-Fraud & Whistleblowing, Conflict of Interest)

Nothing here is invented. Where a figure or a fact was not supplied, the field
is left blank or carries an explicit "to be confirmed" marker rather than a
plausible-sounding guess. See CONTENT-NOTES.md for the full list of gaps.
"""

# ---------------------------------------------------------------------------
# 1. ORGANISATION
# ---------------------------------------------------------------------------

SITE = {
    "name": "Synia Aid Foundation",
    "short_name": "Synia Aid Foundation",
    "initials": "SAF",
    "tagline": "Hope for the Common Man",          # [WB 07] the only tagline to be used
    "descriptor": "A Nigerian humanitarian and development foundation working with "
                  "internally displaced persons and indigent communities.",
    "founded": "December 2018",
    "founded_year": "2018",
    "founder": "Mmaobi Nwafor-Orizu",
    "legal_form": "Incorporated Trustees under the Companies and Allied Matters Act",
    "regulator": "Corporate Affairs Commission, Federal Republic of Nigeria",
    "reg_number": "CAC/IT/NO 121882",
    "address_lines": ["No. 34 Osun Crescent", "Ancestor's Court", "Maitama, FCT", "Abuja, Nigeria"],
    "address_one_line": "No. 34 Osun Crescent, Ancestor's Court, Maitama, FCT, Abuja, Nigeria",
    "email": "info@syniafoundation.org",
    "phone": "+234 703 446 3791",
    "phone_href": "+2347034463791",
    "hotline": "+234 814 129 4061",
    "hotline_href": "+2348141294061",
    "hours": "Monday – Saturday, 8am – 6pm",
    "domain": "www.syniafoundation.org",
    "base_url": "https://www.syniafoundation.org",
    "profile_edition": "Edition 2 · issued July 2026",
    "social": [
        # [WB 07] handles differ by platform — each linked correctly, no X/Twitter.
        {"name": "Facebook",  "handle": "@syniaaidfoundation",
         "url": "https://www.facebook.com/syniaaidfoundation", "icon": "facebook"},
        {"name": "LinkedIn",  "handle": "@syniaaidfoundation",
         "url": "https://www.linkedin.com/company/syniaaidfoundation", "icon": "linkedin"},
        {"name": "Instagram", "handle": "@synia_aid_foundation",
         "url": "https://www.instagram.com/synia_aid_foundation", "icon": "instagram"},
    ],
}

MOTTOS = ["Educate the mind", "Equip the hands", "Secure the home"]

# [CP 02] "at a glance". Partner count follows the Partner List, which is the
# declared source of record (nine partners); the Corporate Profile's "8" is
# superseded — flagged in CONTENT-NOTES.md.
GLANCE_STATS = [
    {"figure": "2018", "label": "Established and registered", "sub": "Corporate Affairs Commission"},
    {"figure": "7",    "label": "States and territories of operation", "sub": "FCT, Nasarawa, Anambra, Lagos, Rivers, Oyo, Ogun"},
    {"figure": "10+",  "label": "Programmes and campaigns delivered", "sub": "2019 to date, with partners"},
    {"figure": "9",    "label": "Named delivery partners", "sub": "Schools, health bodies and foundations"},
]

AT_A_GLANCE = [
    ("Registered name", "Synia Aid Foundation"),
    ("Founded", "December 2018"),
    ("Founder", "Mmaobi Nwafor-Orizu"),
    ("Legal status", "Incorporated Trustees, registered with the Corporate Affairs Commission of the Federal Republic of Nigeria"),
    ("Registration number", "CAC/IT/NO 121882"),
    ("Head office", "No. 34 Osun Crescent, Ancestor's Court, Maitama, FCT, Abuja, Nigeria"),
    ("Governance", "Founder-chaired Board of Trustees, supported by an executive team and advisers"),
    ("Primary focus", "Internally displaced persons in Nigeria"),
    ("Wider focus", "Indigent and vulnerable communities sharing the same roots in poverty and exclusion"),
    ("Areas of operation", "Federal Capital Territory; Nasarawa (Keffi); Anambra (Nnewi); Lagos; Rivers (Port Harcourt); Oyo (Ibadan); Ogun"),
    ("Geographic priority", "The FCT–Nasarawa–Keffi resettlement corridor"),
    ("Pillars", "Education & Skills; Livelihoods & Economic Inclusion; Shelter, WASH & Protection"),
    ("Programmes", "Twelve, of which three are running and one is in set-up as at July 2026"),
    ("Tagline", "Hope for the Common Man"),
]

VISION = ("A Nigeria where the dignity and potential of every indigent person — and especially of "
          "internally displaced persons — are recognised and protected, even amid rising insecurity, "
          "so that no one is left behind on the road out of poverty.")

MISSION = ("To provide humanitarian relief to internally displaced and indigent persons across Nigeria "
           "through educational sponsorship, entrepreneurial support and the provision of shelter — "
           "delivered through fundraising, partnership and advocacy — so that lives disrupted by "
           "displacement and poverty are protected, rebuilt and made self-reliant.")

VALUES = [  # [CP 04]
    ("Love", "Love is the reason the Foundation exists before it is a value we practise. We serve because every person carries a worth that displacement and poverty cannot take from them — not because a programme requires it, but because we are convinced of it."),
    ("Kindness", "How we serve matters as much as what we deliver. A family that has lost its home is owed patience and gentleness, not efficiency alone, so kindness governs the manner of every interaction, from the Board to the field."),
    ("Solidarity", "We work with the people we serve as partners and equals. They understand their communities better than any outsider, so our efforts grow from their views and ideas — we listen, we learn, and we build solutions together."),
    ("Social justice", "We act with urgency. We cannot be patient while people endure preventable hardship, so we press for both immediate relief and the deeper changes that address its causes."),
    ("Need-led service", "Our programmes are determined solely by need — not by status, ethnicity, gender, religion or outside interest. We recognise that poverty has many faces and respond to all of them."),
    ("Commitment", "Real progress demands more than sympathy; it demands commitment and, at times, self-sacrifice. We hold ourselves to that standard in everything we deliver."),
    ("Independence", "We work for the people of our society and no one else. We partner widely but remain independent of political, economic, religious and social interests, so the people we serve are never used to promote causes that are not their own."),
    ("Hope & strength", "We draw our energy from a realistic, undying hope for a better tomorrow — and from the skill and resourcefulness of the people we serve, which we make the foundation of every programme."),
]

DISTINCTIONS = [  # [CP 03]
    ("Founded in legal research",
     "The Foundation grew out of academic work on the protection of persons displaced by conflict and disaster. "
     "This gives us an unusual grounding in the rights dimension of displacement — documentation, housing and land "
     "rights, and access to justice — and it is the basis of our Protection & Rights programme."),
    ("Rooted, not parachuted",
     "We are Nigerian, based in Abuja, and we work in communities where we are known. Our access is relational, not contractual."),
    ("Focused on non-camp displacement",
     "Most displaced Nigerians do not live in camps. Our footprint sits along the corridor where families relocated from "
     "the Federal Capital Territory are being resettled — an under-served part of the response."),
    ("Partnership as method",
     "Almost every project in our record was delivered with someone else. We treat collaboration as the engine of impact "
     "rather than a supporting tactic."),
    ("Honest by policy",
     "We publish what is running and what is planned, and we do not claim numbers we cannot evidence. "
     "We would rather be trusted than impressive."),
]

WHAT_WE_ARE_NOT = ("We are a growing national organisation, not an international NGO, and we say so deliberately. "
                   "We do not operate outside Nigeria. We do not hold engineering or clinical capacity in house — "
                   "where technical delivery is required, we say who our partner is. And we are candid that our "
                   "monitoring systems and audited reporting are being built rather than long established. "
                   "Overstating any of this would cost us the one asset a young foundation cannot afford to lose.")

# ---------------------------------------------------------------------------
# 2. STATUS LABELS  [WB 04 — CRITICAL]
# ---------------------------------------------------------------------------

STATUSES = {
    "running": {
        "label": "Running now",
        "key": "running",
        "definition": "The programme is operating today. We report on it.",
    },
    "setup": {
        "label": "In set-up",
        "key": "setup",
        "definition": "Designed and being put in place, but not yet awarding or delivering.",
    },
    "planned": {
        "label": "Planned",
        "key": "planned",
        "definition": "Approved in our plan and scheduled, but not yet started. We say so plainly "
                      "rather than implying it is already running.",
    },
}

# ---------------------------------------------------------------------------
# 3. PILLARS AND PROGRAMMES
# ---------------------------------------------------------------------------

PILLARS = [
    {
        "slug": "education-skills",
        "number": "1",
        "name": "Education & Skills",
        "motto": "Educate the mind",
        "icon": "book",
        "lede": "Displacement takes children out of school, often for years. This pillar exists to put them "
                "back in, keep them there, and carry those who can go further as far as they are able to go.",
        "intro": [
            "Our first pillar is built on a conviction the Foundation inherited from the educationist "
            "Dr A. A. Nwafor-Orizu: to educate the mind is to liberate it. We treat education and skills "
            "not as acts of generosity but as the most effective and lasting route out of poverty.",
            "A child out of school for three years does not simply resume where they stopped. That is why "
            "this pillar covers catch-up learning as well as fees, and why we measure whether a child is "
            "still in school at the end of the year rather than whether a fee was paid.",
        ],
    },
    {
        "slug": "livelihoods-economic-inclusion",
        "number": "2",
        "name": "Livelihoods & Economic Inclusion",
        "motto": "Equip the hands",
        "icon": "lightbulb",
        "lede": "Relief meets today's need; an income meets next year's. This pillar helps adults who have "
                "lost their livelihood to build one that holds — and then to stop needing us.",
        "intro": [
            "A trader who lost her stock loses her customers, then her credit, then her standing. "
            "Rebuilding an income is not a matter of a single grant; it is training, staged capital, "
            "mentoring and a route to actual buyers.",
            "Every programme in this pillar is designed to end. Support closes by a recorded route — "
            "completion, progression, graduation or handover — and is never simply allowed to lapse.",
        ],
    },
    {
        "slug": "shelter-wash-protection",
        "number": "3",
        "name": "Shelter, WASH & Protection",
        "motto": "Secure the home",
        "icon": "house",
        "lede": "A safe home is the floor everything else stands on. This pillar covers the roof over a "
                "family's head, the water they drink, the help they need in a crisis — and their right to "
                "remain where they have rebuilt.",
        "intro": [
            "Shelter and protection are paired deliberately. A family whose right to occupy their shelter "
            "is undocumented cannot safely invest in it, and improving a structure a household is later "
            "evicted from converts a grant into a loss.",
            "So we verify a family's right to remain before shelter works begin, and we assess every "
            "shelter against a written minimum standard derived from Sphere — before the work, after it, "
            "and again at three and twelve months.",
        ],
    },
]

CROSS_CUTTING = {
    "slug": "across-all-pillars",
    "name": "Across all pillars",
    "motto": "Running through everything",
    "lede": "Two programmes are not confined to a single pillar. They support all three, and they are how "
            "we meet people before a programme begins and stay with them after it ends.",
}

PROGRAMMES = [
    # ---------------- PILLAR ONE ----------------
    {
        "slug": "learning-access-retention",
        "name": "Learning Access & Retention Programme",
        "short_name": "Learning Access & Retention",
        "public_name": "Train a Child",
        "pillar": "education-skills",
        "status": "running",
        "flagship": "Our flagship education programme",
        "one_line": "Gets out-of-school children back into school, and keeps them there.",
        "what_it_does": [
            "We find children who are out of school and bring them back. Where a child has missed too much "
            "to simply rejoin their year group, we run a catch-up learning block first so they can be placed "
            "at the right level.",
            "We then cover school fees and levies, uniform, books and examination costs, and we follow up "
            "every term to confirm the child is actually attending — by physical visit, not by administrative "
            "record alone.",
        ],
        "who_for": [
            "Displaced and indigent children who have never attended school, who have dropped out, or who are "
            "enrolled but at risk of leaving for reasons of cost, distance, caring duties or menstrual health.",
            "Support for girls to remain in school — the work we have run as Pad A Girl — sits inside this programme.",
        ],
        "success": "The child is still in school at the end of the academic year and progresses to the next "
                   "grade — not simply that a fee was paid.",
        "where": "Federal Capital Territory and Nasarawa State (Keffi), within the corridor where the Foundation "
                 "already works. Delivery locations are confirmed with each partner school before a cohort opens.",
        "delivery": "Through written partnership agreements with schools, including Covenant Academy from "
                    "September 2026, and with state education authorities for placement recognition.",
        "partners": ["covenant-academy", "deborah-counselling-consult"],
        "extra": [
            ("How this programme is measured", [
                "Outputs: children assessed, enrolled or re-enrolled; terms of support delivered.",
                "Outcomes: retention to the end of the academic year; attendance above threshold; transition to "
                "the next grade; girls retained across the year.",
                "All indicators are disaggregated by sex, displacement status, disability and age group.",
            ]),
        ],
        "support_line": "Fund a child's school year.",
    },
    {
        "slug": "synia-scholars-fund",
        "name": "Synia Scholars Fund",
        "short_name": "Synia Scholars Fund",
        "public_name": None,
        "pillar": "education-skills",
        "status": "setup",
        "flagship": None,
        "one_line": "Scholarships for senior secondary and tertiary study.",
        "what_it_does": [
            "Funds senior secondary and tertiary study for students who have the ability but not the means. "
            "Awards are made by a selection panel against criteria we publish.",
            "The money is held and accounted for separately from our general funds, so that donors can see "
            "exactly where their gift went.",
        ],
        "who_for": [
            "Students progressing beyond basic education, including those who came to us through Train a Child. "
            "Selection is need-led first.",
        ],
        "success": "Scholars complete their course and qualify — not merely that they enrolled.",
        "where": "National in scope. Award locations follow the successful applicants' places of study.",
        "delivery": "A selection panel operating against published, need-based criteria, with ring-fenced accounting.",
        "partners": [],
        "extra": [
            ("Why it is not yet open", [
                "The Fund will not be promoted externally until a fund agreement, published need-based selection "
                "criteria, a selection panel and ring-fenced accounting are in place.",
                "Naming a thing a Fund creates obligations, and we intend to meet them before we fundraise. "
                "An obligation we cannot yet meet is a liability rather than an asset.",
            ]),
        ],
        "support_line": "Register your interest in supporting the Fund when it opens.",
    },
    {
        "slug": "youth-skills-employability",
        "name": "Youth Skills & Employability Programme",
        "short_name": "Youth Skills & Employability",
        "public_name": None,
        "pillar": "education-skills",
        "status": "planned",
        "flagship": None,
        "one_line": "Trade skills and apprenticeships that end in a real job.",
        "what_it_does": [
            "Practical trade and vocational training for young people, paired with apprenticeships and active "
            "help finding work at the end of it.",
            "Training that leads nowhere is training wasted, so placement is built into the programme rather "
            "than left to chance.",
        ],
        "who_for": [
            "Young people aged approximately 15 to 24, particularly those who left school without a qualification.",
        ],
        "success": "The young person is certified and in work.",
        "where": "Planned for the FCT–Nasarawa–Keffi corridor, where the Foundation already operates. "
                 "Locations are confirmed at launch.",
        "delivery": "To be delivered with training institutions and employers. Nasarawa State College of Health "
                    "is a current partner in education, awareness and empowerment for students.",
        "partners": ["nasarawa-state-college-of-health"],
        "extra": [
            ("Where education ends and livelihoods begin", [
                "If the measured outcome is learning or certification, the person is supported under Pillar One. "
                "If the measured outcome is income or enterprise, they move to Pillar Two.",
                "The rule is simple, it is applied consistently, and it prevents the same person being counted "
                "twice in our reported figures.",
            ]),
        ],
        "support_line": "Support the launch of this programme.",
    },
    # ---------------- PILLAR TWO ----------------
    {
        "slug": "enterprise-development",
        "name": "Enterprise Development Programme",
        "short_name": "Enterprise Development",
        "public_name": "Start · Grow · Scale",
        "pillar": "livelihoods-economic-inclusion",
        "status": "running",
        "flagship": "Our flagship livelihoods programme",
        "one_line": "Skills, staged capital and mentoring to build a business that lasts.",
        "what_it_does": [
            "Business and trade skills training, followed by a grant or asset package to begin trading, six months "
            "of mentoring from someone who has done it, and introductions to actual buyers.",
            "Grants are released in stages against agreed milestones rather than as a single lump sum — a control "
            "that protects the funds and the participant alike.",
        ],
        "who_for": [
            "Displaced and indigent adults aged 18 and above, with priority to female-headed households, relocated "
            "households and persons with disability.",
            "We do not describe this programme as an accelerator, and we do not use the language of investment "
            "readiness — that vocabulary draws a programme away from the households it exists to serve.",
        ],
        "success": "The enterprise is still trading twelve months later, and the household is earning measurably "
                   "more than at baseline.",
        "where": "Nasarawa State (Keffi) and the Federal Capital Territory.",
        "delivery": "Delivered directly by the Foundation, with mentoring drawn from experienced traders and "
                    "business owners in the same market.",
        "partners": [],
        "extra": [
            ("The three tiers", [
                "<strong>Start</strong> — for those with no business or trading under six months: skills, seed "
                "capital and entry to a savings group.",
                "<strong>Grow</strong> — working capital, pricing and record-keeping, and buyer linkage for those "
                "already trading.",
                "<strong>Scale</strong> — growth capital, formalisation support and aggregation for those employing "
                "others.",
                "A participant progresses when ready, and is never enrolled in two tiers at once.",
            ]),
            ("How this programme is measured", [
                "Outputs: participants trained; grants disbursed; savings groups formed; mentoring sessions delivered.",
                "Outcomes: enterprises still trading at 6 and 12 months; median income change against baseline; "
                "active savings balance; repeat buyers secured.",
            ]),
        ],
        "support_line": "Fund a trader's start in business.",
    },
    {
        "slug": "savings-financial-inclusion",
        "name": "Savings & Financial Inclusion Programme",
        "short_name": "Savings & Financial Inclusion",
        "public_name": None,
        "pillar": "livelihoods-economic-inclusion",
        "status": "planned",
        "flagship": None,
        "one_line": "Small savings groups that keep working after we leave.",
        "what_it_does": [
            "Brings people together into small savings groups where members save regularly, borrow from a shared "
            "pool and build a cushion against shock.",
            "It is among the most evidence-backed and lowest-cost livelihoods interventions available, and it "
            "continues working long after facilitation ends.",
        ],
        "who_for": [
            "Anyone in our livelihoods programmes, and others in the same community who wish to join.",
        ],
        "success": "Members hold real savings and can absorb an illness or a bad month without selling the tools "
                   "of their trade.",
        "where": "Planned alongside Enterprise Development in Nasarawa State (Keffi) and the Federal Capital Territory.",
        "delivery": "Group facilitation by trained community mobilisers, with the group continuing independently "
                    "after facilitation ends.",
        "partners": [],
        "extra": [],
        "support_line": "Support the launch of this programme.",
    },
    {
        "slug": "womens-economic-empowerment",
        "name": "Women's Economic Empowerment Programme",
        "short_name": "Women's Economic Empowerment",
        "public_name": None,
        "pillar": "livelihoods-economic-inclusion",
        "status": "planned",
        "flagship": None,
        "one_line": "Targeted economic support for women and female-headed households.",
        "what_it_does": [
            "Skills, assets, market access and rights awareness aimed specifically at women facing economic "
            "exclusion, including widows and women displaced with dependent children.",
        ],
        "who_for": [
            "Women and female-headed households, including widows and women displaced with dependent children.",
        ],
        "success": "Women earning independently, and holding decisions about their own income.",
        "where": "Planned for the FCT–Nasarawa–Keffi corridor. Locations are confirmed at launch.",
        "delivery": "To be delivered alongside Enterprise Development and Protection & Rights, so that economic "
                    "support and rights awareness reach the same households.",
        "partners": [],
        "extra": [
            ("An important qualification", [
                "This programme exists to go further for women — not to excuse the others. Every programme in "
                "the portfolio carries a gender commitment, monitored quarterly, so that inclusion is not "
                "confined to a single line in the budget.",
            ]),
        ],
        "support_line": "Support the launch of this programme.",
    },
    # ---------------- PILLAR THREE ----------------
    {
        "slug": "safe-shelter",
        "name": "Safe Shelter Programme",
        "short_name": "Safe Shelter",
        "public_name": None,
        "pillar": "shelter-wash-protection",
        "status": "running",
        "flagship": "Our flagship shelter programme",
        "one_line": "Repairs, upgrades and builds homes to a written safety standard.",
        "what_it_does": [
            "Repairs and upgrades shelter that is leaking, unsafe or offers no privacy; builds transitional "
            "shelter where none exists; and provides household kits.",
            "Every shelter is assessed against a written minimum standard derived from Sphere before and after "
            "the work, then re-inspected at three and twelve months.",
        ],
        "who_for": [
            "Displaced households in camps, host communities and resettlement sites, with priority to "
            "female-headed households, older people living alone and families with infants.",
        ],
        "success": "The shelter meets the standard on re-inspection and the family is still living in it a year later.",
        "where": "Federal Capital Territory and Nasarawa State, including resettlement sites along the "
                 "FCT–Nasarawa–Keffi corridor.",
        "delivery": "Technical and engineering capacity is partner-supplied. The Foundation does not hold "
                    "engineering capacity in house and says so.",
        "partners": ["sam-empowerment-foundation"],
        "extra": [
            ("How we work", [
                "Households contribute their own labour wherever able — homes people helped build are homes "
                "people maintain. Where a household cannot contribute, that is recorded as a reason, never "
                "treated as ineligibility.",
                "A family's right to remain is verified before shelter works begin. Improving a structure a "
                "household is later evicted from converts a grant into a loss.",
            ]),
            ("How this programme is measured", [
                "Outputs: shelters assessed and completed; kits distributed; occupancy documented.",
                "Outcomes: shelters meeting standard on re-inspection; households reporting improved safety and "
                "privacy; occupancy retained at 12 months.",
            ]),
        ],
        "support_line": "Fund a household's shelter repair.",
    },
    {
        "slug": "water-sanitation-hygiene",
        "name": "Water, Sanitation & Hygiene (WASH) Programme",
        "short_name": "Water, Sanitation & Hygiene",
        "public_name": None,
        "pillar": "shelter-wash-protection",
        "status": "planned",
        "flagship": None,
        "one_line": "Clean water, safe toilets and hygiene, built to keep working.",
        "what_it_does": [
            "Access to clean water, safe toilets, handwashing facilities and hygiene education, delivered with "
            "specialist technical partners.",
            "We budget for keeping facilities working — operations and maintenance — not only for installing them.",
        ],
        "who_for": [
            "Camps, resettlement sites and host communities where water and sanitation are inadequate.",
        ],
        "success": "Facilities still functioning a year on, and fewer preventable illnesses in the community.",
        "where": "Planned for camps, resettlement sites and host communities within our existing footprint.",
        "delivery": "Technical work delivered with specialist WASH partners. Partner to be confirmed at launch.",
        "partners": [],
        "extra": [],
        "support_line": "Support the launch of this programme.",
    },
    {
        "slug": "emergency-response-household-recovery",
        "name": "Emergency Response & Household Recovery Programme",
        "short_name": "Emergency Response & Household Recovery",
        "public_name": None,
        "pillar": "shelter-wash-protection",
        "status": "planned",
        "flagship": None,
        "one_line": "Essential items, cash or vouchers, and support through recovery.",
        "what_it_does": [
            "Essential household items immediately after a crisis and — where markets are functioning — cash or "
            "vouchers, so families can buy what they most need rather than what we assumed they needed.",
            "Support continues through the months of recovery, not only in the first days.",
        ],
        "who_for": [
            "Newly displaced or relocated households, and families recovering from conflict, flood or fire.",
        ],
        "success": "The household meets its basic needs without selling the assets it will need to recover.",
        "where": "Planned within our existing footprint, with response location determined by the crisis.",
        "delivery": "Delivered with community relief partners. Rotary Club of Nigeria (Nnewi) is our partner "
                    "in community relief and charity drives.",
        "partners": ["rotary-club-nigeria-nnewi"],
        "extra": [],
        "support_line": "Support the launch of this programme.",
    },
    {
        "slug": "protection-rights",
        "name": "Protection & Rights Programme",
        "short_name": "Protection & Rights",
        "public_name": None,
        "pillar": "shelter-wash-protection",
        "status": "planned",
        "flagship": None,
        "one_line": "Legal help, documents, and the right to stay in a rebuilt home.",
        "what_it_does": [
            "Displaced people frequently lose their papers along with their homes — and without papers they "
            "cannot enrol a child, claim what they are owed or prove where they live.",
            "The programme provides legal advice and assistance, help recovering identity and civil documents, "
            "advice on housing, land and property rights so families are not evicted from homes they have rebuilt, "
            "and referral pathways to specialist services for anyone at risk.",
        ],
        "who_for": [
            "Displaced households whose right to remain, or whose legal identity, is uncertain or contested.",
        ],
        "success": "Households hold the documents they need, and families are not evicted from homes they have rebuilt.",
        "where": "Planned for the FCT–Nasarawa–Keffi corridor, alongside Safe Shelter and Durable Solutions.",
        "delivery": "Technical oversight from the Foundation's Legal Adviser, with referral pathways to "
                    "specialist services.",
        "partners": [],
        "extra": [
            ("Why it matters to us", [
                "The Foundation grew out of legal research into the protection of displaced persons, and is "
                "advised by a Managing Partner with a long pro-bono record. This is the work we were established "
                "to do.",
                "It is also why we verify a family's right to remain before investing in their shelter.",
            ]),
            ("Framework", [
                "Anchored to the African Union's Kampala Convention on the protection and assistance of internally "
                "displaced persons, and to Nigeria's national policy on internal displacement.",
            ]),
        ],
        "support_line": "Support the launch of this programme.",
    },
    # ---------------- CROSS-CUTTING ----------------
    {
        "slug": "community-wellbeing-mental-health",
        "name": "Community Wellbeing & Mental Health",
        "short_name": "Community Wellbeing & Mental Health",
        "public_name": "MindCheck",
        "pillar": "across-all-pillars",
        "status": "planned",
        "status_note": "Formalising work already under way",
        "flagship": None,
        "one_line": "Health and mental-health outreach, and early access to support.",
        "what_it_does": [
            "Health and medical outreaches, mental-health awareness and counselling, community road walks, and "
            "the MindCheck platform — a free, confidential way for someone to assess their wellbeing and reach "
            "support early, without stigma.",
        ],
        "who_for": [
            "Whole communities, not only the households enrolled in our other programmes.",
        ],
        "success": "People reach support earlier, and wellbeing stays at the centre of education, livelihoods "
                   "and shelter work alike.",
        "where": "Nasarawa State (Keffi), Federal Capital Territory and Ogun State, where outreaches have run "
                 "since 2019.",
        "delivery": "Delivered with SpeakOut Mental Health Outreach, CNU Medical Institute (USA), the Kelvin "
                    "Oluchi Diabetes Foundation and student volunteers from the College of Health Science & "
                    "Technology, Keffi. Led at the Foundation by our Public Relations Officer.",
        "partners": ["speakout-mental-health-outreach", "cnu-medical-institute",
                     "kelvin-oluchi-diabetes-foundation", "college-of-health-science-technology-keffi"],
        "extra": [
            ("Why it is being formalised", [
                "This is among the longest-running work we do, and until now it has operated without its own "
                "budget line, indicators or named owner.",
                "Work that is described as cross-cutting but left unmanaged is not integrated — it is simply "
                "unowned. We are giving it the structure it has earned.",
            ]),
            ("Why it sits across everything", [
                "It is how we build trust in a community before a programme begins, and how we keep dignity and "
                "wellbeing at the centre of education, livelihoods and shelter alike.",
            ]),
        ],
        "support_line": "Support community wellbeing work.",
        "mindcheck": True,
    },
    {
        "slug": "durable-solutions-resettlement",
        "name": "Durable Solutions & Resettlement Support",
        "short_name": "Durable Solutions & Resettlement Support",
        "public_name": None,
        "pillar": "across-all-pillars",
        "status": "planned",
        "flagship": None,
        "one_line": "Accompanies households through relocation and settling.",
        "what_it_does": [
            "Many displaced families in and around the Federal Capital Territory are being relocated to "
            "resettlement sites, including in Nasarawa and Keffi. Moving is not the end of displacement; it is "
            "the beginning of settling.",
            "This programme accompanies households through that transition — shelter, schooling, documentation "
            "and a livelihood in the new place.",
        ],
        "who_for": [
            "Households being relocated, and the communities receiving them.",
        ],
        "success": "Households are housed, documented, earning and schooling their children in the place they "
                   "have moved to.",
        "where": "The FCT–Nasarawa–Keffi resettlement corridor.",
        "delivery": "Delivered across all three pillars. We are pursuing a formal partnership with the National "
                    "Commission for Refugees, Migrants and Internally Displaced Persons on this corridor; no "
                    "agreement is in place at present.",
        "partners": [],
        "extra": [
            ("Why we are placed to deliver it", [
                "We already operate along this corridor. Urban and non-camp displacement, and durable solutions "
                "for relocated households, is an area of real need that comparatively few organisations cover.",
            ]),
        ],
        "support_line": "Support the launch of this programme.",
    },
]

# ---------------------------------------------------------------------------
# 4. WHO WE SERVE  [CP 06]
# ---------------------------------------------------------------------------

BENEFICIARY_GROUPS = [
    ("Internally displaced persons",
     "Displaced children of school age, and displaced adults needing livelihoods, shelter and protection. "
     "Our primary focus.",
     "All three pillars"),
    ("Vulnerable children & youth",
     "Out-of-school children, orphans and young people in under-served communities who lack access to "
     "education and opportunity.",
     "Education & Skills"),
    ("Women & widows",
     "Women and female-headed households facing economic exclusion, supported through skills, capital, "
     "savings and rights awareness.",
     "Livelihoods; Protection"),
    ("Families in poverty",
     "Indigent and rural families unable to meet basic needs for food, shelter, water and healthcare.",
     "Shelter, WASH & Protection"),
    ("Persons with disability",
     "People facing barriers to education, healthcare, employment and mobility — supported to participate "
     "fully and with dignity.",
     "All three pillars"),
    ("Host & affected communities",
     "Communities absorbing displaced populations, and those recovering from conflict and disaster.",
     "WASH; Wellbeing; Durable Solutions"),
]

SELECTION_STEPS = [
    ("Community consultation first",
     "No programme begins without listening to the community it will serve, and to the people who will be "
     "affected by it."),
    ("Written scoring",
     "Candidates are assessed against a documented vulnerability scoring sheet, not by impression. "
     "A referral alone is never a route into a programme."),
    ("Verification",
     "Circumstances are verified in the community, and where relevant at the household, with the consent "
     "of the family."),
    ("Priority within need",
     "Where demand exceeds capacity we give priority to displaced households, female-headed households, "
     "persons with disability, older people living alone and families with young children."),
    ("Recorded decisions",
     "Selection outcomes and their reasons are documented, so that decisions can be reviewed and challenged."),
]

CONDUCT_COMMITMENT = ("No payment, favour or relationship is ever a condition of receiving support from the "
                      "Foundation, and no support is ever conditional on a person appearing in our photography, "
                      "films or fundraising material. This is stated to every community we work with, and any "
                      "breach is treated as a serious disciplinary matter.")

# [CP 05] — IOM DTM figures, with sources cited.
NEED_STATS = [
    {"figure": "2.33m", "label": "IDPs in the north-east",
     "sub": "IOM DTM Round 51, assessed September–October 2025"},
    {"figure": "1.38m", "label": "IDPs across ten north-central & north-west states",
     "sub": "IOM DTM Site Assessment Round 18, October 2025"},
    {"figure": "56%",   "label": "of north-east IDPs live in host communities, not camps",
     "sub": "1,300,127 of 2,333,190 people"},
    {"figure": "2.25m", "label": "returnees recorded in the north-east",
     "sub": "IOM DTM Round 51"},
]

NEED_SOURCE = ("Sources: IOM DTM Nigeria, North-East Displacement Report Round 51 (assessment September–October "
               "2025) — 2,333,190 IDPs in 478,229 households, of whom 1,300,127 (56%) were in host communities "
               "and 912,881 (39%) in camps or camp-like settings; and DTM North-Central & North-West Site "
               "Assessment Round 18 (October 2025) — 1,378,124 IDPs across Benue, Kano, Kaduna, Katsina, Kogi, "
               "Niger, Nasarawa, Plateau, Sokoto and Zamfara.")

NEED_IMPLICATIONS = [
    ("The majority of displaced people are not in camps. In the north-east, 56 per cent live in host communities.",
     "Camp-based delivery alone reaches a minority. Programmes must work in host communities and urban settings, "
     "where needs are less visible and services are shared with residents already under strain."),
    ("Displacement affects the middle belt, not only the north-east. Nasarawa is among the ten north-central and "
     "north-west states assessed.",
     "Our footprint in the FCT and Keffi sits inside a genuine displacement geography, not adjacent to one."),
    ("Return and resettlement are now major movements. Over two million returnees were recorded in the north-east alone.",
     "Moving is not the end of displacement. Households need shelter, schooling, documentation and a livelihood "
     "in the place they arrive — the basis of our durable-solutions work."),
    ("Displacement is protracted, not temporary. Populations have remained broadly stable across successive "
     "assessment rounds.",
     "Children are losing years of schooling, not weeks. Recovery programming must be designed for duration, "
     "not for emergency alone."),
]

BEHIND_THE_FIGURES = [
    "Displaced families in Nigeria commonly face overcrowded shelter, food shortages, poor sanitation, limited "
    "healthcare and broken access to schooling. Protection risks are significant: displaced people face heightened "
    "exposure to extortion, gender-based violence, exploitation and trafficking, alongside psychosocial needs "
    "intensified by loss and prolonged uncertainty. Schools in affected areas have been used as displacement "
    "sites, and insecurity has caused repeated closures.",
    "The consequences compound. A child out of school for three years does not simply resume where they stopped. "
    "A trader who lost her stock loses her customers, then her credit, then her standing. A family whose right to "
    "occupy their shelter is undocumented cannot safely invest in it. It is into these compounding gaps that the "
    "Foundation directs its work — and it is why our three pillars are designed to be used together rather than "
    "in isolation.",
]

# ---------------------------------------------------------------------------
# 5. WHERE WE WORK  [CP 13]
# ---------------------------------------------------------------------------

LOCATIONS = [
    ("Federal Capital Territory", "Maitama, Durumi, New Kuchingoro", "Head office and primary operational base",
     "IDP medical outreach; Durumi camp learning-space work; needs assessment; durable-solutions focus"),
    ("Nasarawa State", "Keffi", "Principal community base",
     "Girls' health and safeguarding campaigns; community mental-health outreach; leadership summit; support to "
     "women traders. A destination state in the FCT resettlement corridor."),
    ("Anambra State", "Nnewi, Oraifite", "Founding location",
     "The Foundation's first charity drive, delivered with the Rotary Club of Nigeria"),
    ("Ogun State", "", "Outreach location",
     "Community health outreach and mental-wellbeing sessions"),
    ("Lagos, Rivers & Oyo", "Lagos, Port Harcourt, Ibadan", "Supporter and volunteer network",
     "Community engagement and volunteer mobilisation"),
]

FOOTPRINT_NOTE = [
    "The largest displaced populations in Nigeria are in the north-east and north-west. We do not currently "
    "operate there, and we say so plainly rather than implying national coverage we do not have.",
    "What we do have is a position along the FCT–Nasarawa–Keffi resettlement corridor. Displaced families based "
    "in the Federal Capital Territory are being relocated to resettlement centres in states including Nasarawa, "
    "and the federal commission responsible has publicly identified funding as its principal constraint and "
    "appealed for partnerships with private sector and civil society actors. This is precisely where we already "
    "work and are already known.",
    "Our growth strategy is therefore depth before breadth: to become genuinely expert in urban and non-camp "
    "displacement and in post-relocation recovery along one corridor, rather than to claim a presence in many "
    "states we could not properly serve.",
]

OPERATING_PRINCIPLES = [
    ("Listen first",
     "Every intervention opens with community consultation. The classroom furniture project at Durumi began with "
     "an assessment and an agreement with camp coordinators, not with a decision made in Abuja."),
    ("Build local capability",
     "Where a community holds the skill, we buy it there. Classroom furniture at Durumi is built by a carpenter "
     "living in the camp — the same expenditure creates a learning space and an income."),
    ("Design for measurement",
     "Each programme has a written model: who it serves, the standard package, the cost per person, its indicators "
     "and its exit criteria. A programme without one is not launched."),
    ("Concentrate, don't spread",
     "We would rather run a few programmes properly and prove they worked than run many and prove nothing. This is "
     "why nine of our twelve programmes are marked as planned rather than launched at once."),
    ("Plan the exit",
     "Every programme defines what completion looks like. Support ends by a recorded route — completion, "
     "progression, graduation or handover — and is never simply allowed to lapse."),
    ("Report honestly",
     "We publish what we can evidence and disclose what we cannot. Where a figure is not yet verified, we describe "
     "the work rather than quantify it."),
]

# ---------------------------------------------------------------------------
# 6. THEORY OF CHANGE  [CP 07]
# ---------------------------------------------------------------------------

THEORY_OF_CHANGE = [
    ("Inputs", ["Programme funding", "Trained team and volunteers", "Partner capability",
                "Community relationships", "Legal and technical expertise", "Safeguarding systems"]),
    ("Activities", ["Needs assessment and consultation", "Enrolment and catch-up learning",
                    "Skills, capital and mentoring", "Shelter repair and construction",
                    "Legal advice and documentation", "Health and wellbeing outreach"]),
    ("Outputs", ["Children enrolled", "Adults trained and capitalised", "Shelters completed to standard",
                 "Households documented", "Communities reached"]),
    ("Outcomes", ["Children retained and progressing", "Enterprises still trading at 12 months",
                  "Households securely housed", "Rights and tenure protected", "Improved wellbeing"]),
    ("Impact", ["Self-reliant households", "Dignity restored", "Poverty reduced", "Resilient communities"]),
]

TOC_ASSUMPTIONS = [
    ("That school places exist and partner schools will honour fee agreements",
     "Written place commitments secured before a cohort is enrolled; payment against invoice, per term"),
    ("That a market exists for what the people we train produce or sell",
     "Demand verified before a trade is selected; buyer linkage treated as part of the programme"),
    ("That households can remain where we invest in their shelter",
     "Right to remain verified before shelter works begin — the reason Protection is paired with Shelter"),
    ("That support reaches those most in need",
     "Written scoring, community verification, and recorded selection decisions open to challenge"),
]

# ---------------------------------------------------------------------------
# 7. TIMELINE AND TRACK RECORD  [CP 15, 16]
# ---------------------------------------------------------------------------

TIMELINE = [
    ("2018", "Foundation established",
     "Founded in December by Mmaobi Nwafor-Orizu, inspired by her law thesis on the protection of persons "
     "displaced by conflict and disaster, and registered with the Corporate Affairs Commission."),
    ("2019", "Charity Drive — our first programme",
     "On 5 January, with the Rotary Club of Nigeria (Nnewi), we reached a home for the needy in Oraifite with "
     "clothing, funds and food items."),
    ("2019", "The Valentine Special",
     "An awareness road walk across Keffi, Nasarawa State, with donations to motherless-babies' homes — our "
     "first public campaign."),
    ("2020", "The Love Initiative — IDP medical outreach",
     "A major medical outreach at New Kuchingoro IDP camp, FCT, with Sam Empowerment Foundation — testing, "
     "maternal supplements, birthing kits and consultations."),
    ("2021", "Diabetes outreach",
     "Community screening and health education delivered with the Kelvin Oluchi Diabetes Foundation."),
    ("2025", "Pad A Girl campaign",
     "On 22 May, with Deborah Counselling Consult, Pad A Girl reached ECWA School, Keffi — health education, "
     "safeguarding sensitisation, and distribution of pads and books."),
    ("2025", "Ogun community health outreach",
     "A general health outreach with SpeakOut closing out the year — health checks, education and wellbeing "
     "conversations."),
    ("2026", "Community Mental Health Road Walk",
     "On 19 January, with students of the College of Health Science and Technology, Keffi, volunteers took "
     "wellbeing education into the streets."),
    ("2026", "Mind Check pilot & MindCheck App launch",
     "On 21 January, with SpeakOut, we launched the MindCheck App — a free, confidential platform to assess "
     "wellbeing and reach support early."),
    ("2026", "SAF Leadership Development Summit",
     "On “Strategic Leadership in a Changing World”, attended by representatives of the Emir of Keffi."),
    ("2026", "Love on the Street",
     "On 20 May, the founder's birthday was marked with service rather than celebration — supporting women "
     "traders in Keffi and honouring security personnel."),
    ("2026", "Durumi IDP camp — assessment and learning spaces",
     "A multi-sector needs assessment at Durumi camp, and agreement with coordinators on a classroom furniture "
     "project built by a carpenter living in the camp."),
    ("2026", "Professionalising the Foundation",
     "A strategic review of the portfolio, a refreshed three-pillar architecture, written programme models, and "
     "the launch of Learning Access & Retention with Covenant Academy."),
]

PROJECTS = [  # year, project, partner, type, delivered, location, pillar tag
    ("2019", "Charity Drive", "Rotary Club of Nigeria (Nnewi)", "Relief",
     "Clothing, funds and food to a home for the needy in Oraifite", "Oraifite, Anambra", "shelter-wash-protection"),
    ("2019", "The Valentine Special", "—", "Community outreach",
     "Awareness walk across Keffi, with donations to motherless-babies' homes", "Keffi, Nasarawa", "across-all-pillars"),
    ("2020", "The Love Initiative", "Sam Empowerment Foundation", "Displacement",
     "Medical outreach for IDPs at New Kuchingoro camp — testing, treatment, maternal care, consultations",
     "New Kuchingoro, FCT", "across-all-pillars"),
    ("2021", "Diabetes Outreach", "Kelvin Oluchi Diabetes Foundation", "Community outreach",
     "Community screening and health education", "Keffi, Nasarawa", "across-all-pillars"),
    ("2025", "Pad A Girl", "Deborah Counselling Consult; SpeakOut", "Education",
     "Menstrual health, dignity and safeguarding at ECWA School, Keffi; pads and educational books distributed",
     "Keffi, Nasarawa", "education-skills"),
    ("2025", "Ogun Health Outreach", "SpeakOut Mental Outreach", "Community outreach",
     "Health checks, education and wellbeing sessions", "Ogun State", "across-all-pillars"),
    ("2026", "Mental Health Road Walk", "SpeakOut; College of Health Science & Technology", "Community outreach",
     "Community-wide awareness across Keffi with student volunteers", "Keffi, Nasarawa", "across-all-pillars"),
    ("2026", "Mind Check & MindCheck App", "SpeakOut Mental Health Outreach", "Community outreach",
     "Pilot and launch of a free, confidential wellbeing platform", "Keffi, Nasarawa", "across-all-pillars"),
    ("2026", "Leadership Development Summit", "—", "Youth & skills",
     "Youth leadership summit on ethical leadership and emotional intelligence", "Keffi, Nasarawa", "education-skills"),
    ("2026", "Love on the Street", "—", "Livelihoods",
     "Support for vulnerable women traders and security personnel in Keffi", "Keffi, Nasarawa",
     "livelihoods-economic-inclusion"),
]

TRACK_RECORD_NOTE = (
    "Most of the projects below are community outreaches — health, dignity and relief campaigns run with partners. "
    "That is an accurate picture of our first seven years, and it was deliberate. Outreach is how a foundation of "
    "our size earns trust and access in a community before it asks that community to enrol its children in a "
    "programme or accept a shelter assessment. It is how we work, not what we are for. Our mandate is the three "
    "pillars, and from the 2026–27 year our reporting shifts to what those pillar programmes deliver.")

MEASUREMENT_NOTE = [
    "We report our reach honestly and conservatively. The figures we publish are drawn from project records and "
    "are deliberately conservative where records are incomplete.",
    "We are candid that, until recently, our reporting captured outputs — what we delivered — rather than "
    "outcomes — what changed as a result. That is a limitation, not an achievement, and it is the single thing "
    "we are working hardest to correct. From the 2026–27 academic year, figures we publish will be backed by "
    "project-level data with sources and dates. We would rather publish a smaller number we can defend than a "
    "larger one we cannot.",
]

# ---------------------------------------------------------------------------
# 8. LEADERSHIP  [CP 18, LB]
# ---------------------------------------------------------------------------

BOARD = [
    {
        "slug": "mmaobi-nwafor-orizu",
        "name": "Mmaobi Nwafor-Orizu",
        "role": "Founder & Chair, Board of Trustees",
        "credentials": "LL.M. International Economic Law, Queen Mary University of London · ACIArb",
        "summary": "Founded the Foundation in December 2018 to address poverty, inequality and social exclusion "
                   "among vulnerable populations in Nigeria.",
        "bio": [
            "Mmaobi Nwafor-Orizu is the Founder of Synia Aid Foundation, a humanitarian and development "
            "organisation established in December 2018 to address poverty, inequality and social exclusion among "
            "vulnerable populations in Nigeria. Driven by a commitment to social justice, human dignity and "
            "sustainable development, she founded the Foundation with the vision of a society in which indigent "
            "persons — particularly internally displaced persons — have access to education, empowerment "
            "opportunities and safe living conditions.",
            "A trained legal professional, she holds a Master of Laws in International Economic Law from Queen "
            "Mary University of London. Her academic background, combined with a commitment to humanitarian "
            "service, shapes her approach to complex social challenges through advocacy, education and "
            "community-driven development.",
            "The inspiration for the Foundation emerged from her research into the conditions faced by internally "
            "displaced persons in Nigeria. While studying law she undertook a project titled <em>Conditions of "
            "Persons Internally Displaced by Conflict and Natural Disaster: The UN Perspective and the Need for "
            "More Protective Legislation in Nigeria</em>. That work exposed her to the realities of displacement, "
            "poverty and systemic inequality affecting millions of vulnerable Nigerians, and she transformed "
            "those academic insights into practical intervention through the establishment of Synia Aid Foundation.",
            "Under her leadership the Foundation was built on the conviction that poverty is most effectively "
            "addressed through interconnected pillars of education, economic empowerment and shelter. She believes "
            "education is the most powerful instrument for liberation and social transformation, and guided by the "
            "philosophy that to educate the mind is to liberate it, has positioned education as the cornerstone of "
            "the Foundation's mission.",
            "Her leadership philosophy emphasises partnership with communities, recognising that lasting solutions "
            "emerge when vulnerable populations participate actively in identifying challenges and shaping "
            "responses to them. Her vision extends beyond temporary assistance: she advocates long-term, systemic "
            "solutions addressing the root causes of poverty and social exclusion, consistently promoting community "
            "ownership, capacity development and sustainable interventions designed to empower individuals rather "
            "than foster dependency.",
        ],
        "remit": "Chairs the Board of Trustees. Holds strategic direction, programme and policy approval, and "
                 "financial oversight. Her legal grounding in displacement law underpins the Foundation's "
                 "Protection & Rights Programme.",
        "group": "board",
    },
    {
        "slug": "henry-leonard",
        "name": "Henry Leonard",
        "role": "Legal Adviser",
        "credentials": "Legal practitioner, Leonard and Nzom",
        "summary": "Provides strategic legal guidance, ensuring compliance, accountability and sound governance "
                   "within the Foundation.",
        "bio": [
            "Henry Leonard is the Legal Adviser of Synia Aid Foundation and a distinguished legal practitioner at "
            "Leonard and Nzom. With extensive experience in legal practice, he provides strategic legal guidance, "
            "ensuring compliance, accountability and sound governance within the Foundation.",
            "Known for his professionalism and commitment to justice, he combines legal expertise with a "
            "commitment to community development, and holds a long record of pro-bono service to indigent clients. "
            "His counsel supports the Foundation's mission to create positive and lasting social impact.",
        ],
        "remit": "Legal counsel to the Board, regulatory compliance and governance. Provides technical oversight "
                 "of the Protection & Rights Programme, covering housing, land and property rights, documentation "
                 "and access to legal assistance for displaced households.",
        "group": "adviser",
    },
    {
        "slug": "chinasa-fabian-ijeruh",
        "name": "Chinasa Fabian-Ijeruh",
        "role": "Human Resources Adviser",
        "credentials": "Chartered MCIPD · SPHRi · ACIPM",
        "summary": "A chartered HR professional with over fifteen years' experience across finance, EdTech and "
                   "the non-profit sector.",
        "bio": [
            "Chinasa Fabian-Ijeruh is a seasoned human resources professional with over fifteen years of "
            "experience across the finance, EdTech and non-profit sectors. She brings expertise in strategic "
            "human resource management, organisational development, employee relations and talent management, "
            "with experience supporting multi-country teams across the United Kingdom and Europe.",
            "She has a proven track record of partnering with leadership to drive people-focused strategies that "
            "enhance organisational effectiveness, support workforce transformation and ensure compliance with "
            "employment legislation. Her experience spans HR policy development, organisational change, "
            "performance management and the implementation of HR systems that improve operational efficiency.",
            "A Chartered Member of the CIPD, she holds additional professional certifications including SPHRi and "
            "ACIPM, and is an active contributor within the CIPD Manchester professional community, where she "
            "supports knowledge sharing and policy development initiatives.",
            "Beyond her professional work, she is deeply committed to supporting the less privileged, particularly "
            "children and young people. Through her volunteering within the Christian community she has "
            "contributed to initiatives focused on mentorship, development and social support.",
        ],
        "remit": "Advises the Board on people strategy, organisational structure and safeguarding in employment — "
                 "including the vetting and code-of-conduct requirements that apply to everyone working with "
                 "children in our programmes.",
        "group": "adviser",
    },
    {
        "slug": "sariki-abungwo",
        "name": "Dr Sariki Abungwo",
        "role": "Media Strategist Adviser",
        "credentials": "FBCS · Forbes Coaches Council · Global Recognition Award recipient",
        "summary": "A business strategist, entrepreneur and international speaker; Founder and Chief Executive of "
                   "Blesatech Consultancy Services.",
        "bio": [
            "Dr Sariki Abungwo is a business strategist, entrepreneur and international speaker committed to "
            "empowering people and communities through education and entrepreneurship. He is the Founder and "
            "Chief Executive of Blesatech Consultancy Services, where he helps coaches, consultants and "
            "service-based businesses grow using proven marketing and business systems.",
            "He is a Fellow of the British Computer Society, a member of the Forbes Coaches Council, and a "
            "university lecturer. As a recipient of the Global Recognition Award, he brings together business "
            "leadership, academic insight and a commitment to social impact in support of initiatives that expand "
            "opportunity and transform lives.",
        ],
        "remit": "Advises the Board on media strategy, positioning and the Foundation's reach beyond Nigeria, "
                 "including diaspora engagement and the profile of its education and entrepreneurship work.",
        "group": "adviser",
    },
]

EXECUTIVE = [
    {
        "slug": "amos-endem-rejoice",
        "name": "Amos Endem Rejoice",
        "role": "Chief Operations Officer",
        "credentials": "Operations and administrative leadership",
        "summary": "Responsible for day-to-day delivery, staff coordination and the build-out of the Foundation's "
                   "operating systems.",
        "bio": [
            "Amos Endem Rejoice is a dedicated operations and administrative professional serving as Chief "
            "Operations Officer of Synia Aid Foundation. She brings a strong background in leadership and "
            "organisational management, having previously served as Head Administrator of a school, where she "
            "oversaw daily operations, staff coordination and institutional development.",
            "Committed to community impact and effective service delivery, she brings strategic vision, "
            "operational excellence and a commitment to empowering people and advancing humanitarian initiatives "
            "at the Foundation.",
        ],
        "remit": "Day-to-day programme delivery, staff coordination and the build-out of the Foundation's "
                 "operating systems, including the documented programme models behind each flagship. Policy owner "
                 "for the Foundation's safeguarding and conduct policies.",
        "group": "executive",
    },
    {
        "slug": "offorka-n-jerry",
        "name": "Offorka N. Jerry",
        "role": "Public Relations Officer",
        "credentials": "Certified Mental Health Advocate · Founder, Speak Out Mental Health Outreach",
        "summary": "Communications lead and certified mental-health advocate; leads the Foundation's MindCheck work.",
        "bio": [
            "Offorka Jerry is a certified Mental Health Advocate and the Founder of Speak Out Mental Health "
            "Outreach, an initiative dedicated to promoting mental health awareness, education and support within "
            "communities.",
            "As Public Relations Officer of Synia Aid Foundation he plays a key role in strengthening public "
            "engagement, fostering strategic partnerships and advancing the Foundation's humanitarian mission. "
            "Committed to advocacy and social impact, he works to break the stigma surrounding mental health and "
            "to empower individuals through education, outreach and community-driven initiatives.",
        ],
        "remit": "Public engagement, media relations and partnership development. Leads the Foundation's "
                 "cross-cutting Community Wellbeing & Mental Health work, delivered publicly as MindCheck.",
        "group": "executive",
    },
]

GOVERNANCE_BODIES = [
    ("Board of Trustees",
     "Strategy, programme approval, policy adoption, financial oversight and risk. Programmes may not launch, "
     "and programme models may not be adopted, without Board sign-off."),
    ("Executive team",
     "Day-to-day delivery, programme management, and operational control within Board-approved budgets and policies."),
    ("Programme owners",
     "Named accountability for a single programme — its model, its data and its exit decisions."),
    ("Advisers to the Board",
     "Specialist counsel at Board level in law, human resources and media strategy, informing decisions without "
     "executive responsibility for delivery."),
]

GOVERNANCE_COMMITMENTS = [
    ("Recruit two to three independent Trustees", "Agreed — in progress"),
    ("Appoint a Treasurer or finance lead", "Agreed — in progress"),
    ("Establish a Finance & Audit sub-committee with independent membership", "Agreed — in progress"),
    ("Maintain a conflicts of interest register with disclosure and recusal", "Agreed — in progress"),
    ("Plan a transition from Founder-Chair to an independent Chair over three to five years", "Agreed in principle"),
]

GOVERNANCE_CANDOUR = ("We are candid that governance in a founder-led organisation requires deliberate "
                      "strengthening, and that funders are right to examine it. The Board has committed to the "
                      "following, and will report against it.")

# ---------------------------------------------------------------------------
# 9. PARTNERS  [PL — the source of record]
# ---------------------------------------------------------------------------

PARTNER_CATEGORIES = [
    ("education-skills", "Education & Skills",
     "Schools and institutions helping us get children into learning and keep them there."),
    ("displacement-response", "Displacement Response",
     "Organisations we deliver alongside in camps and displaced communities."),
    ("community-outreach", "Community Outreach",
     "Health, wellbeing and mobilisation partners whose work runs across all our programmes."),
]

# logo_permission: None = not yet confirmed by the Foundation.
# Per [PL 01/04] a logo is published ONLY where permission is confirmed; until
# then the partner is displayed as a text entry in the same card layout.
PARTNERS = [
    {"slug": "covenant-academy", "name": "Covenant Academy", "category": "education-skills", "order": 1,
     "description": "School partner for the Learning Access & Retention Programme from September 2026",
     "programmes": ["learning-access-retention"], "logo_permission": None, "logo": None, "url": None},
    {"slug": "deborah-counselling-consult", "name": "Deborah Counselling Consult", "category": "education-skills", "order": 2,
     "description": "Girls' health, safeguarding and the Pad A Girl campaign",
     "programmes": ["learning-access-retention"], "logo_permission": None, "logo": None, "url": None},
    {"slug": "nasarawa-state-college-of-health", "name": "Nasarawa State College of Health", "category": "education-skills", "order": 3,
     "description": "Education, awareness and empowerment for students",
     "programmes": ["youth-skills-employability"], "logo_permission": None, "logo": "partner-nascoal.png", "url": None},
    {"slug": "sam-empowerment-foundation", "name": "Sam Empowerment Foundation", "category": "displacement-response", "order": 1,
     "description": "Medical outreach for internally displaced persons at New Kuchingoro camp",
     "programmes": ["safe-shelter", "community-wellbeing-mental-health"], "logo_permission": None, "logo": None, "url": None},
    {"slug": "rotary-club-nigeria-nnewi", "name": "Rotary Club of Nigeria (Nnewi)", "category": "displacement-response", "order": 2,
     "description": "Community relief and charity drives",
     "programmes": ["emergency-response-household-recovery"], "logo_permission": None, "logo": None, "url": None},
    {"slug": "speakout-mental-health-outreach", "name": "SpeakOut Mental Health Outreach", "category": "community-outreach", "order": 1,
     "description": "Community wellbeing awareness and the MindCheck platform",
     "programmes": ["community-wellbeing-mental-health"], "logo_permission": None, "logo": "partner-speakout.jpg", "url": None},
    {"slug": "cnu-medical-institute", "name": "CNU Medical Institute (USA)", "category": "community-outreach", "order": 2,
     "description": "Healthcare support and community-based initiatives",
     "programmes": ["community-wellbeing-mental-health"], "logo_permission": None, "logo": "partner-cnu.jpg", "url": None},
    {"slug": "kelvin-oluchi-diabetes-foundation", "name": "Kelvin Oluchi Diabetes Foundation", "category": "community-outreach", "order": 3,
     "description": "Community health screening and education",
     "programmes": ["community-wellbeing-mental-health"], "logo_permission": None, "logo": None, "url": None},
    {"slug": "college-of-health-science-technology-keffi", "name": "College of Health Science & Technology, Keffi", "category": "community-outreach", "order": 4,
     "description": "Student volunteers and community mobilisation",
     "programmes": ["community-wellbeing-mental-health"], "logo_permission": None, "logo": None, "url": None},
]

PARTNERS_INTRO = ("We multiply our impact by partnering rather than acting alone. Almost every project in our "
                  "record was delivered alongside someone else — health bodies, schools, service organisations "
                  "and fellow foundations.")

PARTNER_CTA = {
    "heading": "Partner with us",
    "body": "We offer partners credible, community-rooted access to displaced and indigent Nigerians, on-the-ground "
            "delivery, and a commitment to honest reporting. We welcome programme partners, funders, technical "
            "collaborators and institutional allies.",
    "button": "Start a conversation",
}

# [PL 06] Actively pursued, NOT partners. Named here only as ambition, never as
# a relationship, and never on the Partners page.
PARTNERSHIPS_PURSUED = [
    "National Commission for Refugees, Migrants and Internally Displaced Persons — a formal partnership on the "
    "FCT–Nasarawa–Keffi resettlement corridor.",
    "UN agencies and country-based pooled funds — as a national implementing partner, in line with localisation "
    "commitments.",
    "State education and health authorities — for placement recognition and service integration.",
    "Corporate foundations and diaspora networks — for programme funding and the Synia Scholars Fund.",
]

WHAT_WE_OFFER_PARTNERS = [
    "Credible, community-rooted access to displaced and indigent Nigerians",
    "On-the-ground delivery in a corridor few organisations cover",
    "Documented programme models with defined costs and indicators",
    "A commitment to honest reporting, including when results disappoint",
    "A safeguarding standard that applies to everyone acting in our name",
]

# ---------------------------------------------------------------------------
# 10. ACCOUNTABILITY  [CP 17, 19, 20, 21; PO]
# ---------------------------------------------------------------------------

SAFEGUARDING_COMMITMENT = ("The Foundation is committed to the protection of children, vulnerable adults and every "
                           "person who comes into contact with our work. No programme begins delivery before our "
                           "Safeguarding Policy is adopted and in force, and no exception to this is permitted for "
                           "any reason, including funding deadlines.")

SAFEGUARDING_CONTROLS = [
    ("Vetting", "All staff, volunteers, tutors, mobilisers and partner personnel in contact with children are "
                "vetted and sign a code of conduct held on file."),
    ("Two-adult rule", "No unaccompanied one-to-one contact between an adult and a child."),
    ("Consent for images", "Written caregiver consent before any child is photographed or filmed, including in "
                           "wide shots. A child's full name is never published alongside their image."),
    ("No conditionality", "Support is never conditional on appearing in photography, films or fundraising "
                          "material, and anyone may decline without consequence. Consent may be withdrawn."),
    ("Reporting route", "A plain-language complaints and reporting route is displayed wherever we work, with a "
                        "named safeguarding focal point known to schools, partners and communities."),
    ("Partners bound too", "Every partner holding contact with children is covered by our safeguarding "
                           "requirements as a condition of the partnership."),
]

# Policies 01–05 are drafted and available for download; the remainder are in development.
POLICIES = [
    {"num": "01", "slug": "safeguarding", "title": "Safeguarding Policy",
     "subtitle": "Protection of children and adults at risk in all of the Foundation's work",
     "status": "Version 1.0 · approved by the Board of Trustees",
     "file": "SAF-Policy-01-Safeguarding.pdf",
     "summary": "Sets the Foundation's safeguarding commitment, the vetting and two-adult rules, consent for "
                "images, how a concern is reported and what happens next, and the records and review regime.",
     "category": "Safeguarding"},
    {"num": "02", "slug": "code-of-conduct", "title": "Code of Conduct",
     "subtitle": "The standard of behaviour required of everyone acting in the Foundation's name",
     "status": "Version 1.0 · approved by the Board of Trustees",
     "file": "SAF-Policy-02-Code-of-Conduct.pdf",
     "summary": "Signed by every trustee, member of staff, volunteer, consultant, ambassador and partner "
                "representative before engagement begins, and on each renewal.",
     "category": "Conduct"},
    {"num": "03", "slug": "pseah", "title": "Protection from Sexual Exploitation, Abuse and Harassment",
     "subtitle": "Zero tolerance, survivor-centred response, and the duty on everyone to report",
     "status": "Version 1.0 · approved by the Board of Trustees",
     "file": "SAF-Policy-03-PSEAH.pdf",
     "summary": "Adopts the six core principles of the Inter-Agency Standing Committee on protection from sexual "
                "exploitation and abuse, and sets out a survivor-centred response.",
     "category": "Safeguarding"},
    {"num": "04", "slug": "anti-fraud-whistleblowing", "title": "Anti-Fraud, Bribery, Corruption and Whistleblowing",
     "subtitle": "Protecting the funds entrusted to us, and protecting those who speak up",
     "status": "Version 1.0 · approved by the Board of Trustees",
     "file": "SAF-Policy-04-AntiFraud-Whistleblowing.pdf",
     "summary": "Zero tolerance of fraud, bribery, corruption and theft, whoever commits them and whatever their "
                "seniority — with protection for anyone who reports a concern in good faith.",
     "category": "Financial control"},
    {"num": "05", "slug": "conflict-of-interest", "title": "Conflict of Interest Policy",
     "subtitle": "Keeping decisions clean, and visibly so",
     "status": "Version 1.0 · approved by the Board of Trustees",
     "file": "SAF-Policy-05-Conflict-of-Interest.pdf",
     "summary": "Declaration, recording and management of actual, potential and perceived conflicts, with a "
                "register reviewed by the Board annually.",
     "category": "Governance"},
]

POLICIES_IN_DEVELOPMENT = [
    ("Financial controls & procurement", "In development",
     "Budget approval, payment authorisation, documented procurement, monthly review"),
    ("Complaints & feedback", "In development", "How anyone raises a concern, and what happens next"),
    ("Data protection", "In development", "Handling of personal data under the Nigeria Data Protection Act 2023"),
    ("Risk management", "In development", "A live register of key risks, owners and mitigations"),
]

FINANCIAL_CONTROLS = [
    ("Budget approval", "Programme budgets are approved by the Board before expenditure is committed."),
    ("Payment authorisation", "Defined authorisation thresholds, with separation between the person requesting a "
                              "payment and the person approving it."),
    ("Documented procurement", "Written quotations above threshold, and separation between specifying goods and "
                               "purchasing them."),
    ("Staged disbursement", "Grants to participants are released against milestones, not as lump sums, and no one "
                            "both selects a participant and releases their funds."),
    ("Signed records", "Distribution lists, receipts and delivery records retained for every item issued."),
    ("Monthly review", "Management accounts reviewed monthly against budget."),
]

DISCLOSURE_COMMITMENTS = [
    ("Annual report and accounts", "From the next full financial year"),
    ("Independently audited accounts", "Target: two consecutive years by 2028"),
    ("Cost per beneficiary for each flagship", "Once one full delivery cycle is complete"),
    ("Programme-level results with sources and dates", "From the 2026–27 academic year"),
]

FINANCIAL_CANDOUR = ("Stated plainly: the Foundation has not yet published audited accounts. We have moved from "
                     "family-and-friends giving to structured, partner-led delivery, and the financial systems are "
                     "being built to match. We would rather a prospective funder read that here than discover it "
                     "in due diligence.")

RISKS = [
    ("Safeguarding",
     "We work with children and vulnerable adults. A failure here would be both an ethical and an existential "
     "reputational failure.",
     "Policy adoption as a precondition of delivery; vetting; two-adult rule; consent discipline; reporting route; "
     "partner obligations"),
    ("Security & access",
     "Insecurity can restrict access to communities and endanger staff and participants.",
     "Community-rooted delivery; local partners; movement decisions made locally; no activity where staff or "
     "participants would be placed at risk"),
    ("Funding concentration",
     "The wider funding environment has contracted sharply, and over-reliance on any single source would be fragile.",
     "Diversification across individual, diaspora, corporate, institutional and partnership income; growth of "
     "recurring giving"),
    ("Over-extension",
     "Committing to more programmes than we can deliver would damage credibility and dilute quality.",
     "Phased portfolio; only programmes with a written model launch; honest status labelling"),
    ("Evidence deficit",
     "Without outcome data we cannot prove impact or compete for institutional funding.",
     "Baselines mandatory; monitoring framework; external evaluation planned"),
    ("Key-person dependency",
     "Concentration of relationships, knowledge and profile in the founder.",
     "Independent Trustees; documented programme models; delegated programme ownership; leadership development"),
    ("Tenure & investment",
     "Improving shelter a household is later evicted from converts a grant into a loss.",
     "Right to remain verified before shelter works; Protection paired with Shelter; written site permissions"),
    ("Financial control",
     "Weak controls in a growing organisation create exposure to error and to fraud.",
     "Separation of duties; staged disbursement; documented procurement; Finance & Audit sub-committee; audit"),
]

PROGRAMME_PRELAUNCH = [
    ("A written programme model",
     "Purpose, target group, theory of change, standard package, unit cost, indicators and exit criteria, signed "
     "off by the Board."),
    ("A named owner",
     "Accountable for the numbers being real and current, not for them being flattering."),
    ("A baseline",
     "Without a baseline at enrolment, change cannot be claimed at all — the most frequent and most costly "
     "omission in first-time programming."),
    ("A small indicator set",
     "Typically three to five, distinguishing outputs from outcomes."),
    ("Defined exit criteria",
     "So that completion is a status we record rather than a contact that lapses."),
]

INDICATORS = [
    ("Education & Skills",
     "Children assessed, enrolled or re-enrolled; terms of support delivered",
     "Retention to end of academic year; attendance above threshold; transition to the next grade; girls retained "
     "across the year"),
    ("Livelihoods",
     "Participants trained; grants disbursed; savings groups formed; mentoring sessions delivered",
     "Enterprises still trading at 6 and 12 months; median income change against baseline; active savings balance; "
     "repeat buyers secured"),
    ("Shelter, WASH & Protection",
     "Shelters assessed and completed; kits distributed; occupancy documented",
     "Shelters meeting standard on re-inspection; households reporting improved safety and privacy; occupancy "
     "retained at 12 months"),
]

MEL_POSITION = ("As at July 2026 the monitoring framework is being introduced rather than long established, and "
                "the Foundation has not yet published audited accounts or commissioned an external evaluation. "
                "Both are in our roadmap. We set this out here because a funder will discover it in due diligence, "
                "and it is better that they read it from us.")

ROADMAP = [
    ("Phase 1", "to mid-2027",
     ["Adopt the Safeguarding Policy and code of conduct.",
      "Launch three flagships — Train a Child, Enterprise Development, Safe Shelter — each with a written model.",
      "Establish the Synia Scholars Fund architecture.",
      "Introduce the monitoring framework.",
      "Recruit independent Trustees and a finance lead."],
     "All three flagships have a model, a unit cost, an indicator set and one completed delivery cycle with data"),
    ("Phase 2", "2027–2028",
     ["Launch Protection & Rights, Savings & Financial Inclusion, WASH, and Emergency Response & Household Recovery.",
      "Formalise the Community Wellbeing platform.",
      "Publish annual report and accounts.",
      "Register as a UN implementing partner and join relevant clusters."],
     "Two years of audited accounts; one institutional grant delivered and reported on time; monitoring producing "
     "outcome data"),
    ("Phase 3", "2028–2029",
     ["Launch Youth Skills & Employability, Durable Solutions & Resettlement Support, and Women's Economic "
      "Empowerment at scale.",
      "Formalise the NCFRMI partnership.",
      "Commission an external evaluation.",
      "Build the country and regional model layer."],
     "Published cost per beneficiary for each flagship; one external evaluation completed; formal federal or "
     "state partnership in place"),
]

BENCHMARK_NOTE = ("In July 2026 we commissioned an independent strategic review of our programme architecture, "
                  "which scored our portfolio at 52 out of 100 against the standard expected of an "
                  "institutional-donor-ready organisation. We publish that number deliberately. The review "
                  "identified a clear path to 75 within twelve months and to 90 within three years, and its "
                  "recommendations form the roadmap above. We will re-run the same assessment and report the result.")

# ---------------------------------------------------------------------------
# 11. REPORTS & PUBLICATIONS
# ---------------------------------------------------------------------------

PUBLICATIONS = [
    {"title": "Corporate Profile 2026", "category": "Corporate", "date": "July 2026",
     "file": "SAF-Corporate-Profile-2026.pdf",
     "summary": "Edition 2. Who we are, what we do, how we are governed, and what we hold ourselves accountable "
                "for — including our theory of change, track record, risk register and roadmap to 2029.",
     "pages": "29 pages"},
    {"title": "Our Programmes — structure guide", "category": "Programmes", "date": "July 2026",
     "file": "SAF-Our-Programmes-Structure-Guide.pdf",
     "summary": "A plain-language guide to the three pillars and the twelve programmes within them — what each "
                "one does, who it is for, what it sets out to change, and which are running today.",
     "pages": "10 pages"},
    {"title": "Leadership Biographies", "category": "Governance", "date": "July 2026",
     "file": "SAF-Leadership-Biographies.pdf",
     "summary": "Biographies of the Board of Trustees, its specialist advisers, and the executive team "
                "responsible for delivering the Foundation's work.",
     "pages": "6 pages"},
]

PUBLICATIONS_PENDING = [
    ("Annual report and accounts", "From the next full financial year"),
    ("Independently audited accounts", "Target: two consecutive years by 2028"),
    ("Programme-level results with sources and dates", "From the 2026–27 academic year"),
]

# ---------------------------------------------------------------------------
# 12. GET INVOLVED
# ---------------------------------------------------------------------------

GET_INVOLVED = [
    {"slug": "donate", "num": "01", "title": "Donate", "icon": "heart",
     "summary": "Fund a child's school year, a household's shelter repair, or a trader's start in business. "
                "One-off or recurring gifts, from ₦5,000 upward.",
     "detail": "Recurring giving matters more to us than any single total, because it lets us commit to a child "
               "for a full academic year.",
     "cta": "Give now"},
    {"slug": "partner", "num": "02", "title": "Partner with us", "icon": "handshake",
     "summary": "Bring your organisation's resources, reach or technical expertise to a shared programme of work.",
     "detail": "Partnership is how we multiply our impact, and we welcome programme partners, funders, technical "
               "collaborators and institutional allies.",
     "cta": "Start a conversation"},
    {"slug": "volunteer", "num": "03", "title": "Volunteer", "icon": "people",
     "summary": "Give your time and skills in your own community and on our outreaches.",
     "detail": "Volunteers working with children are subject to vetting and a code of conduct.",
     "cta": "Apply to volunteer"},
    {"slug": "ambassador", "num": "04", "title": "Become an ambassador", "icon": "megaphone",
     "summary": "Champion our mission and amplify its impact beyond borders.",
     "detail": "Our ambassadors carry the Foundation's work into their own networks, at home and in the diaspora.",
     "cta": "Register your interest"},
]

# [WB 05] Preset tiers from ₦5,000 upward, each labelled with what it funds.
# The amounts are presets; the descriptions describe the standard package, not a
# verified unit cost — unit costs are published once a delivery cycle completes.
DONATION_TIERS = [
    {"amount": 5000,  "label": "₦5,000",  "funds": "Books and exercise materials for a child returning to school"},
    {"amount": 10000, "label": "₦10,000", "funds": "A school uniform and shoes for a child in Train a Child"},
    {"amount": 25000, "label": "₦25,000", "funds": "Toward a term of school fees, levies and examination costs"},
    {"amount": 50000, "label": "₦50,000", "funds": "Toward a household kit and shelter repair materials"},
    {"amount": 100000, "label": "₦100,000", "funds": "Toward seed capital and mentoring for one trader"},
]

DONATION_DESIGNATIONS = [
    ("where-most-needed", "Where it is most needed"),
    ("education-skills", "Education & Skills — educate the mind"),
    ("livelihoods-economic-inclusion", "Livelihoods & Economic Inclusion — equip the hands"),
    ("shelter-wash-protection", "Shelter, WASH & Protection — secure the home"),
    ("learning-access-retention", "Train a Child (Learning Access & Retention)"),
    ("enterprise-development", "Enterprise Development"),
    ("safe-shelter", "Safe Shelter"),
    ("community-wellbeing-mental-health", "Community Wellbeing & Mental Health (MindCheck)"),
]

# Bank details are supplied privately by the Foundation [WB 10] and are NOT in
# any handover document. Placeholders are marked so they cannot go live by
# accident — the build fails loudly on these if PLACEHOLDER_GUARD is enabled.
BANK_TRANSFER = {
    "bank": "[BANK NAME — to be supplied by the Foundation]",
    "account_name": "Synia Aid Foundation",
    "account_number": "[ACCOUNT NUMBER — to be supplied]",
    "sort_or_swift": "[SWIFT/BIC — to be supplied for international transfers]",
    "reference": "Please use the reference SAF-[YOUR SURNAME] so we can reconcile your gift, and email "
                 "info@syniafoundation.org so we can send your receipt.",
}

VOLUNTEER_ROLES = [
    ("Community outreach volunteer",
     "Support health, wellbeing and dignity outreaches in Keffi, the FCT and Ogun. Mobilisation, registration, "
     "crowd care and set-up."),
    ("Learning support volunteer",
     "Support catch-up learning blocks and school follow-up visits under the Learning Access & Retention "
     "Programme. Subject to vetting."),
    ("Skills and enterprise mentor",
     "Six months of mentoring for a participant in the Enterprise Development Programme. Suited to experienced "
     "traders and business owners."),
    ("Professional skills volunteer",
     "Legal, monitoring and evaluation, design, finance or communications support offered remotely or in Abuja."),
]

VOLUNTEER_VETTING = ("Volunteers working with children are subject to vetting and a code of conduct. That means a "
                     "documented selection process, verified identity, at least two references taken up before "
                     "engagement, a check for any history of concern, safeguarding induction before your first "
                     "contact with a programme, and a signed Code of Conduct held on file. The two-adult rule "
                     "applies to everyone: there is no unaccompanied one-to-one contact between an adult and a "
                     "child in any Foundation activity.")

AMBASSADOR_WHAT = [
    "Champion the Foundation's work in your own network, at home or in the diaspora.",
    "Introduce us to people and organisations who could partner with or fund a programme.",
    "Represent the Foundation at events, and help us raise for a specific programme or appeal.",
    "Carry the same standard as everyone else acting in our name: ambassadors sign the Code of Conduct.",
]

FUNDER_EXPECTATIONS = [
    "Programme models with defined costs and indicators",
    "Honest reporting, including where results disappoint",
    "Restricted funds honoured and separately accounted",
    "A safeguarding standard binding on staff, volunteers and partners",
    "A named contact who will answer a difficult question directly",
]

# ---------------------------------------------------------------------------
# 13. NEWS  — seeded strictly from the documented milestone record [CP 15, 16]
#     See CONTENT-NOTES.md: these are factual notes drawn from the Corporate
#     Profile, to be reviewed and extended by the Foundation in the CMS.
# ---------------------------------------------------------------------------

NEWS = [
    {
        "slug": "professionalising-the-foundation",
        "title": "A strategic review, three pillars, and twelve programme models",
        "date_iso": "2026-07-31", "date_display": "July 2026",
        "category": "Foundation news", "pillar": None,
        "excerpt": "The Foundation completed a strategic review of its programme architecture, refreshed the "
                   "three-pillar structure, wrote a model for every programme, and published Edition 2 of the "
                   "Corporate Profile.",
        "body": [
            "In July 2026 the Foundation completed a deliberate review of everything it does. Programmes that "
            "overlapped were consolidated, work that had been running without a name was named, and protection, "
            "wellbeing and durable-solutions work was added to the portfolio.",
            "The review produced a refreshed three-pillar architecture — Education &amp; Skills, Livelihoods &amp; "
            "Economic Inclusion, and Shelter, WASH &amp; Protection — with twelve programmes underneath it and a "
            "written model behind each one.",
            "It also produced a discipline that now runs through all of the Foundation's published material: we "
            "describe what is running as running, what is planned as planned, and we do not claim a number we "
            "cannot evidence. Three programmes are operating today, one is in set-up, and the remainder are "
            "scheduled.",
            "The review scored the portfolio at 52 out of 100 against the standard expected of an "
            "institutional-donor-ready organisation, and identified a path to 75 within twelve months. That number "
            "is published deliberately. The same assessment will be re-run and the result reported.",
        ],
    },
    {
        "slug": "durumi-assessment-and-learning-spaces",
        "title": "Durumi IDP camp: a needs assessment, and a classroom built from within the camp",
        "date_iso": "2026-06-30", "date_display": "2026",
        "category": "Programmes", "pillar": "education-skills",
        "excerpt": "A multi-sector needs assessment at Durumi camp in the FCT, and an agreement with camp "
                   "coordinators on a classroom furniture project — built by a carpenter living in the camp.",
        "body": [
            "The Foundation carried out a multi-sector needs assessment at Durumi IDP camp in the Federal Capital "
            "Territory, and agreed a classroom furniture project with camp coordinators.",
            "The furniture is being built by a carpenter living in the camp. The same expenditure creates a "
            "learning space and an income — an example of the Foundation's operating principle that where a "
            "community holds the skill, we buy it there.",
            "The project began with an assessment and an agreement with camp coordinators, not with a decision "
            "made in Abuja. No intervention opens without consultation with the community it will serve.",
        ],
    },
    {
        "slug": "love-on-the-street-2026",
        "title": "Love on the Street: a birthday marked with service in Keffi",
        "date_iso": "2026-05-20", "date_display": "20 May 2026",
        "category": "Outreach", "pillar": "livelihoods-economic-inclusion",
        "excerpt": "On 20 May the founder's birthday was marked with service rather than celebration — supporting "
                   "women traders in Keffi and honouring security personnel.",
        "body": [
            "On 20 May 2026 the Foundation ran Love on the Street in Keffi, Nasarawa State. The founder's birthday "
            "was marked with service rather than celebration.",
            "The day supported vulnerable women traders in the market and honoured security personnel serving in "
            "the community.",
        ],
    },
    {
        "slug": "leadership-development-summit-2026",
        "title": "SAF Leadership Development Summit: strategic leadership in a changing world",
        "date_iso": "2026-03-31", "date_display": "2026",
        "category": "Events", "pillar": "education-skills",
        "excerpt": "A youth leadership summit on ethical leadership and emotional intelligence, attended by "
                   "representatives of the Emir of Keffi.",
        "body": [
            "The Foundation convened the SAF Leadership Development Summit on the theme “Strategic Leadership "
            "in a Changing World”.",
            "The summit addressed ethical leadership and emotional intelligence with young participants, and was "
            "attended by representatives of the Emir of Keffi.",
        ],
    },
    {
        "slug": "mindcheck-app-launch",
        "title": "MindCheck launches: a free, confidential way to reach support early",
        "date_iso": "2026-01-21", "date_display": "21 January 2026",
        "category": "Programmes", "pillar": "across-all-pillars",
        "excerpt": "On 21 January, with SpeakOut Mental Health Outreach, the Foundation piloted and launched the "
                   "MindCheck App — a free, confidential platform to assess wellbeing and reach support early.",
        "body": [
            "On 21 January 2026, with SpeakOut Mental Health Outreach, the Foundation piloted and launched the "
            "MindCheck App.",
            "MindCheck is a free and confidential way for someone to assess their own wellbeing and reach support "
            "early, without stigma. It sits within the Foundation's cross-cutting Community Wellbeing &amp; Mental "
            "Health work.",
            "That work is among the longest-running the Foundation does. It is now being formalised — given its "
            "own budget line, indicators and a named owner — because work described as cross-cutting but left "
            "unmanaged is not integrated, it is simply unowned.",
        ],
    },
    {
        "slug": "community-mental-health-road-walk-2026",
        "title": "Students take wellbeing education into the streets of Keffi",
        "date_iso": "2026-01-19", "date_display": "19 January 2026",
        "category": "Outreach", "pillar": "across-all-pillars",
        "excerpt": "On 19 January, with students of the College of Health Science and Technology, Keffi, "
                   "volunteers took mental-health education across the community.",
        "body": [
            "On 19 January 2026 the Foundation ran a Community Mental Health Road Walk across Keffi with students "
            "of the College of Health Science and Technology, Keffi.",
            "Volunteers took wellbeing education into the streets, reaching people who would not attend a clinic "
            "or a formal session. A road walk becomes a district-wide conversation — which is how the Foundation "
            "builds trust in a community before a programme begins.",
        ],
    },
    {
        "slug": "pad-a-girl-ecwa-school-keffi",
        "title": "Pad A Girl reaches ECWA School, Keffi",
        "date_iso": "2025-05-22", "date_display": "22 May 2025",
        "category": "Programmes", "pillar": "education-skills",
        "excerpt": "On 22 May 2025, with Deborah Counselling Consult, Pad A Girl delivered health education, "
                   "safeguarding sensitisation and the distribution of pads and books at ECWA School, Keffi.",
        "body": [
            "On 22 May 2025, with Deborah Counselling Consult, the Foundation's Pad A Girl campaign reached ECWA "
            "School in Keffi, Nasarawa State.",
            "The day combined menstrual health education, safeguarding sensitisation and the distribution of "
            "sanitary pads and educational books.",
            "Pad A Girl now sits inside the Learning Access &amp; Retention Programme, as part of the support that "
            "keeps girls in school across a full academic year.",
        ],
    },
]

# ---------------------------------------------------------------------------
# 14. STORIES  [WB 04] — filterable by pillar and format. The documentary work
#     is delivered from September 2026; the section is built to receive it.
# ---------------------------------------------------------------------------

STORIES = [
    {
        "slug": "a-classroom-built-from-within-the-camp",
        "title": "A classroom built from within the camp",
        "format": "Written", "pillar": "education-skills",
        "date_display": "2026", "date_iso": "2026-06-30",
        "excerpt": "At Durumi, the furniture for a learning space is being made by a carpenter who lives in the "
                   "camp. One budget line, two results.",
        "body": [
            "The Foundation's assessment at Durumi IDP camp in the Federal Capital Territory found what "
            "assessments in non-camp and camp settings across Nigeria tend to find: children present, willing and "
            "without a place to sit and learn.",
            "The response was a classroom furniture project agreed with camp coordinators. The detail that matters "
            "is who is building it. The carpenter lives in the camp.",
            "Where a community holds the skill, we buy it there. The same expenditure creates a learning space and "
            "an income — and a piece of furniture made by a neighbour is a piece of furniture that gets repaired "
            "rather than replaced.",
        ],
    },
    {
        "slug": "the-market-women-of-keffi",
        "title": "The market women of Keffi",
        "format": "Written", "pillar": "livelihoods-economic-inclusion",
        "date_display": "20 May 2026", "date_iso": "2026-05-20",
        "excerpt": "A trader who loses her stock loses her customers, then her credit, then her standing. "
                   "Love on the Street began where that chain starts.",
        "body": [
            "On 20 May 2026 the Foundation spent the day in the market at Keffi, supporting women traders and "
            "honouring the security personnel who work alongside them.",
            "The economics of a small trade are unforgiving. A trader who loses her stock loses her customers, "
            "then her credit, then her standing in the market — and each loss makes the next one harder to "
            "reverse.",
            "It is the reason the Enterprise Development Programme releases capital in stages against milestones "
            "rather than as a lump sum, pairs it with six months of mentoring, and measures whether the business "
            "is still trading twelve months later rather than whether a grant was disbursed.",
        ],
    },
]

STORIES_NOTE = ("Three documentary narratives are in production from September 2026. This section is built to "
                "receive them: film, photo essays and written pieces, filterable by pillar and by format.")

STORY_FORMATS = ["Film", "Photo essay", "Written"]

# ---------------------------------------------------------------------------
# 15. CONTACT
# ---------------------------------------------------------------------------

CONTACT_SUBJECTS = [
    ("general", "General enquiry"),
    ("partnership", "Partnership enquiry"),
    ("funding", "Funding or institutional donor enquiry"),
    ("volunteer", "Volunteering"),
    ("ambassador", "Becoming an ambassador"),
    ("media", "Media or press"),
    ("donation", "A question about a donation"),
    ("safeguarding", "A safeguarding concern or complaint"),
]

COMPLAINTS_STEPS = [
    ("Tell us", "Raise your concern by telephone, by email, in person, or in writing. You may raise it "
                "anonymously, and you may raise it without going through the person whose conduct is in question."),
    ("We record it the same day", "The Safeguarding Focal Point records the concern on the day it is received and "
                                  "takes immediate action to secure the safety of anyone affected."),
    ("Support comes first", "Support to the person affected comes before anything else — medical, psychosocial, "
                            "legal or protection referral as required, with their informed agreement."),
    ("We investigate fairly", "Investigation is conducted promptly and by someone with no involvement in the "
                              "matter. Serious concerns are notified to the Board within seventy-two hours."),
    ("We respond", "We acknowledge, investigate and respond. Where an allegation may involve a criminal offence, "
                   "the matter is referred to the Nigeria Police Force or other competent authority, subject to "
                   "the safety and wishes of the person affected."),
]

COMPLAINTS_PROTECTION = ("No one raising a concern in good faith will suffer any disadvantage, and no one's "
                         "support will be affected. Reports made in good faith attract full protection under the "
                         "Foundation's whistleblowing provisions.")


# ---------------------------------------------------------------------------
# 16. PHOTOGRAPHY
#
# Supplied by the Foundation through SageView Productions (its contracted media
# agency — a supplier, not a programme partner, so it is credited in the site
# credit line and never on the Partners page).
#
# Safeguarding rules applied to every entry [WB 07; PO 01 §6.2]:
#   · alt text describes only what is visible. No photograph is captioned as
#     being from a named camp, school, state or event unless the Foundation
#     confirms it — a caption is a factual claim.
#   · no child's name appears anywhere near an image.
#   · all EXIF data, including any GPS location, is stripped at build time.
#   · `consent` records the Foundation's confirmation status. Nothing here is
#     published on the strength of an assumption; see CONTENT-NOTES.md.
#   · `withheld` images are downloaded and available but deliberately NOT
#     published, with the reason stated.
# ---------------------------------------------------------------------------

PHOTO_CREDIT = "SageView Productions"

PHOTOS = {
    # --- learning ---------------------------------------------------------
    "classroom-boy-desk": {
        "file": "DSC06584.JPG",
        "alt": "A boy sitting at a wooden desk in a classroom, smiling towards the camera",
        "focus": "upper", "tags": ["education", "portrait"]},
    "classroom-girl-bench": {
        "file": "DSC06597.JPG",
        "alt": "A girl in a blue dress sitting on a classroom bench, with other children behind her",
        "focus": "upper", "tags": ["education"]},
    "classroom-group": {
        "file": "DSC06657.JPG",
        "alt": "A group of children standing together between the benches of their classroom",
        "focus": "upper", "tags": ["education", "group"]},
    "classroom-boy-yellow": {
        "file": "DSC06671.JPG",
        "alt": "A boy in a yellow school shirt smiling in a classroom",
        "focus": "upper", "tags": ["education", "portrait"]},
    "classroom-writing": {
        "file": "IMG_1195.JPG",
        "alt": "A boy writing in an exercise book at a shared classroom desk while other children work beside him",
        "tags": ["education"]},
    "classroom-lesson": {
        "file": "IMG_1199.JPG",
        "alt": "Children sitting at their benches during a lesson, some writing and some listening",
        "focus": "upper", "tags": ["education"]},
    "classroom-desks": {
        "file": "IMG_1213.JPG",
        "alt": "Children reading and writing together at classroom desks",
        "tags": ["education"]},
    "classroom-friends": {
        "file": "DSC06576.JPG",
        "alt": "Two children leaning on a classroom bench together, smiling",
        "tags": ["education", "group"]},
    "classroom-doorway": {
        "file": "DSC06603.JPG",
        "alt": "Children looking towards the camera from the doorway of their classroom",
        "focus": "upper", "tags": ["education", "group"]},

    # --- children and community ------------------------------------------
    "children-outside": {
        "file": "DSC06766.JPG",
        "alt": "Two children waving, standing outside with others behind them",
        "focus": "upper", "tags": ["community", "group"]},
    "children-laughing": {
        "file": "DSC07050.JPG",
        "alt": "A young girl laughing, with other children playing behind her",
        "focus": "upper", "tags": ["community", "portrait"]},
    "children-community": {
        "file": "IMG_1173.JPG",
        "alt": "A group of children standing together and smiling in their community",
        "tags": ["community", "group"]},
    "children-yard": {
        "file": "DSC07071.JPG",
        "alt": "Children gathered outdoors in their community",
        "tags": ["community", "group"]},
    "children-playing": {
        "file": "IMG_0021.JPG",
        "alt": "Two children lying on the ground, laughing together",
        "focus": "upper", "tags": ["community", "group"]},
    "boys-lorry": {
        "file": "o+boy5.jpg",
        "alt": "Two boys resting against the back of a brightly painted lorry",
        "focus": "upper", "tags": ["community", "group"]},

    # --- inclusion --------------------------------------------------------
    "wheelchair-crossing": {
        "file": "IMG_0025.JPG",
        "alt": "A young person using a wheelchair being helped across a road, smiling",
        "focus": "upper", "tags": ["disability", "community"]},

    # --- women ------------------------------------------------------------
    "women-gathering": {
        "file": "IMG_9169.JPG",
        "alt": "Women sitting together at a community gathering",
        "tags": ["women", "group"]},
    "women-smiling": {
        "file": "IMG_9186.JPG",
        "alt": "A group of women and girls standing together, smiling",
        "tags": ["women", "group"]},
    "woman-portrait": {
        "file": "mama2.jpg",
        "alt": "A woman in a green head covering smiling, photographed on a roadside",
        "focus": "upper", "tags": ["women", "portrait"]},

    # --- older people -----------------------------------------------------
    "elder-smiling": {
        "file": "old5.jpg",
        "alt": "An older man sitting on a kerb, smiling towards the camera",
        "focus": "upper", "tags": ["older", "portrait"]},
    "elder-seated": {
        "file": "IMG_9597.jpg",
        "alt": "An older man sitting beside a railing, smiling and gesturing towards the camera",
        "focus": "upper", "tags": ["older", "portrait"]},
}

# Downloaded and held, deliberately not published. The Foundation's own rule is
# that people are shown as capable partners, never as objects of pity, and that
# no image may show a person in distress. These read as destitution rather than
# agency. The decision is the Foundation's to overturn — see CONTENT-NOTES.md.
PHOTOS_WITHHELD = {
    "IMG_4016.JPG": "A woman and two small children sitting on bare ground. Composed with care, but it "
                    "reads as destitution rather than agency, and a small child is identifiable.",
    "IMG_4017.JPG": "A man sitting at a roadside with his belongings in sacks. Same reasoning.",
    "IMG_4018.JPG": "An older man sitting on a roadside kerb. Dignified, but it depicts the subject at his "
                    "lowest point; the smiling portraits of older men are used instead.",
}


# Which photograph illustrates which page. Kept as a mapping rather than a
# field on each record so that the Foundation can re-point an image without
# touching programme content — and so that no photograph is ever tied to a
# claim about where or when it was taken.
PROGRAMME_PHOTOS = {
    "learning-access-retention": "classroom-writing",
    "synia-scholars-fund": "classroom-boy-desk",
    "youth-skills-employability": "classroom-desks",
    "enterprise-development": "woman-portrait",
    "savings-financial-inclusion": "women-gathering",
    "womens-economic-empowerment": "women-smiling",
    "safe-shelter": "children-outside",
    "water-sanitation-hygiene": "children-community",
    "emergency-response-household-recovery": "children-yard",
    "protection-rights": "elder-seated",
    "community-wellbeing-mental-health": "elder-smiling",
    "durable-solutions-resettlement": "boys-lorry",
}

PILLAR_PHOTOS = {
    "education-skills": "classroom-lesson",
    "livelihoods-economic-inclusion": "women-smiling",
    "shelter-wash-protection": "children-outside",
}

NEWS_PHOTOS = {
    "professionalising-the-foundation": "classroom-group",
    "durumi-assessment-and-learning-spaces": "classroom-doorway",
    "love-on-the-street-2026": "women-smiling",
    "leadership-development-summit-2026": "women-gathering",
    "mindcheck-app-launch": "elder-smiling",
    "community-mental-health-road-walk-2026": "children-community",
    "pad-a-girl-ecwa-school-keffi": "classroom-girl-bench",
}

STORY_PHOTOS = {
    "a-classroom-built-from-within-the-camp": "classroom-desks",
    "the-market-women-of-keffi": "woman-portrait",
}
