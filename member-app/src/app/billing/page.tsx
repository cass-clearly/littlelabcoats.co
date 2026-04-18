import { AppShell, Card } from '@/components/app-shell';
import { ActionButton } from '@/components/action-button';
import { getOfferCatalog } from '@/lib/access-model';
import { getImplementationStatus } from '@/lib/member-state';

type BillingPageProps = {
  searchParams?: {
    checkout?: string;
  };
};

export default function BillingPage({ searchParams }: BillingPageProps) {
  const implementation = getImplementationStatus();
  const notice = searchParams?.checkout === 'cancelled' ? 'Checkout was cancelled before payment completed.' : null;
  const offers = getOfferCatalog();

  return (
    <AppShell
      currentPath="/billing"
      eyebrow="Billing flow"
      title="Checkout and billing routes are ready to demonstrate the member purchase flow"
      description="The billing page now has a real MVP shell with pricing copy slots, checkout actions, portal actions, and credential-aware messaging for the Stripe integration boundary."
    >
      {notice ? <div className="notice-banner">{notice}</div> : null}

      <div className="pricing-grid">
        <Card title={offers.unitBundleOffer.title} eyebrow="One-time purchase">
          <div className="pricing-card">
            <p className="price-amount">{offers.unitBundleOffer.priceLabel}</p>
            <p className="body-copy">{offers.unitBundleOffer.description}</p>
            <p className="muted">{offers.unitBundleOffer.cadenceLabel}</p>
            <ul className="check-list">
              {offers.unitBundleOffer.highlights.map((highlight) => (
                <li key={highlight}>{highlight}</li>
              ))}
            </ul>
            <ActionButton endpoint="/api/stripe/checkout" label="Start unit-bundle checkout" pendingLabel="Starting checkout…" body={{ plan: offers.unitBundleOffer.checkoutPlan }} />
          </div>
        </Card>

        <Card title="Full grade access" eyebrow="Recurring membership">
          <div className="pricing-card">
            <p className="price-amount">$28–$35</p>
            <p className="body-copy">Unlock one grade across the site. Families pick the grade at checkout, then see that grade open automatically inside the member library.</p>
            <p className="muted">Annual membership</p>
            <ul className="check-list">
              <li>Grade access is tied to the account, not a shareable code.</li>
              <li>Members keep access through the paid period, then lose it automatically if billing ends.</li>
              <li>The account page should show exactly which grade is unlocked.</li>
            </ul>
            <div className="library-meta">
              {offers.gradeOffers.slice(0, 6).map((offer) => (
                <span key={offer.id} className="inline-chip">{offer.grade}</span>
              ))}
            </div>
            <ActionButton endpoint="/api/stripe/checkout" label="Start grade-access checkout" pendingLabel="Starting checkout…" body={{ plan: 'grade-access', grade: 'Grade 3' }} />
          </div>
        </Card>

        <Card title={offers.fullSiteOffer.title} eyebrow="Recurring membership">
          <div className="pricing-card">
            <p className="price-amount">{offers.fullSiteOffer.priceLabel}</p>
            <p className="body-copy">{offers.fullSiteOffer.description}</p>
            <p className="muted">{offers.fullSiteOffer.cadenceLabel}</p>
            <ul className="check-list">
              {offers.fullSiteOffer.highlights.map((highlight) => (
                <li key={highlight}>{highlight}</li>
              ))}
            </ul>
            <ActionButton endpoint="/api/stripe/checkout" label="Start full-site checkout" pendingLabel="Starting checkout…" body={{ plan: offers.fullSiteOffer.checkoutPlan }} />
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
            <p className="body-copy">Creates the correct checkout flow for one-time unit bundles, grade access, or full-site access. Grade and full-site memberships should land as account-linked subscriptions, not unlock codes.</p>
          </article>
          <article className="route-card">
            <h3><code>POST /api/stripe/portal</code></h3>
            <p className="body-copy">Creates a Billing Portal session when a customer ID is available, otherwise returns the account route in mock mode.</p>
          </article>
          <article className="route-card">
            <h3><code>POST /api/stripe/webhook</code></h3>
            <p className="body-copy">This becomes the source of truth for granting permanent unit ownership, activating subscriptions, and revoking grade/full-site access after the paid period ends.</p>
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
