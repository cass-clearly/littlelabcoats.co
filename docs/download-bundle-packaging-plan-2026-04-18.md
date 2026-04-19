# Little Lab Coats bundle packaging plan — 2026-04-18

## Launch packaging rule
Every paid Little Lab Coats product should map to one of these only:
1. **Unit bundle**
2. **Full-grade bundle**

No subscriptions. No member-only library as a launch requirement. No login-gated delivery as the default storefront outcome.

## Canonical product catalog
Use `ops/download-product-catalog.json` as the source of truth for:
- SKU names
- launch pricing
- post-early-bird pricing
- packaging status
- expected export path
- checkout-link status
- full-grade bundle composition

Use `scripts/store-product-links.js` as the single place to add real public checkout URLs.

## Standard bundle contents

### Unit bundle
Target contents for every unit bundle:
- full lesson PDF set for the unit
- printable reference card
- printable unit quiz
- answer keys / teacher-facing pages already included in the lesson PDFs
- one clear thank-you/download product key

### Full-grade bundle
Target contents for every full-grade bundle:
- all current unit bundles for that grade
- a clean grade-level download structure that makes the domain breakdown obvious
- one grade-level thank-you/download product key
- the contact note: `Need more than one grade? Contact us`

## File/folder convention

### Unit bundles
Expected export path pattern:
- `exports/<sku>/`
- final file example: `exports/k-ls1-unit2-bundle/k-ls1-unit2-six-lesson-bundle.pdf`

### Full-grade bundles
Expected export path pattern:
- `exports/<grade-full-sku>/`
- example target folder: `exports/grade-k-complete/`

## Packaging workflow
1. Confirm the unit or grade SKU in `ops/download-product-catalog.json`
2. Assemble the lesson PDFs
3. Add the reference card
4. Add the quiz
5. Export the final bundled PDF or download package into the expected export path
6. Update `bundlePdfStatus` in the catalog
7. Add the checkout URL in `scripts/store-product-links.js`
8. If delivery is email/manual first, update the matching fulfillment template/runbook
9. Verify the public store button now resolves correctly

## Current ready vs pending snapshots

### Already packaged as bundle PDFs
- `k-ls1-unit2-bundle`
- `k-ls1-unit3-bundle`
- `gr1-ps4-unit1-bundle`
- `gr3-ps2-unit1-bundle`

### Partially packaged
- `k-ps3-unit2-bundle` has lesson PDFs exported but still needs the finished bundle packaging shape

### Still pending packaging
Everything else listed in `ops/download-product-catalog.json` should be treated as packaging work remaining until its `bundlePdfStatus` says otherwise.

## Checkout wiring rule
When a SKU is ready to sell:
- add the real checkout URL to `scripts/store-product-links.js`
- leave the storefront copy alone
- do not invent a second pricing model
- do not add subscription/member wording back into the public flow

## Delivery rule for launch
The storefront copy is already shaped around this promise:
- **digital PDF delivered immediately after purchase**
- **printed copies available by contact**

That means checkout wiring and fulfillment must preserve that promise literally.
