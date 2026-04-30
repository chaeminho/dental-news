import re, json
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
dpat = re.compile(r'## \U0001f4c5 (\d{4})년 (\d{1,2})월 (\d{1,2})일\n(.*?)(?=## \U0001f4c5 |## \U0001f4c6 |\Z)', re.DOTALL)
SECS = [
    ('\U0001f9b7 치과 업계 뉴스', 'blue', '업계뉴스', '\U0001f9b7'),
    ('\U0001f4a1 치과 기술 트렌드', 'green', '기술트렌드', '\U0001f4a1'),
    ('\U0001f3e5 건강보험 정책', 'purple', '건강보험', '\U0001f3e5'),
    ('\U0001f4e3 SNS 마케팅 트렌드', 'orange', 'SNS마케팅', '\U0001f4e3'),
]
def parse_items(text, heading):
    m = re.search(rf'### {re.escape(heading)}\n(.*?)(?=###|\Z)', text, re.DOTALL)
    if not m: return []
    out = []
    for line in m.group(1).strip().splitlines():
        line = line.strip()
        if not line.startswith('- **'): continue
        tm = re.match(r'- \*\*(.*?)\*\*:?\s*(.*)', line)
        if not tm: continue
        title, rest = tm.group(1), tm.group(2)
        sm = re.search(r'\(출처:\s*\[([^\]]+)\]\(([^)]+)\)\)', rest)
        sn = sm.group(1) if sm else ''
        su = sm.group(2) if sm else '#'
        body = re.sub(r'\s*\(출처:.*?\)\s*$', '', rest).strip()
        out.append({'title': title, 'body': body, 'src_name': sn, 'src_url': su})
    return out
articles, seen = [], set()
for m in dpat.finditer(content):
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    ds = f'{y}-{mo:02d}-{d:02d}'
    dl = f'{y}.{mo:02d}.{d:02d}'
    seen.add(ds)
    for heading, color, tag, icon in SECS:
        for item in parse_items(m.group(4), heading):
            articles.append(dict(date=ds, date_label=dl, color=color, tag=tag, icon=icon, **item))
dates_sorted = sorted(seen, reverse=True)
latest_date = dates_sorted[0] if dates_sorted else ''
if latest_date:
    p = latest_date.split('-')
    latest_heading = p[0] + '년 ' + p[1] + '월 ' + p[2] + '일 뉴스'
else:
    latest_heading = '뉴스'
aj = json.dumps(articles, ensure_ascii=False)
dj = json.dumps(dates_sorted, ensure_ascii=False)
soj = json.dumps([{'t':tag,'c':color,'i':icon,'h':heading} for heading,color,tag,icon in SECS], ensure_ascii=False)
EXT = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'
CSS = """
:root{--b9:#0c2340;--b7:#1a4f8a;--b6:#1e6bb8;--b5:#2980d4;--b3:#89c4f2;--b1:#ddeeff;--g1:#f4f6f9;--g3:#cbd5e1;--g5:#64748b;--g7:#334155;--gn:#0e9f6e;--pu:#7c3aed;--or:#d97706;--r:14px;--sh:0 4px 20px rgba(12,35,64,.10);--shh:0 8px 32px rgba(12,35,64,.18)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',sans-serif;background:var(--g1);color:var(--g7);line-height:1.7}
header{background:linear-gradient(135deg,var(--b9) 0%,var(--b7) 60%,var(--b5) 100%);color:#fff;padding:48px 24px 40px;text-align:center}
header .logo{font-size:3rem;margin-bottom:8px;display:block}
header h1{font-size:clamp(1.6rem,5vw,2.4rem);font-weight:800;letter-spacing:-.5px;margin-bottom:10px}
.subtitle{font-size:.95rem;opacity:.8;max-width:480px;margin:0 auto 12px}
.date-heading{font-size:1.15rem;font-weight:700;opacity:.95;margin-bottom:14px}
.filter-bar{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;padding-bottom:8px}
.filter-bar input[type=date]{padding:8px 14px;border-radius:8px;border:none;font-size:.9rem;background:rgba(255,255,255,.9);color:var(--g7);cursor:pointer}
.filter-bar button{padding:8px 18px;border-radius:8px;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.15);color:#fff;font-size:.9rem;font-weight:600;cursor:pointer;transition:background .15s}
.filter-bar button:hover{background:rgba(255,255,255,.3)}
main{max-width:1080px;margin:32px auto 48px;padding:0 16px}
.section{margin-bottom:40px}
.section-header{display:flex;align-items:center;gap:12px;margin-bottom:20px}
.section-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0}
.section-icon.blue{background:var(--b6)}.section-icon.green{background:var(--gn)}.section-icon.purple{background:var(--pu)}.section-icon.orange{background:var(--or)}
.section-title{font-size:1.25rem;font-weight:800;color:var(--b9)}
.section-count{margin-left:auto;font-size:.8rem;color:var(--g5);background:var(--g3);border-radius:999px;padding:2px 10px;font-weight:600}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;overflow:visible}
.card{background:#fff;border-radius:var(--r);padding:22px 22px 18px;box-shadow:var(--sh);border:1px solid rgba(200,220,240,.5);transition:transform .2s,box-shadow .2s;display:flex;flex-direction:column;gap:12px}
.card:hover{transform:translateY(-3px);box-shadow:var(--shh)}
.card-top{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap}
.card-tag{display:inline-flex;align-items:center;font-size:.72rem;font-weight:700;letter-spacing:.5px;border-radius:6px;padding:3px 8px}
.card-date{font-size:.75rem;color:var(--g5)}
.card-tag.blue{background:var(--b1);color:var(--b7)}.card-tag.green{background:#d1fae5;color:#065f46}.card-tag.purple{background:#ede9fe;color:#5b21b6}.card-tag.orange{background:#fef3c7;color:#92400e}
.card-title{font-size:1rem;font-weight:700;color:var(--b9);line-height:1.5}
.card-body{font-size:.88rem;color:var(--g5);line-height:1.7;flex:1}
.card-footer{display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--g1);padding-top:12px;margin-top:4px;flex-wrap:wrap;gap:8px}
.source-label{font-size:.78rem;color:var(--g5)}
.source-link{display:inline-flex;align-items:center;gap:4px;font-size:.78rem;font-weight:600;color:var(--b6);text-decoration:none;border:1px solid var(--b3);border-radius:6px;padding:4px 10px;transition:background .15s,color .15s}
.source-link:hover{background:var(--b6);color:#fff;border-color:var(--b6)}
.source-link svg{width:12px;height:12px;stroke:currentColor}
.empty-msg{text-align:center;padding:60px 20px;color:var(--g5);font-size:1rem}
footer{text-align:center;padding:32px 16px 48px;color:var(--g5);font-size:.82rem}
footer .tooth{font-size:1.4rem;display:block;margin-bottom:6px}
@media(max-width:600px){header{padding:36px 16px 32px}header .logo{font-size:2.4rem}.card-grid{grid-template-columns:1fr}.card{padding:18px 16px 14px}}
"""
JS = f"""var ARTS={aj};var DATES={dj};var SO={soj};var EXT='{EXT}';
function esc(s){{return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}}
function card(a){{return '<article class="card" data-date="'+a.date+'">'+'<div class="card-top"><span class="card-tag '+a.color+'">'+esc(a.tag)+'</span><span class="card-date">'+esc(a.date_label)+'</span></div>'+'<h3 class="card-title">'+esc(a.title)+'</h3><p class="card-body">'+esc(a.body)+'</p>'+'<div class="card-footer"><span class="source-label">출처</span><a class="source-link" href="'+a.src_url+'" target="_blank" rel="noopener">'+esc(a.src_name)+' '+EXT+'</a></div></article>';}}
function render(list){{var mc=document.getElementById('mc');if(!list.length){{mc.innerHTML='<p class="empty-msg">해당 날짜의 뉴스가 없습니다.</p>';return;}}var h='';SO.forEach(function(s){{var it=list.filter(function(a){{return a.tag===s.t;}});if(!it.length)return;h+='<section class="section"><div class="section-header"><div class="section-icon '+s.c+'">'+s.i+'</div><h2 class="section-title">'+s.h+'</h2><span class="section-count">'+it.length+'건</span></div><div class="card-grid">'+it.map(card).join('')+'</div></section>';}});mc.innerHTML=h;}}
function updateHeading(dateStr){{var p=dateStr.split('-');document.getElementById('dh').textContent=p[0]+'년 '+p[1]+'월 '+p[2]+'일 뉴스';}}
function showLatest(){{if(!DATES.length)return;var d=DATES[0];document.getElementById('dp').value=d;updateHeading(d);render(ARTS.filter(function(a){{return a.date===d;}}));}}
document.addEventListener('DOMContentLoaded',function(){{var dp=document.getElementById('dp');if(DATES.length){{dp.min=DATES[DATES.length-1];dp.max=DATES[0];}}dp.addEventListener('change',function(){{var d=dp.value;if(d){{updateHeading(d);render(ARTS.filter(function(a){{return a.date===d;}}));}}}} );document.getElementById('ba').addEventListener('click',showLatest);showLatest();}});"""
html = ('<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><title>\U0001f9b7 미르치과 뉴스 데일리</title><style>'+CSS+'</style></head><body>'
  +'<header><span class="logo">\U0001f9b7</span><h1>미르치과 뉴스 데일리</h1><p class="subtitle">매일 자동으로 업데이트되는 치과 업계 뉴스, 기술 트렌드, 건강보험 정책, SNS 마케팅 트렌드 모음</p>'
  +f'<p class="date-heading" id="dh">{latest_heading}</p>'
  +'<div class="filter-bar"><input type="date" id="dp"/><button id="ba">오늘 뉴스</button></div></header>'
  +'<main id="mc"></main>'
  +'<footer><span class="tooth">\U0001f9b7</span>매일 자동 업데이트 · 미르치과 뉴스 데일리</footer>'
  +f'<script>{JS}</script></body></html>')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html 생성 완료')
