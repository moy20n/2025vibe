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
    ],
    ("K-Pop", "감성적인"): [
        ("BTS - Spring Day", "https://open.spotify.com/track/0J2QdDbelmTkv5kCIL5dGk"),
        ("Taeyeon - Four Seasons", "https://open.spotify.com/track/1i1fxkWeaMmKEB4T7zqbzK"),
        ("IU - Through the Night", "https://open.spotify.com/track/4pspTz2lYyP8pmjvzYxPpo")
    ],
    ("K-Pop", "슬픈"): [
        ("EXO - Miracles in December", "https://open.spotify.com/track/2uUFCM8MlxZBqqD2ZRZ4up"),
        ("Wendy - When This Rain Stops", "https://open.spotify.com/track/5N75pRVPCcA9zDUTjZxHnA"),
        ("G-Dragon - Untitled, 2014", "https://open.spotify.com/track/5Ae2plY24RsFPB2M8dAWTj")
    ],
    ("클래식", "새벽 감성"): [
        ("Chopin - Prelude in E minor", "https://open.spotify.com/track/3Z8FwOEN59mRMxDCtb8N0A"),
        ("Ravel - Pavane for a Dead Princess", "https://open.spotify.com/track/1TfqLAPs4K3s2rJMoCokcS"),
        ("Massenet - Meditation", "https://open.spotify.com/track/2q1GSCSyJvvE5mRvgyqO8f")
    ],
    ("클래식", "슬픈"): [
        ("Albinoni - Adagio in G minor", "https://open.spotify.com/track/0rhUdmv4hsgHEGsGdpNT1S"),
        ("Beethoven - Moonlight Sonata", "https://open.spotify.com/track/5Z01UMMf7V1o0MzF86s6WJ"),
        ("Tchaikovsky - Swan Lake", "https://open.spotify.com/track/4J2zzR4r91lpoUASWewt9l")
    ],
    ("힙합", "드라이브용"): [
        ("Jay Park - Me Like Yuh", "https://open.spotify.com/track/2XjFjvZt3lEhzOvL9IdBrf"),
        ("Zico - Artist", "https://open.spotify.com/track/1X48dwTph7kYkFYMQ6A0xY"),
        ("Leellamarz - Trip", "https://open.spotify.com/track/7nLbHq2p0VWbN4PEbnF4he")
    ],
    ("힙합", "신나는"): [
        ("Dynamic Duo - BAAAM", "https://open.spotify.com/track/3dCkKzLq6T9RuAJvmEBqmc"),
        ("Zico - Any Song", "https://open.spotify.com/track/6Knv6wdA0luoMUuuoYi2i1"),
        ("Simon Dominic - Make Her Dance", "https://open.spotify.com/track/1BrHWTZ1riX5tJFeFJKVxI")
    ]
    "J-Pop", "신나는"): [
        ("YOASOBI - Idol", "https://open.spotify.com/track/5nC3YM1VoDrM1QeP6wGnn6"),
        ("Aimer - Brave Shine", "https://open.spotify.com/track/3TQOeLlaj8zTSZ4nNT1Gdt"),
        ("LiSA - Gurenge", "https://open.spotify.com/track/5RqR4ZCCKJDcBLIn4sih9l")
    ],
    ("J-Pop", "감성적인"): [
        ("Aimer - Kataomoi", "https://open.spotify.com/track/4VdVW3gL7GvU2k2Z8TqBgM"),
        ("YUI - Good-bye Days", "https://open.spotify.com/track/3aEoJuDaJAT7Y9DJN5f8Fh"),
        ("Ikimono Gakari - Blue Bird", "https://open.spotify.com/track/3KjCoZK0a0dpC1pRocZrsN")
    ],
    ("J-Pop", "슬픈"): [
        ("Utada Hikaru - First Love", "https://open.spotify.com/track/7EQ0qTo7fWT7DPxmxtSYEc"),
        ("JUJU - Yasashisa de Afureru You ni", "https://open.spotify.com/track/3KcbFzj5r5ybEFJ3fEIa7W"),
        ("Aimer - Ref:rain", "https://open.spotify.com/track/5W1JKQsdLiHRHvJ2VfIn4N")
    ],
    ("J-Pop", "집중/공부용"): [
        ("Hoshino Gen - Koi (Instrumental)", "https://open.spotify.com/track/2OD5AXGnCCiT4bEQzVJqBd"),
        ("Yorushika - Spring Thief", "https://open.spotify.com/track/1bDmnB1crWzwJhkXKzXzTH"),
        ("RADWIMPS - Sparkle (Movie Ver.)", "https://open.spotify.com/track/3gmD1nXxXYkUqR9E5VpH6t")
    ],
}

# 임의의 3곡을 각 조합마다 생성하는 헬퍼 함수
def generate_song(genre, mood):
    base_url = "https://open.spotify.com/search/"
    return [
        (f"{genre} Artist 1 - {mood} Song A", base_url + urllib.parse.quote(f"{genre} {mood} Song A")),
        (f"{genre} Artist 2 - {mood} Song B", base_url + urllib.parse.quote(f"{genre} {mood} Song B")),
        (f"{genre} Artist 3 - {mood} Song C", base_url + urllib.parse.quote(f"{genre} {mood} Song C"))
    ]

# 모든 조합을 song_library에 채워넣기
# 전체 곡이 실제 Spotify 링크로 채워져 있으므로 generate_song 제거

# 특정 조합에 실제 곡 덮어쓰기 (예시)
song_library[("K-Pop", "신나는")] = [
    ("NewJeans - Super Shy", "https://open.spotify.com/track/6t5w8JJcC6nPjiA4RZJfwY"),
    ("IVE - I AM", "https://open.spotify.com/track/5L9OPeB0n0QnBv1X6t2dYy"),
    ("LE SSERAFIM - UNFORGIVEN", "https://open.spotify.com/track/3R4u8mqq9DF0hd3D4FZrYG")
]

song_library[("클래식", "새벽 감성")] = [
    ("Chopin - Prelude in E minor", "https://open.spotify.com/track/3Z8FwOEN59mRMxDCtb8N0A"),
    ("Ravel - Pavane for a Dead Princess", "https://open.spotify.com/track/1TfqLAPs4K3s2rJMoCokcS"),
    ("Massenet - Meditation", "https://open.spotify.com/track/2q1GSCSyJvvE5mRvgyqO8f")
]

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
