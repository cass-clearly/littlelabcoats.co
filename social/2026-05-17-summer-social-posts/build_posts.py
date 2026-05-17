from pathlib import Path
from textwrap import dedent

base = Path('/home/cass/.openclaw/workspace/littlelabcoats.co/social/2026-05-17-summer-social-posts')
posts_dir = base / 'posts'
images_dir = base / 'images'
posts_dir.mkdir(parents=True, exist_ok=True)

posts = [
    {
        'slug': '01-start-of-summer-sunshine-color-watch',
        'eyebrow': 'Little Lab Coats • Start of Summer Fun',
        'title': 'Sunshine Color Watch',
        'subtitle': 'A simple summer science invitation for little learners: notice what the sun warms, brightens, and changes outside.',
        'image': 'summer-sunshine-color-watch.png',
        'left_label': 'You need',
        'left_items': ['colored paper or crayons', 'a sunny patch outside', 'a clipboard or notebook'],
        'right_label': 'Try this',
        'right_items': ['set colors in sun and shade', 'check back after 10–20 minutes', 'ask what changed first'],
        'footer': 'Perfect for kindergarten and early elementary',
        'cta': 'Easy summer science',
        'accent': '#f6c85f',
        'sage': '#e6f3d8'
    },
    {
        'slug': '02-start-of-summer-fizzy-color-explosions',
        'eyebrow': 'Little Lab Coats • Start of Summer Fun',
        'title': 'Fizzy Color Explosions',
        'subtitle': 'Messy in the best way. Kids mix, predict, and watch bubbling reactions come alive with summer color.',
        'image': 'summer-fizzy-color-explosions.png',
        'left_label': 'You need',
        'left_items': ['baking soda', 'vinegar', 'food coloring or watercolor', 'droppers or spoons'],
        'right_label': 'Try this',
        'right_items': ['guess which color will spread fastest', 'mix one change at a time', 'talk about bubbles and gas'],
        'footer': 'Bright, playful, and great for save-worthy summer content',
        'cta': 'Kid favorite',
        'accent': '#ff9f68',
        'sage': '#fde7da'
    },
    {
        'slug': '03-start-of-summer-shadow-clock-mini-lab',
        'eyebrow': 'Little Lab Coats • Start of Summer Fun',
        'title': 'Shadow Clock Mini Lab',
        'subtitle': 'A first-grade-friendly outdoor science post that turns one sunny morning into observation, pattern spotting, and wonder.',
        'image': 'summer-shadow-clock-mini-lab.png',
        'left_label': 'You need',
        'left_items': ['chalk or paper markers', 'a sunny sidewalk or driveway', 'one object to track'],
        'right_label': 'Try this',
        'right_items': ['mark the shadow', 'check it later in the day', 'ask why it moved'],
        'footer': 'Perfect for first grade summer learning',
        'cta': 'Outdoor mini lab',
        'accent': '#8fc8ff',
        'sage': '#e3f2ff'
    },
    {
        'slug': '04-five-stem-activities-for-kindergarten',
        'eyebrow': 'Little Lab Coats • Kindergarten STEM',
        'title': '5 STEM Activities for Kindergarten',
        'subtitle': 'Gentle, hands-on ideas that build noticing, testing, comparing, and talking — without making home science feel overwhelming.',
        'image': 'kindergarten-5-stem-activities.png',
        'left_label': 'Try these',
        'left_items': ['ramp roll rescue', 'sink or float bowl', 'magnet hunt', 'leaf detective walk', 'paper bridge rescue'],
        'right_label': 'Why they work',
        'right_items': ['easy setup', 'real observation', 'great language-building', 'perfect for curious beginners'],
        'footer': 'Kindergarten science can stay simple and beautiful',
        'cta': 'Save for later',
        'accent': '#7acb9f',
        'sage': '#e2f5ea'
    },
    {
        'slug': '05-three-easy-first-grade-experiments',
        'eyebrow': 'Little Lab Coats • First Grade Science',
        'title': '3 Easy Hands-On Experiments for First Grade',
        'subtitle': 'Three approachable ways to bring patterns, light, sound, and questions into your week without buying a giant science kit.',
        'image': 'first-grade-3-easy-hands-on-experiments.png',
        'left_label': 'Start here',
        'left_items': ['shadow clock mini lab', 'vibrating strings and sound', 'mirror light signals'],
        'right_label': 'Talk about',
        'right_items': ['what changed', 'what stayed the same', 'what your child wants to test next'],
        'footer': 'Exactly the kind of post parents save and come back to',
        'cta': 'Low-prep wins',
        'accent': '#b79cff',
        'sage': '#efe9ff'
    },
    {
        'slug': '06-household-science-supplies',
        'eyebrow': 'Little Lab Coats • Science at Home',
        'title': 'Useful Items to Keep Around the House for Science',
        'subtitle': 'You do not need fancy supplies. A small stash of everyday materials can carry weeks of meaningful science play.',
        'image': 'science-supplies-around-the-house.png',
        'left_label': 'Keep these handy',
        'left_items': ['tape', 'toilet roll tubes', 'baking soda + vinegar', 'food coloring', 'paper plates'],
        'right_label': 'Also useful',
        'right_items': ['string', 'craft sticks', 'droppers', 'magnifying glass', 'measuring cups'],
        'footer': 'Practical, parent-helpful, and easy to share',
        'cta': 'Household science kit',
        'accent': '#f2b36d',
        'sage': '#fcebd9'
    },
    {
        'slug': '07-top-10-homeschool-science-tips',
        'eyebrow': 'Little Lab Coats • Homeschool Science',
        'title': 'Top 10 Tips for Homeschool Science',
        'subtitle': 'The goal is not a perfect lab. It is curious kids, a simple plan, and space to notice what happens.',
        'image': 'top-10-homeschool-science-tips.png',
        'left_label': 'Remember this',
        'left_items': ['keep it short', 'use what you have', 'let kids predict', 'repeat favorite experiments', 'go outside often'],
        'right_label': 'And this',
        'right_items': ['ask better questions', 'embrace a little mess', 'write down observations', 'link science to real life', 'stop before burnout'],
        'footer': 'A strong trust-building post for new followers',
        'cta': 'Share with a homeschool mom',
        'accent': '#f08aa5',
        'sage': '#fde6ee'
    },
]

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #f8fbf5;
      --card: #fffefb;
      --ink: #2f3b2d;
      --muted: #5f6f5d;
      --green: #456d42;
      --accent: {accent};
      --soft: {sage};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      background: linear-gradient(180deg, #edf6e8 0%, #f8fbf5 100%);
      color: var(--ink);
    }}
    .frame {{
      width: 1080px;
      min-height: 1350px;
      margin: 0 auto;
      padding: 52px;
    }}
    .card {{
      background: var(--card);
      border-radius: 34px;
      overflow: hidden;
      box-shadow: 0 25px 80px rgba(74, 110, 56, 0.15);
      border: 1px solid #e5eddf;
    }}
    .hero img {{
      display: block;
      width: 100%;
      height: 500px;
      object-fit: cover;
    }}
    .content {{ padding: 32px 36px 36px; }}
    .eyebrow {{
      display: inline-block;
      padding: 8px 15px;
      border-radius: 999px;
      background: var(--soft);
      color: var(--green);
      font-size: 22px;
      font-weight: 700;
      letter-spacing: 0.02em;
      margin-bottom: 14px;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: 54px;
      line-height: 1.04;
      color: #375e34;
    }}
    .sub {{
      margin: 0 0 22px;
      font-size: 26px;
      line-height: 1.4;
      color: var(--muted);
    }}
    .grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 18px;
    }}
    .box {{
      background: #fbfff8;
      border: 2px solid #e4eee0;
      border-radius: 24px;
      padding: 18px 20px 20px;
      min-height: 210px;
    }}
    .box h2 {{
      margin: 0 0 10px;
      font-size: 24px;
      color: #587627;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    ul {{
      margin: 0;
      padding-left: 26px;
    }}
    li {{
      font-size: 26px;
      line-height: 1.34;
      margin: 0 0 4px;
    }}
    .footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      margin-top: 8px;
    }}
    .tagline {{
      max-width: 700px;
      font-size: 23px;
      line-height: 1.28;
      color: var(--green);
      font-weight: 700;
    }}
    .cta {{
      background: var(--accent);
      color: #4d3a00;
      padding: 12px 18px;
      border-radius: 999px;
      font-size: 21px;
      font-weight: 700;
      text-align: center;
    }}
  </style>
</head>
<body>
  <div class="frame">
    <div class="card">
      <div class="hero"><img src="../images/{image}" alt="{title}" /></div>
      <div class="content">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <p class="sub">{subtitle}</p>
        <div class="grid">
          <div class="box">
            <h2>{left_label}</h2>
            <ul>
              {left_list}
            </ul>
          </div>
          <div class="box">
            <h2>{right_label}</h2>
            <ul>
              {right_list}
            </ul>
          </div>
        </div>
        <div class="footer">
          <div class="tagline">{footer}</div>
          <div class="cta">{cta}</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
'''

for post in posts:
    left_list = '\n'.join(f'<li>{item}</li>' for item in post['left_items'])
    right_list = '\n'.join(f'<li>{item}</li>' for item in post['right_items'])
    html = html_template.format(left_list=left_list, right_list=right_list, **post)
    (posts_dir / f"{post['slug']}.html").write_text(html)

captions = dedent('''
# Little Lab Coats — Summer Social Post Pack

## What I made
- 3 single-page “start of summer fun experiments” posts
- 1 kindergarten STEM infographic
- 1 first grade experiments infographic
- 1 household science supplies post
- 1 top 10 homeschool science tips post

## Captions

### 1) Sunshine Color Watch
Start-of-summer science does not need to be complicated.

This sunshine color watch is such an easy way to get little kids noticing what the sun changes, warms, and brightens.

All you really need is a sunny patch, a few colors, and a child ready to say, “Wait… that one changed!”

Save this for your next warm morning. ☀️

### 2) Fizzy Color Explosions
If you want one summer science activity that feels instantly exciting, this is it.

Kids get color, fizz, bubbles, prediction, and a tiny bit of glorious chaos — which is honestly a pretty strong recipe.

You can do this with simple household supplies and still get a real conversation going about reactions.

Save for summer science week.

### 3) Shadow Clock Mini Lab
This is one of my favorite first-grade science ideas because it turns an ordinary sunny day into a real investigation.

Mark the shadow, come back later, and suddenly your child is spotting patterns in the sky without needing a complicated setup.

Simple. Beautiful. Memorable.

### 4) 5 STEM Activities for Kindergarten
If you are doing kindergarten science at home, you do not need a giant plan.

You need a few gentle activities that invite your child to notice, compare, test, and talk.

These are five of my favorite low-pressure STEM ideas to keep in your back pocket.

### 5) 3 Easy Hands-On Experiments for First Grade
If first grade science has been feeling harder to plan than it should, start here.

These three hands-on ideas are simple to set up, easy to repeat, and actually give kids something real to observe and discuss.

Low prep. High curiosity. My favorite combination.

### 6) Useful Items to Keep Around the House for Science
You really do not need fancy science supplies to do meaningful science at home.

A few simple things like tape, toilet roll tubes, food coloring, droppers, paper plates, and measuring cups can carry so many experiments.

This is the kind of post I wish I had when I first started.

### 7) Top 10 Tips for Homeschool Science
If homeschool science feels like one more thing to figure out, here is the gentle reminder:

It does not have to be perfect to be powerful.

A short lesson, a simple material, one good question, and a child who is curious already gets you a long way.

Save this if you need science to feel more doable.

## More post ideas like this
1. 5 rainy-day science activities with household supplies
2. 10 questions to ask on a nature walk
3. 7 easy ways to make science feel less overwhelming
4. 5 kitchen items that secretly make great science tools
5. 10 things I wish I knew before homeschooling science
6. 3 science activities for kids who hate worksheets
7. 5 outdoor summer science invitations
8. 7 ways to turn a child’s question into a science lesson
9. 5 low-mess science ideas for busy weeks
10. 10 science words worth teaching naturally at home
11. 3 experiment ideas for mixed-age siblings
12. 5 signs your child is already thinking like a scientist

## My recommendation for what to post first
1. Useful Items to Keep Around the House for Science
2. 5 STEM Activities for Kindergarten
3. Fizzy Color Explosions
4. Top 10 Tips for Homeschool Science
5. Shadow Clock Mini Lab
''').strip() + '\n'

(base / 'captions-and-ideas.md').write_text(captions)
