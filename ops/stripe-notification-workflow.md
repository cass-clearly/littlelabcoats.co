# Stripe notification to operator workflow

## Goal
When a customer pays, the operator sees it immediately and can fulfill the order from `clearlycass10@gmail.com`.

## Fastest version for today
1. Stripe payment succeeds.
2. Stripe sends a payment notification email.
3. Operator opens the Stripe payment email or Stripe dashboard.
4. Operator copies the buyer email and purchased product.
5. Operator opens the matching Gmail draft in `clearlycass10@gmail.com`.
6. Operator sends the product PDF to the buyer.
7. Operator marks the order fulfilled.

## What needs to be set up
- Stripe account notifications turned on for successful payments
- Notification destination confirmed, preferably `clearlycass10@gmail.com`
- Product-to-fulfillment map documented
- One draft/template per live product
- Simple fulfilled log, spreadsheet or email label is enough for now

## Recommended operator setup
- Gmail label: `llc-orders`
- Gmail label: `llc-fulfilled`
- Optional Gmail filter: messages from Stripe with payment confirmations -> label `llc-orders`
- Stripe dashboard bookmark for payments

## First live product mapping
- Product: Grade 1 Physical Science Unit 1 bundle
- Fulfillment asset: `exports/gr1-ps4-unit1-bundle/gr1-ps4-unit1-six-lesson-bundle.pdf`
- Draft subject: `Your Grade 1 Physical Science Unit 1 bundle is ready`

## Next products to prepare the same way
- One unit bundle PDF per SKU
- One Gmail draft per SKU
- One row in a fulfillment map file per SKU
