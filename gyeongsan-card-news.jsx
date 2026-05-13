import { useState } from "react";

const BRAND = {
  main: "#00695C",
  light: "#00897B",
  accent: "#26A69A",
  pale: "#E0F2F1",
  gold: "#FFB300",
  white: "#FFFFFF",
  dark: "#0A1F1C",
  gray: "#607D8B",
  lightGray: "#F1FAF9",
};

const cards = [
  {
    id: 1,
    type: "cover",
    badge: "경산 구강예방 가이드",
    headline: ["경산 치과,", "건강보험으로", "받는 예방치료"],
    subtext: "스케일링부터 임플란트까지 한 번에 정리",
    tags: ["#경산치과", "#경산스케일링", "#경산임플란트", "#경산치과추천"],
    icon: "🦷",
    note: "2026년 건강보험 기준",
  },
  {
    id: 2,
    type: "scaling",
    badge: "스케일링 건강보험",
    headline: "1년에 한 번!\n스케일링 건강보험 완전 정리",
    items: [
      {
        icon: "📅",
        title: "적용 대상",
        value: "만 19세 이상 전국민",
        highlight: false,
      },
      {
        icon: "🔁",
        title: "적용 횟수",
        value: "연 1회 (매년 1월 1일 리셋)",
        highlight: false,
      },
      {
        icon: "💳",
        title: "본인부담금",
        value: "약 1만 6천 원",
        highlight: true,
      },
      {
        icon: "💰",
        title: "비급여 대비 절약",
        value: "5~6만 원 → 약 1만 6천 원",
        highlight: false,
      },
    ],
    tip: "💡 매년 1월에 스케일링 예약하면 구강 건강 관리가 훨씬 쉬워요!",
    tags: ["#경산스케일링", "#스케일링보험"],
  },
  {
    id: 3,
    type: "age",
    badge: "연령별 예방치료 혜택",
    headline: "나이에 따라 받을 수 있는\n치과 건강보험 혜택",
    ageItems: [
      {
        age: "만 18세\n이하",
        color: "#E91E63",
        bg: "#FCE4EC",
        benefits: ["치아홈메우기(실란트)", "불소도포"],
        note: "충치 예방 급여 항목",
      },
      {
        age: "만 19세\n이상",
        color: "#1565C0",
        bg: "#E3F2FD",
        benefits: ["연 1회 스케일링", "충치·신경치료"],
        note: "기본 보험 진료 적용",
      },
      {
        age: "만 65세\n이상",
        color: "#00695C",
        bg: "#E0F2F1",
        benefits: ["임플란트 평생 2개", "틀니(7년 1회)"],
        note: "본인부담 30~50%",
      },
    ],
    note: "※ 충치·신경치료·발치는 연령 관계없이 건강보험 적용",
    tags: ["#치과건강보험", "#경산치과보험"],
  },
  {
    id: 4,
    type: "checklist",
    badge: "경산 치과 방문 체크리스트",
    headline: "경산 치과 방문 전,\n이것만 확인하세요",
    checks: [
      {
        icon: "📋",
        title: "건강보험증 또는 신분증 지참",
        desc: "급여 진료 시 반드시 필요",
      },
      {
        icon: "🗓️",
        title: "스케일링 마지막 날짜 확인",
        desc: "연 1회 건강보험 혜택, 놓치지 마세요",
      },
      {
        icon: "🦷",
        title: "6개월마다 정기 구강검진",
        desc: "초기 발견이 치료비 절약의 핵심",
      },
      {
        icon: "🏥",
        title: "만 65세 이상 임플란트 급여 확인",
        desc: "평생 2개 한도, 신청 전 반드시 문의",
      },
    ],
    cta: "경산 치과 예약 문의 → 프로필 링크",
    tags: ["#경산치과예약", "#경산구강건강"],
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
      <div
        style={{
          position: "absolute",
          top: -50,
          right: -50,
          width: 200,
          height: 200,
          borderRadius: "50%",
          background: "rgba(38,166,154,0.2)",
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: 30,
          left: -40,
          width: 140,
          height: 140,
          borderRadius: "50%",
          background: "rgba(255,179,0,0.12)",
        }}
      />

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

      <div style={{ zIndex: 1 }}>
        <div style={{ fontSize: 52, marginBottom: 12 }}>{card.icon}</div>
        {card.headline.map((line, i) => (
          <div
            key={i}
            style={{
              fontSize: i === 0 ? 28 : 36,
              fontWeight: 900,
              color: BRAND.white,
              lineHeight: 1.28,
              letterSpacing: -0.5,
            }}
          >
            {line}
          </div>
        ))}
        <div
          style={{
            marginTop: 14,
            fontSize: 14,
            color: "rgba(255,255,255,0.72)",
            fontWeight: 500,
            lineHeight: 1.5,
          }}
        >
          {card.subtext}
        </div>
      </div>

      <div style={{ zIndex: 1 }}>
        <div
          style={{
            width: 40,
            height: 3,
            background: BRAND.gold,
            marginBottom: 14,
            borderRadius: 2,
          }}
        />
        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
          {card.tags.map((tag) => (
            <span
              key={tag}
              style={{
                fontSize: 11,
                color: "rgba(255,255,255,0.62)",
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

function ScalingCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: BRAND.white,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        padding: "28px 28px 22px",
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
          marginBottom: 14,
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
          marginBottom: 16,
          whiteSpace: "pre-line",
        }}
      >
        {card.headline}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 9, flex: 1 }}>
        {card.items.map((item, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 12,
              background: item.highlight
                ? `linear-gradient(90deg, ${BRAND.main}18, ${BRAND.accent}18)`
                : BRAND.lightGray,
              borderRadius: 12,
              padding: "10px 14px",
              border: item.highlight
                ? `1.5px solid ${BRAND.accent}55`
                : `1px solid ${BRAND.pale}`,
            }}
          >
            <span style={{ fontSize: 20 }}>{item.icon}</span>
            <div style={{ flex: 1 }}>
              <div
                style={{ fontSize: 11, color: BRAND.gray, fontWeight: 600, marginBottom: 2 }}
              >
                {item.title}
              </div>
              <div
                style={{
                  fontSize: item.highlight ? 16 : 13,
                  fontWeight: item.highlight ? 900 : 700,
                  color: item.highlight ? BRAND.main : BRAND.dark,
                }}
              >
                {item.value}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 12,
          background: BRAND.pale,
          borderRadius: 12,
          padding: "10px 14px",
          fontSize: 12,
          color: BRAND.main,
          fontWeight: 700,
          lineHeight: 1.45,
        }}
      >
        {card.tip}
      </div>
    </div>
  );
}

function AgeCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: BRAND.white,
        borderRadius: 24,
        display: "flex",
        flexDirection: "column",
        padding: "28px 28px 22px",
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
          marginBottom: 14,
        }}
      >
        {card.badge}
      </div>

      <div
        style={{
          fontSize: 19,
          fontWeight: 900,
          color: BRAND.dark,
          lineHeight: 1.35,
          marginBottom: 16,
          whiteSpace: "pre-line",
        }}
      >
        {card.headline}
      </div>

      <div style={{ display: "flex", gap: 10, flex: 1 }}>
        {card.ageItems.map((item, i) => (
          <div
            key={i}
            style={{
              flex: 1,
              background: item.bg,
              borderRadius: 14,
              padding: "14px 10px",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              border: `1.5px solid ${item.color}33`,
            }}
          >
            <div
              style={{
                background: item.color,
                color: BRAND.white,
                borderRadius: 10,
                padding: "5px 8px",
                fontSize: 11,
                fontWeight: 900,
                textAlign: "center",
                whiteSpace: "pre-line",
                lineHeight: 1.3,
                marginBottom: 10,
              }}
            >
              {item.age}
            </div>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                gap: 4,
                width: "100%",
              }}
            >
              {item.benefits.map((b, bi) => (
                <div
                  key={bi}
                  style={{
                    fontSize: 11,
                    color: item.color,
                    fontWeight: 700,
                    textAlign: "center",
                    background: "rgba(255,255,255,0.7)",
                    borderRadius: 7,
                    padding: "4px 6px",
                    lineHeight: 1.3,
                  }}
                >
                  {b}
                </div>
              ))}
            </div>
            <div
              style={{
                marginTop: 8,
                fontSize: 10,
                color: BRAND.gray,
                textAlign: "center",
                lineHeight: 1.3,
              }}
            >
              {item.note}
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 12,
          fontSize: 11.5,
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

function ChecklistCard({ card }) {
  return (
    <div
      style={{
        width: "100%",
        aspectRatio: "1/1",
        background: `linear-gradient(160deg, ${BRAND.dark} 0%, #004D40 100%)`,
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
        {card.checks.map((check, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: 12,
              alignItems: "flex-start",
              background: "rgba(255,255,255,0.08)",
              borderRadius: 12,
              padding: "11px 14px",
              border: "1px solid rgba(255,255,255,0.1)",
            }}
          >
            <span style={{ fontSize: 20, lineHeight: 1.2 }}>{check.icon}</span>
            <div>
              <div
                style={{ fontSize: 13, fontWeight: 800, color: BRAND.white, marginBottom: 3 }}
              >
                {check.title}
              </div>
              <div
                style={{ fontSize: 11.5, color: "rgba(255,255,255,0.6)", lineHeight: 1.4 }}
              >
                {check.desc}
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
    case "scaling":
      return <ScalingCard card={card} />;
    case "age":
      return <AgeCard card={card} />;
    case "checklist":
      return <ChecklistCard card={card} />;
    default:
      return null;
  }
}

export default function GyeongsanCardNews() {
  const [current, setCurrent] = useState(0);

  return (
    <div
      style={{
        fontFamily:
          "'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',sans-serif",
        background: "#EFF7F6",
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
          🦷 경산 지역 타겟 카드뉴스
        </div>
        <div style={{ fontSize: 15, color: BRAND.gray, fontWeight: 600 }}>
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
            border: `2px solid ${
              current === cards.length - 1 ? "#CBD5E1" : BRAND.main
            }`,
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

      {/* 카드 번호 */}
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

      {/* 썸네일 */}
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
                card.type === "cover" || card.type === "checklist"
                  ? BRAND.dark
                  : BRAND.pale,
              cursor: "pointer",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 11,
              fontWeight: 700,
              color:
                card.type === "cover" || card.type === "checklist"
                  ? BRAND.white
                  : BRAND.main,
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
              {["커버", "스케일링", "연령별", "체크리스트"][i]}
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
        GEO 최적화 키워드: 경산 치과, 경산 스케일링, 경산 임플란트, 경산 구강검진
      </div>
    </div>
  );
}
