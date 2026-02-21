import streamlit as st

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="제조업 중처법 리스크 진단", layout="centered")

st.title("🏭 중대재해처벌법 통합 리스크 시뮬레이터")
st.markdown("---")
st.subheader("CEO를 위한 전략적 리스크 분석")
st.write("기업 정보를 입력하시면 사고 발생 시 예상되는 **형량**과 **경제적 손실**을 즉시 산출합니다.")

# 2. 데이터 입력 섹션 (대장의 영업 DB)
with st.form("integrated_risk_form"):
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("기업명", placeholder="OO정밀")
        emp_count = st.number_input("상시 근로자 수", min_value=5, value=50)
        revenue = st.number_input("연 매출액 (단위: 억 원)", min_value=1, value=100)
    with col2:
        safety_manager = st.radio("안전관리자 선임/전담부서 여부", ["미흡", "양호"])
        past_accidents = st.selectbox("최근 3년 내 사고 이력", ["없음", "1회", "2회 이상"])
        risk_level = st.select_slider("현장 위험도", options=["보통", "높음", "매우 높음"])

    submitted = st.form_submit_button("🚨 통합 리스크 분석 결과 확인")

# 3. 통합 계산 및 시각화 로직
if submitted:
    st.markdown("### **[ 분석 보고서 결과 ]**")
    
    # [형량 로직]
    jail_term = "1년 이상 실형"
    if safety_manager == "미흡" or past_accidents != "없음" or risk_level != "보통":
        jail_term = "3년 이상 (구속 수사 및 가중 처벌 대상)"
        jail_color = "red"
    else:
        jail_color = "orange"

    # [금전적 손실 로직]
    avg_settlement = 300000000  # 합의금 3억
    multiplier = 5              # 징벌적 배상 5배
    fine_estimate = 500000000   # 최소 벌금 5억
    loss_of_business = revenue * 0.05 * 100000000  # 매출액의 5%를 조업중단 손실로 가정
    
    total_money_loss = (avg_settlement * multiplier) + fine_estimate + loss_of_business

    # 결과 출력 1: 인신 구속 리스크
    st.error(f"👨‍⚖️ **대표이사 신변 리스크: {jail_term}**")
    
    # 결과 출력 2: 경제적 손실 리스크
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="총 예상 손실액", value=f"약 {total_money_loss/100000000:,.1f}억", delta="자본금 대비 위험")
    with col_b:
        st.metric(label="징벌적 손해배상", value="최대 15억", delta="합의금의 5배")

    # 세부 분석 정보
    with st.expander("상세 손실 내역 보기"):
        st.write(f"- 유족 합의 및 배상금: 약 {avg_settlement * multiplier / 100000000:.1f}억")
        st.write(f"- 법인 벌금 및 소송 비용: 약 {fine_estimate / 100000000:.1f}억")
        st.write(f"- 사고 후 조업 중단 손실액: 약 {loss_of_business / 100000000:.1f}억")

    # 4. 공격적 마무리 (Call to Action)
    st.markdown(f"""
    ---
    ### **대장(The Boss)의 전략 제언:**
    > "{company_name} 대표님, 현재 분석된 **{total_money_loss/100000000:,.1f}억**의 손실과 **{jail_term}**의 리스크는 
    > 단순한 가정이 아니라 법적 현실입니다. 
    > 기업의 생존을 위해 지금 즉시 방어막(보험 및 안전 진단)을 구축하십시오."
    """)
    
    if st.button("대장에게 비밀 컨설팅 요청하기 (https://open.kakao.com/o/s73BLxhi)"):
        st.write("상담 신청이 완료되었습니다. 대장이 곧 연락드립니다.")

st.markdown("---")
st.subheader("📩 CEO 전용 정밀 대응 리포트 신청")
st.write("분석 결과와 **'2026 제조업 안전 점검 가이드라인'**을 송부해 드립니다.")

# 1. 정보 수집 폼
with st.form("contact_form"):
    u_name = st.text_input("성함 / 직함", placeholder="예: 홍길동 대표이사")
    u_phone = st.text_input("연락처", placeholder="예: 010-1234-5678")
    u_email = st.text_input("수신 이메일", placeholder="ceo@company.com")
    
    submit_contact = st.form_submit_button("📊 맞춤형 리포트 및 무료 상담 신청")

    if submit_contact:
        if u_name and u_phone and "@" in u_email:
            st.success(f"신청 완료! {u_name}님, 잠시만 기다려 주십시오.")
            st.info(f"📍 전문 리포트는 **{u_email}**로 발송되며,\n\n전문가(대장)가 직접 **{u_phone}**으로 연락드려 전략을 제안해 드립니다.")
        else:
            st.warning("정보를 정확히 입력해 주셔야 리포트 발송이 가능합니다.")

# 2. 대장님의 공식 프로필 및 연락처 (하단 고정)
st.markdown("---")
st.subheader("📲 즉시 상담이 필요하십니까?")

# 카카오톡 버튼 (가장 크게)
st.link_button("💬 대장과 실시간 1:1 카톡 상담하기", "https://open.kakao.com/o/s73BLxhi", use_container_width=True)

# 메일 및 전화번호 안내
st.markdown(f"""
    📧 **이메일:** soff23@gmail.com  
    📞 **직통번호:** 010-6214-4020  
   
    *실시간 상담이 필요하신 경우 위 번호로 직접 연락 주십시오.*
    """)

st.caption("© 2026 중대재해 리스크 컨설팅 그룹. All rights reserved.")