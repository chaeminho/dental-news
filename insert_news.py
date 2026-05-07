with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if today's date section already exists
if '## 📅 2026년 05월 08일' in content:
    print('이미 존재합니다. 삽입하지 않습니다.')
    exit(0)

new_section = """## 📅 2026년 05월 08일

### 🦷 치과 업계 뉴스
- **SIDEX 2026 사전등록 마감 임박, 5월 29~31일 코엑스 AI 주제로 개최**: 서울시치과의사회 창립 101주년 기념 SIDEX 2026이 5월 29~31일 코엑스에서 'The Future of Dentistry, Starts with AI'를 주제로 개최되며 현재 사전등록이 진행 중이다. 253개사 1,063부스 규모로 치과 AI·디지털 최신 기자재를 한자리에서 체험할 수 있다. (출처: [치과투데이](https://www.dttoday.com/news/articleView.html?idxno=96541))
- **SIDEX 2026 신동열 대회장 인터뷰, "AI 시대 치과의 디지털 전환이 핵심"**: 신동열 SIDEX 2026 대회장이 치과신문과의 인터뷰에서 AI가 치과 임상·경영 전 분야를 바꾸고 있다고 강조하며, 이번 학술대회가 개원의들의 실질적 AI 도입을 위한 로드맵을 제시할 것이라고 밝혔다. 64명 연자·42개 강연의 대규모 학술 프로그램이 예정되어 있다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=47193))
- **2026 DV world Seoul 사전등록 오픈, 7월 18~19일 서울 세텍 개최**: 치과계 또 다른 대규모 행사인 DV world Seoul이 7월 18~19일 서울 세텍(SETEC)에서 열리며 사전등록이 시작됐다. 최신 치과 재료·장비 트렌드와 학술 프로그램을 결합한 구성으로, 상반기 SIDEX에 이어 하반기 치과계 주요 이벤트로 자리잡고 있다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=137614))

### 💡 치과 기술 트렌드
- **루트랩, WIS 2026서 'K-덴탈 플랫폼' 공개…환자·치과·기공소 통합 SaaS 선보여**: 치과 디지털 스타트업 루트랩이 세계IT쇼(WIS) 2026에서 환자, 치과의원, 치과기공소를 하나의 클라우드 환경으로 연결하는 통합형 SaaS 플랫폼을 최초 공개했다. 대용량 의료·기공 이미지 처리와 멀티테넌시 구조를 적용해 디지털 치과 생태계의 새 방향을 제시했다. (출처: [디지털데일리](https://www.ddaily.co.kr/page/view/2026042816430435877))
- **덴탈아리랑 창간특집, "K-덴탈 AI·디지털·플랫폼으로 전면 재편"**: 덴탈아리랑이 창간 특집 기획에서 국내 치과 산업이 AI·디지털·플랫폼 3대 축으로 전면 재편되고 있다고 분석했다. 임플란트 수출 강국에서 AI 진단·디지털 보철 소프트웨어 강국으로의 전환이 가속화되고 있다는 평가다. (출처: [덴탈아리랑](https://www.dentalarirang.com/news/articleView.html?idxno=47240))
- **SIDEX 2026 특별강연 '자신에게 맞는 디지털 운영방식 찾기' 세션 편성**: SIDEX 2026에서는 치과 규모·진료 특성별로 맞춤형 디지털 전환 전략을 안내하는 실용 세션이 편성됐다. 대형·중소형 치과의 디지털 장비 도입 단계와 ROI 분석이 주요 내용으로, 디지털 워크플로우 구축을 고민하는 개원의들의 참여가 기대된다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=47065))

### 🏥 건강보험 정책
- **2026년 치과 스케일링 건강보험 현황 총정리, 연 1회 본인부담 약 1만 6천 원**: 2026년 기준 만 19세 이상 성인의 치과 스케일링은 연 1회 건강보험이 적용되며, 1차 의료기관 기준 본인부담금은 약 1만 6,000~1만 8,600원이다. 보험 주기가 매년 1월 1일 리셋되므로 연초 활용이 유리하다는 안내가 주목받고 있다. (출처: [위기브](https://www.wegive.co.kr/wezine/detail/1365))
- **2026년 임플란트 단계별 건강보험 수가표 공개, 65세 이상 2개 급여 기준 재확인**: 2026년 개정 임플란트 단계별 건강보험 수가표가 공개됐다. 65세 이상 환자를 대상으로 평생 2개까지 급여가 적용되며, 본인부담률(일반 30%, 차상위·기초수급자 감면)과 단계별 수가 기준이 명시됐다. (출처: [앤드윈](https://www.andwin.co.kr/02/ab-1335-1.asp?ins_no=27&page=1))
- **건강보험심사평가원, 치과 청구 관련 최신 공지사항 게재**: 건강보험심사평가원(HIRA)이 치과 진료비 청구 기준 관련 최신 공지를 게재했다. 청구 오류 예방을 위한 세부 지침과 심사 기준 변경 내용이 포함되어, 치과 원무팀의 정기적인 확인이 권고된다. (출처: [건강보험심사평가원](https://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020002000100&brdScnBltNo=4&brdBltNo=11398&pageIndex=1))

### 📣 SNS 마케팅 트렌드
- **2026 인스타그램 알고리즘 핵심 변화, 'DM 공유'가 도달률 결정 최강 지표로**: 2026년 인스타그램 알고리즘은 좋아요보다 DM 공유·저장·시청 시간을 훨씬 강하게 반영하며, 콘텐츠를 친구에게 보내는 'Send' 행동이 노출 점수에 가장 높은 가중치를 부여받는다. 치과 계정도 공유 유도 콘텐츠(유용한 구강 건강 정보, 공감 가는 증상 카드뉴스 등) 제작이 핵심 전략이 됐다. (출처: [폴라애드](https://polarad.co.kr/marketing-news/instagram-algorithm-2026-latest-trends-complete-an))
- **인스타그램 릴스 마케팅 2026 성공 전략, 피드 광고보다 평균 30% 높은 참여율**: 2026년 인스타그램 릴스 광고는 기존 피드 광고 대비 평균 30% 높은 참여율을 기록하며 치과 마케팅의 핵심 포맷으로 자리잡고 있다. 릴스 최대 길이가 20분으로 확장되면서 시술 과정 상세 영상, 환자 상담 스토리 등 심층 콘텐츠 활용도 가능해졌다. (출처: [폴라애드](https://www.polarad.co.kr/marketing-news/2026-instagram-reels-marketing-strategy-update))
- **인스타그램, '검색 엔진' 역할 강화…치과 교육성 콘텐츠 SEO 효과 주목**: 2026년 인스타그램은 단순 소셜 미디어를 넘어 검색 엔진 역할을 강화하며, 사용자가 검색·저장·오래 머무는 콘텐츠를 알고리즘이 선호한다. 치과 계정의 경우 '임플란트 과정', '사랑니 발치 후 주의사항' 등 검색어 기반 교육 콘텐츠가 신규 환자 유입에 효과적이다. (출처: [폴라애드](https://polarad.co.kr/marketing-news/instagram-reels-trends-2026-z-content))

---

"""

# Insert after the header (---\n\n) and before the first date section
insert_marker = '---\n\n## 📅 2026년 05월 07일'
if insert_marker in content:
    content = content.replace(insert_marker, '---\n\n' + new_section + '## 📅 2026년 05월 07일', 1)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print('2026년 05월 08일 섹션 삽입 완료')
else:
    print('삽입 위치를 찾지 못했습니다.')
    # Try fallback: insert after "---\n\n"
    header_end = '---\n\n'
    idx = content.find(header_end)
    if idx != -1:
        insert_pos = idx + len(header_end)
        content = content[:insert_pos] + new_section + content[insert_pos:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print('대체 위치에 삽입 완료')
    else:
        print('삽입 실패: 헤더를 찾을 수 없습니다.')
