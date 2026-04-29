import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=30)

header_match = re.match(r'^(.*?)(?=## 📅 )', content, re.DOTALL)
header = header_match.group(1) if header_match else ''

pattern = re.compile(r'(## 📅 (\d{4})년 (\d{1,2})월 (\d{1,2})일.*?)(?=## 📅 |\Z)', re.DOTALL)

kept = []
removed = 0
for m in pattern.finditer(content):
    year, month, day = int(m.group(2)), int(m.group(3)), int(m.group(4))
    sec_date = datetime(year, month, day)
    if sec_date >= cutoff:
        kept.append(m.group(1))
    else:
        removed += 1

new_content = header + ''.join(kept)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"유지: {len(kept)}개 섹션, 삭제: {removed}개 섹션 (30일 기준: {cutoff.strftime('%Y-%m-%d')} 이전)")
