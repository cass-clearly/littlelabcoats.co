# Little Lab Coats manual fulfillment (Option #1)

## Goal
Use Stripe checkout for payment, then send a manual welcome email with the purchased PDF/link.

## Current recommended launch path
- Sell one unit bundle first
- Stripe handles checkout + buyer receipt
- Cass/manual ops sends the welcome email with the content link

## Flow
1. Customer pays through the Stripe payment link.
2. Stripe sends the buyer a receipt.
3. Stripe sends seller notification / dashboard record shows a completed payment.
4. Open the payment record and copy the buyer email.
5. Match the purchased product to the correct fulfillment link.
6. Send the matching welcome email.
7. Archive / mark fulfilled.

## What must exist for each product
- Product name
- Stripe payment link
- Final downloadable asset or library link
- Welcome email template
- Support reply-to email

## Minimum viable setup for this week
### Unit bundle
- One Stripe product
- One PDF bundle zip or one protected download page
- One welcome email template

### All access
- One Stripe monthly or annual product
- One library link or hub link
- One welcome email template
- Clear policy for what happens if payment stops

## Current blockers to fully operating this
- Need confirmed sender inbox/account to use for fulfillment
- Need final link/file for each SKU we plan to sell
- Need agreement on which products are actually live first
- Need Stripe seller notifications to be visible to the fulfillment inbox or operator

## Suggested first launch cut
- Launch only one unit bundle first
- Rehearse the fulfillment flow once manually
- Then add all access after the manual flow is stable
