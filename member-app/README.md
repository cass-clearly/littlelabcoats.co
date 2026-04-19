# Little Lab Coats member app MVP

> **Status: deferred / not the current launch path.**
> As of 2026-04-18, the Little Lab Coats launch direction is a download-first storefront with unit bundles and full-grade bundles only. No subscriptions, no member area, and no login dependence are required for launch. This `member-app/` directory is historical scaffold work, not the primary public storefront path.

This is the separate authenticated app for the older Little Lab Coats member-launch direction. It does **not** replace or rewrite the public static site at `littlelabcoats.co`; it adds a dedicated app shell for login, library, account, and billing.

## What is implemented now

### Member-facing routes
- `/` — launch hub inside the member app with MVP status, quick actions, manifest summary, and pending launch dependencies
- `/auth` — branded auth UX with magic-link, sign-in, and sign-up modes
- `/account` — account shell for member status, billing recovery, and support messaging
- `/library` — manifest-driven library grouped by grade with launch-ready / coming-soon / free-preview states
- `/billing` — pricing shell, checkout action, billing-portal action, and credential readiness messaging
- `/checkout/success` — post-checkout landing route for successful returns
- `/checkout/cancel` — explicit cancel route so checkout exits cleanly

### API / integration boundaries
- `/api/health` — readiness snapshot for env/config status
- `/api/auth/callback` — Supabase callback route with real code-exchange path when credentials are present
- `/api/stripe/checkout` — creates a live Stripe Checkout Session when configured, otherwise redirects to a safe local mock-success route
- `/api/stripe/portal` — creates a live Billing Portal session when configured and given a customer ID, otherwise returns a mock account route
- `/api/stripe/webhook` — verifies Stripe signatures when webhook secrets are present; still needs persistence + entitlement sync

### MVP scaffolding improvements in this pass
- Replaced static placeholder bullets with a branded Little Lab Coats UI shell and coherent navigation.
- Added interactive auth UX instead of disabled buttons.
- Expanded the content manifest into a more realistic launch catalog with structured metadata.
- Added account, billing, and checkout result flows that can be reviewed without live credentials.
- Upgraded health/auth/Stripe placeholders so they are closer to real integration points.

## Local setup
1. Install dependencies:
   ```bash
   npm install
   ```
2. Copy the env template:
   ```bash
   cp .env.example .env.local
   ```
3. Fill in values as they become available.
4. Run the app:
   ```bash
   npm run dev
   ```
5. Run checks:
   ```bash
   npm run build
   npm run typecheck
   npm run lint
   ```

## Environment variables

### Required to fully wire the app
- `NEXT_PUBLIC_APP_URL`
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_PRICE_ID_ANNUAL`

### Also expected for real production behavior
- `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `SUPPORT_EMAIL`
- `STRIPE_BILLING_PORTAL_RETURN_URL`

## What is mock-safe vs live-ready

### Works now without credentials
- Route rendering and navigation
- Auth page UX/copy/flow states
- Manifest-driven library browsing
- Account and billing shells
- Checkout success/cancel flow via local mock redirects
- Health endpoint and readiness reporting

### Still waiting on final decisions or live credentials
- Final annual price and any launch coupon/promo rules
- Production hostname (`app.littlelabcoats.co` vs `members.littlelabcoats.co`)
- Supabase project creation, auth email templates, and live callback configuration
- Stripe product + price setup, webhook secret, and real customer sync
- Persistent entitlement updates and protected asset delivery

## Recommended next integration steps
1. Create the Supabase project and apply `supabase/migrations/0001_mvp_schema.sql`.
2. Create the Stripe product/price for the annual all-access membership and capture the live/test `STRIPE_PRICE_ID_ANNUAL`.
3. Hook webhook verification up to `webhook_events` + `entitlements` persistence.
4. Replace mock account/library state with live Supabase session + entitlement reads.
5. Point the public site CTAs at this app after deployment.

## Deployment shape
- Keep the public marketing/curriculum site on its current static deployment.
- Deploy this app separately (for example on Vercel).
- Point `app.littlelabcoats.co` or `members.littlelabcoats.co` at the deployment once the final hostname decision is made.
