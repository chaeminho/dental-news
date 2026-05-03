import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=12)

# 헤더 보존
header_match = re.match(r'^(.*?)(?=## 📆 |## 📅 )', content, re.DOTALL)
header = header_match.group(1) if header_match else ''

# 주간 섹션 파싱 (## 📆 로 시작하는 섹션)
weekly_pattern = re.compile(
    r'(## 📆 (\d{4})년 (\d{1,2})주차 \((\d{1,2})월 (\d{1,2})일.*?)(?=## 📆 |## 📅 |\Z)',
    re.DOTALL
)

# 일간 섹션 전체 보존
daily_match = re.search(r'(## 📅 .*)', content, re.DOTALL)
daily_content = daily_match.group(1) if daily_match else ''

kept_weekly = []
removed = 0
for m in weekly_pattern.finditer(content):
    year, month, day = int(m.group(2)), int(m.group(4)), int(m.group(5))
    try:
        sec_date = datetime(year, month, day)
        if sec_date >= cutoff:
            kept_weekly.append(m.group(1))
        else:
            removed += 1
    except ValueError:
        kept_weekly.append(m.group(1))

new_content = header + ''.join(kept_weekly) + daily_content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"주간 유지: {len(kept_weekly)}개, 삭제: {removed}개 (12주 기준: {cutoff.strftime('%Y-%m-%d')} 이전)")
