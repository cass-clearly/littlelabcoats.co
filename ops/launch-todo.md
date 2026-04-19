# Little Lab Coats launch todo

Last updated: 2026-04-18

## Launch direction locked
- [x] Download-first storefront
- [x] No subscriptions for launch
- [x] No member-area dependence for launch
- [x] Two paid product types only: unit bundles + full-grade bundles
- [x] Free lessons separated from paid shopping flow
- [x] Serena pricing set in repo: unit bundle `$18 → $22`, full grade `$99 → $129`

## Already changed in repo
- [x] Public store rewritten around grade → domain → unit flow
- [x] Homepage pricing/copy updated away from subscription framing
- [x] Curriculum page note updated to point at the bundle shop
- [x] Canonical bundle catalog added at `ops/download-product-catalog.json`
- [x] Public checkout-link placeholder map added at `scripts/store-product-links.js`
- [x] Packaging plan docs added

## Still needed before every SKU is truly live
- [ ] Finish packaging bundle PDFs for pending unit SKUs
- [ ] Assemble full-grade download packages
- [ ] Add real checkout links SKU by SKU in `scripts/store-product-links.js`
- [ ] Verify each live storefront CTA resolves to the correct checkout
- [ ] Verify thank-you/download outcome for each live SKU

## Highest-value next SKUs to finish
- [ ] Next Kindergarten unit bundle
- [ ] Next Grade 1 unit bundle
- [ ] First full-grade bundle
- [ ] First Grade 2 unit bundle

## Deferred work
- [ ] Member app remains deferred and should not be treated as the launch blocker
- [ ] Any future login/account build should start only after the download-first store is proving demand

## Rule for closing items
A product is only done when all of these are true:
1. bundle asset exists
2. checkout link exists
3. storefront button is wired
4. delivery outcome is clear and tested
