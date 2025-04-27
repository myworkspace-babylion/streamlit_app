import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 관리자만 CSV 파일 업로드
st.title('초등학교 교재 인사이트 대시보드')

# 관리자가 업로드하는 CSV 파일
uploaded_file = st.file_uploader("초등학교 교재 CSV 파일을 업로드해주세요.", type="csv")

# 2. 파일이 업로드되면
if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)
    
    # 3. 초등학교 교재 타이틀 필터링
    st.header("초등학교 교재를 선택하세요")
    titles = df['교재 제목'].unique()  # 교재 제목만 추출하여 선택하게 함
    
    # 교재 타이틀 선택
    selected_title = st.selectbox("교재 타이틀 선택", titles)
    
    # 4. 선택된 교재 관련 정보 표시
    if selected_title:
        st.subheader(f"선택된 교재: {selected_title}")
        
        # 교재 정보 필터링
        selected_data = df[df['교재 제목'] == selected_title]
        
        # 선택된 교재의 상세 정보 표시
        for index, row in selected_data.iterrows():
            st.write(f"**난이도**: {row['난이도']}")
            st.write(f"**추천 학년**: {row['추천 학년']}")
            st.write(f"**어떻게 가르칠까요?**: {row['어떻게 가르칠까요?']}")
            st.write(f"**산업 연계**: {row['산업 연계']}")
            st.write(f"**관련 교수학습자료**: {row['관련 교수학습자료']}")
            st.write("---")
        
        # 5. 난이도별 교재 개수 그래프
        st.subheader('난이도별 교재 개수')
        difficulty_count = df['난이도'].value_counts()
        st.bar_chart(difficulty_count)

else:
    st.warning("CSV 파일을 업로드해주세요. 교재 목록이 없으면 선택할 수 없습니다.")
