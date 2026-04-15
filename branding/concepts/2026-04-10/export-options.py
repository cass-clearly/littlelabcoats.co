from pathlib import Path
import re

SRC = Path('branding/concepts/2026-04-10/branding-options.html')
out_dir = SRC.parent
html = SRC.read_text()
style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
articles = re.findall(r'(<article class="card concept-[a-d]">.*?</article>)', html, re.S)
meta = [
    ('option-a-pocket-lab', 'Option A — Pocket Lab'),
    ('option-b-rocket-notebook', 'Option B — Rocket Notebook'),
    ('option-c-tiny-scientist', 'Option C — Tiny Scientist'),
    ('option-d-coat-hanger-spark', 'Option D — Coat Hanger + Spark'),
]
for (slug, title), article in zip(meta, articles):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet" />
<style>
{style}
body {{ padding: 24px; background: linear-gradient(180deg, #f6fbff 0%, #fffdf8 100%); }}
.wrap {{ max-width: 980px; padding: 0; }}
.grid {{ display: block; }}
.card {{ margin: 0 auto; max-width: 900px; }}
.top, .analytics, .files {{ display: none; }}
</style>
</head>
<body>
<div class="wrap">
{article}
</div>
</body>
</html>'''
    (out_dir / f'{slug}.html').write_text(doc)
print('wrote', len(meta), 'html files')
