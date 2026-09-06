import re
from datetime import datetime, timedelta

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_kst = datetime.utcnow() + timedelta(hours=9)
cutoff = today_kst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(weeks=12)

# 고정 헤더 (첫 4줄: 제목, 설명, 빈줄, ---)
header = "# 🦷 치과 뉴스 데일리\n> 매일 자동으로 업데이트되는 치과 업계 뉴스, 기술 트렌드, 건강보험 정책, SNS 마케팅 트렌드 모음\n\n---\n\n"

# 주간 섹션: ## 📆 2026년 N주차 로 시작하는 섹션만 (날짜 포함 패턴)
weekly_pattern = re.compile(
    r'## 📆 (\d{4})년 (\d{1,2})주차 \((\d{1,2})월 (\d{1,2})일.*?\n(.*?)(?=## 📆 \d{4}년 \d{1,2}주차 |## 📅 2026년 \d{1,2}월 |\Z)',
    re.DOTALL
)

# 일간 섹션: ## 📅 2026년 MM월 DD일 로 시작하는 섹션만 (실제 날짜 형식)
daily_pattern = re.compile(
    r'(## 📅 2026년 \d{1,2}월 \d{1,2}일.*?)(?=## 📅 2026년 \d{1,2}월 \d{1,2}일|\Z)',
    re.DOTALL
)

# 주간 섹션 수집 (중복 제거 - 주차 번호 기준, 최초 등장이 최신)
seen_weeks = set()
kept_weekly = []
removed_dup = 0
removed_old = 0

for m in weekly_pattern.finditer(content):
    year, week_num = int(m.group(1)), int(m.group(2))
    month, day = int(m.group(3)), int(m.group(4))
    key = (year, week_num)

    try:
        sec_date = datetime(year, month, day)
    except ValueError:
        sec_date = datetime(year, 1, 1)

    if key in seen_weeks:
        removed_dup += 1
        continue

    seen_weeks.add(key)

    if sec_date < cutoff:
        removed_old += 1
        continue

    # 전체 섹션 텍스트 재구성
    section_text = f"## 📆 {m.group(1)}년 {m.group(2)}주차 ({m.group(3)}월 {m.group(4)}일"
    # 원래 매칭의 전체 텍스트 복원
    full_match = m.group(0)
    kept_weekly.append(full_match)

# 일간 섹션 수집 (중복 제거 - 날짜 기준)
seen_days = set()
kept_daily = []
removed_daily_dup = 0

for m in daily_pattern.finditer(content):
    # 날짜 추출
    date_match = re.match(r'## 📅 2026년 (\d{1,2})월 (\d{1,2})일', m.group(0))
    if not date_match:
        continue
    month, day = int(date_match.group(1)), int(date_match.group(2))
    key = (2026, month, day)

    if key in seen_days:
        removed_daily_dup += 1
        continue

    seen_days.add(key)
    kept_daily.append(m.group(0))

new_content = header + ''.join(kept_weekly) + ''.join(kept_daily)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"주간 유지: {len(kept_weekly)}개, 주간 중복: {removed_dup}개, 주간 오래된 것: {removed_old}개")
print(f"일간 유지: {len(kept_daily)}개, 일간 중복: {removed_daily_dup}개")
print(f"12주 기준: {cutoff.strftime('%Y-%m-%d')} 이전 삭제")
