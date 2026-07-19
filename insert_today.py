with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

header_end = content.find('\n---\n')
if header_end == -1:
    header_end = content.find('\n---')

insert_pos = header_end + len('\n---\n')

today_section = """
## 📅 2026년 07월 20일

### 🦷 치과 업계 뉴스
- **INDEX 2026, 'Smart Bio Dentistry' 대주제로 7월 26일 인천 개막 예고**: 인천 바이오 치의학 종합학술대회(INDEX 2026)가 오는 7월 26일 인천 송도 컨벤시아에서 개최되며, 'Smart Bio Dentistry: 과학과 AI 그리고 지속 가능한 치과'를 대주제로 AI 접목 치과 임상·경영의 미래를 제시할 예정이다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138330))
- **치과계 '석션 혁명' 바람, 자동 석션 장비 잇따라 출시 — 구인난 해소 기대**: 치과 진료 보조 인력 부족 문제를 해결하기 위한 자동 석션 장비 및 관련 제품이 잇따라 공개·출시되면서 치과계에 이른바 '석션 혁명'이 불고 있으며, 만성적인 구인난 해소에 대한 기대감이 높아지고 있다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138417))
- **덴티스, 즉시 식립 마스터클래스 글로벌 웨비나 시리즈 예고**: 덴티스가 7월 16일부터 9월 3일까지 총 4회에 걸쳐 즉시 식립(Immediate Placement) 임상 노하우를 공유하는 'DENTIS Global Live Webinar Series'를 개최하며, 글로벌 치과 교육 플랫폼으로서의 입지를 강화하고 있다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=47705))
- **병원 속 치과, 협진 모델로 경계 확장 움직임 본격화**: 종합병원 내 치과 진료과가 전신 질환 환자와의 협진 체계를 강화하며 영역을 넓히고 있으며, 고령화 사회에서 전신 질환자 구강 관리 수요 증가에 대응하는 협진 모델이 주목받고 있다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138245))

### 💡 치과 기술 트렌드
- **덴티움, AI 기반 디지털 덴티스트리 통합 솔루션 제시**: 덴티움이 AI 기반 진단·설계·제작을 아우르는 디지털 덴티스트리 통합 솔루션을 공개하며, CAD/CAM·구강 스캐너·3D 프린팅을 연결한 데이터 흐름 중심의 차세대 치과 임상 워크플로우를 선보였다. (출처: [치의신보](https://www.dailydental.co.kr/news/article.html?no=138007))
- **치아 재생 약 2030년 상용화 목표 — 선천적 무치증 임상 2상 진입 예정**: 일본 기업이 개발 중인 치아 재생 신약이 2026년 선천적 무치증 어린이를 대상으로 임상 2상에 진입할 예정이며, 2030년 상용화를 목표로 하고 있어 임플란트 시장에 미칠 파장에 치과계의 관심이 집중되고 있다. (출처: [와블라이프](https://www.wablelife.com/2026/03/tooth-regeneration-drug.html))
- **K-임플란트, 유럽 시장서 기술력 인정 — 글로벌 수출 확대 가속**: 국내 임플란트 브랜드들이 유럽 치과의사들에게 기술력과 가성비를 인정받으며 글로벌 수출을 확대하고 있으며, 대구 기업들의 두바이 치과기자재전시회 462만 달러 계약 성과도 K-덴탈의 글로벌 경쟁력을 입증했다. (출처: [치과신문](https://www.dentalnews.or.kr/news/article.html?no=47593))

### 🏥 건강보험 정책
- **2026년 치과 스케일링 건강보험 연 1회 적용 — 의원급 1만 8,600원**: 만 19세 이상이라면 누구나 연 1회 치과 스케일링에 건강보험 혜택을 받을 수 있으며, 2026년 기준 동네 치과 의원 초진 시 약 18,600원으로 비보험(5~6만 원) 대비 큰 폭의 비용 절감이 가능하다. (출처: [원진치과 매거진](https://wonjindc.com/magazine/dental-insurance-guide-2025))
- **의료급여 치과 임플란트 65세 이상 평생 2개 급여 — 지르코니아도 급여 확대**: 65세 이상 의료급여 수급권자는 치과 임플란트 평생 2개에 대해 급여 혜택을 받을 수 있으며, 2025년 2월부터 고품질 지르코니아 재료도 건강보험이 적용돼 본인부담금 30%로 개당 약 38~40만 원 수준으로 치료가 가능해졌다. (출처: [benefit.knews-info.com](https://benefit.knews-info.com/entry/2026%EB%85%84-%EC%9D%98%EB%A3%8C%EA%B8%89%EC%97%AC-%EC%B9%98%EA%B3%BC%C2%B7%EC%95%88%EA%B3%BC-%ED%98%9C%ED%83%9D-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EC%9E%84%ED%94%8C%EB%9E%80%ED%8A%B8%EB%B6%80%ED%84%B0-%EB%B0%B1%EB%82%B4%EC%9E%A5-%EC%88%98%EC%88%A0%EA%B9%8C%EC%A7%80)))
- **마약류 관리법 개정안 의견수렴 마감 — 치과 마약류 취급자 관리 강화**: 식품의약품안전처의 '마약류 관리에 관한 법률 시행령·시행규칙 개정안' 의견수렴이 7월 20일 마감되며, 치과를 포함한 의료기관의 의료용 마약류 도난·유출 방지를 위한 지도·감독 의무가 강화될 예정이다. (출처: [치의신보](https://www.dailydental.co.kr/))

### 📣 SNS 마케팅 트렌드
- **2026년 치과 인스타그램 마케팅 핵심은 'Reels로 신뢰 구축'**: 2026년 치과 SNS 마케팅에서 Reels는 가장 높은 도달 범위와 상호작용을 제공하는 포맷으로, 치료 과정을 간결하게 설명하거나 자주 묻는 질문에 답하는 짧은 영상이 신환 유입에 가장 효과적인 전략으로 자리잡았다. (출처: [socialchamp](https://www.socialchamp.com/blog/instagram-marketing-for-dentists/))
- **치과 SNS 전후 사진·환자 후기 콘텐츠 '환자 동의 필수' 주의**: 치과 SNS에서 효과적인 전후(Before/After) 이미지와 환자 후기 콘텐츠가 신뢰 형성에 큰 효과를 발휘하지만, 의료법상 환자 동의 없는 얼굴 사진 게시나 대가성 후기 유도는 의료광고 위반에 해당하므로 투명성 준수가 선행되어야 한다. (출처: [덴탈아리랑](https://www.dentalarirang.com/news/articleView.html?idxno=41436))
- **2026년 치과 마케팅 SNS 플랫폼별 전략 — 인스타·유튜브·틱톡 차별화 필요**: 2026년 치과 SNS 마케팅은 인스타그램(비주얼·Reels), 유튜브(심층 교육 영상), 틱톡(바이럴 숏폼) 등 플랫폼 특성에 맞는 차별화된 콘텐츠 전략이 요구되며, 단일 채널 집중보다 멀티 채널 운영이 신환 유입 효과를 높인다. (출처: [ssjum.com](https://ssjum.com/marketing-sns.html))

---
"""

new_content = content[:insert_pos] + today_section + content[insert_pos:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('오늘 날짜 섹션 삽입 완료')
