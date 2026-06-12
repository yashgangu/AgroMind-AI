import streamlit as st
import requests

from streamlit_js_eval import get_geolocation
from services.weather_service import get_weather_by_coordinates

from modules.translator import translate_text


def show_weather_page():

    # =====================================================
    # CUSTOM CSS
    # =====================================================

    st.markdown("""
    <style>

    .main {
        background-color: #f4fff7;
    }

    .weather-card {
        background: linear-gradient(135deg, #2d6a4f, #40916c);
        padding: 30px;
        border-radius: 22px;
        color: white;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }

    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        text-align: center;
    }

    .metric-title {
        font-size: 18px;
        color: #555;
    }

    .metric-value {
        font-size: 34px;
        font-weight: bold;
        color: #1b4332;
    }

    .insight-card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #1b4332;
        margin-bottom: 10px;
    }

    .location-card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(f"""
    <div class="weather-card">
        <h1>{translate_text("🌦 Smart Weather Monitoring Panel")}</h1>
        <p style="font-size:18px;">
            {translate_text("Real-time weather insights for smart farming and crop protection.")}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # GET USER LOCATION
    # =====================================================

    location = get_geolocation()

    if location is None:
        st.warning(translate_text("📍 Please allow browser location access."))
        st.stop()

    if "coords" not in location:
        st.info(translate_text("📍 Detecting your current location..."))
        st.stop()

    latitude = location["coords"]["latitude"]
    longitude = location["coords"]["longitude"]

    # =====================================================
    # GET CITY NAME
    # =====================================================

    city = "Unknown"
    state = ""
    country = ""

    try:
        headers = {
            "User-Agent": "AgroMindAI"
        }

        geo_url = (
            "https://nominatim.openstreetmap.org/reverse"
            f"?lat={latitude}"
            f"&lon={longitude}"
            f"&format=json"
        )

        response = requests.get(
            geo_url,
            headers=headers,
            timeout=10
        )

        geo_data = response.json()

        if "address" in geo_data:
            address = geo_data["address"]

            city = (
                address.get("city")
                or address.get("town")
                or address.get("village")
                or address.get("county")
                or "Unknown"
            )

            state = address.get("state", "")
            country = address.get("country", "")

    except Exception:
        pass

    # Translate regional location output values dynamically if applicable
    translated_city = translate_text(city)
    translated_state = translate_text(state)
    translated_country = translate_text(country)

    # =====================================================
    # LOCATION DISPLAY
    # =====================================================

    st.markdown(f"""
    <div class="location-card">
        <h3>{translate_text("📍 Current Location")}</h3>
        <p style="font-size:22px; color:#1b4332;">
            {translated_city}, {translated_state}, {translated_country}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # GET WEATHER DATA
    # =====================================================

    data = get_weather_by_coordinates(latitude, longitude)

    if "error" in data:
        st.error(translate_text(data["error"]))
        st.stop()

    temperature = data["temperature"]
    humidity = data["humidity"]
    wind_speed = data["wind_speed"]
    soil_temperature = data["soil_temperature"]
    soil_moisture = data["soil_moisture"]
    rain_probability = data["rain_probability"]

    # =====================================================
    # WEATHER METRICS
    # =====================================================

    st.markdown(
        f'<div class="section-title">{translate_text("🌤 Live Weather Conditions")}</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("🌡 Temperature")}</div>
            <div class="metric-value">{temperature}°C</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("💧 Humidity")}</div>
            <div class="metric-value">{humidity}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("🌬 Wind Speed")}</div>
            <div class="metric-value">{wind_speed} km/h</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("##")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("🌱 Soil Temperature")}</div>
            <div class="metric-value">{soil_temperature}°C</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("💦 Soil Moisture")}</div>
            <div class="metric-value">{soil_moisture}</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{translate_text("🌧 Rain Probability")}</div>
            <div class="metric-value">{rain_probability}%</div>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.markdown("##")

    st.markdown(
        f'<div class="section-title">{translate_text("🤖 AI Agricultural Insights")}</div>',
        unsafe_allow_html=True
    )

    insight_found = False

    if rain_probability > 70:
        st.warning(
            translate_text("🌧 Heavy rain expected. Delay pesticide spraying and harvesting.")
        )
        insight_found = True

    if humidity > 80:
        st.warning(
            translate_text("💧 High humidity may increase fungal disease risk.")
        )
        insight_found = True

    if temperature > 35:
        st.error(
            translate_text("🔥 High temperature detected. Increase irrigation frequency.")
        )
        insight_found = True

    if soil_moisture < 0.15:
        st.warning(
            translate_text("🌱 Soil moisture is low. Irrigation recommended.")
        )
        insight_found = True

    if not insight_found:
        st.success(
            translate_text("✅ Weather conditions are favorable for crop growth.")
        )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("##")

    st.caption(
        translate_text("Powered by Open-Meteo API • Real-time AI Smart Agriculture Monitoring")
    )
