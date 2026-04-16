import { AppShell, Card } from '@/components/app-shell';

export default function BillingPage() {
  return (
    <AppShell eyebrow="Billing" title="Checkout and billing portal">
      <Card title="Stripe integration boundary">
        <ul>
          <li><code>POST /api/stripe/checkout</code> will create a Checkout Session for the annual all-access plan.</li>
          <li><code>POST /api/stripe/portal</code> will create a Billing Portal session for signed-in members.</li>
          <li><code>POST /api/stripe/webhook</code> is the source of truth for subscription state and entitlement changes.</li>
        </ul>
      </Card>

      <Card title="Placeholder actions">
        <p>These buttons stay disabled until real Stripe and Supabase credentials are configured.</p>
        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
          <button disabled style={buttonStyle}>
            Start annual checkout
          </button>
          <button disabled style={buttonStyle}>
            Open billing portal
          </button>
        </div>
      </Card>
    </AppShell>
  );
}

const buttonStyle = {
  borderRadius: '999px',
  border: '1px solid #d7c08f',
  padding: '0.85rem 1.2rem',
  background: '#f6f1e5',
  color: '#6f5a34',
  fontWeight: 700,
};
