import streamlit as st
import random
import requests

# 1. YouTube API 키 (여기에 본인의 키를 입력하세요)
YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"

# 2. 장르 및 무드 선택 옵션
songs_by_mood = {
    "K-Pop": ["신나는", "감성적인", "사랑에 빠진 느낌"],
    "락발라드": ["감성적인", "슬픈"],
    "클래식": ["집중/공부용"],
    "J-Pop": ["신나는", "새벽 감성"],
    "팝": ["드라이브용", "혼자 듣기 좋은"],
    "인디": ["감성적인", "새벽 감성"]
}

# 3. 유튜브 검색 함수
def search_youtube(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json().get("items", [])
        if items:
            choice = random.choice(items)
            video_id = choice["id"]["videoId"]
            title = choice["snippet"]["title"]
            return title, f"https://www.youtube.com/watch?v={video_id}"
    return None, None

# 4. Streamlit UI
st.title("🎧 무드 기반 유튜브 노래 추천기")
st.write("장르와 무드를 선택하면, YouTube에서 노래를 실시간으로 추천해드려요!")

genre = st.selectbox("장르를 선택하세요 🎼", list(songs_by_mood.keys()))
mood = st.radio("기분/상황을 선택하세요 🧠", songs_by_mood[genre])

if st.button("노래 추천 받기 🎁"):
    query = f"{genre} {mood} 음악"
    title, url = search_youtube(query)
    if title and url:
        st.success(f"**추천곡:** {title}")
        st.markdown(f"[▶️ 유튜브에서 보기]({url})")
        st.video(url)
    else:
        st.error("추천 결과를 가져올 수 없습니다. API 키를 확인하거나 다시 시도해보세요.")

st.markdown("---")
st.caption("© 2025 Music Recommender by ChatGPT")
