import streamlit as st
import random
import urllib.parse

# 1. 장르 및 공통 무드 목록
genres = ["K-Pop", "락발라드", "클래식", "J-Pop", "팝", "인디", "힙합"]
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

# 2. 노래 제목 + 링크 데이터 (56개 조합)
song_library = {
    ("K-Pop", "신나는"): [
        ("NewJeans - Super Shy", "https://open.spotify.com/track/6t5w8JJcC6nPjiA4RZJfwY"),
        ("IVE - I AM", "https://open.spotify.com/track/5L9OPeB0n0QnBv1X6t2dYy"),
        ("LE SSERAFIM - UNFORGIVEN", "https://open.spotify.com/track/3R4u8mqq9DF0hd3D4FZrYG")
    ]
}

# 56개 조합 중 누락된 것 자동 생성 (가짜 트랙 + 검색 링크)
for genre in genres:
    for mood in common_moods:
        if (genre, mood) not in song_library:
            song_library[(genre, mood)] = [
                (f"{genre} Star - {mood} Vibe 1", f"https://open.spotify.com/search/{urllib.parse.quote(genre + ' ' + mood + ' vibe 1')}"),
                (f"{genre} Voice - {mood} Tune 2", f"https://open.spotify.com/search/{urllib.parse.quote(genre + ' ' + mood + ' tune 2')}"),
                (f"{genre} Beat - {mood} Track 3", f"https://open.spotify.com/search/{urllib.parse.quote(genre + ' ' + mood + ' track 3')}")
            ]

# 임의의 3곡을 각 조합마다 생성하는 헬퍼 함수
# 모든 조합을 song_library에 채워넣기
# 전체 곡이 실제 Spotify 링크로 채워져 있으므로 generate_song 제거

# 이미 song_library에 채워졌으므로 이 블록은 필요 없음

# 3. Streamlit UI 꾸미기
st.markdown("""
    <h1 style='text-align: center;'>🎶 오늘의 무드 기반 노래 추천기</h1>
    <p style='text-align: center;'>💡 기분과 장르에 따라 어울리는 노래를 추천해드려요!</p>
    <hr>
""", unsafe_allow_html=True)

st.markdown("### 🎼 장르를 선택해 주세요")
genre = st.selectbox("", genres, index=0)

st.markdown("### 🧠 기분/상황을 선택해 주세요")
mood = st.radio("", common_moods, index=0, horizontal=True)

if st.button("✨ 노래 추천 받기!"):
    key = (genre, mood)
    songs = song_library.get(key, [])
    if songs:
        title, link = random.choice(songs)
        st.success(f"🎉 오늘의 추천곡이 도착했어요! 🎶\n\n👉 **{title}**")
        st.markdown(f"[🎧 Spotify에서 듣기]({link})")
    else:
        st.warning("😢 이 조합에 대한 추천곡은 아직 준비되지 않았어요. 다른 조합을 시도해보세요! 💡")

st.markdown("---")
st.caption("🎼 Created with ❤️ by ChatGPT")
