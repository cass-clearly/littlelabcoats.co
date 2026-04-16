import { AppShell, Card } from '@/components/app-shell';

export default function AccountPage() {
  return (
    <AppShell eyebrow="Account" title="Your subscription account">
      <Card title="Account state placeholder">
        <ul>
          <li>Show customer email, Stripe customer ID, and current entitlement summary.</li>
          <li>Display renewal date, cancel-at-period-end state, and failed-payment warnings.</li>
          <li>Link to billing portal and support steps for duplicate-customer recovery.</li>
        </ul>
      </Card>

      <Card title="Why this route exists now">
        <p>
          The MVP plan specifically calls for a clear account page so families can self-serve common issues instead of relying on the old
          browser-local unlock flow.
        </p>
      </Card>
    </AppShell>
  );
}
