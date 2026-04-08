#!/usr/bin/env python3
import json
from html import escape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "lesson-plans" / "_generated" / "lesson-index-data.json"
OUTPUT_PATH = REPO_ROOT / "lesson-plans" / "review" / "index.html"


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


def render_group(group: dict) -> str:
    rows = []
    for entry in group["entries"]:
        meta = lesson_meta(entry)
        meta_html = f'<div class="lesson-meta">{escape(meta)}</div>' if meta else ""
        rows.append(
            f"""
            <li class="lesson-row">
              <a class="lesson-link" href="{escape(entry['reviewUrl'])}" target="_blank" rel="noopener">
                <span class="lesson-title">{escape(entry['displayTitle'])}</span>
                {meta_html}
              </a>
            </li>
            """.strip()
        )

    return f"""
    <section class="group-card" id="{escape(section_id(group))}">
      <div class="group-header">
        <div>
          <h2>{escape(group['gradeLabel'])}</h2>
          <p>{escape(group['domainLabel'])}</p>
        </div>
        <div class="group-count">{group['count']}</div>
      </div>
      <ul class="lesson-list">
        {''.join(rows)}
      </ul>
    </section>
    """.strip()


def build_page(data: dict) -> str:
    groups = data["groups"]
    total = data["entryCount"]
    group_nav = "".join(
        f'<a href="#{escape(section_id(group))}">{escape(group["gradeLabel"])} · {escape(group["domainLabel"])} <span>{group["count"]}</span></a>'
        for group in groups
    )
    group_sections = "\n".join(render_group(group) for group in groups)

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
    .lesson-list {{ list-style: none; }}
    .lesson-row + .lesson-row {{ border-top: 1px solid #eef9f8; }}
    .lesson-link {{
      display: block;
      text-decoration: none;
      padding: 12px 16px;
      background: transparent;
    }}
    .lesson-link:hover {{ background: var(--teal-pale); }}
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


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_page(data), encoding="utf-8")
    print(f"Wrote review index page to {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
