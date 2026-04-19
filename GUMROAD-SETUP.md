# Download-first product setup guide — Little Lab Coats

**Time required:** ~20-30 minutes per batch of products  
**Goal:** Create real checkout products for Little Lab Coats bundle downloads

## Launch model to use
Little Lab Coats is launching with **two paid product types only**:
1. **Unit bundle**
2. **Full-grade bundle**

Do **not** create:
- subscriptions
- recurring memberships
- member-only library products
- login-dependent products as the primary storefront path

Free lessons stay separate from the paid store flow.

## Required pricing
Use Serena's exact pricing:
- **Unit bundle:** `$18` for the first 50 customers, then `$22`
- **Full-grade bundle:** `$99` for the first 50 customers, then `$129`

## Product naming pattern

### Unit bundle
`Little Lab Coats — <Grade> <Domain/Unit Name> Unit Bundle`

Examples:
- `Little Lab Coats — Kindergarten Animal Needs Unit Bundle`
- `Little Lab Coats — Grade 1 Sound & Light Unit Bundle`

### Full-grade bundle
`Little Lab Coats — Complete <Grade> Science Bundle`

Examples:
- `Little Lab Coats — Complete Kindergarten Science Bundle`
- `Little Lab Coats — Complete Grade 3 Science Bundle`

## Product description pattern
Use language like this:

> This is a digital PDF product delivered immediately after purchase.
> 
> Inside you'll get the Little Lab Coats lesson bundle for this unit/grade, built for homeschool families and designed by a homeschooling PhD scientist. The lessons are hands-on, NGSS-aligned, secular, and built around simple household materials.
> 
> Printed copies are available by contact.

## What to package before creating a product
Check `ops/download-product-catalog.json` first.

For each SKU you want to sell, confirm:
- bundle PDF is actually ready
- export path exists
- checkout-link status is still pending
- storefront SKU matches the catalog exactly

## If using Gumroad
Create each bundle as a **digital product** and upload the finished PDF or download asset.

### Unit bundle settings
- Product type: digital product
- Price: `$18`
- Early-bird note: first 50 customers
- After early bird: update to `$22`

### Full-grade bundle settings
- Product type: digital product
- Price: `$99`
- Early-bird note: first 50 customers
- After early bird: update to `$129`

## If using Stripe Payment Links instead
Create one payment link per SKU using the same names and prices above.
Then drop the real checkout URL into:
- `scripts/store-product-links.js`

## Store wiring rule
Once a product exists:
1. Copy the real checkout URL
2. Add it to `scripts/store-product-links.js`
3. Verify the matching storefront button now goes live
4. Do not rewrite the page copy or pricing structure again

## Contact language to preserve
Keep these promises consistent everywhere:
- digital PDF delivered immediately after purchase
- printed copies available by contact
- need more than one grade? contact us

## Source of truth files
- Product catalog: `ops/download-product-catalog.json`
- Public checkout-link map: `scripts/store-product-links.js`
- Packaging plan: `docs/download-bundle-packaging-plan-2026-04-18.md`
- Storefront audit/status: `docs/download-first-storefront-audit-2026-04-18.md`
