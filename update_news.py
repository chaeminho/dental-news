import re

new_section = """## 📅 2026년 6월 12일

### 🦷 치과 업계 뉴스
- **한국사회약학회, 서울대치과병원서 2026년 전기학술대회 개최**: 한국사회약학회가 6월 12일 서울대학교 치과병원 한화홀(8층)에서 '안전한 의약품 사용, 지불가능한 비용 부담'을 주제로 2026년 전기학술대회를 개최했다. 건강보험 약제정책 변화, 의약품 사용오류 예방 정책 등 사회약학 분야 핵심 현안이 집중 조명됐다. (출처: [약사공론](https://www.kpanews.co.kr/news/articleView.html?idxno=536131))
- **HODEX 2026, 호남권 최대 치과 학술-전시회 7월 4~5일 광주 개막 예정**: 호남권 최대 치과 행사인 HODEX 2026이 7월 4~5일 광주 김대중컨벤션센터에서 개최된다. 'AI로 여는 치과계 새 100년' 슬로건 아래 71개사 235부스 규모의 전시와 AI·디지털 덴티스트리 중심 학술 프로그램이 마련됐다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=47463))
- **덴트로닉, 미국 SPC 펠로우십 선정·프리시드 100만 달러 유치**: 치과 AI 로봇 스타트업 덴트로닉이 미국 SPC 펠로우십에 선정되며 프리시드 100만 달러(약 15억 원)를 유치했다. 실리콘밸리에서 치과 정밀 진료 자동화 기술의 글로벌 경쟁력을 인정받았으며, K-덴탈 스타트업의 해외 진출이 본격화되고 있다. (출처: [플래텀](https://platum.kr/archives/283815))
- **2026년 1분기 치과 서비스 지출 월평균 3만8천 원, 전년比 0.9% 하락**: 통계청 발표에 따르면 2026년 1분기 국민 1인당 월평균 치과 서비스 지출액이 3만8,000원으로 전년 동기 대비 0.9% 하락했다. 건강보험 급여 확대로 인한 환자 부담 완화가 주요 원인으로 분석된다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=137973))

### 💡 치과 기술 트렌드
- **덴탈로보틱스, AI 자율주행 석션 로봇 'DentVLA' 공개**: 덴탈로보틱스가 치과 보조 인력난 해결을 위한 AI 자율주행 석션 로봇 'DentVLA'를 공개했다. 3D CBCT와 구강스캐너 데이터로 구강 내 공간 좌표를 구성하고 비전 AI·로봇 제어를 결합해 석션을 자동화하며, 향후 스케일링·발치 보조로 기능을 단계적으로 확대할 계획이다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138019))
- **덴티움 'bright CT & Viewer', AI 진단으로 디지털 덴티스트리 선도**: 덴티움이 4초 안면 스캔이 가능한 AI 기반 진단 솔루션 'bright CT & Viewer'와 클라우드 플랫폼 'Dentium Link'로 디지털 덴티스트리를 선도하고 있다. AI 음성 메모·챗봇 기능이 추가돼 치과 진료 데이터 접근성이 크게 향상됐다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138007))
- **HODEX 2026, AI 진단·최소침습 임플란트·디지털 교정 집중 전시 예고**: HODEX 2026이 AI 기반 진단, 최소침습 임플란트, 투명교정 등 최신 치과 기술을 한자리에서 체험할 수 있는 전시 프로그램을 확정했다. 인공지능 교정 임상 적용, 디지털 총의치 포인트 등 AI 임상 세션이 특히 주목받고 있다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=137991))

### 🏥 건강보험 정책
- **치과 급여 기준 최신판 발간, 심평원 주요 변경 사항 안내**: 건강보험심사평가원이 치과 급여 인정 기준 최신판을 발간해 현장 혼란이 잦았던 항목을 체계적으로 정리했다. 치과의사와 환자 모두 급여 기준을 명확히 확인할 수 있어 불필요한 분쟁 예방에 도움이 될 전망이다. (출처: [치의신보](https://dailydental.co.kr/mobile/article.html?no=137070))
- **2026년 달라지는 치과 관련 제도 총정리**: 방문구강관리 서비스 제도화, 건강보험 수가 2% 인상(점수당 101.1원), 돌봄통합지원법 내 치과의사 포함 등 2026년 치과 의료 접근성 강화를 위한 주요 제도 변화가 정리됐다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=46229))
- **치과 치료 급여·비급여 항목 2026년 기준 최신 안내**: 임플란트·충치·신경치료·스케일링·교정 등 주요 치과 치료의 건강보험 급여 여부와 본인부담 기준이 2026년 기준으로 재정리됐다. 비급여 항목을 미리 파악하면 예상치 못한 진료비 부담을 줄일 수 있다. (출처: [리버타드 보험 꿀팁](https://libertadwebsite.com/%EC%B9%98%EA%B3%BC-%EC%B9%98%EB%A3%8C-%EA%B8%89%EC%97%AC-%EB%B9%84%EA%B8%89%EC%97%AC-%ED%97%B7%EA%B0%88%EB%A6%AC%EB%A9%B4-%EC%A7%84%EB%A3%8C%EB%B9%84-%ED%8F%AD%ED%83%84-2026%EB%85%84-%EA%B8%B0/))

### 📣 SNS 마케팅 트렌드
- **2026년 인스타그램 알고리즘 변화 총정리: 도달 증가, 전환은 전략 필요**: 2026년 인스타그램 알고리즘이 '일관된 주제'와 '다음 행동 유도(CTA)'를 핵심 기준으로 삼는 방향으로 개편됐다. AI 콘텐츠 범람 속에서 진정성 있는 콘텐츠와 명확한 CTA가 치과 마케팅 성공의 핵심 열쇠로 부각됐다. (출처: [스튜디오퍼시](https://www.studiopupcy.com/blog/instagramalgorithm2026/))
- **캐러셀 vs 릴스 역할 구분이 2026년 인스타 전략의 핵심**: 캐러셀은 팔로워 신뢰·전환 무기, 릴스는 신규 비팔로워 도달 무기로 역할이 명확히 나뉜다. 치과 계정 운영 시 릴스로 새 환자를 발견시키고 캐러셀로 전문성과 신뢰를 쌓는 투트랙 전략이 효과적이다. (출처: [Threads @solution.kim](https://www.threads.com/@solution.kim/post/DTIEXajkzLa/))
- **2026 인스타그램 성장 전략: 콘텐츠 28개로 팔로워 3.4만 달성 리포트 공개**: 콘텐츠 28개만으로 팔로워 3만4,000명을 달성한 실제 사례 분석 리포트가 공개됐다. 일관된 카테고리 유지, 릴스 중심 성장, 저장·공유 유도 CTA가 핵심 공통점으로 꼽혀 치과 계정 운영에도 직접 적용 가능하다. (출처: [하이아웃풋클럽](https://blog.highoutputclub.com/2026-reels-growth-instagram-accounts-strategy/))
- **릴스 첫 1초 승부·저장·DM공유가 2026 노출의 핵심 지표**: 2026년 인스타그램 릴스는 시청자를 잡을 수 있는 시간이 사실상 1초로 단축됐으며 저장과 DM 공유가 노출 핵심 지표로 자리 잡았다. 치과 마케팅에서도 '이거 저장해야지', '친구에게 보내야지' 반응을 유도하는 교육형 구강 건강 콘텐츠가 효과적이다. (출처: [폴라애드](https://polarad.co.kr/marketing-news/instagram-reels-trends-2026-z-content))

---

"""

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

today_section = '## 📅 2026년 6월 12일'
if today_section in content:
    print('오늘 날짜 섹션이 이미 존재합니다. 추가하지 않습니다.')
else:
    header_end = '---\n\n'
    insert_pos = content.find(header_end)
    if insert_pos == -1:
        print('헤더 구분선을 찾을 수 없습니다.')
    else:
        insert_pos += len(header_end)
        content = content[:insert_pos] + new_section + content[insert_pos:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print('오늘 날짜 섹션을 README.md 상단에 삽입했습니다.')
