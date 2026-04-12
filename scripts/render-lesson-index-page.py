#!/usr/bin/env python3
import json
from html import escape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "lesson-plans" / "_generated" / "lesson-index-data.json"
LESSON_INDEX_OUTPUT_PATH = REPO_ROOT / "lesson-plans" / "index.html"
REVIEW_INDEX_OUTPUT_PATH = REPO_ROOT / "lesson-plans" / "review" / "index.html"


def section_id(group: dict) -> str:
    return (
        f"{group['gradeLabel'].lower().replace(' ', '-')}-{group['domainLabel'].lower().replace(' ', '-').replace('&', 'and')}"
    )


def lesson_meta(entry: dict) -> str:
    parts = []
    if entry.get("unitNumber") is not None:
        parts.append(f"Unit {entry['unitNumber']}")
    if entry.get("lessonNumber") is not None:
        parts.append(f"Lesson {entry['lessonNumber']}")
    if entry.get("isFreeSample"):
        parts.append("Free sample")
    return " • ".join(parts)


def render_status_badge(status: dict | None) -> str:
    if not status:
        return ""
    return f'<span class="status-badge">{escape(status["label"])}</span>'


def render_status_summary(group: dict) -> str:
    summaries = group.get("statusSummaries") or []
    if not summaries:
        return ""
    items = "".join(
        f'<li><span class="status-badge">{escape(summary["label"])}</span><span class="status-summary-note">{escape(summary["note"])}</span></li>'
        for summary in summaries
    )
    return f'<ul class="status-summary-list">{items}</ul>'


def render_review_group(group: dict) -> str:
    rows = []
    for entry in group["entries"]:
        meta = lesson_meta(entry)
        meta_html = f'<div class="lesson-meta">{escape(meta)}</div>' if meta else ""
        status_badge = render_status_badge(entry.get("directoryStatus"))
        rows.append(
            f"""
            <li class="lesson-row">
              <a class="lesson-link" href="{escape(entry['reviewUrl'])}" target="_blank" rel="noopener">
                <span class="lesson-title-row"><span class="lesson-title">{escape(entry['displayTitle'])}</span>{status_badge}</span>
                {meta_html}
              </a>
            </li>
            """.strip()
        )

    status_summary_html = render_status_summary(group)
    return f"""
    <section class="group-card" id="{escape(section_id(group))}">
      <div class="group-header">
        <div>
          <h2>{escape(group['gradeLabel'])}</h2>
          <p>{escape(group['domainLabel'])}</p>
          {status_summary_html}
        </div>
        <div class="group-count">{group['count']}</div>
      </div>
      <ul class="lesson-list">
        {''.join(rows)}
      </ul>
    </section>
    """.strip()


def render_lesson_group(group: dict) -> str:
    rows = []
    for entry in group["entries"]:
        meta = lesson_meta(entry)
        meta_html = f'<div class="lesson-meta">{escape(meta)}</div>' if meta else ""
        status_badge = render_status_badge(entry.get("directoryStatus"))
        rows.append(
            f"""
            <li class="lesson-row">
              <div class="lesson-main">
                <div class="lesson-title-row"><div class="lesson-title">{escape(entry['displayTitle'])}</div>{status_badge}</div>
                {meta_html}
              </div>
              <div class="lesson-links">
                <a href="{escape(entry['canonicalUrl'])}" target="_blank" rel="noopener">Open lesson</a>
                <a href="{escape(entry['reviewUrl'])}" target="_blank" rel="noopener">Review mode</a>
              </div>
            </li>
            """.strip()
        )

    lesson_label = "lesson" if group["count"] == 1 else "lessons"
    status_summary_html = render_status_summary(group)
    return f"""
    <section class="group-card" id="{escape(section_id(group))}">
      <div class="group-header">
        <div>
          <h2>{escape(group['gradeLabel'])}</h2>
          <p>{escape(group['domainLabel'])}</p>
          {status_summary_html}
        </div>
        <div class="group-count">{group['count']} {lesson_label}</div>
      </div>
      <ul class="lesson-list">
        {''.join(rows)}
      </ul>
    </section>
    """.strip()


def build_review_page(data: dict) -> str:
    groups = data["groups"]
    total = data["entryCount"]
    group_nav = "".join(
        f'<a href="#{escape(section_id(group))}">{escape(group["gradeLabel"])} · {escape(group["domainLabel"])} <span>{group["count"]}</span></a>'
        for group in groups
    )
    group_sections = "\n".join(render_review_group(group) for group in groups)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lesson Review Index — Little Lab Coats</title>
  <meta name="description" content="Review-only lesson index for Little Lab Coats. Every lesson link opens directly in review mode for fast scanning and feedback." />
  <style>
    :root {{
      --cream: #F9FFFE;
      --cream-dark: #E8F8F6;
      --teal: #4ECDC4;
      --teal-pale: #D4F5F3;
      --navy: #3B1F6B;
      --navy-light: #5A3490;
      --white: #FFFFFF;
      --border: #C8F0ED;
      --text-muted: #5A7A78;
      --shadow-sm: 0 2px 8px rgba(43,58,103,0.07);
      --radius-md: 14px;
      --radius-lg: 22px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: Arial, Helvetica, sans-serif;
      background: var(--cream);
      color: var(--navy);
      line-height: 1.5;
    }}
    a {{ color: inherit; }}
    .container {{ max-width: 1080px; margin: 0 auto; padding: 0 20px; }}
    .hero {{
      background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
      color: var(--white);
      padding: 28px 0 22px;
    }}
    .hero h1 {{ font-size: clamp(1.9rem, 4vw, 2.6rem); margin-bottom: 8px; }}
    .hero p {{ max-width: 760px; color: rgba(255,255,255,0.86); }}
    .hero-meta {{ margin-top: 12px; font-size: 0.95rem; color: #d7fff9; }}
    .toolbar {{
      position: sticky;
      top: 0;
      z-index: 5;
      background: rgba(249,255,254,0.96);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
    }}
    .toolbar-inner {{ padding: 12px 0; }}
    .toolbar-label {{ display: block; font-size: 0.82rem; font-weight: 700; color: var(--text-muted); margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.04em; }}
    .toolbar-links {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .toolbar-links a {{
      text-decoration: none;
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 7px 10px;
      font-size: 0.88rem;
      white-space: nowrap;
    }}
    .toolbar-links span {{ color: var(--text-muted); }}
    main {{ padding: 18px 0 40px; }}
    .group-grid {{ display: grid; gap: 16px; }}
    .group-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}
    .group-header {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      background: #fcfffe;
      align-items: baseline;
    }}
    .group-header h2 {{ font-size: 1.2rem; margin-bottom: 2px; }}
    .group-header p {{ color: var(--text-muted); font-weight: 700; font-size: 0.92rem; }}
    .group-count {{ color: var(--teal); font-weight: 700; font-size: 0.95rem; }}
    .status-summary-list {{ list-style: none; margin-top: 10px; display: grid; gap: 6px; }}
    .status-summary-list li {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
    .status-badge {{ display: inline-block; background: #eef9f8; border: 1px solid var(--border); border-radius: 999px; padding: 3px 8px; font-size: 0.76rem; font-weight: 700; color: var(--navy); white-space: nowrap; }}
    .status-summary-note {{ color: var(--text-muted); font-size: 0.88rem; }}
    .lesson-list {{ list-style: none; }}
    .lesson-row + .lesson-row {{ border-top: 1px solid #eef9f8; }}
    .lesson-link {{
      display: block;
      text-decoration: none;
      padding: 12px 16px;
      background: transparent;
    }}
    .lesson-link:hover {{ background: var(--teal-pale); }}
    .lesson-title-row {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }}
    .lesson-title {{ display: block; font-weight: 700; font-size: 0.98rem; color: var(--navy); }}
    .lesson-meta {{ margin-top: 4px; font-size: 0.88rem; color: var(--text-muted); }}
    .footer-note {{ margin-top: 18px; font-size: 0.9rem; color: var(--text-muted); }}
    code {{ background: #f1fbfa; padding: 1px 5px; border-radius: 4px; }}
    @media (max-width: 700px) {{
      .group-header {{ flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="container">
      <h1>Lesson Review Index</h1>
      <p>Fast review page for Serena. Every lesson link on this page opens directly in review mode.</p>
      <div class="hero-meta">Stable URL: <strong>/lesson-plans/review/</strong> • Lessons indexed: <strong>{total}</strong></div>
    </div>
  </header>

  <div class="toolbar">
    <div class="container toolbar-inner">
      <span class="toolbar-label">Jump to section</span>
      <div class="toolbar-links">
        {group_nav}
      </div>
    </div>
  </div>

  <main>
    <div class="container">
      <div class="group-grid">
        {group_sections}
      </div>
      <p class="footer-note">Generated from <code>lesson-plans/_generated/lesson-index-data.json</code>, which is derived from <code>lesson-plans/*.html</code>. Review links use the canonical lesson path plus <code>?review=1</code>.</p>
    </div>
  </main>
</body>
</html>
"""


def build_lesson_page(data: dict) -> str:
    groups = data["groups"]
    entries = data["entries"]
    total = data["entryCount"]
    group_nav = "".join(
        f'<a href="#{escape(section_id(group))}">{escape(group["gradeLabel"])} · {escape(group["domainLabel"])} </a>'
        for group in groups
    )
    group_sections = "\n".join(render_lesson_group(group) for group in groups)

    grade_counts = {}
    for entry in entries:
        label = entry.get("gradeLabel", "Other Lessons")
        grade_counts[label] = grade_counts.get(label, 0) + 1

    grade_order = ["Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Other Lessons"]
    stats_html = "".join(
        f'<div class="stat"><span class="stat-number">{grade_counts.get(label, 0)}</span><span class="stat-label">{escape(label)}</span></div>'
        for label in grade_order
        if label in grade_counts
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lesson Index — Little Lab Coats</title>
  <meta name="description" content="Operational lesson index for Little Lab Coats. Browse every lesson with direct open and review-mode links." />
  <meta property="og:image" content="https://littlelabcoats.co/images/site/llc-logo-serena-approved-2026-04-10.png" />
  <meta name="twitter:image" content="https://littlelabcoats.co/images/site/llc-logo-serena-approved-2026-04-10.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="/images/site/favicon-32x32.png" />
  <link rel="apple-touch-icon" href="/images/site/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --cream: #F9FFFE;
      --cream-dark: #E8F8F6;
      --teal: #4ECDC4;
      --teal-pale: #D4F5F3;
      --coral: #FF6B6B;
      --navy: #3B1F6B;
      --navy-light: #5A3490;
      --white: #FFFFFF;
      --border: #C8F0ED;
      --text-muted: #5A7A78;
      --shadow-sm: 0 2px 8px rgba(43,58,103,0.07);
      --shadow-md: 0 8px 24px rgba(43,58,103,0.10);
      --radius-md: 14px;
      --radius-lg: 22px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Lato', sans-serif;
      background: var(--cream);
      color: var(--navy);
      line-height: 1.6;
    }}
    a {{ color: inherit; }}
    .container {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}
    nav {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: rgba(249,255,254,0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
    }}
    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 24px;
      max-width: 1100px;
      margin: 0 auto;
      gap: 16px;
    }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.15rem; color: var(--teal); text-decoration: none; }}
    .nav-links {{ display: flex; gap: 18px; flex-wrap: wrap; justify-content: flex-end; }}
    .nav-links a {{ text-decoration: none; font-weight: 700; font-size: 0.95rem; color: var(--navy); }}
    .hero {{
      background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
      color: var(--white);
      padding: 56px 0 34px;
    }}
    .hero h1 {{ font-family: 'Playfair Display', serif; font-size: clamp(2rem, 5vw, 3rem); margin-bottom: 12px; }}
    .hero p {{ max-width: 760px; color: rgba(255,255,255,0.84); font-size: 1.02rem; }}
    .hero-note {{ margin-top: 14px; font-size: 0.95rem; color: #d7fff9; }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      gap: 12px;
      margin-top: 28px;
    }}
    .stat {{
      background: rgba(255,255,255,0.10);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: var(--radius-md);
      padding: 14px;
    }}
    .stat-number {{ display: block; font-size: 1.4rem; font-weight: 700; }}
    .stat-label {{ display: block; font-size: 0.9rem; color: rgba(255,255,255,0.82); }}
    .main {{ padding: 28px 0 72px; }}
    .toolbar {{
      background: var(--cream-dark);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px;
      box-shadow: var(--shadow-sm);
      margin-bottom: 24px;
    }}
    .toolbar strong {{ display: block; margin-bottom: 10px; }}
    .toolbar-links {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .toolbar-links a {{
      text-decoration: none;
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 8px 12px;
      font-size: 0.9rem;
      color: var(--navy);
    }}
    .group-grid {{ display: grid; gap: 18px; }}
    .group-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}
    .group-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
      padding: 20px 20px 14px;
      background: linear-gradient(180deg, #ffffff 0%, #f8fffe 100%);
      border-bottom: 1px solid var(--border);
    }}
    .group-header h2 {{ font-family: 'Playfair Display', serif; font-size: 1.45rem; margin-bottom: 4px; }}
    .group-header p {{ color: var(--text-muted); font-weight: 700; }}
    .group-count {{ font-weight: 700; color: var(--teal); white-space: nowrap; }}
    .status-summary-list {{ list-style: none; margin-top: 10px; display: grid; gap: 6px; }}
    .status-summary-list li {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
    .status-badge {{ display: inline-block; background: var(--cream-dark); border: 1px solid var(--border); border-radius: 999px; padding: 3px 8px; font-size: 0.76rem; font-weight: 700; color: var(--navy); white-space: nowrap; }}
    .status-summary-note {{ color: var(--text-muted); font-size: 0.9rem; }}
    .lesson-list {{ list-style: none; }}
    .lesson-row {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 16px;
      padding: 14px 20px;
      border-top: 1px solid #eef9f8;
      align-items: center;
    }}
    .lesson-title-row {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
    .lesson-title {{ font-weight: 700; font-size: 1rem; color: var(--navy); }}
    .lesson-meta {{ margin-top: 4px; color: var(--text-muted); font-size: 0.9rem; }}
    .lesson-links {{ display: flex; flex-wrap: wrap; gap: 10px; justify-content: flex-end; }}
    .lesson-links a {{
      text-decoration: none;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--cream);
    }}
    .lesson-links a:last-child {{ background: var(--teal-pale); }}
    .footer-note {{ margin-top: 24px; color: var(--text-muted); font-size: 0.92rem; }}
    @media (max-width: 760px) {{
      .nav-inner {{ flex-direction: column; align-items: flex-start; }}
      .lesson-row {{ grid-template-columns: 1fr; }}
      .lesson-links {{ justify-content: flex-start; }}
      .group-header {{ flex-direction: column; }}
    }}
  </style>
  <script>
    (function () {{
      var host = window.location.hostname;
      if (host !== 'littlelabcoats.co' && host !== 'www.littlelabcoats.co') return;
      if (document.querySelector('script[data-llc-analytics="plausible"]')) return;
      var script = document.createElement('script');
      script.defer = true;
      script.dataset.domain = 'littlelabcoats.co';
      script.dataset.llcAnalytics = 'plausible';
      script.src = 'https://plausible.io/js/script.js';
      document.head.appendChild(script);
    }})();
  </script>
</head>
<body>
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="/"><img src="/images/site/llc-logo-serena-approved-2026-04-10.png" alt="Little Lab Coats" style="height:72px; width:auto; object-fit:contain; vertical-align:middle;"></a>
      <div class="nav-links">
        <a href="/curriculum.html">Curriculum</a>
        <a href="/store.html">Shop</a>
        <a href="/lesson-plans/">Lesson Index</a>
      </div>
    </div>
  </nav>

  <header class="hero">
    <div class="container">
      <h1>Lesson Index</h1>
      <p>Auto-generated from the lesson directory so Chris and Serena can browse every lesson from one stable page. Each row includes the normal lesson link and a direct review-mode link.</p>
      <div class="hero-note">Stable URL: <strong>/lesson-plans/</strong> • Total lessons indexed: <strong>{total}</strong> • <a href="/lesson-plans/review/" target="_blank" rel="noopener" style="color: #d7fff9; font-weight: 700; text-decoration: underline;">Open review-only index</a></div>
      <div class="stats">
        {stats_html}
      </div>
    </div>
  </header>

  <main class="main">
    <div class="container">
      <section class="toolbar">
        <strong>Jump to a section</strong>
        <div class="toolbar-links">
          {group_nav}
        </div>
      </section>

      <div class="group-grid">
        {group_sections}
      </div>

      <p class="footer-note">Generated from <code>lesson-plans/_generated/lesson-index-data.json</code>, which is derived from <code>lesson-plans/*.html</code>. Review links use the canonical lesson path plus <code>?review=1</code>.</p>
    </div>
  </main>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    REVIEW_INDEX_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    LESSON_INDEX_OUTPUT_PATH.write_text(build_lesson_page(data), encoding="utf-8")
    REVIEW_INDEX_OUTPUT_PATH.write_text(build_review_page(data), encoding="utf-8")
    print(f"Wrote lesson index page to {LESSON_INDEX_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"Wrote review index page to {REVIEW_INDEX_OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
