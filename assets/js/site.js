/* Synia Aid Foundation — site behaviour.
   Progressive enhancement only: every page works with JavaScript disabled.
   No third-party scripts. Analytics load only after explicit consent. */
(function () {
  'use strict';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------------
     Configuration. The Foundation's developer sets these once at handover.
     --------------------------------------------------------------------- */
  var CONFIG = window.SAF_CONFIG || {};
  var FORM_ENDPOINT   = CONFIG.formEndpoint || '';     // e.g. '/api/forms'
  var DONATE_ENDPOINT = CONFIG.donateEndpoint || '';   // Paystack / Flutterwave checkout
  var ANALYTICS_SRC   = CONFIG.analyticsSrc || '';     // privacy-respecting analytics
  var CONTACT_EMAIL   = 'info@syniafoundation.org';

  /* ---------------------------------------------------------------------
     Sticky header shadow
     --------------------------------------------------------------------- */
  var header = $('[data-header]');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------------------------------------------------------------------
     Mobile navigation
     --------------------------------------------------------------------- */
  var burger = $('[data-burger]');
  var nav    = $('#site-nav');
  var scrim  = $('[data-scrim]');

  function setNav(open) {
    if (!burger || !nav) return;
    burger.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('is-locked', open);
    if (scrim) { scrim.hidden = !open; scrim.classList.toggle('is-open', open); }
    if (open) {
      var first = nav.querySelector('a, button');
      if (first) first.focus();
    }
  }

  if (burger) {
    burger.addEventListener('click', function () {
      setNav(burger.getAttribute('aria-expanded') !== 'true');
    });
  }
  if (scrim) scrim.addEventListener('click', function () { setNav(false); });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (burger && burger.getAttribute('aria-expanded') === 'true') {
      setNav(false);
      burger.focus();
    }
  });

  // Keep state honest when resizing across the desktop breakpoint.
  var desktop = window.matchMedia('(min-width: 1140px)');
  var onBreak = function (e) { if (e.matches) setNav(false); };
  if (desktop.addEventListener) desktop.addEventListener('change', onBreak);
  else if (desktop.addListener) desktop.addListener(onBreak);

  // Dropdown disclosure buttons (touch devices — no hover dependency)
  $$('.nav__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      var dd = btn.parentNode.querySelector('.dd');
      btn.setAttribute('aria-expanded', String(!open));
      if (dd) dd.classList.toggle('is-open', !open);
    });
  });

  /* ---------------------------------------------------------------------
     Cookie consent. Nothing non-essential runs before a choice is made.
     --------------------------------------------------------------------- */
  var COOKIE_KEY = 'saf-consent-v1';
  var banner = $('[data-cookie]');

  function readConsent() {
    try { return window.localStorage.getItem(COOKIE_KEY); } catch (e) { return null; }
  }
  function writeConsent(v) {
    try { window.localStorage.setItem(COOKIE_KEY, v); } catch (e) { /* storage blocked */ }
  }
  function loadAnalytics() {
    if (!ANALYTICS_SRC) return;
    if (document.querySelector('script[data-analytics]')) return;
    var s = document.createElement('script');
    s.src = ANALYTICS_SRC;
    s.defer = true;
    s.setAttribute('data-analytics', '');
    document.head.appendChild(s);
  }

  if (banner) {
    var choice = readConsent();
    if (!choice) {
      banner.hidden = false;
    } else if (choice === 'accepted') {
      loadAnalytics();
    }
    var accept = $('[data-cookie-accept]', banner);
    var reject = $('[data-cookie-reject]', banner);
    if (accept) accept.addEventListener('click', function () {
      writeConsent('accepted'); banner.hidden = true; loadAnalytics();
    });
    if (reject) reject.addEventListener('click', function () {
      writeConsent('rejected'); banner.hidden = true;
    });
  }

  // Any page can offer a "change your cookie choice" control.
  $$('[data-cookie-reset]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      e.preventDefault();
      try { window.localStorage.removeItem(COOKIE_KEY); } catch (err) {}
      if (banner) banner.hidden = false;
      window.scrollTo({ top: document.body.scrollHeight, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  /* ---------------------------------------------------------------------
     Reveal on scroll
     --------------------------------------------------------------------- */
  var revealables = $$('[data-reveal]');
  if (revealables.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------------------------------------------------------------------
     Donation widget
     --------------------------------------------------------------------- */
  var donate = $('[data-donate]');
  if (donate) {
    var custom   = $('[data-donate-custom]', donate);
    var out      = $('[data-donate-amount]', donate);
    var outFreq  = $('[data-donate-freq]', donate);
    var submit   = $('[data-donate-submit]', donate);

    var fmt = function (n) {
      try { return '₦' + Number(n).toLocaleString('en-NG'); }
      catch (e) { return '₦' + n; }
    };

    function currentAmount() {
      var checked = donate.querySelector('input[name="amount"]:checked');
      if (checked && checked.value === 'custom') {
        var v = parseFloat(custom && custom.value);
        return isNaN(v) ? 0 : v;
      }
      return checked ? parseFloat(checked.value) : 0;
    }

    function refresh() {
      var amt = currentAmount();
      var freq = donate.querySelector('input[name="frequency"]:checked');
      var monthly = freq && freq.value === 'monthly';
      if (out) out.textContent = amt > 0 ? fmt(amt) : '—';
      if (outFreq) outFreq.textContent = monthly ? 'every month' : 'one-off gift';
      if (submit) {
        submit.textContent = amt > 0
          ? (monthly ? 'Give ' + fmt(amt) + ' monthly' : 'Give ' + fmt(amt))
          : 'Choose an amount';
        submit.disabled = !(amt >= 5000);
      }
      var warn = $('[data-donate-min]', donate);
      if (warn) warn.hidden = !(amt > 0 && amt < 5000);
    }

    $$('input[name="amount"], input[name="frequency"]', donate).forEach(function (el) {
      el.addEventListener('change', refresh);
    });
    if (custom) {
      custom.addEventListener('input', function () {
        var radio = donate.querySelector('input[name="amount"][value="custom"]');
        if (radio) radio.checked = true;
        refresh();
      });
      custom.addEventListener('focus', function () {
        var radio = donate.querySelector('input[name="amount"][value="custom"]');
        if (radio) { radio.checked = true; refresh(); }
      });
    }
    refresh();
  }

  /* ---------------------------------------------------------------------
     Filters (programmes, stories, projects, news)
     --------------------------------------------------------------------- */
  $$('[data-filter-group]').forEach(function (group) {
    var key      = group.getAttribute('data-filter-group');
    var targets  = $$('[data-filter-target="' + key + '"] [data-facets]');
    var counter  = $('[data-filter-count="' + key + '"]');
    var empty    = $('[data-filter-empty="' + key + '"]');
    var state    = {};

    function apply() {
      var shown = 0;
      targets.forEach(function (item) {
        var facets = (item.getAttribute('data-facets') || '').split(/\s+/);
        var ok = Object.keys(state).every(function (dim) {
          return state[dim] === 'all' || facets.indexOf(state[dim]) !== -1;
        });
        item.hidden = !ok;
        if (ok) shown++;
      });
      if (counter) {
        counter.textContent = shown + (shown === 1 ? ' item' : ' items');
      }
      if (empty) empty.hidden = shown !== 0;
    }

    $$('[data-filter]', group).forEach(function (btn) {
      var dim = btn.getAttribute('data-dimension') || 'default';
      if (!(dim in state)) state[dim] = 'all';
      if (btn.getAttribute('aria-pressed') === 'true') state[dim] = btn.getAttribute('data-filter');

      btn.addEventListener('click', function () {
        state[dim] = btn.getAttribute('data-filter');
        $$('[data-filter][data-dimension="' + dim + '"]', group).forEach(function (b) {
          b.setAttribute('aria-pressed', String(b === btn));
        });
        apply();
      });
    });
    apply();
  });

  /* ---------------------------------------------------------------------
     Site search — a small index, fetched only on the search page.
     --------------------------------------------------------------------- */
  var search = $('[data-search]');
  if (search) {
    var input   = $('[data-search-input]', search);
    var results = $('[data-search-results]', search);
    var status  = $('[data-search-status]', search);
    var index   = null;

    var params = new URLSearchParams(window.location.search);
    var initial = params.get('q') || '';
    if (initial && input) input.value = initial;

    function highlight(text, terms) {
      var safe = text.replace(/[<>&]/g, function (c) {
        return { '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c];
      });
      terms.forEach(function (t) {
        if (t.length < 2) return;
        safe = safe.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'),
          '<mark>$1</mark>');
      });
      return safe;
    }

    function run(q) {
      if (!index) return;
      var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
      if (!terms.length) {
        results.innerHTML = '';
        status.textContent = 'Type a word or two to search the site.';
        return;
      }
      var hits = index.map(function (doc) {
        var hay = (doc.t + ' ' + doc.s + ' ' + doc.b).toLowerCase();
        var score = 0;
        terms.forEach(function (t) {
          if (doc.t.toLowerCase().indexOf(t) !== -1) score += 8;
          if (doc.s.toLowerCase().indexOf(t) !== -1) score += 4;
          var m = hay.split(t).length - 1;
          score += Math.min(m, 6);
        });
        return { doc: doc, score: score };
      }).filter(function (h) { return h.score > 0; })
        .sort(function (a, b) { return b.score - a.score; })
        .slice(0, 40);

      status.textContent = hits.length
        ? hits.length + (hits.length === 1 ? ' result' : ' results') + ' for “' + q + '”'
        : 'No results for “' + q + '”. Try a different word, or use the sitemap.';

      results.innerHTML = hits.map(function (h) {
        return '<li class="card card--link"><h2 class="h4"><a href="' + h.doc.u + '">' +
          highlight(h.doc.t, terms) + '</a></h2>' +
          '<p class="card__meta">' + h.doc.k + '</p>' +
          '<p>' + highlight(h.doc.s, terms) + '</p></li>';
      }).join('');
    }

    var debounce;
    if (input) {
      input.addEventListener('input', function () {
        clearTimeout(debounce);
        debounce = setTimeout(function () { run(input.value.trim()); }, 140);
      });
    }
    var form = $('[data-search-form]', search);
    if (form) form.addEventListener('submit', function (e) {
      e.preventDefault();
      run(input.value.trim());
    });

    status.textContent = 'Loading the search index…';
    fetch('/search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        index = data;
        run(input ? input.value.trim() : '');
      })
      .catch(function () {
        status.textContent = 'Search is unavailable right now. Please use the sitemap.';
      });
  }

  /* ---------------------------------------------------------------------
     Forms — validation, spam honeypot, and a working fallback.
     If no endpoint is configured the submission opens a pre-filled email to
     the correct inbox, so no enquiry is ever silently lost.
     --------------------------------------------------------------------- */
  var INBOX = {
    contact:     CONTACT_EMAIL,
    partnership: CONTACT_EMAIL,
    volunteer:   CONTACT_EMAIL,
    ambassador:  CONTACT_EMAIL,
    newsletter:  CONTACT_EMAIL,
    complaint:   CONTACT_EMAIL
  };

  $$('form[data-form]').forEach(function (form) {
    var kind   = form.getAttribute('data-form');
    var status = $('[data-form-status]', form);

    form.addEventListener('submit', function (e) {
      // Honeypot: a real person never fills this in.
      var hp = form.querySelector('input[name="website"]');
      if (hp && hp.value) { e.preventDefault(); return; }

      var invalid = null;
      $$('[required]', form).forEach(function (f) {
        var bad = (f.type === 'checkbox') ? !f.checked : !String(f.value).trim();
        if (!bad && f.type === 'email') bad = !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.value);
        if (bad && !invalid) invalid = f;
        f.setAttribute('aria-invalid', bad ? 'true' : 'false');
      });

      if (invalid) {
        e.preventDefault();
        if (status) {
          status.textContent = 'Please check the highlighted fields and try again.';
          status.className = 'form-status is-error';
        }
        invalid.focus();
        return;
      }

      // A donation is never routed to email. Until the payment gateway is
      // connected, we send the donor to the bank-transfer panel rather than to
      // a checkout page that does not exist.
      if (kind === 'donation') {
        if (DONATE_ENDPOINT) { form.action = DONATE_ENDPOINT; return; }
        e.preventDefault();
        if (status) {
          status.innerHTML = 'Card and mobile payments are not connected on this site yet. ' +
            'You can give by bank transfer using the details below, or email ' +
            '<a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> and we will help.';
          status.className = 'form-status is-error';
        }
        var bank = document.getElementById('bank-transfer');
        if (bank) {
          bank.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
          bank.setAttribute('tabindex', '-1');
          bank.focus({ preventScroll: true });
        }
        return;
      }

      if (FORM_ENDPOINT) return;   // real endpoint handles it

      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (v, k) {
        if (k === 'website' || !String(v).trim()) return;
        lines.push(k.replace(/[-_]/g, ' ').replace(/^./, function (c) { return c.toUpperCase(); }) + ': ' + v);
      });
      var subject = form.getAttribute('data-subject') || ('Website enquiry — ' + kind);
      var to = INBOX[kind] || CONTACT_EMAIL;
      window.location.href = 'mailto:' + to +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      if (status) {
        status.innerHTML = 'Your email app should now open with this message ready to send. ' +
          'If nothing happened, please email <a href="mailto:' + to + '">' + to + '</a> directly.';
        status.className = 'form-status is-ok';
      }
    });
  });

  /* ---------------------------------------------------------------------
     Share and copy
     --------------------------------------------------------------------- */
  $$('[data-share]').forEach(function (btn) {
    if (!navigator.share) { btn.hidden = true; return; }
    btn.addEventListener('click', function () {
      navigator.share({
        title: document.title,
        url: window.location.href
      }).catch(function () {});
    });
  });

  $$('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(text).then(function () {
        var old = btn.textContent;
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = old; }, 1600);
      });
    });
  });

  /* ---------------------------------------------------------------------
     Contact form: preset the subject from ?subject= in the URL
     --------------------------------------------------------------------- */
  var subjectSelect = $('#contact-subject');
  if (subjectSelect) {
    var want = new URLSearchParams(window.location.search).get('subject');
    if (want) {
      Array.prototype.forEach.call(subjectSelect.options, function (o) {
        if (o.value === want) subjectSelect.value = want;
      });
    }
  }
})();
