import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=12)

# 헤더 보존 (파일 상단, 첫 번째 주간/일간 섹션 이전)
header_match = re.match(r'^(.*?)(?=#{2,3} 📆 |## 📅 )', content, re.DOTALL)
header = header_match.group(1) if header_match else ''

# 전체 섹션을 ## 📆, ### 📆, ## 📅 로 분할
section_pattern = re.compile(r'(?=#{2,3} 📆 |## 📅 )')
all_sections = section_pattern.split(content[len(header):])

weekly_sections = {}  # key: "YYYY-WW", value: (start_date, section_text)
daily_sections_ordered = []  # (date_str, section_text) 순서 유지

for sec in all_sections:
    if not sec.strip():
        continue
    if sec.startswith('## 📆') or sec.startswith('### 📆'):
        # 주차 추출
        m = re.search(r'(\d{4})년 (\d{1,2})주차 \((\d{1,2})월 (\d{1,2})일', sec)
        if m:
            year = int(m.group(1))
            week = int(m.group(2))
            month = int(m.group(3))
            day = int(m.group(4))
            key = f"{year}-{week:02d}"
            try:
                sec_date = datetime(year, month, day)
                if key not in weekly_sections:
                    # 헤딩 레벨을 ## 로 정규화
                    normalized = re.sub(r'^### 📆', '## 📆', sec, count=1)
                    weekly_sections[key] = (sec_date, normalized)
            except ValueError:
                pass
    elif sec.startswith('## 📅'):
        # 날짜 추출 (중복 허용, 그대로 보존)
        m = re.search(r'(\d{4})년 (\d{1,2})월 (\d{1,2})일', sec)
        if m:
            y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
            try:
                date_key = datetime(y, mo, d).strftime('%Y-%m-%d')
            except ValueError:
                date_key = sec[:30]
        else:
            date_key = sec[:30]
        # 중복 일간 섹션도 첫 번째만 보존
        if not any(dk == date_key for dk, _ in daily_sections_ordered):
            daily_sections_ordered.append((date_key, sec))

# 12주 이전 주간 섹션 삭제 및 역순 정렬
kept = {k: v for k, v in weekly_sections.items() if v[0] >= cutoff}
removed_count = len(weekly_sections) - len(kept)
sorted_keys = sorted(kept.keys(), reverse=True)

# 일간 섹션 역순 정렬 (최신 날짜 먼저)
daily_sections_ordered.sort(key=lambda x: x[0], reverse=True)

# 재구성
new_content = header
for k in sorted_keys:
    new_content += kept[k][1]
for _, sec_text in daily_sections_ordered:
    new_content += sec_text

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"주간 섹션 유지: {len(kept)}개 (총 {len(weekly_sections)}개 중), 삭제: {removed_count}개 (12주 기준: {cutoff.strftime('%Y-%m-%d')} 이전)")
print(f"일간 섹션: {len(daily_sections_ordered)}개")
