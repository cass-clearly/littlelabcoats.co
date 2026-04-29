(function () {
  var ACCESS_KEY = 'llc_free_access_email_granted';
  var EMAIL_KEY = 'llc_free_access_email';
  var API_URL = 'https://cassclearly.com/leads';
  var SOURCE = 'littlelabcoats-free-access';
  var originalPrint = window.print ? window.print.bind(window) : null;
  var pendingAction = null;

  function hasQueryFlag(name) {
    try { return new URLSearchParams(window.location.search).get(name) === '1'; }
    catch (e) { return window.location.search.indexOf(name + '=1') !== -1; }
  }

  function isInternalPreview() {
    var host = window.location.hostname;
    return window.location.protocol === 'file:' ||
      host === 'localhost' ||
      host === '127.0.0.1' ||
      host.indexOf('192.168.') === 0 ||
      host === 'ai-server.local' ||
      hasQueryFlag('review') ||
      hasQueryFlag('internal') ||
      hasQueryFlag('preview');
  }

  function shouldBypassGate() {
    return isInternalPreview() || isUnlocked();
  }

  function isUnlocked() {
    try { return localStorage.getItem(ACCESS_KEY) === 'true'; }
    catch (e) { return false; }
  }

  function setUnlocked(email) {
    try {
      localStorage.setItem(ACCESS_KEY, 'true');
      localStorage.setItem(EMAIL_KEY, email);
    } catch (e) {}
  }

  function validEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function isPrintableAsset(url) {
    return /\.(pdf|png|jpe?g|webp|svg)(\?|#|$)/i.test(url || '');
  }

  function classifyLink(link) {
    if (!link || !link.getAttribute) return null;
    var href = link.getAttribute('href') || '';
    if (!href || href.charAt(0) === '#') return null;
    var text = (link.textContent || '').toLowerCase();
    var absHref = '';
    try { absHref = new URL(href, window.location.href).href; }
    catch (e) { absHref = href; }

    if (link.hasAttribute('download') || isPrintableAsset(absHref)) {
      return {
        type: 'link',
        href: absHref,
        target: link.getAttribute('target') || '',
        download: link.getAttribute('download') || ''
      };
    }

    if (/\b(print|download)\b/.test(text)) {
      return {
        type: 'link',
        href: absHref,
        target: link.getAttribute('target') || '',
        download: link.getAttribute('download') || ''
      };
    }

    return null;
  }

  function runPendingAction() {
    if (!pendingAction) return;
    var action = pendingAction;
    pendingAction = null;

    if (action.type === 'print') {
      if (originalPrint) originalPrint();
      return;
    }

    if (action.type === 'link' && action.href) {
      if (action.target === '_blank') {
        window.open(action.href, '_blank', 'noopener');
      } else {
        window.location.href = action.href;
      }
    }
  }

  function removeGate() {
    var gate = document.querySelector('.llc-email-gate');
    if (gate) gate.remove();
  }

  function createGate() {
    removeGate();
    var gate = document.createElement('div');
    gate.className = 'llc-email-gate';
    gate.setAttribute('role', 'dialog');
    gate.setAttribute('aria-modal', 'true');
    gate.setAttribute('aria-labelledby', 'llc-email-gate-title');
    gate.innerHTML = '' +
      '<style>' +
      '.llc-email-gate{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:24px;background:rgba(43,31,107,.36);backdrop-filter:blur(6px);font-family:Lato,Arial,sans-serif;color:#3B1F6B}' +
      '.llc-email-gate-card{width:min(100%,520px);background:#fff;border:1px solid #C8F0ED;border-radius:28px;padding:30px;box-shadow:0 22px 70px rgba(43,31,107,.18);text-align:left}' +
      '.llc-email-gate-kicker{display:inline-block;background:#D4F5F3;border-radius:999px;padding:6px 12px;font-size:.78rem;font-weight:900;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px}' +
      '.llc-email-gate h2{font-family:"Playfair Display",Georgia,serif;font-size:clamp(1.85rem,5vw,2.45rem);line-height:1.05;margin:0 0 10px;color:#3B1F6B}' +
      '.llc-email-gate p{margin:0 0 18px;color:#5A7A78;line-height:1.55;font-size:1rem}' +
      '.llc-email-gate-form{display:grid;gap:10px}' +
      '.llc-email-gate label{font-weight:900;color:#3B1F6B}' +
      '.llc-email-gate input{width:100%;border:2px solid #C8F0ED;border-radius:14px;padding:14px 15px;font-size:1rem;font-family:inherit;color:#3B1F6B}' +
      '.llc-email-gate input:focus{outline:3px solid rgba(78,205,196,.25);border-color:#4ECDC4}' +
      '.llc-email-gate button{border:0;border-radius:999px;background:#FF6B6B;color:#fff;font-weight:900;font-size:1rem;padding:14px 18px;cursor:pointer;box-shadow:0 10px 24px rgba(255,107,107,.24)}' +
      '.llc-email-gate button[disabled]{opacity:.7;cursor:wait}' +
      '.llc-email-gate-note{font-size:.86rem!important;color:#78908e!important;margin-top:12px!important}' +
      '.llc-email-gate-cancel{background:#fff!important;color:#3B1F6B!important;border:2px solid #C8F0ED!important;box-shadow:none!important}' +
      '.llc-email-gate-actions{display:grid;grid-template-columns:1fr;gap:10px}' +
      '.llc-email-gate-error{display:none;background:#FFE8E8;border:1px solid #FFB4B4;border-radius:12px;padding:10px 12px;color:#8f2f2f!important;font-weight:700;margin:4px 0 0!important}' +
      '@media(min-width:560px){.llc-email-gate-actions{grid-template-columns:1fr 1fr}}' +
      '</style>' +
      '<div class="llc-email-gate-card">' +
      '<span class="llc-email-gate-kicker">Free printable access</span>' +
      '<h2 id="llc-email-gate-title">Preview first. Enter your email to print or download.</h2>' +
      '<p>You can browse the free lessons and resource pages first. We only ask for an email when you’re ready to print or save the files.</p>' +
      '<form class="llc-email-gate-form">' +
      '<label for="llc-free-access-email">Email address</label>' +
      '<input id="llc-free-access-email" type="email" name="email" autocomplete="email" placeholder="family@example.com" required />' +
      '<div class="llc-email-gate-actions">' +
      '<button type="submit">Unlock print + download</button>' +
      '<button type="button" class="llc-email-gate-cancel">Keep browsing</button>' +
      '</div>' +
      '<p class="llc-email-gate-error" aria-live="polite"></p>' +
      '</form>' +
      '<p class="llc-email-gate-note">No account or payment needed. Review/internal preview links skip this automatically.</p>' +
      '</div>';

    document.body.appendChild(gate);
    var form = gate.querySelector('form');
    var input = gate.querySelector('input');
    var submitButton = gate.querySelector('button[type="submit"]');
    var cancelButton = gate.querySelector('.llc-email-gate-cancel');
    var error = gate.querySelector('.llc-email-gate-error');

    function showError(message) {
      error.textContent = message;
      error.style.display = 'block';
    }

    cancelButton.addEventListener('click', function () {
      pendingAction = null;
      removeGate();
    });

    gate.addEventListener('click', function (event) {
      if (event.target === gate) {
        pendingAction = null;
        removeGate();
      }
    });

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var email = input.value.trim().toLowerCase();
      if (!validEmail(email)) {
        showError('Please enter a valid email address.');
        input.focus();
        return;
      }
      error.style.display = 'none';
      submitButton.disabled = true;
      submitButton.textContent = 'Unlocking…';
      fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          source: SOURCE,
          path: window.location.pathname,
          referrer: document.referrer || null
        })
      }).then(function (response) {
        if (!response.ok) throw new Error('lead capture failed');
        return response.json();
      }).then(function () {
        setUnlocked(email);
        removeGate();
        runPendingAction();
      }).catch(function () {
        submitButton.disabled = false;
        submitButton.textContent = 'Unlock print + download';
        showError('Something went wrong saving your email. Please try again in a moment.');
      });
    });

    setTimeout(function () { input.focus(); }, 50);
  }

  function promptForAction(action) {
    if (shouldBypassGate()) {
      pendingAction = action;
      runPendingAction();
      return;
    }
    pendingAction = action;
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', createGate, { once: true });
    } else {
      createGate();
    }
  }

  if (window.print) {
    window.print = function () {
      if (shouldBypassGate()) {
        return originalPrint && originalPrint();
      }
      promptForAction({ type: 'print' });
    };
  }

  document.addEventListener('click', function (event) {
    if (shouldBypassGate()) return;
    var link = event.target && event.target.closest ? event.target.closest('a') : null;
    var action = classifyLink(link);
    if (!action) return;
    event.preventDefault();
    promptForAction(action);
  }, true);
})();
