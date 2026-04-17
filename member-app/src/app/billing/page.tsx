import { AppShell, Card } from '@/components/app-shell';
import { ActionButton } from '@/components/action-button';
import { getImplementationStatus } from '@/lib/member-state';

type BillingPageProps = {
  searchParams?: {
    checkout?: string;
  };
};

export default function BillingPage({ searchParams }: BillingPageProps) {
  const implementation = getImplementationStatus();
  const notice = searchParams?.checkout === 'cancelled' ? 'Checkout was cancelled before payment completed.' : null;

  return (
    <AppShell
      currentPath="/billing"
      eyebrow="Billing flow"
      title="Checkout and billing routes are ready to demonstrate the member purchase flow"
      description="The billing page now has a real MVP shell with pricing copy slots, checkout actions, portal actions, and credential-aware messaging for the Stripe integration boundary."
    >
      {notice ? <div className="notice-banner">{notice}</div> : null}

      <div className="pricing-grid">
        <Card title="Annual all-access membership" eyebrow="Launch offer shell">
          <div className="pricing-card">
            <p className="price-amount">Pricing TBD</p>
            <p className="body-copy">This slot is intentionally ready for the real Stripe price ID without hard-coding an amount before the business decision is final.</p>
            <ul className="check-list">
              <li>One clean launch offer keeps the first billing experience simple.</li>
              <li>Checkout success returns to the member app instead of dropping families into a dead-end thank-you page.</li>
              <li>Portal support is already carved out for card updates and cancellation flows.</li>
            </ul>
            <ActionButton endpoint="/api/stripe/checkout" label="Start checkout" pendingLabel="Starting checkout…" body={{ plan: 'annual-all-access' }} />
          </div>
        </Card>

        <Card title="Existing subscribers" eyebrow="Portal path">
          <div className="pricing-card">
            <p className="body-copy">Returning families should manage cards, invoices, and cancellations without emailing support.</p>
            <ActionButton endpoint="/api/stripe/portal" label="Open billing portal" pendingLabel="Opening portal…" variant="secondary" body={{ customerId: 'cus_launch_preview' }} />
            <p className="muted">If a real Stripe customer ID is supplied, the same endpoint is ready to create a live portal session.</p>
          </div>
        </Card>
      </div>

      <Card title="What the Stripe layer is responsible for" eyebrow="Integration boundary">
        <div className="route-grid">
          <article className="route-card">
            <h3><code>POST /api/stripe/checkout</code></h3>
            <p className="body-copy">Creates a live Checkout Session when Stripe credentials exist, otherwise falls back to a local mock success route.</p>
          </article>
          <article className="route-card">
            <h3><code>POST /api/stripe/portal</code></h3>
            <p className="body-copy">Creates a Billing Portal session when a customer ID is available, otherwise returns the account route in mock mode.</p>
          </article>
          <article className="route-card">
            <h3><code>POST /api/stripe/webhook</code></h3>
            <p className="body-copy">Reserved as the source of truth for subscription lifecycle changes and entitlement sync.</p>
          </article>
        </div>
      </Card>

      <Card title="Credential readiness" eyebrow="Still pending">
        <div className="status-grid">
          {implementation.readiness.map((item) => (
            <article key={item.id} className="info-card">
              <span className={`status-chip ${item.ready ? 'status-available' : 'status-coming'}`}>{item.ready ? 'Ready' : 'Waiting'}</span>
              <h3>{item.label}</h3>
              <p className="body-copy">{item.detail}</p>
              {item.missing.length > 0 ? <p className="muted">Missing: {item.missing.join(', ')}</p> : <p className="muted">Configured for this environment.</p>}
            </article>
          ))}
        </div>
      </Card>
    </AppShell>
  );
}
