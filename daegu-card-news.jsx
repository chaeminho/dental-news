import { useState } from "react";

const BRAND = {
  main: "#0B3D91",
  light: "#1565C0",
  accent: "#2196F3",
  pale: "#E3F2FD",
  gold: "#FFB300",
  white: "#FFFFFF",
  dark: "#0D1B2A",
  gray: "#607D8B",
  lightGray: "#F5F9FF",
};

const cards = [
  {
    id: 1,
    type: "cover",
    badge: "대구 임플란트 가이드",
    headline: ["대구 임플란트,", "건강보험으로", "얼마나 절약될까?"],
    subtext: "만 65세 이상이라면 꼭 확인하세요",
    tags: ["#대구임플란트", "#대구치과", "#임플란트보험", "#대구치과추천"],
    icon: "🦷",
    note: "2026년 건강보험 기준",
  },
  {
    id: 2,
    type: "info",
    badge: "건강보험 적용 조건",
    headline: "이런 분은 임플란트\n건강보험 받을 수 있어요",
    items: [
      {
        icon: "✅",
        title: "만 65세 이상",
        desc: "나이 조건만 충족하면 누구나",
      },
      {
        icon: "✅",
        title: "평생 2개 한도",
        desc: "상·하악 구분 없이 총 2개",
      },
      {
        icon: "✅",
        title: "본인부담 30%",
        desc: "건강보험공단이 70% 지원",
      },
      {
        icon: "✅",
        title: "골유착형 임플란트",
        desc: "1~3단계 전 과정 급여 적용",
      },
    ],
    note: "※ 완전·부분 무치악 모두 해당",
    tags: ["#대구임플란트보험", "#임플란트급여"],
  },
  {
    id: 3,
    type: "compare",
    badge: "비용 비교",
    headline: "비급여 vs 건강보험\n얼마나 차이날까?",
    compareData: {
      left: {
        label: "비급여 (건강보험 미적용)",
        value: "약 100~150만 원",
        sub: "1개 기준 (병원마다 상이)",
        color: "#FF5252",
        bg: "#FFF5F5",
      },
      right: {
        label: "건강보험 적용 (65세 이상)",
        value: "약 30~40만 원대",
        sub: "본인부담 30% 기준",
        color: "#0B3D91",
        bg: "#E3F2FD",
      },
    },
    savings: "최대 100만 원 이상 절약",
    note: "※ 병원·지역·치료 난이도에 따라 다를 수 있음",
    tags: ["#대구임플란트비용", "#임플란트건강보험"],
  },
  {
    id: 4,
    type: "steps",
    badge: "치료 3단계 과정",
    headline: "임플란트 치료,\n이렇게 진행됩니다",
    steps: [
      {
        num: "1",
        title: "정밀 진단 & 치료계획",
        desc: "파노라마 X-ray·CT 촬영 후 뼈 상태 확인, 개인 맞춤 계획 수립",
        time: "1~2회 방문",
      },
      {
        num: "2",
        title: "임플란트 식립 & 골유착",
        desc: "티타늄 픽스처를 잇몸뼈에 심고 뼈와 완전히 결합될 때까지 대기",
        time: "3~6개월 소요",
      },
      {
        num: "3",
        title: "최종 보철물 장착",
        desc: "지대주(어버트먼트)와 크라운 연결 후 교합 조정·완성",
        time: "2~3회 방문",
      },
    ],
    cta: "대구 치과 상담 예약 → 프로필 링크",
    tags: ["#대구치과상담", "#임플란트과정"],
  },
];

function CoverCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: `linear-gradient(145deg, ${BRAND.dark} 0%, ${BRAND.main} 45%, ${BRAND.light} 100%)`,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: "36px 32px 28px",
        position: "relative",
        overflow: "hidden",
        boxSizing: "border-box",
      }}
    >
      {/* 배경 장식 */}
      <div
        style={{
          position: "absolute",
          top: -60,
          right: -60,
          width: 220,
          height: 220,
          borderRadius: "50%",
          background: "rgba(33,150,243,0.18)",
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: 40,
          left: -40,
          width: 160,
          height: 160,
          borderRadius: "50%",
          background: "rgba(255,179,0,0.10)",
        }}
      />

      {/* 배지 */}
      <div style={{ display: "flex", alignItems: "center", gap: 8, zIndex: 1 }}>
        <div
          style={{
            background: BRAND.gold,
            borderRadius: 20,
            padding: "5px 14px",
            fontSize: 12,
            fontWeight: 800,
            color: BRAND.dark,
            letterSpacing: 0.3,
          }}
        >
          {card.badge}
        </div>
        <div
          style={{
            background: "rgba(255,255,255,0.15)",
            borderRadius: 20,
            padding: "5px 12px",
            fontSize: 11,
            color: "rgba(255,255,255,0.85)",
            fontWeight: 600,
          }}
        >
          {card.note}
        </div>
      </div>

      {/* 메인 텍스트 */}
      <div style={{ zIndex: 1 }}>
        <div style={{ fontSize: 56, marginBottom: 12 }}>{card.icon}</div>
        {card.headline.map((line, i) => (
          <div
            key={i}
            style={{
              fontSize: i === 0 ? 30 : 38,
              fontWeight: 900,
              color: BRAND.white,
              lineHeight: 1.25,
              letterSpacing: -0.5,
            }}
          >
            {line}
          </div>
        ))}
        <div
          style={{
            marginTop: 16,
            fontSize: 15,
            color: "rgba(255,255,255,0.75)",
            fontWeight: 500,
            lineHeight: 1.5,
          }}
        >
          {card.subtext}
        </div>
      </div>

      {/* 해시태그 */}
      <div style={{ zIndex: 1 }}>
        <div
          style={{ width: 40, height: 3, background: BRAND.gold, marginBottom: 14, borderRadius: 2 }}
        />
        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
          {card.tags.map((tag) => (
            <span
              key={tag}
              style={{
                fontSize: 11,
                color: "rgba(255,255,255,0.65)",
                fontWeight: 600,
              }}
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

function InfoCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: BRAND.white,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        padding: "28px 28px 24px",
        boxSizing: "border-box",
        border: `2px solid ${BRAND.pale}`,
      }}
    >
      <div
        style={{
          background: BRAND.main,
          borderRadius: 10,
          padding: "5px 14px",
          fontSize: 12,
          fontWeight: 800,
          color: BRAND.white,
          alignSelf: "flex-start",
          marginBottom: 16,
          letterSpacing: 0.3,
        }}
      >
        {card.badge}
      </div>

      <div
        style={{
          fontSize: 20,
          fontWeight: 900,
          color: BRAND.dark,
          lineHeight: 1.35,
          marginBottom: 18,
          whiteSpace: "pre-line",
        }}
      >
        {card.headline}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 10, flex: 1 }}>
        {card.items.map((item, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              alignItems: "flex-start",
              gap: 12,
              background: BRAND.lightGray,
              borderRadius: 12,
              padding: "11px 14px",
              border: `1px solid ${BRAND.pale}`,
            }}
          >
            <span style={{ fontSize: 18, lineHeight: 1.3 }}>{item.icon}</span>
            <div>
              <div
                style={{ fontSize: 14, fontWeight: 800, color: BRAND.main, marginBottom: 2 }}
              >
                {item.title}
              </div>
              <div style={{ fontSize: 12, color: BRAND.gray, lineHeight: 1.4 }}>
                {item.desc}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 12,
          fontSize: 11,
          color: BRAND.gray,
          borderTop: `1px solid ${BRAND.pale}`,
          paddingTop: 10,
        }}
      >
        {card.note}
      </div>
    </div>
  );
}

function CompareCard({ card }) {
  const { left, right } = card.compareData;
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: BRAND.white,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        padding: "28px 28px 24px",
        boxSizing: "border-box",
        border: `2px solid ${BRAND.pale}`,
      }}
    >
      <div
        style={{
          background: BRAND.accent,
          borderRadius: 10,
          padding: "5px 14px",
          fontSize: 12,
          fontWeight: 800,
          color: BRAND.white,
          alignSelf: "flex-start",
          marginBottom: 16,
        }}
      >
        {card.badge}
      </div>

      <div
        style={{
          fontSize: 20,
          fontWeight: 900,
          color: BRAND.dark,
          lineHeight: 1.35,
          marginBottom: 20,
          whiteSpace: "pre-line",
        }}
      >
        {card.headline}
      </div>

      <div style={{ display: "flex", gap: 12, flex: 1 }}>
        {[left, right].map((side, i) => (
          <div
            key={i}
            style={{
              flex: 1,
              background: side.bg,
              borderRadius: 16,
              padding: "16px 14px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
              border: `2px solid ${side.color}22`,
            }}
          >
            <div
              style={{
                fontSize: 11,
                fontWeight: 700,
                color: side.color,
                marginBottom: 10,
                lineHeight: 1.4,
              }}
            >
              {side.label}
            </div>
            <div>
              <div
                style={{
                  fontSize: 22,
                  fontWeight: 900,
                  color: side.color,
                  lineHeight: 1.2,
                  marginBottom: 4,
                }}
              >
                {side.value}
              </div>
              <div style={{ fontSize: 11, color: BRAND.gray }}>{side.sub}</div>
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 14,
          background: `linear-gradient(90deg, ${BRAND.main}, ${BRAND.accent})`,
          borderRadius: 12,
          padding: "12px 16px",
          textAlign: "center",
          color: BRAND.white,
          fontSize: 15,
          fontWeight: 900,
        }}
      >
        💰 {card.savings}
      </div>

      <div style={{ marginTop: 8, fontSize: 10.5, color: BRAND.gray, textAlign: "center" }}>
        {card.note}
      </div>
    </div>
  );
}

function StepsCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: `linear-gradient(160deg, ${BRAND.dark} 0%, #1a237e 100%)`,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        padding: "28px 28px 24px",
        boxSizing: "border-box",
      }}
    >
      <div
        style={{
          background: BRAND.gold,
          borderRadius: 10,
          padding: "5px 14px",
          fontSize: 12,
          fontWeight: 800,
          color: BRAND.dark,
          alignSelf: "flex-start",
          marginBottom: 14,
        }}
      >
        {card.badge}
      </div>

      <div
        style={{
          fontSize: 20,
          fontWeight: 900,
          color: BRAND.white,
          lineHeight: 1.35,
          marginBottom: 18,
          whiteSpace: "pre-line",
        }}
      >
        {card.headline}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 10, flex: 1 }}>
        {card.steps.map((step, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: 12,
              alignItems: "flex-start",
            }}
          >
            <div
              style={{
                width: 32,
                height: 32,
                borderRadius: "50%",
                background: i === 0 ? BRAND.gold : i === 1 ? BRAND.accent : "#4CAF50",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 15,
                fontWeight: 900,
                color: i === 0 ? BRAND.dark : BRAND.white,
                flexShrink: 0,
              }}
            >
              {step.num}
            </div>
            <div style={{ flex: 1 }}>
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                  marginBottom: 3,
                }}
              >
                <span
                  style={{ fontSize: 14, fontWeight: 800, color: BRAND.white }}
                >
                  {step.title}
                </span>
                <span
                  style={{
                    fontSize: 10,
                    color: "rgba(255,255,255,0.5)",
                    background: "rgba(255,255,255,0.1)",
                    padding: "2px 7px",
                    borderRadius: 10,
                  }}
                >
                  {step.time}
                </span>
              </div>
              <div
                style={{
                  fontSize: 12,
                  color: "rgba(255,255,255,0.65)",
                  lineHeight: 1.45,
                }}
              >
                {step.desc}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 14,
          background: BRAND.gold,
          borderRadius: 12,
          padding: "11px 16px",
          textAlign: "center",
          color: BRAND.dark,
          fontSize: 13,
          fontWeight: 900,
        }}
      >
        📞 {card.cta}
      </div>
    </div>
  );
}

function renderCard(card) {
  switch (card.type) {
    case "cover":
      return <CoverCard card={card} />;
    case "info":
      return <InfoCard card={card} />;
    case "compare":
      return <CompareCard card={card} />;
    case "steps":
      return <StepsCard card={card} />;
    default:
      return null;
  }
}

export default function DaeguCardNews() {
  const [current, setCurrent] = useState(0);

  return (
    <div
      style={{
        fontFamily:
          "'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',sans-serif",
        background: "#F0F4F8",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "24px 16px",
      }}
    >
      {/* 헤더 */}
      <div
        style={{
          width: "100%",
          maxWidth: 480,
          marginBottom: 20,
          textAlign: "center",
        }}
      >
        <div
          style={{
            display: "inline-block",
            background: BRAND.main,
            color: BRAND.white,
            borderRadius: 20,
            padding: "6px 18px",
            fontSize: 13,
            fontWeight: 800,
            marginBottom: 8,
          }}
        >
          🦷 대구 지역 타겟 카드뉴스
        </div>
        <div
          style={{ fontSize: 15, color: BRAND.gray, fontWeight: 600 }}
        >
          인스타그램 게시용 · 4장 구성
        </div>
      </div>

      {/* 카드 */}
      <div style={{ width: "100%", maxWidth: 420 }}>
        {renderCard(cards[current])}
      </div>

      {/* 네비게이션 */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 16,
          marginTop: 20,
        }}
      >
        <button
          onClick={() => setCurrent((c) => Math.max(0, c - 1))}
          disabled={current === 0}
          style={{
            width: 40,
            height: 40,
            borderRadius: "50%",
            border: `2px solid ${current === 0 ? "#CBD5E1" : BRAND.main}`,
            background: current === 0 ? "#F1F5F9" : BRAND.main,
            color: current === 0 ? "#CBD5E1" : BRAND.white,
            fontSize: 18,
            cursor: current === 0 ? "not-allowed" : "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 0.2s",
          }}
        >
          ‹
        </button>

        <div style={{ display: "flex", gap: 8 }}>
          {cards.map((_, i) => (
            <button
              key={i}
              onClick={() => setCurrent(i)}
              style={{
                width: i === current ? 28 : 10,
                height: 10,
                borderRadius: 5,
                border: "none",
                background: i === current ? BRAND.main : "#CBD5E1",
                cursor: "pointer",
                transition: "all 0.3s",
                padding: 0,
              }}
            />
          ))}
        </div>

        <button
          onClick={() => setCurrent((c) => Math.min(cards.length - 1, c + 1))}
          disabled={current === cards.length - 1}
          style={{
            width: 40,
            height: 40,
            borderRadius: "50%",
            border: `2px solid ${current === cards.length - 1 ? "#CBD5E1" : BRAND.main}`,
            background: current === cards.length - 1 ? "#F1F5F9" : BRAND.main,
            color: current === cards.length - 1 ? "#CBD5E1" : BRAND.white,
            fontSize: 18,
            cursor: current === cards.length - 1 ? "not-allowed" : "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 0.2s",
          }}
        >
          ›
        </button>
      </div>

      {/* 카드 번호 표시 */}
      <div
        style={{
          marginTop: 12,
          fontSize: 13,
          color: BRAND.gray,
          fontWeight: 600,
        }}
      >
        {current + 1} / {cards.length} — {cards[current].badge}
      </div>

      {/* 썸네일 미리보기 */}
      <div
        style={{
          display: "flex",
          gap: 10,
          marginTop: 20,
          width: "100%",
          maxWidth: 420,
          justifyContent: "center",
        }}
      >
        {cards.map((card, i) => (
          <button
            key={i}
            onClick={() => setCurrent(i)}
            style={{
              flex: 1,
              aspectRatio: "1/1",
              borderRadius: 10,
              border: `2px solid ${i === current ? BRAND.main : "transparent"}`,
              background:
                card.type === "cover" || card.type === "steps"
                  ? BRAND.dark
                  : BRAND.pale,
              cursor: "pointer",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 11,
              fontWeight: 700,
              color: card.type === "cover" || card.type === "steps" ? BRAND.white : BRAND.main,
              transition: "border-color 0.2s",
              padding: "6px 4px",
              lineHeight: 1.3,
              textAlign: "center",
              maxWidth: 90,
            }}
          >
            {i + 1}장
            <br />
            <span style={{ fontSize: 10, fontWeight: 500, opacity: 0.8 }}>
              {["커버", "조건", "비용", "과정"][i]}
            </span>
          </button>
        ))}
      </div>

      <div
        style={{
          marginTop: 24,
          fontSize: 11,
          color: "#94A3B8",
          textAlign: "center",
          maxWidth: 420,
          lineHeight: 1.6,
        }}
      >
        * 본 콘텐츠는 2026년 건강보험 기준입니다. 실제 진료비는 병원·치료 난이도에 따라 다를 수 있습니다.
        <br />
        GEO 최적화 키워드: 대구 임플란트, 대구 치과, 대구 임플란트 비용, 대구 임플란트 보험
      </div>
    </div>
  );
}
