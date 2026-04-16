import Link from 'next/link';
import { AppShell, Card } from '@/components/app-shell';
import { contentManifest } from '@/lib/content-manifest';
import { getMarketingSiteUrl } from '@/lib/env';

export default function LibraryPage() {
  return (
    <AppShell eyebrow="Library" title="Member library placeholder">
      <Card title="Hybrid content-access model">
        <p>
          Public lesson previews stay on the static site. Paid users come here for their entitled downloads and future in-app library browsing.
        </p>
      </Card>

      <Card title="Sample manifest-backed listing">
        <ul>
          {contentManifest.map((item) => (
            <li key={item.id}>
              <strong>{item.grade}</strong> — {item.domain} / {item.unit}{' '}
              <a href={`${getMarketingSiteUrl()}${item.previewUrl}`}>Preview page</a>
              {' · '}
              <span>{item.launchIncluded ? 'launch candidate' : 'deferred item'}</span>
            </li>
          ))}
        </ul>
        <p>
          Next step: replace this static list with server-verified entitlement checks and signed asset links.
        </p>
        <p>
          Need billing first? Visit <Link href="/billing">billing</Link>.
        </p>
      </Card>
    </AppShell>
  );
}
