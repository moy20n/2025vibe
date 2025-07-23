import streamlit as st
import random

# 1. 장르 및 공통 무드 목록
genres = ["K-Pop", "락발라드", "클래식", "J-Pop", "팝", "인디"]
common_moods = [
    "신나는",
    "감성적인",
    "슬픈",
    "집중/공부용",
    "새벽 감성",
    "사랑에 빠진 느낌",
    "드라이브용",
    "혼자 듣기 좋은"
]

# 2. 노래 제목 데이터 (링크 없이 제목만)
song_library = {
    ("K-Pop", "신나는"): ["IVE - I AM", "NewJeans - Super Shy"],
    ("클래식", "집중/공부용"): ["Beethoven - Moonlight Sonata", "Debussy - Clair de Lune"],
    ("J-Pop", "새벽 감성"): ["YOASOBI - 夜に駆ける", "Aimer - Brave Shine"],
    ("팝", "드라이브용"): ["Dua Lipa - Levitating"],
    ("인디", "감성적인"): ["볼빨간사춘기 - 우주를 줄게"],
    ("락발라드", "슬픈"): ["김경호 - 금지된 사랑"]
}

# 3. Streamlit UI
st.title("🎧 무드 기반 노래 추천기 (링크 없이)")
st.write("장르와 무드를 선택하면 추천곡을 알려드려요!")

genre = st.selectbox("장르를 선택하세요 🎼", genres)
mood = st.radio("기분/상황을 선택하세요 🧠", common_moods)

if st.button("노래 추천 받기 🎁"):
    key = (genre, mood)
    if key in song_library:
        title = random.choice(song_library[key])
        st.success(f"**추천곡:** {title}")
    else:
        st.warning("이 조합에 대한 추천곡이 아직 없어요. 다른 조합을 선택해보세요!")

st.markdown("---")
st.caption("© 2025 Music Recommender by ChatGPT")
