import streamlit as st

col1,col2,col3 = st.columns([4,4,4])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스도 넣을 수 있다.')

with col1 :
  # column 1 에 담을 내용
  st.title('여기는 1 열 ')
with col3:
  st.title('여기는 3 열 ')
with col2 :
  # column 2 에 담을 내용
  st.title('여기는 2열')
  st.checkbox('2열 체크박스 1 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' 1열 서브헤더 !! ')
col1.write("안녕하세요")
col2.checkbox('2열 체크박스 2 ') 

#=>위에 with col2: 안의 내용과 같은 기능을합니다

st.title("📦 Streamlit Container 예제")

# 컨테이너 1 - 요약 영역
with st.container():
    st.subheader("1️⃣ KPI 요약")
    col1, col2, col3 = st.columns(3)
    col1.metric("매출", "₩120,000")
    col2.metric("주문", "58건")
    col3.metric("고객 수", "34명")

# 구분선
st.markdown("---")

# 컨테이너 2 - 필터 + 표 영역
with st.container():
    st.subheader("2️⃣ 필터링 & 데이터")

    # 사이드 필터 (예시)
    category = st.selectbox("카테고리 선택", ["전체", "전자", "가구", "사무"])

    # 샘플 데이터 출력
    import pandas as pd
    df = pd.DataFrame({
        "제품명": ["노트북", "책상", "펜"],
        "카테고리": ["전자", "가구", "사무"],
        "매출": [100000, 20000, 3000]
    })

    if category != "전체":
        df = df[df["카테고리"] == category]

    st.dataframe(df)

# 컨테이너 3 - 하단 메모
with st.container():
    st.subheader("3️⃣ 메모 작성")
    st.text_area("학습 또는 회의 메모를 입력하세요")

users = [{"id": 1, "name": "홍길동"}, {"id": 2, "name": "이몽룡"}]
selected_user = st.selectbox(
    "사용자 선택",
    users,
    format_func=lambda x: f"{x['name']} (ID: {x['id']})"
)
st.write("선택한 사용자 ID:", selected_user['id'])

import plotly.express as px
import pandas as pd

# 샘플 데이터
df = pd.DataFrame({
    "과일": ["사과", "바나나", "체리", "사과", "바나나", "체리"],
    "판매량": [10, 15, 8, 12, 18, 6],
    "지점": ["서울", "서울", "서울", "부산", "부산", "부산"]
})

# plotly 그래프 생성
fig = px.bar(df, x="과일", y="판매량", color="지점", barmode="group", title="과일별 판매량")

# Streamlit에 출력
st.plotly_chart(fig, use_container_width=True)

import time

st.write("황여준")

progress = st.progress(0)

for i in range(101):
    time.sleep(0.03)  # 작업 시뮬레이션
    progress.progress(i)

st.success("완료되었습니다!")

st.write("데이터를 불러옵니다...")

with st.spinner("잠시만 기다려 주세요..."):
    time.sleep(5)  # 실제 작업 시뮬레이션

st.success("데이터 로딩 완료!")