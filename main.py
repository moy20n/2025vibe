import streamlit as st
import random

# 🎵 노래 데이터 (간단히 하드코딩)
songs = {
    "K-Pop": {
        "신나는": [
            ("IVE - I AM", "https://www.youtube.com/watch?v=6ZUIwj3FgUY"),
            ("NewJeans - Super Shy", "https://www.youtube.com/watch?v=ArmDp-zijuc")
        ],
        "감성적인": [
            ("BTS - Spring Day", "https://www.youtube.com/watch?v=xEeFrLSkMm8"),
            ("태연 - 그대라는 시", "https://www.youtube.com/watch?v=7C2z4GqqS5E")
        ]
    },
    "클래식": {
        "집중/공부용": [
            ("Beethoven - Moonlight Sonata", "https://www.youtube.com/watch?v=4Tr0otuiQuU"),
            ("Debussy - Clair de Lune", "https://www.youtube.com/watch?v=CvFH_6DNRCY")
        ]
    },
    "J-Pop": {
        "새벽 감성": [
            ("YOASOBI - 夜に駆ける", "https://www.youtube.com/watch?v=x8VYWazR5mE"),
            ("Aimer - Brave Shine", "https://www.youtube.com/watch?v=3ExaJIB5Phk")
        ]
    }
}

# 🖼️ 앱 UI
st.title("🎧 간단한 노래 추천기")
st.write("장르와 분위기를 선택하면 노래를 추천해드릴게요!")

# 선택 항목
genre = st.selectbox("장르 선택", list(songs.keys()))
mood = st.radio("무드 선택", list(songs[genre].keys()))

# 추천 버튼
if st.button("노래 추천!"):
    title, url = random.choice(songs[genre][mood])
    st.success(f"추천곡: **{title}**")
    st.markdown(f"[▶️ 유튜브에서 듣기]({url})")
    st.video(url)

st.caption("© 2025 Music Recommender by ChatGPT")
