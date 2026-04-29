import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 가장 최신 날짜 추출
date_m = re.search(r'## 📅 (\d{4})년 (\d{1,2})월 (\d{1,2})일', content)
date_label = f"{date_m.group(1)}년 {int(date_m.group(2)):02d}월 {int(date_m.group(3)):02d}일" if date_m else "날짜 미상"

# 가장 최신 날짜 섹션 추출 (## 📅 첫 번째 ~ 다음 ## 📅 또는 ## 📆 전까지)
sec_m = re.search(r'## 📅 [^\n]+\n(.*?)(?=## 📅 |## 📆 |\Z)', content, re.DOTALL)
section_text = sec_m.group(1) if sec_m else ''

SECTIONS = [
    ('🦷 치과 업계 뉴스',   '🦷', 'blue',   '업계 뉴스'),
    ('💡 치과 기술 트렌드', '💡', 'green',  '기술 트렌드'),
    ('🏥 건강보험 정책',    '🏥', 'purple', '건강보험'),
    ('📣 SNS 마케팅 트렌드','📣', 'orange', 'SNS 마케팅'),
]

def parse_items(text, heading):
    m = re.search(rf'### {re.escape(heading)}\n(.*?)(?=###|\Z)', text, re.DOTALL)
    if not m:
        return []
    items = []
    for line in m.group(1).strip().splitlines():
        line = line.strip()
        if not line.startswith('- **'):
            continue
        tm = re.match(r'- \*\*(.*?)\*\*:?\s*(.*)', line)
        if not tm:
            continue
        title = tm.group(1)
        rest = tm.group(2)
        sm = re.search(r'\(출처:\s*\[([^\]]+)\]\(([^)]+)\)\)', rest)
        src_name = sm.group(1) if sm else ''
        src_url  = sm.group(2) if sm else '#'
        body = re.sub(r'\s*\(출처:.*?\)\s*$', '', rest).strip()
        items.append((title, body, src_name, src_url))
    return items

EXT_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'

def card(title, body, src_name, src_url, color, tag):
    return f'''
      <article class="card">
        <span class="card-tag {color}">{tag}</span>
        <h3 class="card-title">{title}</h3>
        <p class="card-body">{body}</p>
        <div class="card-footer">
          <span class="source-label">출처</span>
          <a class="source-link" href="{src_url}" target="_blank" rel="noopener">{src_name} {EXT_ICON}</a>
        </div>
      </article>'''

def section_html(heading, icon, color, tag, items):
    if not items:
        return ''
    cards = ''.join(card(t,b,sn,su,color,tag) for t,b,sn,su in items)
    return f'''
  <section class="section">
    <div class="section-header">
      <div class="section-icon {color}">{icon}</div>
      <h2 class="section-title">{heading}</h2>
      <span class="section-count">{len(items)}건</span>
    </div>
    <div class="card-grid">{cards}
    </div>
  </section>'''

body_html = ''.join(section_html(h,i,c,t, parse_items(section_text,h)) for h,i,c,t in SECTIONS)

CSS = '''
    :root {
      --blue-900: #0c2340; --blue-800: #0f3460; --blue-700: #1a4f8a;
      --blue-600: #1e6bb8; --blue-500: #2980d4; --blue-400: #56a8e8;
      --blue-300: #89c4f2; --blue-100: #ddeeff; --blue-50: #f0f7ff;
      --white: #ffffff; --gray-100: #f4f6f9; --gray-300: #cbd5e1;
      --gray-500: #64748b; --gray-700: #334155;
      --green: #0e9f6e; --purple: #7c3aed; --orange: #d97706;
      --radius: 14px;
      --shadow: 0 4px 20px rgba(12,35,64,0.10);
      --shadow-hover: 0 8px 32px rgba(12,35,64,0.18);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: \'Apple SD Gothic Neo\', \'Noto Sans KR\', \'Malgun Gothic\', sans-serif; background: var(--gray-100); color: var(--gray-700); line-height: 1.7; }
    header { background: linear-gradient(135deg, var(--blue-900) 0%, var(--blue-700) 60%, var(--blue-500) 100%); color: var(--white); padding: 48px 24px 56px; text-align: center; position: relative; overflow: hidden; }
    header .logo { font-size: 3rem; margin-bottom: 8px; display: block; }
    header h1 { font-size: clamp(1.6rem, 5vw, 2.4rem); font-weight: 800; letter-spacing: -0.5px; margin-bottom: 10px; }
    header .subtitle { font-size: 0.95rem; opacity: 0.8; max-width: 480px; margin: 0 auto 20px; }
    .date-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 999px; padding: 6px 18px; font-size: 0.9rem; font-weight: 600; }
    main { max-width: 1080px; margin: -32px auto 48px; padding: 0 16px; }
    .section { margin-bottom: 40px; }
    .section-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
    .section-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; }
    .section-icon.blue   { background: var(--blue-600); }
    .section-icon.green  { background: var(--green); }
    .section-icon.purple { background: var(--purple); }
    .section-icon.orange { background: var(--orange); }
    .section-title { font-size: 1.25rem; font-weight: 800; color: var(--blue-900); }
    .section-count { margin-left: auto; font-size: 0.8rem; color: var(--gray-500); background: var(--gray-300); border-radius: 999px; padding: 2px 10px; font-weight: 600; }
    .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 18px; }
    .card { background: var(--white); border-radius: var(--radius); padding: 22px 22px 18px; box-shadow: var(--shadow); border: 1px solid rgba(200,220,240,0.5); transition: transform 0.2s, box-shadow 0.2s; display: flex; flex-direction: column; gap: 12px; }
    .card:hover { transform: translateY(-3px); box-shadow: var(--shadow-hover); }
    .card-tag { display: inline-flex; align-items: center; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; border-radius: 6px; padding: 3px 8px; align-self: flex-start; }
    .card-tag.blue   { background: var(--blue-100); color: var(--blue-700); }
    .card-tag.green  { background: #d1fae5; color: #065f46; }
    .card-tag.purple { background: #ede9fe; color: #5b21b6; }
    .card-tag.orange { background: #fef3c7; color: #92400e; }
    .card-title { font-size: 1rem; font-weight: 700; color: var(--blue-900); line-height: 1.5; }
    .card-body  { font-size: 0.88rem; color: var(--gray-500); line-height: 1.7; flex: 1; }
    .card-footer { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--gray-100); padding-top: 12px; margin-top: 4px; flex-wrap: wrap; gap: 8px; }
    .source-label { font-size: 0.78rem; color: var(--gray-500); }
    .source-link { display: inline-flex; align-items: center; gap: 4px; font-size: 0.78rem; font-weight: 600; color: var(--blue-600); text-decoration: none; border: 1px solid var(--blue-300); border-radius: 6px; padding: 4px 10px; transition: background 0.15s, color 0.15s; }
    .source-link:hover { background: var(--blue-600); color: var(--white); border-color: var(--blue-600); }
    .source-link svg { width: 12px; height: 12px; stroke: currentColor; }
    footer { text-align: center; padding: 32px 16px 48px; color: var(--gray-500); font-size: 0.82rem; }
    footer .tooth { font-size: 1.4rem; display: block; margin-bottom: 6px; }
    @media (max-width: 600px) {
      header { padding: 36px 16px 48px; }
      header .logo { font-size: 2.4rem; }
      .card-grid { grid-template-columns: 1fr; }
      .card { padding: 18px 16px 14px; }
    }
'''

html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>🦷 치과 뉴스 데일리</title>
  <style>{CSS}  </style>
</head>
<body>
<header>
  <span class="logo">🦷</span>
  <h1>치과 뉴스 데일리</h1>
  <p class="subtitle">매일 자동으로 업데이트되는 치과 업계 뉴스, 기술 트렌드, 건강보험 정책, SNS 마케팅 트렌드 모음</p>
  <span class="date-badge">📅 {date_label}</span>
</header>
<main>
{body_html}
</main>
<footer>
  <span class="tooth">🦷</span>
  매일 자동 업데이트 · 치과 뉴스 데일리
</footer>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html 생성 완료")
