import { getAppMode, getReadinessChecks, getSupportEmail } from '@/lib/env';
import { getLibraryOverview } from '@/lib/content-manifest';
import { createSupabaseServerClient } from '@/lib/supabase/server';

export type MemberSnapshot = {
  mode: 'mock' | 'live';
  signedIn: boolean;
  displayName: string;
  email: string;
  planName: string;
  statusLabel: string;
  renewalLabel: string;
  librarySummary: string;
  stripeCustomerId: string;
  portalSummary: string;
  supportEmail: string;
};

export async function getMemberSnapshot(): Promise<MemberSnapshot> {
  const overview = getLibraryOverview();
  const supportEmail = getSupportEmail();

  try {
    const supabase = await createSupabaseServerClient();

    if (supabase) {
      const {
        data: { user },
        error,
      } = await supabase.auth.getUser();

      if (!error && user) {
        return {
          mode: 'live',
          signedIn: true,
          displayName: user.user_metadata.full_name ?? 'Little Lab Coats family',
          email: user.email ?? 'Signed-in member',
          planName: 'Subscription sync pending',
          statusLabel: 'Signed in',
          renewalLabel: 'Renewal date appears after Stripe entitlement sync.',
          librarySummary: `${overview.launchIncludedItems} launch bundles are ready to display once entitlements are connected.`,
          stripeCustomerId: 'Created on first successful checkout',
          portalSummary: 'Billing portal unlocks after the Stripe customer record exists.',
          supportEmail,
        };
      }
    }
  } catch {
    // Fall back to a safe demo snapshot for local review.
  }

  return {
    mode: 'mock',
    signedIn: false,
    displayName: 'The Rivera Family',
    email: 'family@example.com',
    planName: 'Annual all-access membership',
    statusLabel: 'Demo member state',
    renewalLabel: 'Launch renewals will appear here after Stripe webhook sync.',
    librarySummary: `${overview.launchIncludedItems} launch bundles spanning ${overview.gradeCount} grades are mapped into the library manifest.`,
    stripeCustomerId: 'cus_launch_preview',
    portalSummary: 'Portal opens in mock mode until real Stripe credentials are added.',
    supportEmail,
  };
}

export function getImplementationStatus() {
  const readiness = getReadinessChecks();
  const appMode = getAppMode();

  return {
    appMode,
    readiness,
    readyCount: readiness.filter((item) => item.ready).length,
    waitingCount: readiness.filter((item) => !item.ready).length,
  };
}

export function getLaunchDecisionsStillNeeded() {
  return [
    'Final annual price and any launch promo/coupon rules.',
    'Production member-app hostname (app.littlelabcoats.co vs members.littlelabcoats.co).',
    'Live Supabase project values and email template settings.',
    'Live Stripe product, price ID, webhook secret, and billing portal configuration.',
    'Canonical protected asset storage path for paid downloads.',
  ];
}
