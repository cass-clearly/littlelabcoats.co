import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';

export default function NotFound() {
  return (
    <AppShell currentPath="/" eyebrow="Missing route" title="That page is not in the member app yet">
      <Card title="Try one of the core MVP routes">
        <div className="route-grid">
          <Link href="/" className="route-card">
            <h3>/</h3>
            <p className="body-copy">Launch hub</p>
          </Link>
          <Link href="/auth" className="route-card">
            <h3>/auth</h3>
            <p className="body-copy">Sign-in and account creation</p>
          </Link>
          <Link href="/library" className="route-card">
            <h3>/library</h3>
            <p className="body-copy">Manifest-driven content library</p>
          </Link>
          <Link href="/account" className="route-card">
            <h3>/account</h3>
            <p className="body-copy">Member account shell</p>
          </Link>
          <Link href="/billing" className="route-card">
            <h3>/billing</h3>
            <p className="body-copy">Checkout and portal actions</p>
          </Link>
        </div>
      </Card>
    </AppShell>
  );
}
