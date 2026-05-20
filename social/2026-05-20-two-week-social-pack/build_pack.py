from pathlib import Path
from textwrap import dedent

base = Path('/home/cass/.openclaw/workspace/littlelabcoats.co/social/2026-05-20-two-week-social-pack')
posts_dir = base / 'posts'
images_dir = base / 'images'
final_dir = base / 'final-posts'
for d in (posts_dir, images_dir, final_dir):
    d.mkdir(parents=True, exist_ok=True)

posts = [
    {
        'slug': '01-rainy-day-science-activities',
        'title': '5 Rainy-Day Science Activities with Household Supplies',
        'eyebrow': 'Little Lab Coats • Rainy Day Science',
        'subtitle': 'When the weather traps everyone inside, these easy ideas turn an ordinary afternoon into real noticing, testing, and discovery.',
        'image': '01-rainy-day-science-activities.png',
        'left_label': 'Try these',
        'left_items': ['penny boat challenge', 'paper towel color walk', 'sink-or-float tub', 'foil rain cloud drop test', 'indoor shadow flashlight hunt'],
        'right_label': 'Why parents love them',
        'right_items': ['fast setup', 'simple supplies', 'easy sibling-friendly wins', 'real science talk without a huge mess'],
        'footer': 'Perfect for those “we need something now” afternoons.',
        'cta': 'Save this rainy-day list',
        'accent': '#8ecae6',
        'soft': '#e5f4fb',
        'caption': 'Rainy-day science does not need to be fancy.\n\nIf everyone is climbing the walls a little, these five household-supply ideas can rescue the afternoon without sending you into full prep mode.\n\nSimple setup. Real curiosity. Very solid trade.\n\nSave this for the next rainy day.',
        'image_prompt': 'Create a warm, colorful infographic-style hero illustration for a homeschool science social post. Scene: cozy rainy-day kitchen table with children doing easy science activities using household supplies — pennies and foil boats in a tub, paper towel color walking, flashlight shadows, cups and droppers. Style: bright modern editorial illustration, clean shapes, playful but polished, engaging for Instagram, lots of color, white space around subjects, no text, no letters, no numbers, no watermark. Vertical-safe composition with the main action centered.'
    },
    {
        'slug': '02-nature-walk-questions',
        'title': '10 Questions to Ask on a Nature Walk',
        'eyebrow': 'Little Lab Coats • Nature Walk Science',
        'subtitle': 'A good science lesson can start with one walk, one good question, and a child who notices something weird, beautiful, or surprising.',
        'image': '02-nature-walk-questions.png',
        'left_label': 'Questions to ask',
        'left_items': ['What do you notice first?', 'What looks different here?', 'What might live under that?', 'Why do you think that plant grows there?', 'What changed since last time?'],
        'right_label': 'Keep going with…',
        'right_items': ['What is making that sound?', 'Which surface feels warmest?', 'What patterns do you see?', 'What would you sketch to remember this?', 'What do you want to find out later?'],
        'footer': 'Nature walks get better when you bring better questions.',
        'cta': 'Screenshot for your next walk',
        'accent': '#95d5b2',
        'soft': '#e8f7ef',
        'caption': 'You do not need a formal lesson to do meaningful science outside.\n\nSometimes you just need better questions.\n\nThese are the kinds of prompts that help kids slow down, observe, compare, and wonder a little more deeply on a nature walk.\n\nSave this before your next outside day.',
        'image_prompt': 'Create a colorful infographic-style hero illustration for a homeschool science post about nature walks. Scene: parent and children on a leafy trail noticing plants, bugs, rocks, bird feathers, and tree bark with magnifying glass and sketch notebook. Bright, friendly, polished editorial style, engaging Instagram look, lots of natural greens and sunny accents, no text, no letters, no numbers, no watermark. Main figures centered with space for overlay text later.'
    },
    {
        'slug': '03-science-less-overwhelming',
        'title': '7 Easy Ways to Make Science Feel Less Overwhelming',
        'eyebrow': 'Little Lab Coats • Gentle Homeschool Science',
        'subtitle': 'If science keeps feeling like one more thing to organize, simplify the rhythm before you add more content.',
        'image': '03-science-less-overwhelming.png',
        'left_label': 'Do less, better',
        'left_items': ['pick one tiny goal', 'repeat favorite activities', 'keep lessons short', 'use everyday materials'],
        'right_label': 'Lower the pressure',
        'right_items': ['let questions count', 'skip perfect outcomes', 'stop while it is still fun'],
        'footer': 'Science feels lighter when it stops trying to be a whole production.',
        'cta': 'A calmer way to do science',
        'accent': '#f4a261',
        'soft': '#fdebdc',
        'caption': 'If homeschool science has been feeling heavier than it should, this is your reminder that it can be much simpler.\n\nShorter lessons. Fewer materials. More repetition. Better questions.\n\nYou do not need a perfect lab setup to raise a curious kid.\n\nSave this if you need science to feel more doable again.',
        'image_prompt': 'Create a colorful infographic-style hero illustration for a homeschooling post about making science feel less overwhelming. Scene: calm organized table with a few simple science supplies, open notebook, magnifying glass, measuring cups, child and parent smiling, relaxed atmosphere, soft cheerful colors, polished editorial illustration, no text, no letters, no numbers, no watermark. Make it feel calming, approachable, and uncluttered.'
    },
    {
        'slug': '04-kitchen-items-science-tools',
        'title': '5 Kitchen Items That Secretly Make Great Science Tools',
        'eyebrow': 'Little Lab Coats • Science at Home',
        'subtitle': 'Some of the best science tools are already sitting in your kitchen drawer just waiting for a better reputation.',
        'image': '04-kitchen-items-science-tools.png',
        'left_label': 'Grab these',
        'left_items': ['measuring cups', 'mixing bowls', 'ice cube trays', 'coffee filters', 'turkey baster or dropper'],
        'right_label': 'Use them for',
        'right_items': ['pouring and measuring', 'sorting and mixing', 'freezing mini tests', 'color walking and filtering', 'transferring liquids'],
        'footer': 'You probably already own a surprisingly decent little science kit.',
        'cta': 'Kitchen science wins',
        'accent': '#ffb703',
        'soft': '#fff2ce',
        'caption': 'You really do not need fancy science equipment to do good science at home.\n\nA few kitchen basics can cover measuring, mixing, sorting, testing, and observing better than most people expect.\n\nThis is one of my favorite reminders for busy weeks.\n\nSave this for the next time you think, “We do not have the right supplies.”',
        'image_prompt': 'Create a bright colorful infographic-style hero illustration for a social post about kitchen items used as science tools. Scene: cheerful kitchen counter with measuring cups, bowls, droppers, coffee filters, ice cube tray, child experimenting with colored water. Clean modern editorial illustration, playful but polished, vivid color, no text, no letters, no numbers, no watermark, centered composition.'
    },
    {
        'slug': '05-things-i-wish-i-knew',
        'title': '10 Things I Wish I Knew Before Homeschooling Science',
        'eyebrow': 'Little Lab Coats • Honest Homeschool Science',
        'subtitle': 'The biggest shift is realizing science at home works better when it feels alive, flexible, and conversation-rich — not overbuilt.',
        'image': '05-things-i-wish-i-knew.png',
        'left_label': 'I wish I knew…',
        'left_items': ['short counts', 'questions count', 'repeat lessons are okay', 'mess is not failure', 'observation matters more than polish'],
        'right_label': 'Also true',
        'right_items': ['you do not need every supply', 'outside time counts', 'kids remember wonder', 'simple beats complicated', 'you can grow into this'],
        'footer': 'The practical version, not the guilt version.',
        'cta': 'For newer homeschool moms',
        'accent': '#e76f51',
        'soft': '#fbe4dd',
        'caption': 'There are so many things I thought homeschool science had to be before I realized it could be simpler, richer, and much more doable.\n\nIf you are newer to this, I hope this post saves you a little unnecessary pressure.\n\nScience at home gets better when it gets more human.\n\nSave this one for the days you need perspective.',
        'image_prompt': 'Create a colorful editorial infographic-style hero illustration for a homeschooling science reflection post. Scene: mother and kids doing science at home with notebooks, leaves, measuring cups, jars, and a relaxed encouraging mood. Warm tones, polished illustration, engaging social-media aesthetic, no text, no letters, no numbers, no watermark. Should feel honest, supportive, and inspiring.'
    },
    {
        'slug': '06-no-worksheet-science',
        'title': '3 Science Activities for Kids Who Hate Worksheets',
        'eyebrow': 'Little Lab Coats • Hands-On Science',
        'subtitle': 'If paper shuts your child down, lead with movement, play, and materials first — the learning can still be wonderfully real.',
        'image': '06-no-worksheet-science.png',
        'left_label': 'Try these instead',
        'left_items': ['balloon rocket race', 'mystery sink-or-float basket', 'backyard bug detective hunt'],
        'right_label': 'Why they help',
        'right_items': ['less resistance', 'more movement', 'real observations', 'easy conversation after the activity'],
        'footer': 'Some kids show their best science thinking with their hands busy.',
        'cta': 'No worksheet required',
        'accent': '#bde0fe',
        'soft': '#edf7ff',
        'caption': 'Not every child wants to prove they learned something by filling in boxes on a page.\n\nSome kids learn best when they are moving, building, hunting, testing, and talking.\n\nThese three ideas are especially good for kids who light up with hands-on science but shut down with worksheets.\n\nSave this for your kinesthetic learner.',
        'image_prompt': 'Create a playful colorful infographic-style hero illustration for a homeschool science post about kids who hate worksheets. Scene: energetic children doing balloon rocket race, bug hunt with magnifying glass, and sink-or-float testing, with no desks or worksheets in view. Bright fun colors, polished editorial illustration, engaging Instagram style, no text, no letters, no numbers, no watermark.'
    },
    {
        'slug': '07-outdoor-summer-science-invitations',
        'title': '5 Outdoor Summer Science Invitations',
        'eyebrow': 'Little Lab Coats • Summer Science',
        'subtitle': 'These simple invitations help summer science feel open-ended, playful, and easy to say yes to when the weather is gorgeous.',
        'image': '07-outdoor-summer-science-invitations.png',
        'left_label': 'Invite them to…',
        'left_items': ['compare hot and cool surfaces', 'build a leaf color chart', 'track shadows', 'test paper airplanes outside', 'watch ants at work'],
        'right_label': 'Keep nearby',
        'right_items': ['clipboard', 'colored pencils', 'magnifying glass', 'water bottle', 'one good question'],
        'footer': 'Summer science gets easier when it starts with an invitation, not a lecture.',
        'cta': 'Outdoor science ideas',
        'accent': '#90be6d',
        'soft': '#edf7e5',
        'caption': 'Outdoor science does not have to be complicated to be memorable.\n\nA simple invitation like “Let’s compare what feels hottest” or “Let’s see if the shadows move” can carry a whole beautiful little lesson.\n\nThis is the kind of summer science I keep coming back to.\n\nSave this for the next sunny day.',
        'image_prompt': 'Create a bright colorful infographic-style hero illustration for an outdoor summer science post. Scene: children outdoors with clipboard, magnifying glass, leaves, shadows on pavement, paper airplanes, and insects in garden. Sunny, joyful, polished editorial illustration, engaging for Instagram, no text, no letters, no numbers, no watermark. Strong summer feel with greens, sky blues, and warm sunshine.'
    },
    {
        'slug': '08-child-question-to-science-lesson',
        'title': '7 Ways to Turn a Child’s Question into a Science Lesson',
        'eyebrow': 'Little Lab Coats • Curious Kids',
        'subtitle': 'The best science lessons often start with a child asking something slightly inconvenient at exactly the right time.',
        'image': '08-child-question-to-science-lesson.png',
        'left_label': 'When they ask “why…”',
        'left_items': ['slow down', 'repeat the question', 'ask what they think first', 'test one small part'],
        'right_label': 'Then try this',
        'right_items': ['observe together', 'compare two examples', 'write down what changed'],
        'footer': 'A child’s question is often the lesson plan trying to introduce itself.',
        'cta': 'Curiosity → lesson',
        'accent': '#cdb4db',
        'soft': '#f4ecf8',
        'caption': 'One of the easiest ways to make science feel more natural at home is to start with the question your child is already asking.\n\nYou do not need a huge detour. Just a small habit of slowing down, wondering together, and testing something simple.\n\nThat is often enough to turn a moment into a lesson.\n\nSave this if you want science to feel more organic.',
        'image_prompt': 'Create a colorful editorial infographic-style hero illustration for a homeschool science post about turning child questions into lessons. Scene: curious child asking a parent about a puddle, plant, bug, or rainbow while they investigate together with notebook and magnifying glass. Warm, bright, polished illustration, engaging and thoughtful, no text, no letters, no numbers, no watermark.'
    },
    {
        'slug': '09-low-mess-science-ideas',
        'title': '5 Low-Mess Science Ideas for Busy Weeks',
        'eyebrow': 'Little Lab Coats • Busy Week Science',
        'subtitle': 'You can keep science in the rhythm without choosing projects that leave your kitchen looking personally betrayed.',
        'image': '09-low-mess-science-ideas.png',
        'left_label': 'Low-mess ideas',
        'left_items': ['ice melt race', 'magnet basket test', 'cloud spotting chart', 'shadow tracing', 'dry seed sorting investigation'],
        'right_label': 'Best for',
        'right_items': ['tight afternoons', 'younger siblings nearby', 'minimal cleanup', 'keeping momentum without burnout'],
        'footer': 'Busy-week science can still feel thoughtful without becoming a whole cleanup event.',
        'cta': 'Low-mess favorites',
        'accent': '#84a59d',
        'soft': '#e8f1ef',
        'caption': 'Some weeks you want science to happen… but you do not want to mop after it.\n\nThese are the kinds of simple ideas I would reach for in a busy season when I still want curiosity in the week without adding chaos to the house.\n\nLow mess. Low prep. Still worth doing.\n\nSave this one.',
        'image_prompt': 'Create a colorful infographic-style hero illustration for a homeschooling post about low-mess science. Scene: neat table with ice cubes, magnets, seeds, simple shadow tracing, and a child calmly observing. Organized, polished editorial illustration with gentle colors, engaging for social media, no text, no letters, no numbers, no watermark. Make it feel tidy and realistic.'
    },
    {
        'slug': '10-science-words-to-teach-naturally',
        'title': '10 Science Words Worth Teaching Naturally at Home',
        'eyebrow': 'Little Lab Coats • Science Language',
        'subtitle': 'The best science vocabulary sticks when it shows up inside real experiences instead of floating alone on a word list.',
        'image': '10-science-words-to-teach-naturally.png',
        'left_label': 'Useful words',
        'left_items': ['observe', 'predict', 'compare', 'measure', 'evidence'],
        'right_label': 'Also worth using',
        'right_items': ['pattern', 'change', 'test', 'record', 'result'],
        'footer': 'Natural science language grows best when kids can use it right away.',
        'cta': 'Teach these naturally',
        'accent': '#f28482',
        'soft': '#fde9e8',
        'caption': 'You do not need flashcards to build science vocabulary at home.\n\nA lot of the most useful science words can be taught naturally while your child is already observing, testing, measuring, and talking about what happened.\n\nThis is the kind of language support that feels simple but adds up.\n\nSave this to keep a few good words in your back pocket.',
        'image_prompt': 'Create a colorful editorial infographic-style hero illustration for a homeschool science language post. Scene: children observing plants and jars with notebook, ruler, magnifying glass, and parent talking with them. Polished bright illustration with educational feel, no text, no letters, no numbers, no watermark. Make it feel thoughtful and natural rather than classroom-stiff.'
    },
    {
        'slug': '11-mixed-age-sibling-experiments',
        'title': '3 Experiment Ideas for Mixed-Age Siblings',
        'eyebrow': 'Little Lab Coats • Mixed-Age Homeschooling',
        'subtitle': 'The sweet spot is choosing one experiment where younger kids can notice and older kids can explain or extend.',
        'image': '11-mixed-age-sibling-experiments.png',
        'left_label': 'Try these together',
        'left_items': ['baking soda balloon inflation', 'paper bridge strength test', 'frozen toy melt rescue'],
        'right_label': 'How to scale them',
        'right_items': ['younger kids sort and notice', 'older kids predict and record', 'everyone compares results'],
        'footer': 'One experiment can hold more than one age when the roles are layered well.',
        'cta': 'For sibling science',
        'accent': '#a0c4ff',
        'soft': '#edf4ff',
        'caption': 'Mixed-age science gets easier when you stop trying to make every child do the exact same job.\n\nA younger child can observe, sort, pour, and compare. An older child can predict, measure, record, and explain.\n\nThe same experiment can stretch in beautiful ways.\n\nSave this if you are juggling multiple ages at home.',
        'image_prompt': 'Create a colorful infographic-style hero illustration for a mixed-age sibling science post. Scene: two or three siblings of different ages doing one experiment together at home — balloon inflation, paper bridge test, frozen toy rescue. Friendly polished editorial illustration, lively but organized, no text, no letters, no numbers, no watermark.'
    },
    {
        'slug': '12-thinking-like-a-scientist-signs',
        'title': '5 Signs Your Child Is Already Thinking Like a Scientist',
        'eyebrow': 'Little Lab Coats • Quiet Wins',
        'subtitle': 'It often shows up long before a polished notebook page does — in questions, comparisons, patterns, and stubborn little experiments of their own.',
        'image': '12-thinking-like-a-scientist-signs.png',
        'left_label': 'You might notice…',
        'left_items': ['they ask follow-up questions', 'they compare what changed', 'they repeat things on purpose'],
        'right_label': 'And also…',
        'right_items': ['they look for patterns', 'they test their own ideas', 'they want to show you evidence'],
        'footer': 'Science thinking often looks wonderfully ordinary before it looks academic.',
        'cta': 'Encouragement post',
        'accent': '#f6bd60',
        'soft': '#fff2d9',
        'caption': 'Sometimes it helps to remember that science thinking does not always look like a formal lesson.\n\nIt can look like a child repeating something to see if it happens again. Or comparing two leaves. Or insisting, “No wait, look at this.”\n\nThose quiet little moments count. A lot.\n\nSave this for the days you need the reminder.',
        'image_prompt': 'Create a warm colorful editorial infographic-style hero illustration for a post about signs a child is thinking like a scientist. Scene: child noticing patterns, comparing leaves or shells, repeating a small experiment, excitedly showing evidence to a parent. Polished illustration, encouraging emotional tone, bright but gentle palette, no text, no letters, no numbers, no watermark.'
    },
]

page_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #f6fbf4;
      --card: #fffefb;
      --ink: #28352b;
      --muted: #5f6d62;
      --green: #446c4c;
      --accent: {accent};
      --soft: {soft};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      background: linear-gradient(180deg, #edf6e8 0%, #f9fcf7 100%);
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
      box-shadow: 0 24px 80px rgba(68,108,76,0.13);
      border: 1px solid #e5ede0;
    }}
    .hero img {{
      display: block;
      width: 100%;
      height: 500px;
      object-fit: cover;
      background: #fff;
    }}
    .content {{ padding: 32px 36px 36px; }}
    .eyebrow {{
      display: inline-block;
      padding: 8px 15px;
      border-radius: 999px;
      background: var(--soft);
      color: var(--green);
      font: 700 22px/1.1 Arial, sans-serif;
      margin-bottom: 14px;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: 52px;
      line-height: 1.03;
      color: #365d3d;
    }}
    .sub {{
      margin: 0 0 22px;
      font-size: 26px;
      line-height: 1.38;
      color: var(--muted);
    }}
    .grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 18px;
    }}
    .box {{
      background: #fbfff9;
      border: 2px solid #e3ece0;
      border-radius: 24px;
      padding: 18px 20px 20px;
      min-height: 230px;
    }}
    .box h2 {{
      margin: 0 0 10px;
      font: 700 24px/1.1 Arial, sans-serif;
      color: #567626;
      text-transform: uppercase;
      letter-spacing: .05em;
    }}
    ul {{ margin: 0; padding-left: 26px; }}
    li {{ font-size: 26px; line-height: 1.34; margin: 0 0 4px; }}
    .footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      margin-top: 8px;
    }}
    .tagline {{
      max-width: 710px;
      font-size: 23px;
      line-height: 1.28;
      color: var(--green);
      font-weight: 700;
    }}
    .cta {{
      background: var(--accent);
      color: #4f3a00;
      padding: 12px 18px;
      border-radius: 999px;
      font: 700 21px/1.1 Arial, sans-serif;
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
    html = page_template.format(left_list=left_list, right_list=right_list, **post)
    (posts_dir / f"{post['slug']}.html").write_text(html)

captions = ['# Little Lab Coats — Two-Week Social Post Pack', '', '## Captions']
for i, post in enumerate(posts, start=1):
    captions.extend([f"", f"### {i}) {post['title']}", post['caption']])
(base / 'captions-and-ideas.md').write_text('\n'.join(captions).strip() + '\n')

prompt_manifest = ['# GPT-Image-2 Prompt Manifest', '']
for post in posts:
    prompt_manifest.extend([f"## {post['title']}", post['image_prompt'], ''])
(base / 'image-prompts.md').write_text('\n'.join(prompt_manifest).strip() + '\n')

cards = []
for post in posts:
    cards.append(f'''
      <div class="card">
        <img src="../images/{post['image']}" alt="{post['title']} preview" />
        <div class="eyebrow">{post['eyebrow']}</div>
        <h2>{post['title']}</h2>
        <p>{post['subtitle']}</p>
        <div class="actions">
          <a class="btn btn-primary" href="../posts/{post['slug']}.html">Open post</a>
          <a class="btn btn-secondary" href="../images/{post['image']}">Open image</a>
        </div>
      </div>
    ''')

hub = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Little Lab Coats — Two-Week Social Pack</title>
  <style>
    :root {{
      --bg: #f5faf3;
      --card: #fffefb;
      --ink: #243127;
      --muted: #5d6b5e;
      --green: #416b47;
      --border: #e3ecdf;
      --shadow: 0 18px 50px rgba(65, 107, 71, 0.12);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      background: linear-gradient(180deg, #edf7e9 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    .wrap {{ max-width: 1240px; margin: 0 auto; padding: 40px 24px 56px; }}
    .hero {{ background: var(--card); border: 1px solid var(--border); border-radius: 28px; padding: 28px; box-shadow: var(--shadow); margin-bottom: 24px; }}
    .pill {{ display:inline-block; padding:8px 14px; border-radius:999px; background:#e6f4e7; color:var(--green); font:800 14px/1 Arial,sans-serif; letter-spacing:.04em; text-transform:uppercase; margin-bottom:12px; }}
    h1 {{ margin:0 0 10px; font-size:42px; line-height:1; color:#355d3d; }}
    .hero p {{ margin:0; font-size:20px; line-height:1.35; color:var(--muted); max-width:900px; }}
    .meta {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:18px; font:700 15px/1.2 Arial,sans-serif; color:#355d3d; }}
    .meta span {{ background:#f1f7ef; border:1px solid #dbe7d8; padding:10px 12px; border-radius:999px; }}
    .section-title {{ margin:30px 0 14px; font-size:28px; color:#355d3d; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:18px; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:24px; padding:18px; box-shadow:0 12px 30px rgba(65,107,71,0.08); display:flex; flex-direction:column; gap:12px; }}
    .card img {{ width:100%; height:190px; object-fit:cover; border-radius:16px; border:1px solid #e8eee4; background:#fff; }}
    .card .eyebrow {{ color:#5d6b5e; font:700 13px/1 Arial,sans-serif; text-transform:uppercase; letter-spacing:.06em; }}
    .card h2 {{ margin:0; font-size:24px; line-height:1.08; color:#355d3d; }}
    .card p {{ margin:0; font-size:17px; line-height:1.32; color:var(--muted); flex:1; }}
    .actions {{ display:flex; flex-wrap:wrap; gap:10px; }}
    .btn {{ text-decoration:none; border-radius:999px; padding:10px 14px; font:800 14px/1 Arial,sans-serif; }}
    .btn-primary {{ background:#3f6f4d; color:#fff; }}
    .btn-secondary {{ background:#eef6ee; color:#355d3d; border:1px solid #dce8dc; }}
    .doc-list {{ display:grid; gap:12px; }}
    .doc-item {{ background:var(--card); border:1px solid var(--border); border-radius:20px; padding:16px 18px; box-shadow:0 10px 24px rgba(65,107,71,0.06); }}
    .doc-item strong {{ display:block; margin-bottom:6px; font-size:20px; color:#355d3d; }}
    .doc-item a {{ color:#2f5f84; text-decoration:none; word-break:break-all; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <div class="pill">Little Lab Coats • Social Hub</div>
      <h1>Two-Week Social Post Pack</h1>
      <p>Twelve ready-to-schedule infographic-style social posts for Little Lab Coats, each with a GPT-Image-2 visual, polished post layout, and caption copy in one place.</p>
      <div class="meta">
        <span>12 finished post layouts</span>
        <span>12 GPT-Image-2 graphics</span>
        <span>Caption file included</span>
      </div>
    </div>

    <h2 class="section-title">Post hub</h2>
    <div class="grid">
      {''.join(cards)}
    </div>

    <h2 class="section-title">Supporting files</h2>
    <div class="doc-list">
      <div class="doc-item"><strong>Captions and scheduling copy</strong><a href="../captions-and-ideas.md">Open captions-and-ideas.md</a></div>
      <div class="doc-item"><strong>Image prompt manifest</strong><a href="../image-prompts.md">Open image-prompts.md</a></div>
      <div class="doc-item"><strong>Build script</strong><a href="../build_pack.py">Open build_pack.py</a></div>
    </div>
  </div>
</body>
</html>
'''

(final_dir / 'index.html').write_text(hub)
print(f'Built {len(posts)} posts in {base}')
