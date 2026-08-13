(function () {
  function isIOSFamily() {
    var platform = window.navigator.platform || '';
    var userAgent = window.navigator.userAgent || '';
    return /iPad|iPhone|iPod/.test(userAgent) || (platform === 'MacIntel' && window.navigator.maxTouchPoints > 1);
  }

  function isMobileSafari() {
    var userAgent = window.navigator.userAgent || '';
    return isIOSFamily() && /WebKit/i.test(userAgent) && !/CriOS|FxiOS|EdgiOS|OPiOS/i.test(userAgent);
  }

  function isLikelyMobile() {
    var userAgent = window.navigator.userAgent || '';
    return window.matchMedia('(max-width: 900px)').matches || /Android|iPhone|iPad|iPod|Mobile/i.test(userAgent);
  }

  function ensureFallbackStyle() {
    if (document.getElementById('llc-print-fallback-style')) return;
    var style = document.createElement('style');
    style.id = 'llc-print-fallback-style';
    style.textContent = '' +
      '.llc-print-fallback-overlay{position:fixed;inset:0;background:rgba(34,34,34,.58);display:none;align-items:center;justify-content:center;padding:20px;z-index:2000}' +
      '.llc-print-fallback-overlay.is-open{display:flex}' +
      '.llc-print-fallback-card{max-width:420px;width:100%;background:#fff;border-radius:18px;padding:22px 20px 18px;box-shadow:0 20px 45px rgba(0,0,0,.22);font-family:Arial,sans-serif;color:#24343b}' +
      '.llc-print-fallback-card h2{margin:0 0 10px;font-size:1.25rem;line-height:1.25;color:#2e7d32}' +
      '.llc-print-fallback-card p{margin:0 0 10px;line-height:1.5;font-size:.98rem}' +
      '.llc-print-fallback-steps{margin:12px 0 16px;padding-left:20px}' +
      '.llc-print-fallback-steps li{margin:0 0 8px;line-height:1.45}' +
      '.llc-print-fallback-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}' +
      '.llc-print-fallback-btn{appearance:none;border:none;border-radius:999px;padding:11px 16px;font-size:.96rem;font-weight:700;cursor:pointer}' +
      '.llc-print-fallback-btn.primary{background:#2e7d32;color:#fff}' +
      '.llc-print-fallback-btn.secondary{background:#eef4ef;color:#2f4b37}' +
      '.llc-print-fallback-note{font-size:.88rem;color:#5c6f76;margin-top:8px}' +
      '@media print{.llc-print-fallback-overlay{display:none!important}}';
    document.head.appendChild(style);
  }

  function buildFallbackDialog() {
    ensureFallbackStyle();
    var overlay = document.getElementById('llc-print-fallback');
    if (overlay) return overlay;

    overlay = document.createElement('div');
    overlay.id = 'llc-print-fallback';
    overlay.className = 'llc-print-fallback-overlay';
    overlay.innerHTML = '' +
      '<div class="llc-print-fallback-card" role="dialog" aria-modal="true" aria-labelledby="llc-print-fallback-title">' +
      '<h2 id="llc-print-fallback-title">Need help printing on mobile?</h2>' +
      '<p id="llc-print-fallback-message">If your phone or tablet did not open the print sheet, use your browser menu to print or save this lesson as a PDF.</p>' +
      '<ol class="llc-print-fallback-steps" id="llc-print-fallback-steps"></ol>' +
      '<div class="llc-print-fallback-actions">' +
      '<button type="button" class="llc-print-fallback-btn primary" id="llc-print-fallback-retry">Try Print Again</button>' +
      '<button type="button" class="llc-print-fallback-btn secondary" id="llc-print-fallback-close">Close</button>' +
      '</div>' +
      '<p class="llc-print-fallback-note">Tip: saving to Files or PDF works great if a wireless printer is not nearby.</p>' +
      '</div>';

    overlay.addEventListener('click', function (event) {
      if (event.target === overlay) hideFallback();
    });

    document.body.appendChild(overlay);

    document.getElementById('llc-print-fallback-close').addEventListener('click', hideFallback);
    document.getElementById('llc-print-fallback-retry').addEventListener('click', function () {
      hideFallback();
      window.setTimeout(function () {
        triggerNativePrint(false);
      }, 50);
    });

    return overlay;
  }

  function fallbackSteps() {
    if (isIOSFamily()) {
      return [
        'Tap the browser Share button.',
        'Choose Print to open Apple’s print sheet.',
        'Or choose Save to Files / Save as PDF if you want a digital copy first.'
      ];
    }

    return [
      'Open your browser menu or Share menu.',
      'Choose Print if your browser offers it.',
      'If you do not see Print, use Save as PDF or Save to Files and print from there.'
    ];
  }

  function showFallback() {
    var overlay = buildFallbackDialog();
    var steps = document.getElementById('llc-print-fallback-steps');
    var message = document.getElementById('llc-print-fallback-message');
    message.textContent = isIOSFamily()
      ? 'If your iPhone or iPad did not open the print sheet, use the Share menu to print or save this lesson as a PDF.'
      : 'If your phone or tablet did not open the print sheet, use your browser menu to print or save this lesson as a PDF.';
    steps.innerHTML = fallbackSteps().map(function (step) {
      return '<li>' + step + '</li>';
    }).join('');
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    var closeButton = document.getElementById('llc-print-fallback-close');
    if (closeButton) closeButton.focus();
  }

  function hideFallback() {
    var overlay = document.getElementById('llc-print-fallback');
    if (!overlay) return;
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  function triggerNativePrint(allowFallback) {
    if (typeof window.print !== 'function') {
      if (allowFallback !== false) showFallback();
      return;
    }

    var sawPrintSignal = false;
    var fallbackTimer = null;
    var cleanupTasks = [];

    function cleanup() {
      while (cleanupTasks.length) {
        var task = cleanupTasks.pop();
        try { task(); } catch (error) {}
      }
      if (fallbackTimer) {
        window.clearTimeout(fallbackTimer);
        fallbackTimer = null;
      }
    }

    function markPrintSignal() {
      sawPrintSignal = true;
      hideFallback();
    }

    var beforePrintHandler = function () {
      markPrintSignal();
    };
    window.addEventListener('beforeprint', beforePrintHandler);
    cleanupTasks.push(function () { window.removeEventListener('beforeprint', beforePrintHandler); });

    var afterPrintHandler = function () {
      markPrintSignal();
      window.setTimeout(cleanup, 50);
    };
    window.addEventListener('afterprint', afterPrintHandler);
    cleanupTasks.push(function () { window.removeEventListener('afterprint', afterPrintHandler); });

    var visibilityHandler = function () {
      if (document.visibilityState === 'hidden') {
        markPrintSignal();
      }
    };
    document.addEventListener('visibilitychange', visibilityHandler);
    cleanupTasks.push(function () { document.removeEventListener('visibilitychange', visibilityHandler); });

    if (window.matchMedia) {
      var printMedia = window.matchMedia('print');
      var mediaHandler = function (event) {
        if (event.matches) markPrintSignal();
      };
      if (printMedia.addEventListener) {
        printMedia.addEventListener('change', mediaHandler);
        cleanupTasks.push(function () { printMedia.removeEventListener('change', mediaHandler); });
      } else if (printMedia.addListener) {
        printMedia.addListener(mediaHandler);
        cleanupTasks.push(function () { printMedia.removeListener(mediaHandler); });
      }
    }

    try {
      if (typeof window.focus === 'function') window.focus();
      window.print();
    } catch (error) {
      cleanup();
      if (allowFallback !== false) showFallback();
      return;
    }

    if (allowFallback === false || !isLikelyMobile()) {
      window.setTimeout(cleanup, 1500);
      return;
    }

    fallbackTimer = window.setTimeout(function () {
      cleanup();
      if (!sawPrintSignal) {
        showFallback();
      }
    }, isMobileSafari() ? 900 : 1200);
  }

  function bindPrintButtons() {
    var buttons = document.querySelectorAll('button.print-btn');
    buttons.forEach(function (button) {
      if (button.dataset.mobilePrintBound === '1') return;
      button.dataset.mobilePrintBound = '1';
      button.removeAttribute('onclick');
      button.setAttribute('type', 'button');
      button.addEventListener('click', function (event) {
        event.preventDefault();
        triggerNativePrint(true);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindPrintButtons, { once: true });
  } else {
    bindPrintButtons();
  }
})();
