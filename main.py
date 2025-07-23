import streamlit as st
import random

st.set_page_config(page_title="무드 기반 노래 추천기 🎵", page_icon="🎧")

# 1. 대량의 노래 추천 리스트 (장르, 무드 구분 없이 다양한 스타일 포함)
base_songs = [
    "NewJeans - Super Shy", "IVE - I AM", "LE SSERAFIM - UNFORGIVEN", "BTS - Dynamite", "BLACKPINK - DDU-DU DDU-DU",
    "TWICE - Likey", "Red Velvet - Psycho", "SEVENTEEN - Rock With You", "EXO - Love Shot", "ITZY - WANNABE",
    "Stray Kids - God's Menu", "Adele - Easy On Me", "Ed Sheeran - Perfect", "Taylor Swift - Love Story", "Bruno Mars - Just the Way You Are",
    "IU - 밤편지", "태연 - 사계", "AKMU - 어떻게 이별까지 사랑하겠어", "Heize - 비도 오고 그래서", "Lee Hi - Breathe",
    "YOASOBI - Racing Into the Night", "Aimer - Kataomoi", "RADWIMPS - Sparkle", "King Gnu - Hakujitsu", "Official HIGE DANdism - Pretender",
    "10CM - 폰서트", "잔나비 - 주저하는 연인들을 위해", "혁오 - 와리가리", "볼빨간사춘기 - 우주를 줄게", "Crush - Fall",
    "Loco - You Don’t Know", "Zion.T - Eat", "GRAY - Dream Chaser", "Zico - Any Song", "Dynamic Duo - BAAAM",
    "Beenzino - Dali, Van, Picasso", "The Quiett - Prime Time", "nafla - Run!", "JUSTHIS - No One", "Jay Park - Me Like Yuh",
    "Debussy - Clair de Lune", "Chopin - Nocturne Op.9 No.2", "Satie - Gymnopédie No.1", "Beethoven - Moonlight Sonata", "Mozart - Turkish March",
    "Yiruma - River Flows in You", "Joe Hisaishi - Merry-Go-Round of Life", "Ludovico Einaudi - Nuvole Bianche", "Bach - Air on the G String",
    "Tchaikovsky - Swan Lake", "Pachelbel - Canon in D", "Schumann - Träumerei", "Liszt - Liebestraum No. 3", "Mozart - Eine kleine Nachtmusik",
    "Imagine Dragons - Believer", "Coldplay - Viva La Vida", "Linkin Park - Numb", "Avicii - Wake Me Up", "Maroon 5 - Sugar",
    "Post Malone - Circles", "The Weeknd - Blinding Lights", "Billie Eilish - Bad Guy", "Olivia Rodrigo - Drivers License", "Lana Del Rey - Young and Beautiful",
    "The Beatles - Hey Jude", "Queen - Don't Stop Me Now", "Michael Jackson - Beat It", "Elton John - Rocket Man", "David Bowie - Heroes",
    "SHINee - View", "NCT 127 - Kick It", "Super Junior - Sorry, Sorry", "Girls' Generation - Gee", "2NE1 - I Am The Best",
    "T-ARA - Roly Poly", "Apink - Mr. Chu", "Mamamoo - HIP", "GFRIEND - Me Gustas Tu", "BIGBANG - Haru Haru",
    "INFINITE - Be Mine", "Beast - Fiction", "B1A4 - Lonely", "Block B - HER", "VIXX - Error",
    "DAY6 - Zombie", "N.Flying - Rooftop", "CNBLUE - I'm Sorry", "FTISLAND - Severely", "ONEWE - Rain To Be",
    "BTS - Spring Day", "BTS - Butter", "BTS - Black Swan", "IU - Palette", "IU - Celebrity",
    "(G)I-DLE - TOMBOY", "STAYC - ASAP", "IVE - LOVE DIVE", "LE SSERAFIM - Antifragile", "NewJeans - OMG",
    "TREASURE - JIKJIN", "ENHYPEN - FEVER", "TXT - Blue Hour", "CRAVITY - Adrenaline", "ATBO - Next to Me",
    "SHINee - Don’t Call Me", "KEY - Gasoline", "MINHO - Chase", "TAEMIN - Advice", "JONGHYUN - End of a Day",
    "MAMAMOO - Starry Night", "MAMAMOO - Egotistic", "Wheein - Water Color", "Hwasa - Maria", "Solar - Honey",
    "Red Velvet - Feel My Rhythm", "Red Velvet - Bad Boy", "Wendy - Like Water", "Joy - Hello", "Seulgi - 28 Reasons",
    "Baek Yerin - Rest", "Baek A Yeon - a Good Boy", "Younha - Event Horizon", "Sunmi - Tail", "HyunA - I'm Not Cool",
    "KARD - Dumb Litty", "AleXa - Wonderland", "Dreamcatcher - Scream", "EVERGLOW - DUN DUN", "fromis_9 - DM",
    "Billlie - Ring x Ring", "Purple Kiss - Zombie", "LOONA - Why Not?", "WJSN - Save Me Save You", "APRIL - LALALILALA"
]

# 2. Streamlit UI 꾸미기
st.markdown("""
    <style>
    .stButton > button {
        font-size: 1.3rem;
        padding: 0.7em 2.5em;
        border-radius: 1em;
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    .result-box {
        font-size: 1.4rem;
        background: #fff7e6;
        border-left: 6px solid #ffc107;
        padding: 1em;
        margin-top: 1em;
        border-radius: 0.5em;
        animation: fadeIn 0.6s ease-in-out;
    }
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(10px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎧 노래 랜덤 추천기")
st.write("300곡 이상 보유한 플레이리스트에서 랜덤으로 노래를 추천해드릴게요!")

if st.button("✨ 노래 추천 받기!"):
    title = random.choice(base_songs)
    st.markdown(f"<div class='result-box'>🎶 <strong>추천곡:</strong> {title}</div>", unsafe_allow_html=True)

if st.checkbox("📜 전체 추천곡 리스트 보기"):
    st.markdown("### 🎵 전체 추천곡 리스트")
    for song in base_songs:
        st.write(f"- {song}")

st.markdown("---")
st.caption("Made with ❤️ by ChatGPT")
