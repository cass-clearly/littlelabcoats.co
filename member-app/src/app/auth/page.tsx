import { AppShell, Card } from '@/components/app-shell';
import { AuthPanel } from '@/components/auth-panel';
import { getAppUrl, getReadinessChecks } from '@/lib/env';

type AuthPageProps = {
  searchParams?: {
    status?: string;
    error?: string;
  };
};

function getNotice(searchParams?: AuthPageProps['searchParams']) {
  if (searchParams?.status === 'callback-success') {
    return 'Magic-link callback completed. If Supabase is live, the session should now be available in the app.';
  }

  if (searchParams?.status === 'signed-in') {
    return 'You are signed in. The account route is ready for post-auth handoff.';
  }

  if (searchParams?.error) {
    return decodeURIComponent(searchParams.error);
  }

  return null;
}

export default function AuthPage({ searchParams }: AuthPageProps) {
  const readiness = getReadinessChecks();
  const supabaseReady = readiness.find((item) => item.id === 'supabase')?.ready ?? false;
  const redirectUrl = `${getAppUrl()}/api/auth/callback`;
  const notice = getNotice(searchParams);

  return (
    <AppShell
      currentPath="/auth"
      eyebrow="Auth experience"
      title="Sign in with the same friendly tone as the public Little Lab Coats brand"
      description="The auth screen now has branded magic-link, sign-in, and sign-up UX. In local review it stays mock-safe, and when Supabase credentials are added it can start working without a visual rewrite."
    >
      {notice ? <div className="notice-banner">{notice}</div> : null}

      <div className="dual-grid">
        <Card title="Member sign-in" eyebrow="Interactive MVP">
          <AuthPanel redirectUrl={redirectUrl} supabaseReady={supabaseReady} />
        </Card>

        <Card title="Why this flow is shaped this way" eyebrow="Launch rationale">
          <ul className="check-list">
            <li>Families can choose magic-link simplicity or an email/password account.</li>
            <li>Checkout should start from inside the member app so account email and billing email stay aligned.</li>
            <li>The callback route is already reserved at <code>/api/auth/callback</code>.</li>
            <li>Demo mode explains missing credentials clearly instead of leaving broken buttons on screen.</li>
          </ul>
        </Card>
      </div>

      <Card title="Integration status for auth" eyebrow="What is still needed">
        <div className="status-grid">
          {readiness.map((item) => (
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
