import { AppShell, Card } from '@/components/app-shell';
import { ActionButton } from '@/components/action-button';
import { getActiveGradeEntitlements, getOwnedUnitItems, hasActiveFullSiteAccess } from '@/lib/access-model';
import { getImplementationStatus, getMemberSnapshot } from '@/lib/member-state';

type AccountPageProps = {
  searchParams?: {
    auth?: string;
    checkout?: string;
    portal?: string;
  };
};

function getAccountNotice(searchParams?: AccountPageProps['searchParams']) {
  if (searchParams?.checkout === 'success') {
    return 'Checkout returned successfully. The final entitlement state will come from the Stripe webhook.';
  }

  if (searchParams?.portal === 'mock') {
    return 'Billing portal opened in mock mode because a real Stripe customer is not attached in this environment yet.';
  }

  if (searchParams?.auth === 'signed-in') {
    return 'Auth handoff reached the account shell.';
  }

  return null;
}

export default async function AccountPage({ searchParams }: AccountPageProps) {
  const member = await getMemberSnapshot();
  const implementation = getImplementationStatus();
  const notice = getAccountNotice(searchParams);
  const ownedUnits = getOwnedUnitItems(member.entitlements);
  const activeGrades = getActiveGradeEntitlements(member.entitlements);
  const fullSiteActive = hasActiveFullSiteAccess(member.entitlements);

  return (
    <AppShell
      currentPath="/account"
      eyebrow="Account hub"
      title="A self-serve member account shell families can use without emailing support first"
      description="This page is ready to become the main home for plan status, billing recovery, and entitlement messaging once Stripe and Supabase are live."
    >
      {notice ? <div className="notice-banner">{notice}</div> : null}

      <Card title="Member snapshot" eyebrow="Current account state">
        <div className="info-grid">
          <article className="info-card">
            <span className="label">Member</span>
            <h3>{member.displayName}</h3>
            <p className="body-copy">{member.email}</p>
          </article>
          <article className="info-card">
            <span className="label">Plan</span>
            <h3>{member.planName}</h3>
            <p className="body-copy">{member.statusLabel}</p>
          </article>
          <article className="info-card">
            <span className="label">Renewal</span>
            <h3>{member.renewalLabel}</h3>
            <p className="body-copy">{member.librarySummary}</p>
          </article>
          <article className="info-card">
            <span className="label">Stripe customer</span>
            <h3>{member.stripeCustomerId}</h3>
            <p className="body-copy">{member.portalSummary}</p>
          </article>
        </div>
      </Card>

      <div className="dual-grid">
        <Card title="Self-serve actions" eyebrow="Billing + support">
          <div className="stack-md">
            <ActionButton
              endpoint="/api/stripe/portal"
              label="Open billing portal"
              pendingLabel="Opening portal…"
              variant="primary"
              body={{ customerId: member.mode === 'live' ? undefined : member.stripeCustomerId }}
            />
            <p className="muted">Members should be able to update cards, cancel, or resume billing from here once Stripe customer sync is live.</p>
          </div>
        </Card>

        <Card title="How access behaves" eyebrow="Rules families will feel">
          <ul className="check-list">
            <li>Unit bundle purchases stay owned permanently and remain downloadable from the account.</li>
            <li>Grade and full-site plans stay open only while the subscription is active.</li>
            <li>If billing ends, access should remain through the paid period, then the paywall returns automatically.</li>
          </ul>
        </Card>
      </div>

      <Card title="Access attached to this account" eyebrow="Entitlements">
        <div className="dual-grid">
          <article className="info-card">
            <span className="label">Full site</span>
            <h3>{fullSiteActive ? 'Active' : 'Not active'}</h3>
            <p className="body-copy">{fullSiteActive ? 'This family should bypass the paywall everywhere.' : 'No site-wide membership is attached right now.'}</p>
          </article>
          <article className="info-card">
            <span className="label">Grade memberships</span>
            <h3>{activeGrades.length}</h3>
            <p className="body-copy">{activeGrades.length > 0 ? activeGrades.map((entry) => entry.grade).join(', ') : 'No active grade memberships yet.'}</p>
          </article>
          <article className="info-card">
            <span className="label">Owned unit bundles</span>
            <h3>{ownedUnits.length}</h3>
            <p className="body-copy">{ownedUnits.length > 0 ? ownedUnits.map((item) => item.title).join(', ') : 'No permanent unit purchases attached yet.'}</p>
          </article>
          <article className="info-card">
            <span className="label">Revocation behavior</span>
            <h3>Automatic</h3>
            <p className="body-copy">Subscription access falls away after Stripe marks the membership inactive, but one-time unit purchases remain.</p>
          </article>
        </div>
      </Card>

      <Card title="Current implementation status" eyebrow="Backend hookup still pending">
        <div className="status-grid">
          {implementation.readiness.map((item) => (
            <article key={item.id} className="info-card">
              <span className={`status-chip ${item.ready ? 'status-available' : 'status-coming'}`}>{item.ready ? 'Ready' : 'Waiting'}</span>
              <h3>{item.label}</h3>
              <p className="body-copy">{item.detail}</p>
              {item.missing.length > 0 ? <p className="muted">Missing: {item.missing.join(', ')}</p> : null}
            </article>
          ))}
        </div>
      </Card>
    </AppShell>
  );
}
