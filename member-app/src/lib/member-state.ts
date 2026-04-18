import { getAppMode, getReadinessChecks, getSupportEmail } from '@/lib/env';
import { getLibraryOverview } from '@/lib/content-manifest';
import { createSupabaseServerClient } from '@/lib/supabase/server';
import { getAccessSummary, getMockEntitlements, type MemberEntitlement } from '@/lib/access-model';

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
  entitlements: MemberEntitlement[];
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
          planName: 'Account-linked access model ready for Stripe sync',
          statusLabel: 'Signed in',
          renewalLabel: 'Renewal dates appear after Stripe entitlement sync lands.',
          librarySummary: `${overview.launchIncludedItems} launch bundles are ready to unlock as soon as webhook-driven entitlements are attached to this account.`,
          stripeCustomerId: 'Created on first successful checkout',
          portalSummary: 'Billing portal unlocks after the Stripe customer record exists.',
          supportEmail,
          entitlements: [],
        };
      }
    }
  } catch {
    // Fall back to a safe demo snapshot for local review.
  }

  const entitlements = getMockEntitlements();

  return {
    mode: 'mock',
    signedIn: false,
    displayName: 'The Rivera Family',
    email: 'family@example.com',
    planName: 'Mixed access example',
    statusLabel: 'Demo member state',
    renewalLabel: 'Grade subscriptions renew automatically until cancelled. Permanent unit purchases stay owned.',
    librarySummary: getAccessSummary(entitlements),
    stripeCustomerId: 'cus_launch_preview',
    portalSummary: 'Portal opens in mock mode until real Stripe credentials are added.',
    supportEmail,
    entitlements,
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
