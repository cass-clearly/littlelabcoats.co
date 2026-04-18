import { contentManifest, type ContentManifestItem } from '@/lib/content-manifest';

export type OfferTier = 'unit-bundle' | 'grade-access' | 'full-site';
export type EntitlementSource = 'purchase' | 'subscription';
export type EntitlementStatus = 'active' | 'scheduled-to-end' | 'expired';

export type OfferDefinition = {
  id: string;
  tier: OfferTier;
  title: string;
  priceLabel: string;
  cadenceLabel: string;
  description: string;
  checkoutPlan: string;
  grade?: string;
  itemId?: string;
  highlights: string[];
};

export type MemberEntitlement = {
  id: string;
  tier: OfferTier;
  label: string;
  source: EntitlementSource;
  status: EntitlementStatus;
  grade?: string;
  itemId?: string;
  itemTitle?: string;
  renewsOn?: string;
  endsOn?: string;
};

export type LibraryAccessState = {
  state: 'owned-unit' | 'included-grade' | 'included-full-site' | 'free-preview' | 'launch-ready-locked' | 'coming-soon';
  label: string;
  detail: string;
};

export function getOfferCatalog() {
  const unitBundleOffer: OfferDefinition = {
    id: 'unit-bundle',
    tier: 'unit-bundle',
    title: 'Unit bundle',
    priceLabel: '$0–$7+',
    cadenceLabel: 'One-time purchase',
    description: 'Buy a single ready-now unit bundle as a PDF/download, then keep it in the family account permanently.',
    checkoutPlan: 'unit-bundle',
    highlights: [
      'Permanent access to the purchased unit',
      'Downloadable PDF plus account-library access',
      'Best for families buying one unit at a time',
    ],
  };

  const gradeOffers = Array.from(new Set(contentManifest.map((item) => item.grade)))
    .sort((left, right) => left.localeCompare(right, undefined, { numeric: true }))
    .map((grade) => ({
      id: `grade-access-${grade.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`,
      tier: 'grade-access' as const,
      title: `${grade} access`,
      priceLabel: '$28–$35',
      cadenceLabel: 'Annual membership',
      description: `Unlock every current and future paid ${grade} lesson while the subscription stays active.`,
      checkoutPlan: 'grade-access',
      grade,
      highlights: ['Choose one grade at checkout', 'Access revokes automatically if the subscription ends', 'Managed from the member account'],
    }));

  const fullSiteOffer: OfferDefinition = {
    id: 'full-site-access',
    tier: 'full-site',
    title: 'Full site access',
    priceLabel: '$99/yr',
    cadenceLabel: 'Annual membership',
    description: 'Unlock the entire paid library across every grade while the subscription stays active.',
    checkoutPlan: 'full-site-access',
    highlights: ['Everything unlocked while active', 'Billing managed in the member portal', 'Best fit for multi-child families'],
  };

  return {
    unitBundleOffer,
    gradeOffers,
    fullSiteOffer,
  };
}

export function getMockEntitlements(): MemberEntitlement[] {
  return [
    {
      id: 'ent_unit_gr1_ps4',
      tier: 'unit-bundle',
      label: 'Light and Sound Investigations',
      source: 'purchase',
      status: 'active',
      itemId: 'gr1-ps4-light-and-sound',
      itemTitle: 'Light and Sound Investigations',
    },
    {
      id: 'ent_grade_3',
      tier: 'grade-access',
      label: 'Grade 3 access',
      source: 'subscription',
      status: 'active',
      grade: 'Grade 3',
      renewsOn: 'Renews August 14, 2026',
    },
    {
      id: 'ent_full_site_expired',
      tier: 'full-site',
      label: 'Full site access',
      source: 'subscription',
      status: 'expired',
      endsOn: 'Ended March 2, 2026',
    },
  ];
}

export function getLibraryAccessState(item: ContentManifestItem, entitlements: MemberEntitlement[]): LibraryAccessState {
  if (item.status === 'free-preview') {
    return {
      state: 'free-preview',
      label: 'Free preview',
      detail: 'This item stays open for everyone and helps families sample the curriculum before buying.',
    };
  }

  if (item.status === 'coming-soon') {
    return {
      state: 'coming-soon',
      label: 'Coming soon',
      detail: 'Keep this visible in the roadmap, but do not treat it as purchasable until the product is actually live.',
    };
  }

  const fullSiteAccess = entitlements.find((entry) => entry.tier === 'full-site' && entry.status === 'active');

  if (fullSiteAccess) {
    return {
      state: 'included-full-site',
      label: 'Included in full access',
      detail: 'This unit should open without a paywall because the account has active site-wide membership.',
    };
  }

  const gradeAccess = entitlements.find((entry) => entry.tier === 'grade-access' && entry.status === 'active' && entry.grade === item.grade);

  if (gradeAccess) {
    return {
      state: 'included-grade',
      label: `Included in ${item.grade}`,
      detail: 'This unit should open because the account has active grade-level access.',
    };
  }

  const purchasedUnit = entitlements.find((entry) => entry.tier === 'unit-bundle' && entry.status === 'active' && entry.itemId === item.id);

  if (purchasedUnit) {
    return {
      state: 'owned-unit',
      label: 'Owned unit bundle',
      detail: 'Permanent purchase. Keep the download available even if every subscription ends later.',
    };
  }

  return {
    state: 'launch-ready-locked',
    label: 'Locked until purchased',
    detail: 'Families should see the title, summary, and learning-objective preview, then upgrade through the right offer.',
  };
}

export function getOwnedUnitItems(entitlements: MemberEntitlement[]) {
  return entitlements
    .filter((entry) => entry.tier === 'unit-bundle' && entry.status === 'active' && entry.itemId)
    .map((entry) => contentManifest.find((item) => item.id === entry.itemId))
    .filter((item): item is ContentManifestItem => Boolean(item));
}

export function getActiveGradeEntitlements(entitlements: MemberEntitlement[]) {
  return entitlements.filter((entry) => entry.tier === 'grade-access' && entry.status === 'active');
}

export function hasActiveFullSiteAccess(entitlements: MemberEntitlement[]) {
  return entitlements.some((entry) => entry.tier === 'full-site' && entry.status === 'active');
}

export function getAccessSummary(entitlements: MemberEntitlement[]) {
  const activeGrades = getActiveGradeEntitlements(entitlements);
  const ownedUnits = getOwnedUnitItems(entitlements);
  const fullSiteActive = hasActiveFullSiteAccess(entitlements);

  if (fullSiteActive) {
    return 'Full site access is active.';
  }

  if (activeGrades.length > 0) {
    return `${activeGrades.map((entry) => entry.grade).join(', ')} unlocked, plus ${ownedUnits.length} permanent unit ${ownedUnits.length === 1 ? 'bundle' : 'bundles'}.`;
  }

  if (ownedUnits.length > 0) {
    return `${ownedUnits.length} permanent unit ${ownedUnits.length === 1 ? 'bundle' : 'bundles'} owned.`;
  }

  return 'No paid entitlements attached yet.';
}
