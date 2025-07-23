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

# 2. 노래 제목 데이터 (모든 조합에 최소 3곡 이상 포함)
song_library = {}

for genre in genres:
    for mood in common_moods:
        key = (genre, mood)
        song_library[key] = [
            f"{genre} - {mood} 곡 1",
            f"{genre} - {mood} 곡 2",
            f"{genre} - {mood} 곡 3",
            f"{genre} - {mood} 곡 4"
        ]

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
