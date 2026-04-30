import re
from datetime import datetime, timedelta
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=30)
header_match = re.match(r'^(.*?)(?=## \U0001f4c5 )', content, re.DOTALL)
header = header_match.group(1) if header_match else ''
pattern = re.compile(r'(## \U0001f4c5 (\d{4})년 (\d{1,2})월 (\d{1,2})일.*?)(?=## \U0001f4c5 |\Z)', re.DOTALL)
kept, removed = [], 0
for m in pattern.finditer(content):
    y, mo, d = int(m.group(2)), int(m.group(3)), int(m.group(4))
    if datetime(y, mo, d) >= cutoff:
        kept.append(m.group(1))
    else:
        removed += 1
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(header + ''.join(kept))
print(f'유지: {len(kept)}개, 삭제: {removed}개')
