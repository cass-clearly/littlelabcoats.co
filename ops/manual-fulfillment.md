# Little Lab Coats manual fulfillment

## Goal
Use checkout for payment, then deliver the correct Little Lab Coats bundle download without any login or member-area dependency.

## Current launch model
- paid products are **unit bundles** and **full-grade bundles** only
- delivery promise is **digital PDF delivered immediately after purchase**
- printed copies are available by contact
- free lessons are separate and do not go through fulfillment

## Flow
1. Customer pays through the product checkout link.
2. Checkout provider sends the buyer receipt.
3. Seller notification or dashboard shows the completed payment.
4. Match the purchased SKU to `ops/download-product-catalog.json`.
5. Confirm the bundle asset exists at the expected export path.
6. Send the matching fulfillment email or download link.
7. Mark the order fulfilled.

## What must exist for each paid SKU
- exact SKU from `ops/download-product-catalog.json`
- real checkout link in `scripts/store-product-links.js`
- final downloadable asset or download page
- fulfillment email template
- support reply-to email

## Minimum viable launch setup

### Unit bundle
- one checkout product
- one finished PDF bundle or direct download page
- one fulfillment email template

### Full-grade bundle
- one checkout product
- one finished full-grade download package
- one fulfillment email template
- note: `Need more than one grade? Contact us`

## Current blockers to full operation
- many SKUs still need final bundle packaging
- many SKUs still need real checkout links dropped into `scripts/store-product-links.js`
- full-grade bundles still need final assembled download packages

## Suggested operating order
1. Package the next highest-priority bundle PDF
2. Add its checkout link
3. Test one purchase manually end to end
4. Repeat SKU by SKU
5. Only call a product live after both packaging and checkout wiring are real
