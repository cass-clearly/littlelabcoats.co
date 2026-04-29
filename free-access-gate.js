(function () {
  var ACCESS_KEY = 'llc_free_access_email_granted';
  var EMAIL_KEY = 'llc_free_access_email';
  var API_URL = 'https://cassclearly.com/leads';
  var SOURCE = 'littlelabcoats-free-access';

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

  function injectPendingStyle() {
    var style = document.createElement('style');
    style.id = 'llc-free-access-pending-style';
    style.textContent = 'html.llc-free-access-pending body > *:not(.llc-email-gate){visibility:hidden!important}html.llc-free-access-pending body{min-height:100vh;background:#F9FFFE!important}';
    document.head.appendChild(style);
    document.documentElement.classList.add('llc-free-access-pending');
  }

  function removePendingStyle() {
    document.documentElement.classList.remove('llc-free-access-pending');
    var style = document.getElementById('llc-free-access-pending-style');
    if (style) style.remove();
    var gate = document.querySelector('.llc-email-gate');
    if (gate) gate.remove();
  }

  function validEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function createGate() {
    var gate = document.createElement('div');
    gate.className = 'llc-email-gate';
    gate.setAttribute('role', 'dialog');
    gate.setAttribute('aria-modal', 'true');
    gate.setAttribute('aria-labelledby', 'llc-email-gate-title');
    gate.innerHTML = '' +
      '<style>' +
      '.llc-email-gate{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:24px;background:linear-gradient(135deg,#F9FFFE 0%,#E8F8F6 52%,#FFE8E8 100%);font-family:Lato,Arial,sans-serif;color:#3B1F6B;visibility:visible!important}' +
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
      '.llc-email-gate-error{display:none;background:#FFE8E8;border:1px solid #FFB4B4;border-radius:12px;padding:10px 12px;color:#8f2f2f!important;font-weight:700;margin:4px 0 0!important}' +
      '</style>' +
      '<div class="llc-email-gate-card">' +
      '<span class="llc-email-gate-kicker">Free access</span>' +
      '<h2 id="llc-email-gate-title">Enter your email to open the free science library.</h2>' +
      '<p>Access is still free. We just ask for an email first so Serena can keep sharing new lessons and printables with families who want them.</p>' +
      '<form class="llc-email-gate-form">' +
      '<label for="llc-free-access-email">Email address</label>' +
      '<input id="llc-free-access-email" type="email" name="email" autocomplete="email" placeholder="family@example.com" required />' +
      '<button type="submit">Open the free resources</button>' +
      '<p class="llc-email-gate-error" aria-live="polite"></p>' +
      '</form>' +
      '<p class="llc-email-gate-note">No account or payment needed. Review/internal preview links skip this gate automatically.</p>' +
      '</div>';

    document.body.appendChild(gate);
    var form = gate.querySelector('form');
    var input = gate.querySelector('input');
    var button = gate.querySelector('button');
    var error = gate.querySelector('.llc-email-gate-error');

    function showError(message) {
      error.textContent = message;
      error.style.display = 'block';
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var email = input.value.trim().toLowerCase();
      if (!validEmail(email)) {
        showError('Please enter a valid email address.');
        input.focus();
        return;
      }
      error.style.display = 'none';
      button.disabled = true;
      button.textContent = 'Opening…';
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
        removePendingStyle();
      }).catch(function () {
        button.disabled = false;
        button.textContent = 'Open the free resources';
        showError('Something went wrong saving your email. Please try again in a moment.');
      });
    });

    setTimeout(function () { input.focus(); }, 50);
  }

  if (isInternalPreview() || isUnlocked()) return;
  injectPendingStyle();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', createGate);
  else createGate();
})();
