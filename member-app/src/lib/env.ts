const requiredServerEnv = [
  'NEXT_PUBLIC_APP_URL',
  'NEXT_PUBLIC_SUPABASE_URL',
  'NEXT_PUBLIC_SUPABASE_ANON_KEY',
  'STRIPE_SECRET_KEY',
  'STRIPE_PRICE_ID_ANNUAL',
] as const;

export function getMissingServerEnv() {
  return requiredServerEnv.filter((key) => !process.env[key]);
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
