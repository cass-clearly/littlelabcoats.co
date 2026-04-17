import { AppShell, Card } from '@/components/app-shell';
import { ActionButton } from '@/components/action-button';
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

        <Card title="Support-safe messaging" eyebrow="What this page covers">
          <ul className="check-list">
            <li>Clarifies whether the family is looking at live data or a demo shell.</li>
            <li>Creates an obvious place for renewal dates, failed-payment warnings, and cancel-at-period-end notices.</li>
            <li>Keeps billing recovery and support escalation visible in one route.</li>
          </ul>
        </Card>
      </div>

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
