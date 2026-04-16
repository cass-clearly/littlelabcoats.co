import Link from 'next/link';
import type { CSSProperties, ReactNode } from 'react';
import { getMarketingSiteUrl } from '@/lib/env';

const navItems = [
  { href: '/', label: 'Overview' },
  { href: '/auth', label: 'Auth' },
  { href: '/library', label: 'Library' },
  { href: '/account', label: 'Account' },
  { href: '/billing', label: 'Billing' },
];

export function AppShell({ title, eyebrow, children }: { title: string; eyebrow: string; children: ReactNode }) {
  return (
    <div style={styles.page}>
      <header style={styles.header}>
        <div>
          <p style={styles.eyebrow}>{eyebrow}</p>
          <h1 style={styles.title}>{title}</h1>
          <p style={styles.subtitle}>
            Small authenticated member-app scaffold for the Little Lab Coats MVP. The existing static site stays in place at{' '}
            <a href={getMarketingSiteUrl()} style={styles.link}>
              {getMarketingSiteUrl()}
            </a>
            .
          </p>
        </div>
        <nav style={styles.nav}>
          {navItems.map((item) => (
            <Link key={item.href} href={item.href} style={styles.navLink}>
              {item.label}
            </Link>
          ))}
          <a href={getMarketingSiteUrl()} style={styles.navLink}>
            Marketing site
          </a>
        </nav>
      </header>
      <main style={styles.main}>{children}</main>
    </div>
  );
}

export function Card({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section style={styles.card}>
      <h2 style={styles.cardTitle}>{title}</h2>
      <div style={styles.cardBody}>{children}</div>
    </section>
  );
}

const styles: Record<string, CSSProperties> = {
  page: {
    minHeight: '100vh',
    background: 'linear-gradient(180deg, #fff8e8 0%, #ffffff 100%)',
    color: '#2f3142',
    fontFamily: 'Arial, Helvetica, sans-serif',
  },
  header: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '1.5rem',
    justifyContent: 'space-between',
    padding: '2rem',
    borderBottom: '1px solid #f2d7a7',
    background: '#fffdf8',
  },
  eyebrow: {
    textTransform: 'uppercase',
    letterSpacing: '0.08em',
    color: '#8c5b16',
    fontWeight: 700,
    margin: '0 0 0.5rem',
    fontSize: '0.8rem',
  },
  title: {
    margin: 0,
    fontSize: '2rem',
  },
  subtitle: {
    maxWidth: '48rem',
    lineHeight: 1.6,
  },
  nav: {
    display: 'flex',
    gap: '0.75rem',
    alignItems: 'flex-start',
    flexWrap: 'wrap',
  },
  navLink: {
    textDecoration: 'none',
    color: '#2f3142',
    fontWeight: 700,
    background: '#fff2cf',
    padding: '0.7rem 1rem',
    borderRadius: '999px',
    border: '1px solid #efca73',
  },
  link: {
    color: '#995b00',
    fontWeight: 700,
  },
  main: {
    padding: '2rem',
    display: 'grid',
    gap: '1rem',
    maxWidth: '1100px',
  },
  card: {
    background: '#ffffff',
    border: '1px solid #f3ddb5',
    borderRadius: '24px',
    padding: '1.25rem',
    boxShadow: '0 10px 30px rgba(127, 82, 20, 0.08)',
  },
  cardTitle: {
    margin: '0 0 0.75rem',
    fontSize: '1.2rem',
  },
  cardBody: {
    display: 'grid',
    gap: '0.75rem',
    lineHeight: 1.6,
  },
};
