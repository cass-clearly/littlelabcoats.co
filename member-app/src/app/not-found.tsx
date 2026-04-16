import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';

export default function NotFound() {
  return (
    <AppShell eyebrow="Missing route" title="Page not found">
      <Card title="Try one of the core MVP routes">
        <ul>
          <li><Link href="/auth">/auth</Link></li>
          <li><Link href="/library">/library</Link></li>
          <li><Link href="/account">/account</Link></li>
          <li><Link href="/billing">/billing</Link></li>
        </ul>
      </Card>
    </AppShell>
  );
}
