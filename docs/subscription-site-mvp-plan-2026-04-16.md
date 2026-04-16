# Little Lab Coats subscription-site MVP plan

## Current state to build from
- Public site is a static HTML site on `littlelabcoats.co` / GitHub Pages.
- Checkout is currently Stripe payment-link based.
- Paid access today is a browser-local unlock (`localStorage` via `scripts/checkout-handoff.js`).
- Manual fulfillment artifacts already exist in `ops/` (`product-fulfillment-map.json`, email templates, manual fulfillment docs).
- Curriculum content already exists as static lesson HTML plus exported PDFs.

That means the fastest sane path is **not** a full rewrite of the public site first. It is:
1. keep the marketing/curriculum site mostly static,
2. add a small real web app for accounts + billing + entitlements,
3. progressively move the paywall/library experience onto that app.

## Recommended architecture

### 1) Split the system in two
**A. Public marketing site**
- Keep the existing static site for homepage, curriculum browsing, free previews, and SEO pages.
- Continue deploying this from the current repo.

**B. Member app (`app.littlelabcoats.co` or `members.littlelabcoats.co`)**
- Build a small authenticated app for:
  - signup/login
  - account page
  - subscription status
  - Stripe checkout launch + billing portal
  - purchased library
  - entitlement checks

### 2) Suggested stack
- **Frontend/app:** Next.js
- **Hosting:** Vercel
- **Database + auth:** Supabase (Postgres + email/password + magic links)
- **Payments:** Stripe Checkout + Stripe Customer Portal + webhooks
- **File/content delivery:** start with existing HTML/PDF assets; store protected PDFs and library metadata in Supabase Storage or Cloudflare R2 if needed

Why this stack:
- fast to start
- low ops burden
- Stripe + webhook flow is straightforward
- Supabase covers auth, DB, and basic admin needs without building auth from scratch

### 3) Core data model
Minimum tables:
- `users`
- `products`
- `prices`
- `content_items`
- `entitlements`
- `stripe_customers`
- `webhook_events`

Minimum rules:
- one Stripe customer per user
- webhook is source of truth for subscription state
- app computes access from entitlements, not from browser local state
- static lesson preview pages stay public, but full downloads/full-library links require signed-in entitlement checks

### 4) Content-access shape for MVP
Use a **hybrid model** first:
- public static lesson pages remain preview pages
- paid users log into the member app
- member app shows their unlocked library by grade/unit
- paid downloads/open actions route through server-verified entitlement checks

This avoids trying to retrofit durable auth into hundreds of static lesson pages on day one.

## MVP scope

### Must-have for launch
- customer accounts
- email login / magic link
- Stripe checkout for one subscription plan
- Stripe webhook handling for:
  - checkout completed
  - subscription updated
  - subscription canceled
  - invoice payment failed
- entitlement creation/removal from webhook events
- account page showing plan + renewal/cancel status
- library page showing only entitled content
- a basic admin/content manifest so the team can control what appears in the library
- support path for failed access / duplicate customer issues

### Explicitly defer from MVP
- complex family seats / multiple child profiles
- mobile app
- granular DRM / perfect content protection
- deep CMS/editorial workflow
- migration of every public lesson page into the app shell
- advanced analytics / affiliate systems
- coupon complexity beyond 1-2 launch offers

## Small build team / role split

### 1) Product / UX owner (Chris + Serena)
Owns:
- MVP decisions
- pricing + subscription rules
- what content is included at launch
- acceptance criteria for account, library, and billing flows

Best split:
- **Chris:** technical/product tradeoffs, final architecture decisions, payment/account edge-case priority
- **Serena:** customer experience, library taxonomy, what families actually need visible in the library

### 2) Frontend/app engineer
Owns:
- Next.js app shell
- auth screens
- account page
- library UX
- connecting member app cleanly to current brand/site

### 3) Backend/payments engineer
Owns:
- Stripe product/price setup
- webhook endpoint
- entitlement service
- Supabase schema and access rules
- subscription lifecycle edge cases

### 4) Content migration + QA operator
Owns:
- content manifest and metadata cleanup
- mapping existing lessons/PDFs into library structure
- testing preview vs paid visibility
- regression testing checkout/account/access flows

### Lean staffing recommendation
Smallest credible team:
- 1 product owner pair (Chris + Serena)
- 1 full-stack engineer who can do frontend + backend
- 1 content/QA operator

Safer/faster team:
- 1 frontend engineer
- 1 backend/payments engineer
- 1 content/QA operator
- Chris/Serena as product owners

## Suggested agent / delegate responsibilities

### Pi / coding delegate lane
Good fits:
- generate content manifests from the existing repo
- build migration scripts for lesson/PDF metadata
- scaffold the member app UI shell
- wire static-site CTAs to the new member app
- create QA checklists and route/link audits

### Backend/payment delegate lane
Good fits:
- Stripe webhook handlers
- entitlement logic
- customer/account reconciliation scripts
- webhook replay/idempotency handling

### Content/QA delegate lane
Good fits:
- verify every launch asset has title, grade, unit, preview URL, paid URL, and thumbnail/cover if needed
- test account creation, checkout, cancel/reactivate, and expired-access states
- confirm live library matches promised offer

## First 1-2 week execution sequence

### Days 1-2: lock scope and unblock implementation
- confirm **one** launch offer: likely annual all-access first
- decide app hostname: `app.` or `members.`
- create Stripe live products/prices in the target shape
- define the MVP library taxonomy: grade -> domain -> unit
- create a single canonical content manifest from existing repo assets

### Days 2-4: stand up the core backend
- create Supabase project
- create schema for users, products, content items, entitlements, webhook events
- implement Stripe checkout session creation
- implement webhook endpoint with idempotency
- on successful checkout, create/update Stripe customer and entitlement

### Days 4-7: build the member app
- auth flow
- account page
- library page driven by manifest + entitlements
- billing portal link
- success/cancel pages in the app
- replace browser-local unlock as the primary paid path

### Days 7-10: connect current site to the app
- update store CTA to route through real app checkout flow
- update paywall CTA on static lesson previews to send users to signup/checkout
- add “Log in” and “My Library” entry points on public site
- keep static previews public; route paid access through the member app

### Days 10-14: QA and launch hardening
- test new subscriber flow end to end
- test returning subscriber login on a second device
- test cancel / failed payment / expired subscription behavior
- test support recovery for “I paid but can’t access”
- soft launch with a tiny set of real users before broad promotion

## Biggest risks and how to de-risk them

### 1) Trying to retrofit auth into every static lesson page immediately
**Risk:** huge migration drag and brittle access control.
**Mitigation:** keep static pages as previews; put durable paid access in the member app first.

### 2) Stripe/customer identity mismatches
**Risk:** people pay with one email and sign up with another.
**Mitigation:** create checkout from inside the signed-in app whenever possible; store Stripe customer ID on the user record; build a manual reconciliation admin path.

### 3) Content library chaos
**Risk:** launch app works, but the library is confusing or incomplete.
**Mitigation:** create one canonical manifest before coding too far; limit launch catalog to the content that is truly ready.

### 4) Overbuilding before proving demand
**Risk:** spending weeks on edge cases before the paid library is selling.
**Mitigation:** launch with one subscription plan, one account model, one clear library UX.

### 5) Support burden from access issues
**Risk:** families lose trust quickly if login/access fails.
**Mitigation:** add clear account page state, resend magic link, billing portal, and a simple manual support runbook from day one.

## Recommendation
If the goal is to start immediately from today’s static-site/PDF-launch state, I would **not** rebuild the whole site first. I’d keep the current static site as the public storefront and stand up a small authenticated member app beside it. That gets Little Lab Coats from test-checkout + localStorage unlock to a real subscription business with the least disruption and the fastest path to live recurring revenue.