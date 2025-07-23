import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# 요금 계산 함수 (전국 공통 기준)
def calculate_fare(distance_km):
    base_fare = 4800        # 기본요금 (2km까지)
    base_distance = 2       # km
    per_100m_price = 100    # 100m당 요금

    if distance_km <= base_distance:
        return base_fare
    else:
        extra_distance_m = (distance_km - base_distance) * 1000
        extra_price = int(extra_distance_m // 100) * per_100m_price
        return base_fare + extra_price

# 주소 → 위경도 변환 함수
def geocode_address(address):
    geolocator = Nominatim(user_agent="taxi_fare_app")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude) if location else None

# 지도에 출발지-도착지 경로 시각화
def plot_route(start_coords, end_coords):
    m = folium.Map(location=start_coords, zoom_start=13)
    folium.Marker(start_coords, tooltip="출발지", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(end_coords, tooltip="도착지", icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine([start_coords, end_coords], color="blue", weight=3).add_to(m)
    return m

# Streamlit UI
st.title("🚕 전국 택시 요금 예측 앱")
st.markdown("출발지와 목적지를 입력하면 예상 택시요금과 경로를 알려드립니다.")

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    start_address = st.text_input("출발지 주소", placeholder="예: 서울특별시 강남구 삼성동")
with col2:
    end_address = st.text_input("목적지 주소", placeholder="예: 부산광역시 해운대구")

# 버튼으로 예측 실행
if st.button("🚖 요금 예측하기") and start_address and end_address:
    start_coords = geocode_address(start_address)
    end_coords = geocode_address(end_address)

    if start_coords and end_coords:
        distance = geodesic(start_coords, end_coords).km
        fare = calculate_fare(distance)

        st.success(f"📏 예상 거리: **{distance:.2f} km**")
        st.success(f"💰 예상 요금: **{fare:,} 원**")

        map_obj = plot_route(start_coords, end_coords)
        st_folium(map_obj, width=700)
    else:
        st.error("❌ 주소를 찾을 수 없습니다. 정확한 도로명 주소 또는 지명을 입력해주세요.")
