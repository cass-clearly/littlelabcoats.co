from pathlib import Path
root = Path('lesson-plans')
base_style = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 8.5in; margin: 0 auto; padding: 0.5in; font-size: 11pt; line-height: 1.4; color: #222; }}
    h1 {{ text-align: center; font-size: 22pt; margin-bottom: 5px; border-bottom: 3px solid #8e44ad; padding-bottom: 10px; color: #8e44ad; }}
    .subtitle {{ text-align: center; font-style: italic; margin-bottom: 20px; color: #555; font-size: 13pt; }}
    .meta {{ display: flex; justify-content: space-between; background: #f4e6fb; padding: 10px 15px; border-radius: 8px; margin-bottom: 20px; font-size: 10pt; border: 1px solid #d2b4de; flex-wrap: wrap; gap: 5px; }}
    h2 {{ font-size: 14pt; background: #8e44ad; color: white; padding: 8px 14px; margin: 24px 0 12px 0; border-radius: 6px; }}
    h3 {{ font-size: 12pt; color: #6c3483; border-bottom: 2px solid #d2b4de; padding-bottom: 4px; margin: 18px 0 8px 0; }}
    ul, ol {{ margin: 8px 0; padding-left: 25px; }}
    li {{ margin-bottom: 5px; }}
    .hero-image {{ text-align: center; margin: 16px 0; }}
    .emoji-hero {{ font-size: 64pt; line-height: 1.2; }}
    .caption {{ font-size: 9pt; color: #777; font-style: italic; margin-top: 4px; }}
    .standards-box {{ background: #f3e5f5; border: 1px solid #ce93d8; border-radius: 8px; padding: 14px 18px; margin: 10px 0; font-size: 10pt; }}
    .objective-box {{ background: #f4e6fb; border: 2px solid #d2b4de; border-radius: 8px; padding: 14px 18px; margin: 10px 0; }}
    .materials-box {{ background: #fff8e1; border: 2px solid #ffcc80; padding: 14px 18px; border-radius: 8px; margin: 10px 0; }}
    .materials-box h3 {{ color: #6c3483; border-color: #ffcc80; }}
    .procedure-step {{ background: #f4e6fb; padding: 10px 15px; margin: 8px 0; border-radius: 6px; border-left: 5px solid #8e44ad; }}
    .question-box {{ background: #fffaf3; border-left: 5px solid #ff8f00; padding: 10px 15px; margin: 10px 0; border-radius: 0 6px 6px 0; }}
    .tip-box {{ background: #e0f7fa; border-left: 5px solid #00bcd4; padding: 10px 15px; margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 10pt; }}
    .extension-box {{ background: #e8eaf6; border: 1px solid #9fa8da; border-radius: 8px; padding: 14px 18px; margin: 10px 0; }}
    .teacher-note, .answer-key {{ background: #f5f5f5; border: 2px dashed #999; border-radius: 8px; padding: 15px; margin: 20px 0; font-size: 10pt; color: #555; }}
    .answer-key {{ border-width: 3px; padding: 20px; }}
    .discussion-hint {{ font-style: italic; color: #555; font-size: 10pt; margin-top: 4px; display: block; }}
    .vocab-chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0; }}
    .vocab-chip {{ background: #faf5ff; border: 1.5px solid #8e44ad; border-radius: 20px; padding: 4px 14px; font-size: 10pt; font-weight: bold; color: #6c3483; }}
    .callout-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin: 16px 0; }}
    .callout-card {{ border: 2px solid #d2b4de; border-radius: 10px; padding: 12px; background: #fff; }}
    .callout-card strong {{ color: #6c3483; }}
    .worksheet-section {{ margin: 20px 0; }}
    .name-date {{ text-align: center; margin-bottom: 16px; font-size: 12pt; }}
    .draw-area {{ border: 1.5px dashed #bbb; border-radius: 6px; height: 90px; background: #fafafa; margin-top: 8px; }}
    .line-block p {{ border-bottom: 1.5px solid #bbb; height: 30px; margin: 0 0 10px 0; }}
    .compare-table {{ width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 10pt; }}
    .compare-table th {{ background: #8e44ad; color: white; padding: 8px 10px; border: 1.5px solid #6c3483; text-align: left; }}
    .compare-table td {{ border: 1.5px solid #d2b4de; padding: 10px; vertical-align: top; height: 46px; }}
    .compare-table tr:nth-child(even) td {{ background: #faf5ff; }}
    .page-break {{ page-break-before: always; break-before: page; }}
    .print-btn {{ position: fixed; top: 20px; right: 20px; background: #8e44ad; color: white; border: none; padding: 10px 18px; border-radius: 8px; font-size: 0.95rem; font-weight: 600; cursor: pointer; z-index: 1000; }}
    .llc-paywall-overlay {{ position: fixed; bottom: 0; left: 0; right: 0; background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,0.97) 30%, #fff 100%); padding: 48px 24px 40px; text-align: center; z-index: 1000; box-shadow: 0 -8px 40px rgba(59,31,107,0.12); }}
    .llc-paywall-inner {{ max-width: 520px; margin: 0 auto; }}
    .llc-paywall-emoji {{ font-size: 2.2rem; display: block; margin-bottom: 8px; }}
    .llc-paywall-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; color: #3B1F6B; margin-bottom: 8px; }}
    .llc-paywall-sub {{ font-family: 'Lato', sans-serif; font-size: 0.95rem; color: #5A7A78; margin-bottom: 20px; line-height: 1.5; }}
    .llc-btn-subscribe {{ display: inline-block; background: #FF6B6B; color: #fff; font-family: 'Lato', sans-serif; font-weight: 700; font-size: 1rem; padding: 14px 32px; border-radius: 8px; text-decoration: none; }}
    @media print {{
      h1, h2, h3 {{ break-after: avoid; }}
      .procedure-step, .question-box, .teacher-note, .materials-box, .tip-box, .extension-box, .answer-key, .callout-card {{ break-inside: avoid; page-break-inside: avoid; }}
      .print-btn, .llc-paywall-overlay {{ display: none !important; }}
      * {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    }}
  </style>
</head>
<body data-document-id=\"{doc_id}\">
  <button class=\"print-btn\" onclick=\"window.print()\">🖨️ Print Lesson</button>
  <h1>{h1}</h1>
  <p class=\"subtitle\">Engineering — {unit} | Unit 1, Lesson {lesson_no} of 6</p>
  <div class=\"meta\"><span>📚 <strong>Grade:</strong> 5th Grade</span><span>⏱️ <strong>Duration:</strong> {duration}</span><span>🛠️ <strong>Subject:</strong> Engineering — {unit}</span></div>
  <div class=\"hero-image\"><div class=\"emoji-hero\">{hero}</div><div class=\"caption\">{caption}</div></div>
  <div class=\"standards-box\"><strong>📋 NGSS Standard:</strong><br><strong>3-5-ETS1-1 / 3-5-ETS1-2 / 3-5-ETS1-3</strong> — Define a design problem that reflects a need or a want, includes specified criteria for success and constraints on materials, time, or cost; generate and compare multiple possible solutions; and plan and carry out fair tests with variables controlled.</div>
  <h2>🎯 Learning Objective</h2>
  <div class=\"objective-box\"><p>{objective}</p></div>
  <h2>💡 The Big Idea</h2>
  <p>{big_idea}</p>
  <h2>🔬 Engineering Thinking</h2>
  {science}
  <div class=\"tip-box\"><strong>💡 Key Vocabulary</strong><div class=\"vocab-chips\">{vocab}</div></div>
  <div class=\"callout-grid\">{callouts}</div>
  <h2>Materials</h2>
  <div class=\"materials-box\"><h3>🏠 Household Items to Gather</h3><ul>{materials}</ul><h3>📋 Printables</h3><ul><li>Student worksheet page from this lesson</li></ul></div>
  <h2>Let's Get Started</h2>
  {steps}
  <h2>Discussion Questions</h2>
  {questions}
  <h2>Extensions</h2>
  <div class=\"extension-box\">{extensions}</div>
  <h2>Parent/Teacher Notes</h2>
  <div class=\"teacher-note\">{notes}</div>
  <div class=\"page-break\"><h2>Student Worksheet</h2>
{worksheet}
</div>
  <div class=\"page-break\"><div class=\"answer-key\"><h2>✂️ PARENT ANSWER KEY — Detach before giving worksheet to students</h2>
{answer_key}
</div></div>
  <script src=\"https://cassclearly.com/feedback-layer.js?v=20260408\" data-api-url=\"https://cassclearly.com\" data-document-id=\"{doc_id}\" data-content-selector=\"body\"></script>
  <div class=\"llc-paywall-overlay\" id=\"llcPaywall\" style=\"display:none;\"><div class=\"llc-paywall-inner\"><span class=\"llc-paywall-emoji\">🥼</span><div class=\"llc-paywall-title\">This is a preview. Unlock the full lesson.</div><p class=\"llc-paywall-sub\">You're seeing the lesson preview. Subscribe to access the full procedure, Student Worksheet, discussion questions, and Parent Answer Key — for every lesson in the K–5 curriculum.<br><strong>$99/year. Cancel anytime.</strong></p><a href=\"/store.html\" class=\"llc-btn-subscribe\">Subscribe to Unlock — $99/yr</a></div></div>
  <script>
  (function() {{
    var ACCESS_KEY = 'llc_access';
    function isUnlocked() {{ return localStorage.getItem(ACCESS_KEY) === 'granted'; }}
    function lockLesson() {{
      var allH2 = Array.from(document.querySelectorAll('h2'));
      var lockKeywords = ['materials', 'gather before you start', 'what you need'];
      var lockFromH2 = null;
      for (var i = 0; i < allH2.length; i++) {{
        var text = allH2[i].textContent.toLowerCase().trim();
        if (lockKeywords.some(function(k) {{ return text.indexOf(k) !== -1; }})) {{ lockFromH2 = allH2[i]; break; }}
      }}
      if (!lockFromH2) {{ lockFromH2 = allH2[Math.min(4, allH2.length - 1)]; }}
      if (!lockFromH2) {{ document.body.style.overflow = 'hidden'; document.body.style.maxHeight = '600px'; document.getElementById('llcPaywall').style.display = 'block'; return; }}
      var hiding = false;
      Array.from(document.body.children).forEach(function(child) {{
        if (child === lockFromH2 || child.contains(lockFromH2)) hiding = true;
        if (hiding && child.id !== 'llcPaywall') child.style.display = 'none';
      }});
      document.getElementById('llcPaywall').style.display = 'block';
    }}
    document.addEventListener('DOMContentLoaded', function() {{
      if (window.location.search.indexOf('review=1') !== -1) {{ try {{ localStorage.setItem(ACCESS_KEY, 'granted'); }} catch (e) {{}} return; }}
      if (!isUnlocked()) lockLesson();
    }});
  }})();
  </script>
  <div style=\"text-align:center; padding: 24px 16px 16px; font-family: 'Lato', sans-serif; font-size: 0.78rem; color: #999; border-top: 1px solid #eee; margin-top: 32px;\">© 2026 Little Lab Coats. For personal, non-commercial use only. Unauthorized reproduction, redistribution, or resale is prohibited. Printed copies are for use within your immediate household only.</div>
</body>
</html>
"""
ref_style = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; max-width: 8.5in; margin: 0 auto; padding: 0.45in; color: #4a235a; background: #ffffff; }}
    h1 {{ font-size: 24px; margin: 0 0 6px; color: #8e44ad; text-align: center; }}
    .subtitle {{ text-align: center; color: #567; margin-bottom: 16px; font-size: 14px; }}
    .card {{ border: 2px solid #d2b4de; border-radius: 14px; padding: 18px; background: linear-gradient(180deg,#faf5ff 0%,#f4ecfb 100%); }}
    .section {{ margin-bottom: 16px; }}
    .section-title {{ font-weight: 700; color: #8e44ad; margin-bottom: 6px; font-size: 15px; }}
    ul {{ margin: 6px 0 0 20px; }}
    li {{ margin-bottom: 6px; }}
    .key-box {{ background: #fff8e1; border: 2px solid #ffcc80; border-radius: 10px; padding: 12px; }}
    .example-box {{ background: #f4e6fb; border: 2px solid #d2b4de; border-radius: 10px; padding: 12px; }}
    .use-box {{ background: #eef7ff; border: 2px solid #90caf9; border-radius: 10px; padding: 12px; }}
  </style>
</head>
<body data-document-id=\"{doc_id}\">
  <div class=\"card\">
    <h1>{h1}</h1>
    <div class=\"subtitle\">Grade 5 Engineering — {unit} Quick Reference</div>
    <div class=\"section key-box\"><div class=\"section-title\">Big Idea</div><p>{big_idea}</p></div>
    <div class=\"section\"><div class=\"section-title\">Key Vocabulary</div><ul>{vocab_items}</ul></div>
    <div class=\"section example-box\"><div class=\"section-title\">Remember This</div><ul>{remember}</ul></div>
    <div class=\"section use-box\"><div class=\"section-title\">Use It to Explain</div><ul>{use_it}</ul></div>
  </div>
<script src=\"https://cassclearly.com/feedback-layer.js?v=20260408\" data-api-url=\"https://cassclearly.com\" data-document-id=\"{doc_id}\" data-content-selector=\"body\"></script></body>
</html>
"""
quiz_template = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 8.5in; margin: 0 auto; padding: 0.45in; font-size: 11pt; line-height: 1.45; color: #222; background: #fff; }}
    h1 {{ text-align: center; font-size: 22pt; margin-bottom: 5px; border-bottom: 3px solid #8e44ad; padding-bottom: 10px; color: #8e44ad; }}
    .subtitle {{ text-align: center; font-style: italic; margin-bottom: 20px; color: #555; font-size: 13pt; }}
    .meta {{ display: flex; justify-content: space-between; background: #f4e6fb; padding: 10px 15px; border-radius: 8px; margin-bottom: 20px; font-size: 10pt; border: 1px solid #d2b4de; flex-wrap: wrap; gap: 5px; }}
    h2 {{ font-size: 14pt; background: #8e44ad; color: white; padding: 8px 14px; margin: 24px 0 12px; border-radius: 6px; }}
    .tip-box {{ background: #e0f7fa; border-left: 5px solid #00bcd4; padding: 10px 15px; margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 10pt; }}
    .teacher-note {{ background: #f5f5f5; border: 2px dashed #999; border-radius: 8px; padding: 15px; margin: 20px 0; font-size: 10pt; color: #555; }}
    .question-card {{ background: #fff; border: 2px solid #eadcf1; border-radius: 12px; padding: 18px 20px; margin-bottom: 18px; box-shadow: 0 2px 12px rgba(0,0,0,0.05); }}
    .q-number {{ font-size: 0.8rem; font-weight: 700; color: #8e44ad; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }}
    .q-text {{ font-size: 1.02rem; font-weight: 600; color: #222; margin-bottom: 14px; line-height: 1.4; }}
    .options-list {{ list-style: none; padding: 0; margin: 0; }}
    .options-list li {{ margin-bottom: 8px; }}
    .option-btn {{ width: 100%; text-align: left; background: #faf5ff; border: 2px solid #eadcf1; border-radius: 8px; padding: 10px 14px; font-size: 0.95rem; cursor: pointer; display: flex; align-items: center; gap: 10px; color: #333; font-family: inherit; }}
    .option-btn.correct, .option-btn.revealed-correct {{ background: #e8f5e9; border-color: #4caf50; color: #2e7d32; }}
    .option-btn.wrong {{ background: #ffebee; border-color: #e53935; color: #c62828; }}
    .option-icon {{ font-size: 1.1rem; min-width: 22px; text-align: center; }}
    .explanation {{ display: none; background: #f4e6fb; border-left: 4px solid #8e44ad; border-radius: 0 8px 8px 0; padding: 10px 14px; margin-top: 14px; font-size: 0.9rem; color: #444; line-height: 1.5; }}
    .explanation.show {{ display: block; }}
    .score-bar {{ background: #faf5ff; border: 2px solid #eadcf1; border-radius: 10px; padding: 14px 18px; text-align: center; font-size: 1rem; font-weight: 700; color: #6c3483; margin-bottom: 18px; }}
    .results-section {{ display: none; background: white; border-radius: 14px; box-shadow: 0 4px 20px rgba(0,0,0,0.12); padding: 24px 22px; margin: 24px 0; text-align: center; border: 3px solid #8e44ad; }}
    .results-section.show {{ display: block; }}
    .results-section .score-display {{ font-size: 2.4rem; font-weight: 800; color: #8e44ad; margin: 8px 0; }}
    .see-score-btn {{ background: #8e44ad; color: white; border: none; padding: 14px 32px; border-radius: 8px; font-size: 1.05rem; font-weight: 700; cursor: pointer; display: block; margin: 10px auto; }}
    .back-link {{ display: inline-block; margin-top: 8px; color: #8e44ad; font-weight: 600; text-decoration: none; font-size: 0.95rem; }}
    .worksheet-section {{ margin: 20px 0; }}
    .fill-line {{ border-bottom: 2px solid #d2b4de; min-height: 26px; margin: 8px 0 14px; display: block; }}
    .answer-key {{ background: #f5f5f5; border: 3px dashed #999; border-radius: 8px; padding: 20px; margin: 20px 0; }}
    .answer-key h2 {{ background: #616161; text-align: center; }}
    .page-break {{ page-break-before: always; margin-top: 20px; }}
    .llc-paywall-overlay {{ position: fixed; bottom: 0; left: 0; right: 0; background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,0.97) 30%, #fff 100%); padding: 48px 24px 40px; text-align: center; z-index: 1000; box-shadow: 0 -8px 40px rgba(59,31,107,0.12); }}
    .llc-paywall-inner {{ max-width: 520px; margin: 0 auto; }}
    .llc-paywall-emoji {{ font-size: 2.2rem; display: block; margin-bottom: 8px; }}
    .llc-paywall-title {{ font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; color: #3B1F6B; margin-bottom: 8px; }}
    .llc-paywall-sub {{ font-family: 'Lato', sans-serif; font-size: 0.95rem; color: #5A7A78; margin-bottom: 20px; line-height: 1.5; }}
    .llc-btn-subscribe {{ display: inline-block; background: #FF6B6B; color: #fff; font-family: 'Lato', sans-serif; font-weight: 700; font-size: 1rem; padding: 14px 32px; border-radius: 8px; text-decoration: none; border: none; cursor: pointer; }}
    @media print {{ .see-score-btn, .results-section, .score-bar {{ display:none !important; }} * {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }} }}
  </style>
</head>
<body data-document-id=\"{doc_id}\">
  <h1>{h1}</h1>
  <p class=\"subtitle\">Grade 5 Engineering — Unit 1 Quiz</p>
  <div class=\"meta\"><span>📚 <strong>Grade:</strong> 5th Grade</span><span>🛠️ <strong>Subject:</strong> Engineering</span><span>📝 <strong>Format:</strong> Quiz + short response</span></div>
  <div class=\"tip-box\"><strong>Family tip:</strong> {tip}</div>
  <div class=\"score-bar\">Score: <span id=\"scoreDisplay\">0</span> / <span id=\"answeredDisplay\">0</span> correct &nbsp;|&nbsp; <span id=\"totalDisplay\">8</span> multiple-choice questions</div>
  <a href=\"gr5-ets1-unit1-lesson6-present-and-defend-your-water-filter-solution.html\" class=\"back-link\">← Back to Unit 1 Lesson 6</a>
  <div id=\"questions-container\" style=\"margin-top:20px;\"></div>
  <button class=\"see-score-btn\" onclick=\"showResults()\">📊 See Your Score</button>
  <div class=\"results-section\" id=\"resultsBox\"><div style=\"font-size:2.5rem; margin-bottom:4px;\">🏆</div><div class=\"score-display\" id=\"finalScore\">0 / 8</div><div class=\"encouragement\" id=\"encouragementText\">Nice work, engineer!</div><a href=\"gr5-ets1-unit1-lesson1-define-the-water-filter-design-problem.html\" class=\"back-link\">↺ Review the unit lessons</a></div>
  <div class=\"worksheet-section\"><h2>✍️ Short Response — Use Evidence</h2><p>{prompt}</p><span class=\"fill-line\"></span><span class=\"fill-line\"></span><span class=\"fill-line\"></span></div>
  <h2>👩‍🏫 Parent/Teacher Notes</h2><div class=\"teacher-note\">{teacher_notes}</div>
  <div class=\"page-break\"><div class=\"answer-key\"><h2>✂️ PARENT ANSWER KEY — Detach before giving worksheet to students</h2>{answer_key}</div></div>
<script>
const quizData = {quiz_data};
let score = 0; let answered = 0;
function renderQuiz(){{ const container = document.getElementById('questions-container'); quizData.forEach((item, idx) => {{ const card = document.createElement('div'); card.className = 'question-card'; card.innerHTML = `<div class="q-number">Question ${{idx+1}}</div><div class="q-text">${{item.q}}</div>`; const ul = document.createElement('ul'); ul.className = 'options-list'; const exp = document.createElement('div'); exp.className = 'explanation'; exp.textContent = item.exp; item.opts.forEach((opt, optIdx) => {{ const li = document.createElement('li'); const btn = document.createElement('button'); btn.className = 'option-btn'; btn.innerHTML = `<span class="option-icon">🔹</span><span>${{opt}}</span>`; li.appendChild(btn); ul.appendChild(li); btn.onclick = () => answerQuestion(idx, optIdx, btn, ul, exp); }}); card.appendChild(ul); card.appendChild(exp); container.appendChild(card); }}); }}
function answerQuestion(qIdx, optIdx, btn, ul, exp){{ if (ul.dataset.answered === 'true') return; ul.dataset.answered = 'true'; answered++; const correctIdx = quizData[qIdx].a; Array.from(ul.querySelectorAll('.option-btn')).forEach((b, i) => {{ b.disabled = true; if (i === correctIdx) b.classList.add('revealed-correct'); }}); if (optIdx === correctIdx) {{ btn.classList.remove('revealed-correct'); btn.classList.add('correct'); score++; }} else {{ btn.classList.add('wrong'); }} exp.classList.add('show'); document.getElementById('scoreDisplay').textContent = score; document.getElementById('answeredDisplay').textContent = answered; }}
function showResults(){{ const box = document.getElementById('resultsBox'); box.classList.add('show'); document.getElementById('finalScore').textContent = `${{score}} / ${{quizData.length}}`; let msg = 'Nice work, engineer!'; if (score === quizData.length) msg = 'Perfect score! You can defend a whole engineering design cycle.'; else if (score >= 6) msg = 'Great job! You are connecting evidence and redesign choices well.'; else if (score >= 4) msg = 'Good work! Review the criteria, fair testing, and redesign lessons to strengthen your explanations.'; else msg = 'Keep building! Go back through the unit and practice connecting tests, data, and design decisions.'; document.getElementById('encouragementText').textContent = msg; }}
renderQuiz();
</script>
<script src=\"https://cassclearly.com/feedback-layer.js?v=20260408\" data-api-url=\"https://cassclearly.com\" data-document-id=\"{doc_id}\" data-content-selector=\"body\"></script>
<div class=\"llc-paywall-overlay\" id=\"llcPaywall\" style=\"display:none;\"><div class=\"llc-paywall-inner\"><span class=\"llc-paywall-emoji\">🥼</span><div class=\"llc-paywall-title\">This is a preview. Unlock the full quiz.</div><p class=\"llc-paywall-sub\">You're seeing the quiz preview. Subscribe to access the full unit quiz, short-response review, and every K–5 lesson, worksheet, and Parent Answer Key.<br><strong>$99/year. Cancel anytime.</strong></p><a href=\"/store.html\" class=\"llc-btn-subscribe\">Subscribe to Unlock — $99/yr</a></div></div>
<script>
(function() {{
  var ACCESS_KEY = 'llc_access';
  function isUnlocked() {{ return localStorage.getItem(ACCESS_KEY) === 'granted'; }}
  function lockQuiz() {{
    var cards = Array.from(document.querySelectorAll('.question-card'));
    var freePreviewCount = 2;
    cards.forEach(function(card, index) {{ if (index >= freePreviewCount) card.style.display = 'none'; }});
    var responseSection = document.querySelector('.worksheet-section');
    if (responseSection) responseSection.style.display = 'none';
    var answerKey = document.querySelector('.page-break');
    if (answerKey) answerKey.style.display = 'none';
    var seeScoreButton = document.querySelector('.see-score-btn');
    if (seeScoreButton) seeScoreButton.style.display = 'none';
    var resultsBox = document.getElementById('resultsBox');
    if (resultsBox) resultsBox.style.display = 'none';
    document.body.style.paddingBottom = '220px';
    document.getElementById('llcPaywall').style.display = 'block';
  }}
  document.addEventListener('DOMContentLoaded', function() {{
    if (window.location.search.indexOf('review=1') !== -1) {{
      try {{ localStorage.setItem(ACCESS_KEY, 'granted'); }} catch (e) {{}}
      return;
    }}
    if (!isUnlocked()) lockQuiz();
  }});
}})();
</script>
<div style=\"text-align:center; padding: 24px 16px 16px; font-family: 'Lato', sans-serif; font-size: 0.78rem; color: #999; border-top: 1px solid #eee; margin-top: 32px;\">© 2026 Little Lab Coats. For personal, non-commercial use only. Unauthorized reproduction, redistribution, or resale is prohibited. Printed copies are for use within your immediate household only.</div>
</body>
</html>
"""
# DATA OMITTED FOR BREVITY IN THIS TOOL WRITE; will be appended by next write step if needed
