import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';

type SuccessPageProps = {
  searchParams?: {
    session_id?: string;
    mock?: string;
  };
};

export default function CheckoutSuccessPage({ searchParams }: SuccessPageProps) {
  const isMock = searchParams?.mock === '1';

  return (
    <AppShell
      currentPath="/billing"
      eyebrow="Checkout success"
      title="Thanks for joining the Little Lab Coats member experience"
      description="This route gives the app a real post-checkout destination. In production it will rely on Stripe + webhook sync; in local review it stays useful through a safe mock flow."
    >
      <Card title={isMock ? 'Mock checkout completed' : 'Checkout returned successfully'}>
        <ul className="check-list">
          <li>{isMock ? 'You are looking at the mock success path because live Stripe credentials are not configured in this environment.' : 'Stripe sent the browser back to the member app successfully.'}</li>
          <li>Final access should still be granted by the webhook, not by trusting the browser redirect alone.</li>
          <li>Families now have obvious next steps instead of landing on an orphaned page.</li>
        </ul>
        {searchParams?.session_id ? <p className="muted">Session ID: {searchParams.session_id}</p> : null}
      </Card>

      <Card title="Next steps">
        <div className="quick-action-grid">
          <Link href="/account?checkout=success" className="button button-primary button-link">
            Go to account
          </Link>
          <Link href="/library" className="button button-secondary button-link">
            Open library
          </Link>
          <Link href="/billing" className="button button-secondary button-link">
            Back to billing
          </Link>
        </div>
      </Card>
    </AppShell>
  );
}
