import Link from 'next/link';
import type { ReactNode } from 'react';
import { getAppMode, getAppModeLabel, getMarketingSiteUrl, getSupportEmail } from '@/lib/env';

type AppShellProps = {
  title: string;
  eyebrow: string;
  description?: string;
  currentPath?: string;
  children: ReactNode;
};

type CardProps = {
  title: string;
  children: ReactNode;
  eyebrow?: string;
};

const navItems = [
  { href: '/', label: 'Home' },
  { href: '/auth', label: 'Auth' },
  { href: '/library', label: 'Library' },
  { href: '/account', label: 'Account' },
  { href: '/billing', label: 'Billing' },
];

export function AppShell({ title, eyebrow, description, currentPath = '/', children }: AppShellProps) {
  const marketingSiteUrl = getMarketingSiteUrl();
  const supportEmail = getSupportEmail();
  const appMode = getAppMode();

  return (
    <div className="shell-root">
      <div className="page-container">
        <header className="site-header panel panel-glow">
          <div className="header-top-row">
            <Link href="/" className="brand-lockup">
              <span className="brand-icon" aria-hidden="true">
                🧪
              </span>
              <span>
                <span className="brand-kicker">Little Lab Coats</span>
                <span className="brand-title">Member App</span>
              </span>
            </Link>

            <nav className="nav-pills" aria-label="Member app navigation">
              {navItems.map((item) => {
                const isActive = currentPath === item.href;

                return (
                  <Link key={item.href} href={item.href} className={`nav-pill${isActive ? ' nav-pill-active' : ''}`}>
                    {item.label}
                  </Link>
                );
              })}
              <a href={marketingSiteUrl} className="nav-pill nav-pill-secondary">
                Main site
              </a>
            </nav>
          </div>

          <div className="hero-grid">
            <div className="stack-lg">
              <div className="eyebrow-row">
                <span className="eyebrow">{eyebrow}</span>
                <span className={`status-chip status-${appMode}`}>{getAppModeLabel()}</span>
              </div>
              <div className="stack-sm">
                <h1 className="hero-title">{title}</h1>
                <p className="hero-copy">
                  {description ??
                    'A branded Little Lab Coats member experience for login, library access, and billing—kept separate from the public curriculum site.'}
                </p>
              </div>
            </div>

            <div className="hero-aside">
              <div className="mini-stat-card">
                <span className="mini-stat-label">MVP focus</span>
                <strong>Families can log in, manage billing, and find their library from one place.</strong>
              </div>
              <div className="mini-stat-card">
                <span className="mini-stat-label">Support</span>
                <strong>{supportEmail}</strong>
              </div>
            </div>
          </div>
        </header>

        <main className="content-stack">{children}</main>

        <footer className="site-footer">
          <span>Little Lab Coats member-app MVP</span>
          <span>
            Public storefront stays at{' '}
            <a href={marketingSiteUrl} className="text-link">
              {marketingSiteUrl}
            </a>
          </span>
        </footer>
      </div>
    </div>
  );
}

export function Card({ title, children, eyebrow }: CardProps) {
  return (
    <section className="panel card-stack">
      {eyebrow ? <p className="card-eyebrow">{eyebrow}</p> : null}
      <h2 className="card-title">{title}</h2>
      <div className="stack-md">{children}</div>
    </section>
  );
}
