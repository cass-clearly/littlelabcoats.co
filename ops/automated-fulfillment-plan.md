# Automated fulfillment plan

## Objective
Move from manual send to payment-triggered bundle fulfillment for download-first Little Lab Coats products.

## Launch assumptions
- paid products are **unit bundles** and **full-grade bundles** only
- no subscription logic is required for launch
- no member-account entitlement sync is required for launch
- product catalog source of truth is `ops/download-product-catalog.json`

## Recommended v1 workflow
1. Customer pays in checkout.
2. Checkout provider sends a completion event.
3. Fulfillment service verifies the event.
4. Service reads the purchased SKU.
5. Service looks up the SKU in `ops/download-product-catalog.json`.
6. Service sends the matching download email or link.
7. Service records fulfillment status so the order is not resent accidentally.

## Minimum pieces to build
- webhook endpoint
- product/SKU map
- email sending integration
- fulfillment log
- optional thank-you/download page routing

## Easiest technical shape
- small Node or Python service
- one product catalog JSON file
- transactional email provider or Gmail send path
- SQLite or JSON log for sent orders

## Human decisions still needed
- attachment delivery vs hosted download links
- exact thank-you/download page routing per SKU
- resend policy for duplicate purchases
- alerting path for failures

## Best immediate path
- keep manual fulfillment live while the catalog is being wired
- automate on top of the exact same SKU map and fulfillment templates
- do not reintroduce subscription/member complexity into the automation scope
