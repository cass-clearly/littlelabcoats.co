# Little Lab Coats download-first storefront audit — 2026-04-18

## Objective
Realign the public Little Lab Coats storefront with Serena's requested launch model:
- no subscriptions
- no member area
- no login dependence
- two paid product types only: unit bundles and full-grade bundles
- free lessons clearly separated from paid shopping
- pricing fixed to Serena's exact values

## What the repo looked like before this pass

### Public storefront reality
- `index.html` still framed pricing around one live $7 paid PDF plus coming-soon grade bundles and a `$99/yr` all-access subscription.
- `store.html` mixed a legacy paid single lesson (`Kitchen Chemistry`) with free lessons and preview links, instead of guiding buyers through a clean bundle-first flow.
- `curriculum.html` still told families the live paid product was `Kitchen Chemistry` and described bundles/all-access as coming soon.
- `checkout-success.html` and `scripts/checkout-handoff.js` still used subscription/all-access language from the older preview unlock model.

### Product/pricing reality
- The repo still contained multiple older pricing directions (`$7`, `$28–$35`, `$99/yr`, subscription/member messaging).
- The paid offer model was not yet consistently constrained to Serena's two real launch SKUs.

### Member-app reality
- `member-app/` is a real scaffold for auth, billing, account, and library flows.
- That scaffold was built for a subscription/member launch path and is not the right primary launch shape for Serena's simpler download-first storefront.
- It remains useful historical/technical work, but it should be treated as deferred rather than as the public launch path.

## What changed in this pass

### Public pages changed tonight
- `store.html`
  - rewritten around the literal shop flow Serena requested:
    1. pick grade
    2. pick subject area/domain
    3. pick unit
  - full-grade bundle card added inside each grade
  - pricing updated to:
    - unit bundle: `$18` first 50 customers, then `$22`
    - full-grade bundle: `$99` first 50 customers, then `$129`
  - big buy/download CTA pattern added for every paid SKU
  - explicit copy added that every paid item is a digital PDF product delivered immediately after purchase
  - explicit printed-copy note added
  - `Need more than one grade? Contact us` placed under the full-grade area
  - free lessons moved into a separate dedicated section
- `index.html`
  - homepage nav/hero CTA now points to shopping/free lessons instead of `Subscribe`
  - pricing section now reflects the two-product model only
  - subscription/member funnel copy removed from the public pricing story
- `curriculum.html`
  - shopping note now points families to the bundle-first store flow instead of the old live-product/all-access framing
- `checkout-success.html`, `checkout-cancelled.html`, and `scripts/checkout-handoff.js`
  - legacy checkout flow copy no longer centers subscription/all-access wording

### Durable ops/planning artifacts changed tonight
- `ops/download-product-catalog.json`
  - canonical launch catalog for all current unit bundles plus full-grade bundles
  - includes placeholder checkout status, packaging status, export-path targets, and thank-you product placeholders
- `scripts/store-product-links.js`
  - single place to drop in real checkout URLs without rewriting the storefront again
- `ops/manual-fulfillment.md`, `ops/automated-fulfillment-plan.md`, `ops/launch-todo.md`, and `GUMROAD-SETUP.md`
  - updated toward the new bundle-first launch shape

## What is true after this pass
- The public pricing direction in the repo now matches Serena's requested launch model.
- The public store no longer talks like the primary launch is a subscription/member funnel.
- Free lessons are separated from paid products in the public store flow.
- The repo now has a concrete product catalog and a clean placeholder structure for checkout-link wiring.

## What is still not wired tonight
- Real checkout URLs still need to be added SKU by SKU in `scripts/store-product-links.js`.
- Many unit bundles still need final assembled bundle PDFs even when lesson HTML already exists.
- Full-grade bundles still need their final assembled download package outputs.
- The older `member-app/` scaffold still exists in the repo as deferred work; it is not the public launch path.

## Honest launch summary
Tonight's work gets the storefront, pricing, and packaging structure pointed in the right direction. It does **not** pretend that every checkout link or every bundle PDF is already live. The repo is now shaped so those remaining steps can be finished cleanly instead of requiring another product-model rewrite.
