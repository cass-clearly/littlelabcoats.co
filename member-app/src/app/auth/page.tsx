import { AppShell, Card } from '@/components/app-shell';

export default function AuthPage() {
  return (
    <AppShell eyebrow="Auth" title="Sign in or create your member account">
      <Card title="MVP auth shape">
        <ul>
          <li>Supabase handles email/password and magic-link sign-in.</li>
          <li>Checkout should start from inside the authenticated app to reduce Stripe email mismatch risk.</li>
          <li>Auth callback route is scaffolded at <code>/api/auth/callback</code>.</li>
        </ul>
      </Card>

      <Card title="UI placeholder">
        <p>
          Replace this section with branded sign-in and sign-up forms once the Supabase project is created. The current scaffold keeps the route,
          copy, and integration boundaries in place without wiring real secrets.
        </p>
        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
          <button disabled style={buttonStyle}>
            Continue with magic link
          </button>
          <button disabled style={buttonStyle}>
            Create account with email
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
