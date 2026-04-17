const appRuntimeEnv = ['NEXT_PUBLIC_APP_URL'] as const;
const supabasePublicEnv = ['NEXT_PUBLIC_SUPABASE_URL', 'NEXT_PUBLIC_SUPABASE_ANON_KEY'] as const;
const stripeServerEnv = ['STRIPE_SECRET_KEY', 'STRIPE_PRICE_ID_ANNUAL'] as const;
const stripePublicEnv = ['NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY'] as const;

function getMissing(keys: readonly string[]) {
  return keys.filter((key) => !process.env[key]);
}

export function getMissingAppEnv() {
  return getMissing(appRuntimeEnv);
}

export function getMissingSupabaseEnv() {
  return getMissing(supabasePublicEnv);
}

export function getMissingStripeServerEnv() {
  return getMissing(stripeServerEnv);
}

export function getMissingStripePublicEnv() {
  return getMissing(stripePublicEnv);
}

export function getMissingServerEnv() {
  return [...new Set([...getMissingAppEnv(), ...getMissingSupabaseEnv(), ...getMissingStripeServerEnv()])];
}

export function hasSupabasePublicEnv() {
  return getMissingSupabaseEnv().length === 0;
}

export function hasStripeServerEnv() {
  return getMissingStripeServerEnv().length === 0;
}

export function hasStripePublicEnv() {
  return getMissingStripePublicEnv().length === 0;
}

export function hasRequiredServerEnv() {
  return getMissingServerEnv().length === 0;
}

export function getAppUrl() {
  return process.env.NEXT_PUBLIC_APP_URL ?? 'http://localhost:3000';
}

export function getMarketingSiteUrl() {
  return process.env.NEXT_PUBLIC_MARKETING_SITE_URL ?? 'https://littlelabcoats.co';
}

export function getSupportEmail() {
  return process.env.SUPPORT_EMAIL ?? 'support@littlelabcoats.co';
}

export function getBillingPortalReturnUrl() {
  return process.env.STRIPE_BILLING_PORTAL_RETURN_URL ?? `${getAppUrl()}/account`;
}

export type AppMode = 'mock-safe' | 'partial' | 'launch-ready';

export function getAppMode(): AppMode {
  const supabaseReady = hasSupabasePublicEnv();
  const stripeReady = hasStripeServerEnv();

  if (supabaseReady && stripeReady) {
    return 'launch-ready';
  }

  if (supabaseReady || stripeReady) {
    return 'partial';
  }

  return 'mock-safe';
}

export function getAppModeLabel() {
  const mode = getAppMode();

  if (mode === 'launch-ready') {
    return 'Credentials wired';
  }

  if (mode === 'partial') {
    return 'Partially wired';
  }

  return 'Mock-safe preview';
}

export function getReadinessChecks() {
  return [
    {
      id: 'app',
      label: 'App runtime',
      ready: getMissingAppEnv().length === 0,
      missing: getMissingAppEnv(),
      detail: 'Base URLs for redirects and internal links.',
    },
    {
      id: 'supabase',
      label: 'Supabase auth',
      ready: hasSupabasePublicEnv(),
      missing: getMissingSupabaseEnv(),
      detail: 'Email auth, magic links, and signed-in session hydration.',
    },
    {
      id: 'stripe',
      label: 'Stripe checkout',
      ready: hasStripeServerEnv(),
      missing: getMissingStripeServerEnv(),
      detail: 'Checkout session creation, portal links, and webhook-driven billing state.',
    },
    {
      id: 'stripe-public',
      label: 'Stripe.js client',
      ready: hasStripePublicEnv(),
      missing: getMissingStripePublicEnv(),
      detail: 'Optional client-side Stripe helpers for future UX polish.',
    },
  ];
}
