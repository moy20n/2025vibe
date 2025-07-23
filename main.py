import streamlit as st
import random

st.set_page_config(page_title="무드 기반 노래 추천기 🎵", page_icon="🎧")

# 1. 장르 및 공통 무드 목록
genres = ["🎤 K-Pop", "🎸 락발라드", "🎻 클래식", "🎌 J-Pop", "🎧 팝", "🌿 인디", "🔥 힙합"]
clean_genres = {g: g.split(" ")[1] for g in genres}

common_moods = [
    "🎉 신나는",
    "🌙 감성적인",
    "😭 슬픈",
    "📚 집중/공부용",
    "🌌 새벽 감성",
    "💘 사랑에 빠진 느낌",
    "🚗 드라이브용",
    "🧘 혼자 듣기 좋은"
]
clean_moods = {m: m.split(" ")[1] for m in common_moods}

# 2. 노래 제목 데이터 (전체 장르 복원 포함)
def full_recommendations():
    return {
        "K-Pop": {
            "신나는": ["NewJeans - Super Shy", "IVE - I AM", "LE SSERAFIM - UNFORGIVEN"],
            "감성적인": ["BTS - Spring Day", "태연 - 사계", "AKMU - 어떻게 이별까지 사랑하겠어"],
            "슬픈": ["EXO - Miracles in December", "Wendy - When This Rain Stops", "G-Dragon - Untitled, 2014"],
            "집중/공부용": ["BLACKPINK - Stay (Acoustic Ver.)", "BTS - Butterfly", "IU - 밤편지"],
            "새벽 감성": ["Heize - 밤하늘의 별을", "Crush - Fall", "Baek Yerin - Square (2017)"],
            "사랑에 빠진 느낌": ["TWICE - What is Love?", "Red Velvet - Would U", "SEVENTEEN - Pretty U"],
            "드라이브용": ["STAYC - ASAP", "BIGBANG - BANG BANG BANG", "Kep1er - WA DA DA"],
            "혼자 듣기 좋은": ["IU - 무릎", "Jung Seung Hwan - The Snowman", "Lee Hi - Breathe"]
        },
        "락발라드": {
            "신나는": ["YB - 나는 나비", "부활 - 비와 당신", "이승철 - 소녀시대"],
            "감성적인": ["임재범 - 너를 위해", "이수 - My Way", "김범수 - 보고 싶다"],
            "슬픈": ["김경호 - 금지된 사랑", "이승철 - 그런 사람 또 없습니다", "이수영 - 휠릴리"],
            "집중/공부용": ["YB - 흰수염고래 (Inst.)", "부활 - 아름다운 사실", "김경호 - 금지된 사랑 (Inst.)"],
            "새벽 감성": ["임창정 - 소주 한잔", "이승환 - 어떻게 사랑이 그래요", "김동률 - 감사"],
            "사랑에 빠진 느낌": ["부활 - 사랑할수록", "더 크로스 - Don't Cry", "이승환 - 화려하지 않은 고백"],
            "드라이브용": ["윤도현 - 사랑했나봐", "이승철 - 그런 사람 또 없습니다", "Nell - Time walking on memory"],
            "혼자 듣기 좋은": ["박효신 - 야생화", "이수 - 내 생에 아름다운", "성시경 - 거리에서"]
        },
        "클래식": {
            "신나는": ["Mozart - Turkish March", "Rossini - William Tell Overture", "Beethoven - Symphony No.5"],
            "감성적인": ["Debussy - Clair de Lune", "Chopin - Nocturne Op.9 No.2", "Satie - Gymnopédie No.1"],
            "슬픈": ["Albinoni - Adagio", "Beethoven - Moonlight Sonata", "Tchaikovsky - Swan Lake"],
            "집중/공부용": ["Bach - Prelude in C Major", "Mozart - Piano Sonata No.16", "Beethoven - Für Elise"],
            "새벽 감성": ["Chopin - Prelude in E minor", "Ravel - Pavane", "Massenet - Meditation"],
            "사랑에 빠진 느낌": ["Pachelbel - Canon in D", "Schumann - Träumerei", "Liszt - Liebestraum No.3"],
            "드라이브용": ["Mozart - Eine kleine Nachtmusik", "Vivaldi - Spring", "Beethoven - Symphony No.7 II"],
            "혼자 듣기 좋은": ["Dvorak - Songs My Mother Taught Me", "Chopin - Nocturne Op.27 No.2", "Brahms - Intermezzo"]
        },
        "J-Pop": {
            "신나는": ["YOASOBI - Idol", "King & Prince - Cinderella Girl", "Aimer - Brave Shine"],
            "감성적인": ["Aimer - Kataomoi", "YOASOBI - Yoru ni Kakeru", "RADWIMPS - Sparkle"],
            "슬픈": ["YUI - Goodbye Days", "Utada Hikaru - First Love", "Ikimono Gakari - Blue Bird"],
            "집중/공부용": ["Joe Hisaishi - Summer", "RADWIMPS - Nandemonaiya", "Sakanaction - Shinunoga E-Wa"],
            "새벽 감성": ["King Gnu - Hakujitsu", "Aimer - Ref:rain", "Official HIGE DANdism - Pretender"],
            "사랑에 빠진 느낌": ["Ikimono Gakari - Kaze wa Fuiteiru", "Spitz - Cherry", "Aimyon - Marigold"],
            "드라이브용": ["YOASOBI - Racing into the Night", "Official HIGE DANdism - Cry Baby", "Aimer - STAND-ALONE"],
            "혼자 듣기 좋은": ["Yorushika - Say It", "Eve - Dramaturgy", "Zutomayo - Study Me"]
        },
        "팝": {
            "신나는": ["Taylor Swift - Shake It Off", "Katy Perry - Roar", "Pharrell Williams - Happy"],
            "감성적인": ["Adele - Easy On Me", "Ed Sheeran - Perfect", "Billie Eilish - Everything I Wanted"],
            "슬픈": ["Sam Smith - Too Good at Goodbyes", "Lewis Capaldi - Someone You Loved", "Sia - Breathe Me"],
            "집중/공부용": ["Ludovico Einaudi - Nuvole Bianche", "Yiruma - River Flows in You", "James Blake - Retrograde"],
            "새벽 감성": ["Lana Del Rey - Young and Beautiful", "Troye Sivan - FOOLS", "Norah Jones - Don't Know Why"],
            "사랑에 빠진 느낌": ["Bruno Mars - Just the Way You Are", "Ariana Grande - Into You", "Shawn Mendes - There's Nothing Holdin' Me Back"],
            "드라이브용": ["Dua Lipa - Levitating", "The Weeknd - Blinding Lights", "Miley Cyrus - Party In The USA"],
            "혼자 듣기 좋은": ["Olivia Rodrigo - Drivers License", "Billie Eilish - idontwannabeyouanymore", "Adele - All I Ask"]
        },
        "인디": {
            "신나는": ["잔나비 - 주저하는 연인들을 위해", "혁오 - TOMBOY", "The Black Skirts - Everything"],
            "감성적인": ["볼빨간사춘기 - 우주를 줄게", "10CM - 폰서트", "스탠딩 에그 - 오래된 노래"],
            "슬픈": ["짙은 - 안녕", "소란 - 너를 공부해", "이진아 - 냠냠냠 (어쿠스틱)"],
            "집중/공부용": ["윤하 - 오르트구름 (Acoustic Ver.)", "로이킴 - 그때 헤어지면 돼", "정준일 - 안아줘 (Inst.)"],
            "새벽 감성": ["검정치마 - 기다린 만큼 더", "스무살 - 걱정말아요 그대", "치즈 - Mood Indigo"],
            "사랑에 빠진 느낌": ["10CM - 사랑은 은하수 다방에서", "치즈 - 좋아해", "스텔라장 - 아름다워"],
            "드라이브용": ["혁오 - 와리가리", "ADOY - Wonder", "잔나비 - 알록달록"],
            "혼자 듣기 좋은": ["선우정아 - 도망가자", "정은지 - 너란 봄", "이하이 - 홀로"]
        },
        "힙합": {
            "신나는": ["Dynamic Duo - BAAAM", "Zico - Any Song", "Simon Dominic - Make Her Dance"],
            "감성적인": ["BewhY - Adaptation", "Crush - Sometimes", "E SENS - The Anecdote"],
            "슬픈": ["Beenzino - Break", "염따 - 벚꽃이 피면", "pH-1 - Like Me"],
            "집중/공부용": ["Jay Park - All I Wanna Do (Lo-fi Ver.)", "Crucial Star - Flat Shoes", "Loopy - About Time (Inst.)"],
            "새벽 감성": ["JUSTHIS - No One", "Kid Milli - WHY DO...", "GroovyRoom - Sunday"],
            "사랑에 빠진 느낌": ["Loco - You Don’t Know", "Gray - Dream Chaser", "Zion.T - Eat"],
            "드라이브용": ["Jay Park - Me Like Yuh", "Zico - Artist", "Leellamarz - Trip"],
            "혼자 듣기 좋은": ["The Quiett - Prime Time", "nafla - Run!", "Paloalto - Good Times"]
        }
    }

# 전체 recommendation 등록
song_library = {}
for genre, moods in full_recommendations().items():
    for mood, songs in moods.items():
        song_library[(genre, mood)] = songs

# 3. Streamlit UI 꾸미기
st.markdown("""
    <style>
    .stButton > button {
        font-size: 1.2rem;
        padding: 0.5em 2em;
        border-radius: 0.5em;
        background-color: #ffccf9;
        color: #333;
        border: none;
    }
    .stRadio > div {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎧 무드 기반 노래 추천기")
st.write("장르와 무드를 선택하면 어울리는 노래를 🎵 추천해드릴게요!")

sel_genre = st.selectbox("🎼 장르를 선택하세요", genres)
sel_mood = st.radio("🧠 기분/상황을 선택하세요", common_moods)

genre = clean_genres[sel_genre]
mood = clean_moods[sel_mood]

if st.button("✨ 노래 추천 받기!"):
    key = (genre, mood)
    songs = song_library.get(key, [])
    title = random.choice(songs) if songs else "추천곡이 없습니다."
    st.success(f"🎶 **추천곡:** {title}")

st.markdown("---")
st.caption("Made with ❤️ by ChatGPT")
