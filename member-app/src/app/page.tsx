import { AppShell, Card } from '@/components/app-shell';
import { getLaunchLibraryItems } from '@/lib/content-manifest';
import { getMissingServerEnv } from '@/lib/env';

export default function HomePage() {
  const launchItems = getLaunchLibraryItems();
  const missingEnv = getMissingServerEnv();

  return (
    <AppShell eyebrow="MVP scaffold" title="Little Lab Coats member app">
      <Card title="What this skeleton covers">
        <ul>
          <li>Next.js app-router shell kept separate from the static marketing site.</li>
          <li>Supabase auth client helpers for email/password or magic-link flows.</li>
          <li>Stripe checkout, billing portal, and webhook placeholder routes.</li>
          <li>Library/account/billing routes aligned to the MVP plan.</li>
        </ul>
      </Card>

      <Card title="Launch library manifest stub">
        <p>
          The MVP plan calls for one canonical library manifest before deeper coding. This scaffold includes a small sample manifest sourced from
          existing lesson pages so the app shape is concrete.
        </p>
        <ul>
          {launchItems.map((item) => (
            <li key={item.id}>
              <strong>{item.grade}</strong> — {item.domain} / {item.unit}
            </li>
          ))}
        </ul>
      </Card>

      <Card title="Environment readiness">
        {missingEnv.length === 0 ? (
          <p>Required server-side environment variables are present.</p>
        ) : (
          <>
            <p>Before this app can run checkout or auth flows, set these variables from <code>.env.example</code>:</p>
            <ul>
              {missingEnv.map((key) => (
                <li key={key}>{key}</li>
              ))}
            </ul>
          </>
        )}
      </Card>
    </AppShell>
  );
}
