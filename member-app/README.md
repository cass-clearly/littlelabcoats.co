# Little Lab Coats member app scaffold

This is the initial authenticated member-app skeleton for the subscription-site MVP described in `../docs/subscription-site-mvp-plan-2026-04-16.md`.

## Why this exists
- Keeps the current static marketing/curriculum site untouched.
- Creates a clearly separated Next.js app that can eventually live at `app.littlelabcoats.co` or `members.littlelabcoats.co`.
- Establishes the MVP routing shape for auth, account, library, and billing.
- Adds Supabase + Stripe integration boundaries without committing production secrets.

## Included in this scaffold
- Next.js app-router project in `member-app/`
- Placeholder routes:
  - `/`
  - `/auth`
  - `/account`
  - `/library`
  - `/billing`
- Placeholder API routes:
  - `/api/health`
  - `/api/auth/callback`
  - `/api/stripe/checkout`
  - `/api/stripe/portal`
  - `/api/stripe/webhook`
- Supabase client helpers in `src/lib/supabase/`
- Stripe server helper in `src/lib/stripe.ts`
- Sample content manifest in `src/data/content-manifest.json`
- Initial Supabase schema scaffold in `supabase/migrations/0001_mvp_schema.sql`

## Local setup
1. Install dependencies:
   ```bash
   cd member-app
   npm install
   ```
2. Copy the env template:
   ```bash
   cp .env.example .env.local
   ```
3. Fill in the Supabase and Stripe values.
4. Run the dev server:
   ```bash
   npm run dev
   ```
5. Optional checks:
   ```bash
   npm run typecheck
   npm run build
   ```

## Recommended deployment shape
- Keep the static site on GitHub Pages as-is.
- Deploy this app separately to Vercel.
- Point `app.littlelabcoats.co` or `members.littlelabcoats.co` at the Vercel project.
- Configure the public site CTA links later to send members into this app for login, checkout, and library access.

## Near-term implementation checklist
1. Create the Supabase project and run the SQL migration.
2. Create the Stripe live/test products and capture the annual price ID.
3. Replace placeholder API handlers with real signed-in flows.
4. Add server-side entitlement checks before exposing member downloads.
5. Update static-site store/paywall CTAs once the app is deployed.

## Notes
- The sample library manifest intentionally references existing lesson preview URLs from the current static site.
- The webhook route is a placeholder only; entitlement updates are not live yet.
- This scaffold is meant to reduce migration risk, not replace the public site.
