import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';
import { getLaunchLibraryItems, getLibraryOverview } from '@/lib/content-manifest';
import { getImplementationStatus, getLaunchDecisionsStillNeeded, getMemberSnapshot } from '@/lib/member-state';

const routeCards = [
  {
    href: '/auth',
    title: 'Auth',
    description: 'Magic-link and email/password UX that is safe in demo mode and ready for Supabase wiring.',
  },
  {
    href: '/library',
    title: 'Library',
    description: 'Manifest-driven member library grouped around launch-ready Little Lab Coats curriculum bundles.',
  },
  {
    href: '/account',
    title: 'Account',
    description: 'A self-serve shell for plan status, renewal messaging, and support recovery paths.',
  },
  {
    href: '/billing',
    title: 'Billing',
    description: 'Checkout and billing-portal entry points that can run in mock mode before live Stripe credentials exist.',
  },
];

export default async function HomePage() {
  const overview = getLibraryOverview();
  const launchItems = getLaunchLibraryItems();
  const implementation = getImplementationStatus();
  const member = await getMemberSnapshot();

  return (
    <AppShell
      currentPath="/"
      eyebrow="Member launch hub"
      title="A reviewable member experience for the first Little Lab Coats subscription launch"
      description="This separate app now covers the highest-value MVP paths: home, auth, library, account, billing, and checkout result screens—without touching the public static storefront."
    >
      <Card title="Launch snapshot" eyebrow="What exists now">
        <div className="kpi-grid">
          <div className="kpi-card">
            <span className="kpi-label">Launch bundles</span>
            <p className="kpi-value">{overview.launchIncludedItems}</p>
            <p className="muted">Manifest-backed curriculum bundles already mapped into the member library.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Launch lessons</span>
            <p className="kpi-value">{overview.launchLessons}</p>
            <p className="muted">Printable lesson content represented across the initial launch set.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Readiness checks passed</span>
            <p className="kpi-value">{implementation.readyCount}</p>
            <p className="muted">Out of {implementation.readiness.length} integration checkpoints for app runtime, Supabase, and Stripe.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Current member view</span>
            <p className="kpi-value">{member.mode === 'live' ? 'Live session' : 'Demo mode'}</p>
            <p className="muted">{member.librarySummary}</p>
          </div>
        </div>
      </Card>

      <Card title="Start where families will feel it" eyebrow="Quick paths">
        <div className="quick-action-grid">
          <Link href="/auth" className="button button-primary button-link">
            Open sign-in flow
          </Link>
          <Link href="/library" className="button button-secondary button-link">
            Browse the member library
          </Link>
          <Link href="/billing" className="button button-secondary button-link">
            Review billing flow
          </Link>
          <Link href="/account" className="button button-secondary button-link">
            View the account shell
          </Link>
        </div>
      </Card>

      <Card title="The core MVP routes are now in place" eyebrow="Route coverage">
        <div className="route-grid">
          {routeCards.map((route) => (
            <article key={route.href} className="route-card">
              <h3>{route.title}</h3>
              <p className="body-copy">{route.description}</p>
              <Link href={route.href} className="text-link">
                Go to {route.href}
              </Link>
            </article>
          ))}
        </div>
      </Card>

      <Card title="Launch catalog wired into the app" eyebrow="Manifest highlights">
        <div className="route-grid">
          {launchItems.map((item) => (
            <article key={item.id} className="route-card">
              <span className="inline-chip">{item.grade}</span>
              <h3>{item.title}</h3>
              <p className="body-copy">{item.summary}</p>
              <p className="muted">
                {item.domain} · {item.lessonCount} lessons · {item.format}
              </p>
            </article>
          ))}
        </div>
      </Card>

      <Card title="What still depends on decisions or credentials" eyebrow="Pending before real launch">
        <div className="dual-grid">
          <div className="info-card">
            <h3>Business and product decisions</h3>
            <ul className="check-list">
              {getLaunchDecisionsStillNeeded().slice(0, 2).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>
          <div className="info-card">
            <h3>Credential-dependent work</h3>
            <ul className="check-list">
              {getLaunchDecisionsStillNeeded().slice(2).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>
        </div>
      </Card>
    </AppShell>
  );
}
