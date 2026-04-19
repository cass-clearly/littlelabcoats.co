# Little Lab Coats member-app scaffold notes

> **Superseded on 2026-04-18.**
> The current launch path is the simpler download-first storefront with unit bundles and full-grade bundles only. Keep this file as historical context for the deferred member-app scaffold, not as the current execution plan.


This repo now contains a separate Next.js scaffold in `member-app/` for the subscription-site MVP.

## Intent
- Keep the existing static site on GitHub Pages unchanged as the public storefront.
- Prepare a separate authenticated app for deployment to `app.littlelabcoats.co` or `members.littlelabcoats.co`.
- Avoid retrofitting durable auth into the current static lesson pages on day one.

## What was scaffolded
- App routes for auth, account, library, and billing.
- Placeholder Stripe API routes for checkout, billing portal, and webhook ingestion.
- Supabase helper modules and an initial SQL schema.
- A small content manifest sample referencing existing lesson preview pages.
- Setup docs and environment-variable template.

## Deliberate non-goals of this pass
- No production secrets committed.
- No live Stripe or Supabase project wiring.
- No changes to the existing public static pages yet.
- No entitlement enforcement on lesson assets yet.

## Expected next moves
1. Create Supabase project and apply the migration.
2. Create Stripe products/prices and fill in `member-app/.env.local`.
3. Replace placeholder API handlers with real user/session-aware flows.
4. Update public-site CTAs after the separate app is deployed.
