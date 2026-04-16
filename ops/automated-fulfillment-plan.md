# Automated fulfillment plan

## Objective
Move from manual send to payment-triggered email fulfillment for PDF products.

## Recommended v1 workflow
1. Customer pays in Stripe Checkout.
2. Stripe sends `checkout.session.completed` webhook.
3. Small fulfillment service verifies the event signature.
4. Service reads the purchased product/price id.
5. Service looks up the matching PDF/link in a product map.
6. Service sends the welcome email from `clearlycass10@gmail.com`.
7. Service records fulfillment status so we do not double-send.

## Minimum pieces to build
- Stripe webhook endpoint
- Stripe signing secret
- Product map file: Stripe price/product -> attachment or link
- Email sending integration
- Fulfillment log or database

## Easiest technical shape
- Small Node or Python service
- One JSON product map
- Gmail send or transactional email provider
- SQLite or JSON log for sent orders

## Human decisions still needed
- Should PDFs be attached directly or sent as download links?
- If links, where should the files live?
- Should we resend automatically if the same customer buys again?
- Who gets alerted on failures?

## Best immediate path
- Keep manual fulfillment live today
- Build automated fulfillment next on top of the same product map and email templates

## How Serena can help
- Decide whether delivery is attachment vs link
- Confirm the exact products going live first
- Confirm support inbox: `clearlycass10@gmail.com`
- Confirm where downloadable files should live long-term
