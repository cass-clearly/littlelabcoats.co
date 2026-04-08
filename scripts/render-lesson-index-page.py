#!/usr/bin/env python3
import json
from html import escape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "lesson-plans" / "_generated" / "lesson-index-data.json"
OUTPUT_PATH = REPO_ROOT / "lesson-plans" / "index.html"


def lesson_meta(entry: dict) -> str:
    parts = []
    if entry.get("isFreeSample"):
        parts.append("Free sample")
    if entry.get("unitNumber") is not None:
        parts.append(f"Unit {entry['unitNumber']}")
    if entry.get("lessonNumber") is not None:
        parts.append(f"Lesson {entry['lessonNumber']}")
    return " • ".join(parts)


def render_group(group: dict) -> str:
    section_id = (
        f"{group['gradeLabel'].lower().replace(' ', '-')}-{group['domainLabel'].lower().replace(' ', '-').replace('&', 'and')}"
    )
    rows = []
    for entry in group["entries"]:
        meta = lesson_meta(entry)
        meta_html = f'<div class="lesson-meta">{escape(meta)}</div>' if meta else ""
        rows.append(
            f"""
            <li class="lesson-row">
              <div class="lesson-main">
                <div class="lesson-title">{escape(entry['displayTitle'])}</div>
                {meta_html}
              </div>
              <div class="lesson-links">
                <a href="{escape(entry['canonicalUrl'])}" target="_blank" rel="noopener">Open lesson</a>
                <a href="{escape(entry['reviewUrl'])}" target="_blank" rel="noopener">Review mode</a>
              </div>
            </li>
            """.strip()
        )

    return f"""
    <section class="group-card" id="{escape(section_id)}">
      <div class="group-header">
        <div>
          <h2>{escape(group['gradeLabel'])}</h2>
          <p>{escape(group['domainLabel'])}</p>
        </div>
        <div class="group-count">{group['count']} lessons</div>
      </div>
      <ul class="lesson-list">
        {''.join(rows)}
      </ul>
    </section>
    """.strip()


def build_page(data: dict) -> str:
    total = data["entryCount"]
    groups = data["groups"]
    grade_counts = {}
    for group in groups:
        grade_counts[group["gradeLabel"]] = grade_counts.get(group["gradeLabel"], 0) + group["count"]

    summary_items = "".join(
        f'<div class="stat"><span class="stat-number">{count}</span><span class="stat-label">{escape(grade)}</span></div>'
        for grade, count in grade_counts.items()
    )
    group_nav = "".join(
        f'<a href="#{escape((group["gradeLabel"].lower().replace(" ", "-") + "-" + group["domainLabel"].lower().replace(" ", "-").replace("&", "and")))}">{escape(group["gradeLabel"])} · {escape(group["domainLabel"])}</a>'
        for group in groups
    )
    group_sections = "\n".join(render_group(group) for group in groups)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lesson Index — Little Lab Coats</title>
  <meta name="description" content="Operational lesson index for Little Lab Coats. Browse every lesson with direct open and review-mode links." />
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
    .lesson-list {{ list-style: none; }}
    .lesson-row {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 16px;
      padding: 14px 20px;
      border-top: 1px solid #eef9f8;
      align-items: center;
    }}
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
</head>
<body>
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="/">Little Lab Coats</a>
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
      <div class="hero-note">Stable URL: <strong>/lesson-plans/</strong> • Total lessons indexed: <strong>{total}</strong></div>
      <div class="stats">
        {summary_items}
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

      <p class="footer-note">This page is generated from <code>lesson-plans/*.html</code>. To refresh it after lesson changes, regenerate the lesson index data and re-render this page.</p>
    </div>
  </main>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.write_text(build_page(data), encoding="utf-8")
    print(f"Wrote lesson index page to {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
