import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';

export default function CheckoutCancelPage() {
  return (
    <AppShell
      currentPath="/billing"
      eyebrow="Checkout cancelled"
      title="No problem—families can return to billing without losing their place"
      description="The member app now has an explicit cancel destination so Stripe checkout does not bounce users back into a confusing dead end."
    >
      <Card title="What happened">
        <ul className="check-list">
          <li>No subscription was activated from this checkout attempt.</li>
          <li>The family can restart checkout, sign in, or return to the public site without broken navigation.</li>
          <li>This route is already wired as the default mock cancel fallback.</li>
        </ul>
      </Card>

      <Card title="Choose the next step">
        <div className="quick-action-grid">
          <Link href="/billing?checkout=cancelled" className="button button-primary button-link">
            Return to billing
          </Link>
          <Link href="/auth" className="button button-secondary button-link">
            Sign in instead
          </Link>
          <Link href="/" className="button button-secondary button-link">
            Back to member home
          </Link>
        </div>
      </Card>
    </AppShell>
  );
}
