import { AppShell, Card } from '@/components/app-shell';
import { contentManifest, getLibraryGroups, getLibraryOverview } from '@/lib/content-manifest';
import { getMarketingSiteUrl } from '@/lib/env';

function getGroupedSubjects(items: { domain: string }[]) {
  return Array.from(new Set(items.map((item) => item.domain))).sort();
}

function getStatusClass(status: string) {
  if (status === 'launch-ready') {
    return 'status-available';
  }

  if (status === 'free-preview') {
    return 'status-free';
  }

  return 'status-coming';
}

function getStatusLabel(status: string) {
  if (status === 'launch-ready') {
    return 'Launch ready';
  }

  if (status === 'free-preview') {
    return 'Free preview';
  }

  return 'Coming soon';
}

export default function LibraryPage() {
  const overview = getLibraryOverview();
  const groups = getLibraryGroups();
  const marketingSiteUrl = getMarketingSiteUrl();

  return (
    <AppShell
      currentPath="/library"
      eyebrow="Member library"
      title="A manifest-driven library shell that can grow without rewriting the UI"
      description="The member library is now driven from structured content metadata instead of hard-coded placeholder bullets. That gives the team one place to manage launch-ready, deferred, and free-preview items."
    >
      <Card title="Library overview" eyebrow="Launch scope">
        <div className="kpi-grid">
          <div className="kpi-card">
            <span className="kpi-label">Total items in manifest</span>
            <p className="kpi-value">{overview.totalItems}</p>
            <p className="muted">Including launch-ready, coming-soon, and free-preview entries.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Launch-ready items</span>
            <p className="kpi-value">{overview.launchIncludedItems}</p>
            <p className="muted">These are the highest-confidence bundles for the first 2-week member launch.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Grades represented</span>
            <p className="kpi-value">{overview.gradeCount}</p>
            <p className="muted">Enough coverage to make the library feel real on day one.</p>
          </div>
          <div className="kpi-card">
            <span className="kpi-label">Manifest format</span>
            <p className="kpi-value">JSON</p>
            <p className="muted">Ready to swap from local data to Supabase-backed metadata later.</p>
          </div>
        </div>
      </Card>

      <Card title="Pick your curriculum in 3 simple steps" eyebrow="Family-friendly browse flow">
        <div className="stack-lg">
          <div className="steps-grid">
            <article className="step-card">
              <span className="step-number">Step 1</span>
              <h3>Pick your grade</h3>
              <p className="body-copy">Start with the grade level your child is working in.</p>
            </article>
            <article className="step-card">
              <span className="step-number">Step 2</span>
              <h3>Pick your subject</h3>
              <p className="body-copy">Choose a subject like Life Science, Physical Science, Earth and Space Science, or Engineering.</p>
            </article>
            <article className="step-card">
              <span className="step-number">Step 3</span>
              <h3>Pick your unit</h3>
              <p className="body-copy">Open the unit that fits what you want to teach next.</p>
            </article>
          </div>

          {groups.map((group) => {
            const subjects = getGroupedSubjects(group.items);

            return (
              <section key={group.grade} className="grade-section stack-md">
                <div className="stack-sm">
                  <div className="grade-badge">{group.grade}</div>
                  <h3 className="section-title">{group.grade}</h3>
                  <p className="muted">Subjects available: {subjects.join(', ')}</p>
                </div>

                <div className="stack-lg">
                  {subjects.map((subject) => {
                    const subjectItems = group.items.filter((item) => item.domain === subject);

                    return (
                      <section key={`${group.grade}-${subject}`} className="subject-section stack-md">
                        <div className="subject-header">
                          <span className="subject-label">Subject</span>
                          <h4>{subject}</h4>
                          <p className="muted">Choose a unit below.</p>
                        </div>

                        <div className="library-grid">
                          {subjectItems.map((item) => (
                            <article key={item.id} className="library-item unit-card">
                              <div className="eyebrow-row">
                                <span className={`status-chip ${getStatusClass(item.status)}`}>{getStatusLabel(item.status)}</span>
                                <span className="inline-chip">{item.lessonCount} lessons</span>
                              </div>
                              <div className="unit-label">Unit</div>
                              <h3>{item.unit}</h3>
                              <p className="body-copy">{item.summary}</p>
                              <div className="library-meta">
                                <span className="inline-chip">{item.format}</span>
                                <span className="inline-chip">{item.title}</span>
                              </div>
                              <p className="muted">Member asset path: <code>{item.memberAssetPath}</code></p>
                              <a href={`${marketingSiteUrl}${item.previewUrl}`} className="text-link">
                                Open public preview
                              </a>
                            </article>
                          ))}
                        </div>
                      </section>
                    );
                  })}
                </div>
              </section>
            );
          })}
        </div>
      </Card>

      <Card title="Why this helps the launch" eyebrow="MVP content model">
        <div className="dual-grid">
          <div className="info-card">
            <h3>What is real now</h3>
            <ul className="check-list">
              <li>The library renders from a typed manifest rather than one-off JSX.</li>
              <li>Each item already knows its preview URL and future protected asset path.</li>
              <li>Launch-ready and deferred content are visually separated so the offer can stay honest.</li>
            </ul>
          </div>
          <div className="info-card">
            <h3>What gets wired next</h3>
            <ul className="check-list">
              <li>Entitlement filtering based on the signed-in member.</li>
              <li>Protected asset delivery or signed download URLs.</li>
              <li>Optional admin editing once the manifest moves to Supabase.</li>
            </ul>
          </div>
        </div>
        <p className="muted">Current manifest items loaded: {contentManifest.length}</p>
      </Card>
    </AppShell>
  );
}
