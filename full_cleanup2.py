import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=12)

header = "# 🦷 치과 뉴스 데일리\n> 매일 자동으로 업데이트되는 치과 업계 뉴스, 기술 트렌드, 건강보험 정책, SNS 마케팅 트렌드 모음\n\n---\n\n"

# 모든 top-level 섹션 (## 로 시작하는 줄)을 기준으로 분리
# 각 섹션: ## 로 시작하는 헤더 + 다음 ## 전까지의 내용
sections = re.split(r'\n(?=#{2} )', content)

weekly_seen = {}  # key=(year, week_num), value=section text
daily_seen = {}   # key=(year, month, day), value=section text

skipped = 0

for sec in sections:
    stripped = sec.strip()
    if not stripped:
        continue

    # 주간 섹션 판별
    wm = re.match(r'#{2,3} 📆 (\d{4})년 (\d{1,2})주차 \((\d{1,2})월 (\d{1,2})일', stripped)
    if wm:
        year, week_num = int(wm.group(1)), int(wm.group(2))
        month, day = int(wm.group(3)), int(wm.group(4))
        key = (year, week_num)
        # ## 로 헤더 통일
        normalized = re.sub(r'^#{2,3} 📆', '## 📆', stripped) + '\n\n'
        if key not in weekly_seen:
            try:
                sec_date = datetime(year, month, day)
                if sec_date >= cutoff:
                    weekly_seen[key] = (sec_date, normalized)
                else:
                    skipped += 1
            except ValueError:
                weekly_seen[key] = (datetime(year, 1, 1), normalized)
        continue

    # 일간 섹션 판별 (## 📅 2026년 MM월 DD일)
    dm = re.match(r'## 📅 2026년 (\d{1,2})월 (\d{1,2})일', stripped)
    if dm:
        month, day = int(dm.group(1)), int(dm.group(2))
        key = (2026, month, day)
        if key not in daily_seen:
            daily_seen[key] = stripped + '\n\n'
        continue

    # 그 외 (헤더, 설명 등) 무시

# 주간 섹션 정렬 (최신 주차 우선)
sorted_weekly = sorted(weekly_seen.values(), key=lambda x: x[0], reverse=True)

# 일간 섹션 정렬 (최신 날짜 우선)
sorted_daily = sorted(daily_seen.items(), key=lambda x: x[0], reverse=True)

new_content = header
for _, text in sorted_weekly:
    new_content += text
for _, text in sorted_daily:
    new_content += text

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"주간 유지: {len(weekly_seen)}개 (12주 이전 삭제: {skipped}개)")
print(f"일간 유지: {len(daily_seen)}개")
print(f"12주 기준: {cutoff.strftime('%Y-%m-%d')} 이전 삭제")
