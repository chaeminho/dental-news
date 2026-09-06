import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=12)

# 헤더 보존 (첫 번째 ## 📆 또는 ## 📅 이전)
header_match = re.match(r'^(.*?)(?=#{2,3} 📆 |## 📅 )', content, re.DOTALL)
header = header_match.group(1) if header_match else ''

# 주간 섹션 파싱 (## 또는 ### 로 시작하는 📆 섹션)
weekly_pattern = re.compile(
    r'(#{2,3} 📆 (\d{4})년 (\d{1,2})주차 \((\d{1,2})월 (\d{1,2})일.*?)(?=#{2,3} 📆 |## 📅 |\Z)',
    re.DOTALL
)

# 일간 섹션 전체 보존 (첫 번째 ## 📅 부터)
daily_match = re.search(r'(## 📅 .*)', content, re.DOTALL)
daily_content = daily_match.group(1) if daily_match else ''

# 주간 섹션 중복 제거 (주차 번호 기준, 먼저 나온 것 = 최신 것 유지)
seen_weeks = set()
kept_weekly = []
removed_dup = 0
removed_old = 0

for m in weekly_pattern.finditer(content):
    year, week_num, month, day = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    key = (year, week_num)
    try:
        sec_date = datetime(year, month, day)
    except ValueError:
        sec_date = datetime(year, 1, 1)

    if key in seen_weeks:
        removed_dup += 1
        continue

    if sec_date < cutoff:
        removed_old += 1
        seen_weeks.add(key)
        continue

    seen_weeks.add(key)
    # 헤더를 ## 로 통일
    section_text = m.group(1)
    section_text = re.sub(r'^###', '##', section_text)
    kept_weekly.append(section_text)

new_content = header + ''.join(kept_weekly) + daily_content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"주간 유지: {len(kept_weekly)}개, 중복 제거: {removed_dup}개, 오래된 섹션 삭제: {removed_old}개")
print(f"(12주 기준: {cutoff.strftime('%Y-%m-%d')} 이전 삭제)")
