import streamlit as st
import random

# 노래 데이터베이스 (장르 → 무드 → [(제목, YouTube 링크)])
songs = {
    "팝": {
        "신나는": [
            ("Dua Lipa - Don't Start Now", "https://www.youtube.com/watch?v=oygrmJFKYZY"),
            ("Harry Styles - As It Was", "https://www.youtube.com/watch?v=H5v3kku4y6Q"),
            ("Taylor Swift - Shake It Off", "https://www.youtube.com/watch?v=nfWlot6h_JM")
        ],
        "차분한": [
            ("Billie Eilish - Ocean Eyes", "https://www.youtube.com/watch?v=viimfQi_pUw"),
            ("Adele - Easy On Me", "https://www.youtube.com/watch?v=U3ASj1L6_sY")
        ]
    },
    "힙합": {
        "신나는": [
            ("Drake - God's Plan", "https://www.youtube.com/watch?v=xpVfcZ0ZcFM"),
            ("Kanye West - Stronger", "https://www.youtube.com/watch?v=PsO6ZnUZI0g")
        ],
        "차분한": [
            ("Kendrick Lamar - LOVE.", "https://www.youtube.com/watch?v=ox7RsX1Ee34"),
            ("Tyler, The Creator - See You Again", "https://www.youtube.com/watch?v=TGgcC5xg9YI")
        ]
    },
    "발라드": {
        "신나는": [
            ("임영웅 - 이제 나만 믿어요", "https://www.youtube.com/watch?v=JA5QXpfTKKM"),
            ("이승철 - 소녀시대", "https://www.youtube.com/watch?v=q4bd7Z6jwFQ")
        ],
        "차분한": [
            ("폴킴 - 모든 날, 모든 순간", "https://www.youtube.com/watch?v=-RkqrWcQbCc"),
            ("성시경 - 두 사람", "https://www.youtube.com/watch?v=gkYV8Ez1fRs")
        ]
    },
    "인디": {
        "신나는": [
            ("볼빨간사춘기 - 여행", "https://www.youtube.com/watch?v=sZQkJvgk1bQ"),
            ("잔나비 - 주저하는 연인들을 위해", "https://www.youtube.com/watch?v=l_9zU2GKmL8")
        ],
        "차분한": [
            ("10CM - 폰서트", "https://www.youtube.com/watch?v=bSTxH7N48ck"),
            ("혁오 - Tomboy", "https://www.youtube.com/watch?v=ROO_xL2Plb0")
        ]
    }
}

# Streamlit 앱
st.title("🎶 오늘 뭐 들을까? - 노래 추천기")
st.markdown("장르와 무드를 선택하면 추천 노래를 보여드려요!")

# 선택창
genre = st.selectbox("🎼 장르 선택", list(songs.keys()))
mood = st.radio("🎧 무드 선택", ["신나는", "차분한"])

# 버튼 클릭 시 추천
if st.button("노래 추천 받기 🎁"):
    if genre in songs and mood in songs[genre]:
        recommendation = random.choice(songs[genre][mood])
        title, link = recommendation
        st.success(f"**추천곡:** {title}")
        st.markdown(f"[👉 유튜브에서 듣기]({link})")
        st.video(link)  # YouTube 미리보기
    else:
        st.warning("조건에 맞는 노래가 없습니다 😥")

# 바닥 정보
st.markdown("---")
st.caption("© 2025 Music Recommender by Streamlit & ChatGPT")
