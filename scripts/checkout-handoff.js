(function (window) {
  'use strict';

  var ACCESS_KEY = 'llc_access';
  var RETURN_KEY = 'llc_post_checkout_return';
  var RETURN_LABEL_KEY = 'llc_post_checkout_return_label';
  var PLAN_KEY = 'llc_access_plan';
  var GRANTED_AT_KEY = 'llc_access_granted_at';
  var PENDING_PLAN_KEY = 'llc_pending_checkout_plan';

  function normalizeReturnPath(raw) {
    if (!raw) return null;

    try {
      var url = new URL(raw, window.location.origin);
      if (url.origin !== window.location.origin) return null;
      if (!/^\/lesson-plans\//.test(url.pathname) && !/^\/curriculum\.html$/.test(url.pathname)) return null;
      return url.pathname + url.search + url.hash;
    } catch (error) {
      return null;
    }
  }

  function prettifyLabel(path) {
    if (!path) return 'your lesson preview';
    var fileName = path.split('/').pop() || '';
    var cleaned = fileName
      .replace(/\.html$/i, '')
      .replace(/[-_]+/g, ' ')
      .replace(/\bgr\d+\b/gi, '')
      .replace(/\bk\b/gi, '')
      .replace(/\bunit\d+\b/gi, '')
      .replace(/\blesson\d+\b/gi, '')
      .replace(/\bquiz\b/gi, 'quiz')
      .replace(/\s+/g, ' ')
      .trim();

    if (!cleaned) return 'your lesson preview';
    return cleaned.replace(/(^|\s)\S/g, function (letter) { return letter.toUpperCase(); });
  }

  function rememberReturnPath(raw, label) {
    var normalized = normalizeReturnPath(raw);
    if (!normalized) return null;

    try {
      window.localStorage.setItem(RETURN_KEY, normalized);
      window.localStorage.setItem(RETURN_LABEL_KEY, label || prettifyLabel(normalized));
    } catch (error) {}

    return normalized;
  }

  function rememberReturnFromReferrer() {
    if (!document.referrer) return null;
    return rememberReturnPath(document.referrer, 'your lesson preview');
  }

  function rememberReturnFromParams(search) {
    var params = new URLSearchParams(search || window.location.search);
    return rememberReturnPath(params.get('return_to'), params.get('return_label') || 'your lesson preview');
  }

  function getReturnPath() {
    try {
      return normalizeReturnPath(window.localStorage.getItem(RETURN_KEY));
    } catch (error) {
      return null;
    }
  }

  function getReturnLabel() {
    try {
      return window.localStorage.getItem(RETURN_LABEL_KEY) || 'your lesson preview';
    } catch (error) {
      return 'your lesson preview';
    }
  }

  function clearReturnPath() {
    try {
      window.localStorage.removeItem(RETURN_KEY);
      window.localStorage.removeItem(RETURN_LABEL_KEY);
    } catch (error) {}
  }

  function isUnlocked() {
    try {
      return window.localStorage.getItem(ACCESS_KEY) === 'granted';
    } catch (error) {
      return false;
    }
  }

  function applyUnlock(plan) {
    var chosenPlan = plan || getPendingPlan() || 'all-access-annual';
    try {
      window.localStorage.setItem(ACCESS_KEY, 'granted');
      window.localStorage.setItem(PLAN_KEY, chosenPlan);
      window.localStorage.setItem(GRANTED_AT_KEY, new Date().toISOString());
    } catch (error) {}
    return chosenPlan;
  }

  function rememberPendingPlan(plan) {
    if (!plan) return;
    try {
      window.localStorage.setItem(PENDING_PLAN_KEY, plan);
    } catch (error) {}
  }

  function getPendingPlan() {
    try {
      return window.localStorage.getItem(PENDING_PLAN_KEY);
    } catch (error) {
      return null;
    }
  }

  function looksLikeStripeRedirect(params, referrer) {
    var source = params.get('source');
    return source === 'stripe' || params.has('session_id') || params.has('payment_intent') || params.has('redirect_status') || /stripe\.com/i.test(referrer || '');
  }

  function attachPaidCheckoutTracking(selector) {
    var links = document.querySelectorAll(selector);
    links.forEach(function (link) {
      link.addEventListener('click', function () {
        rememberPendingPlan(link.getAttribute('data-plan') || link.getAttribute('data-stripe-product') || 'checkout');
      });
    });
  }

  window.LLCCheckoutHandoff = {
    applyUnlock: applyUnlock,
    attachPaidCheckoutTracking: attachPaidCheckoutTracking,
    clearReturnPath: clearReturnPath,
    getPendingPlan: getPendingPlan,
    getReturnLabel: getReturnLabel,
    getReturnPath: getReturnPath,
    isUnlocked: isUnlocked,
    looksLikeStripeRedirect: looksLikeStripeRedirect,
    rememberPendingPlan: rememberPendingPlan,
    rememberReturnFromParams: rememberReturnFromParams,
    rememberReturnFromReferrer: rememberReturnFromReferrer,
    rememberReturnPath: rememberReturnPath
  };
})(window);
