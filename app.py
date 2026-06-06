import streamlit as st
from modules.memory_manager import ConversationMemory

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "followup_step" not in st.session_state:
    st.session_state.followup_step = 0

if "followup_answers" not in st.session_state:
    st.session_state.followup_answers = {}

if "original_question" not in st.session_state:
    st.session_state.original_question = ""

if "crop" not in st.session_state:
    st.session_state.crop = ""

if "disease" not in st.session_state:
    st.session_state.disease = ""

if "current_question" not in st.session_state:
    st.session_state.current_question = {}

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "final_recommendation" not in st.session_state:
    st.session_state.final_recommendation = None


# =========================================================
# MULTI LANGUAGE SUPPORT
# =========================================================

from deep_translator import GoogleTranslator

# LANGUAGE SELECTOR
language = st.sidebar.selectbox(
    "🌐 Select Language",
    [
        "English",
        "Hindi",
        "Marathi",
        "Gujarati",
        "Punjabi",
        "Bengali",
        "Tamil",
        "Telugu",
        "Kannada",
        "Malayalam"
    ],
    key="main_dashboard_language_key"
)
# 2. Save it to session state immediately for external pages 
st.session_state.selected_language = language

# 3. Import translate_text from your new independent tracking file
from modules.translator import translate_text
 
# LANGUAGE MAP

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml"
}

# # TRANSLATION FUNCTION

# def translate_text(text):
#     if language == "English" or not text:
#         return text
    
#     try:
#         return GoogleTranslator(
#             source='auto',
#             target=lang_map[language]
#         ).translate(text)
#     except:
#         return text

from PIL import Image
import tempfile
from modules.help_page import show_help_page
from modules.chatbot import format_ai_response
from modules.predict import predict_disease
from modules.weather import show_weather_page


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from modules.conversation_agent import (
    analyze_farmer_query
)

from modules.followup_generator import (
    parse_ai_json
)

from modules.recommendation_engine import (
    generate_final_recommendation
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AgroMind AI",
    page_icon="🌱",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #f4fff7;
}
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #d1fae5;
}
.hero-section {
    background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
    url("https://img.magnific.com/free-photo/agriculture-iot-with-rice-field-background_53876-124635.jpg?semt=ais_hybrid&w=740&q=80");
    background-size: cover;
    background-position: center;
    padding: 90px;
    border-radius: 28px;
    text-align: center;
    color: white;
    margin-bottom: 35px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.18);
}
.main-title {
    font-size: 58px;
    font-weight: bold;
    color: white;
    margin-bottom: 15px;
}
.metric-card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    border: 1px solid #dcfce7;
}
.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton > button:hover {
    transform: scale(1.03);
    background: #15803d;
}
.sidebar-title {
    font-size: 32px;
    font-weight: bold;
    color: #16a34a;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.markdown(
    '<div class="sidebar-title">🌱 AgroMind AI</div>',
    unsafe_allow_html=True
)

# Translate the navigation names so the sidebar matches selection
nav_dashboard = translate_text("🏠 Dashboard")
nav_disease = translate_text("🦠 Disease Detection")
nav_weather = translate_text("🌦 Weather")
nav_chatbot = translate_text("🤖 AI Chatbot")
nav_help = translate_text("📘 Help")

page_translated = st.sidebar.radio(
    translate_text("Navigation"),
    [nav_dashboard, nav_disease, nav_weather, nav_chatbot, nav_help]
)

# =========================================================
# SIDEBAR IMAGE & SUPPORT
# =========================================================

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.sidebar.columns([1,3,1])

with col2:
    st.image("assets/logo.png", width=220)

st.sidebar.markdown(f"""
<div style="background:white; padding:10px; border-radius:10px; text-align:center; margin-top:15px; box-shadow:0 2px 8px rgba(0,0,0,0.06); font-size:13px;">
    <div style="font-size:14px; font-weight:600; margin-bottom:10px; color:#2e7d32;">
        {translate_text('Need help with plant care? 🌱')}
    </div>
    <button style="background:#2e7d32; color:white; border:none; padding:7px 14px; border-radius:8px; font-size:12px; font-weight:bold; cursor:pointer;">
        {translate_text('Contact Support')}
    </button>
</div>
""", unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================

if page_translated == nav_dashboard:

    st.markdown(f"""
    <div class="hero-section">
        <div class="main-title">
            {translate_text('🌱 Smart Agriculture Solutions')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{translate_text('🌿 Total Scans')}</h2>
            <h1>1,245</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{translate_text('📈 Accuracy')}</h2>
            <h1>98.5%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{translate_text('👨‍🌾 Farmers Helped')}</h2>
            <h1>526</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("##")

    st.success(translate_text(
        "AgroMind AI helps farmers detect crop diseases instantly using Artificial Intelligence and provides smart farming recommendations."
    ))
    
    st.markdown("<div style='margin-top:-25px;'></div>", unsafe_allow_html=True)

    left_space, main_image, right_space = st.columns([0.2, 9.6, 0.2])
    with main_image:
        st.image("assets/bottom_image.png", width=900)
    
# =========================================================
# DISEASE DETECTION
# =========================================================

elif page_translated == nav_disease:

    st.title(
        translate_text("🦠 Smart Crop Assistant")
    )

    input_method = st.radio(
        translate_text("📸 Choose Image Source:"),
        [translate_text("📁 Upload from Gallery"), translate_text("📷 Take a Photo")],
        horizontal=True
    )

    uploaded_file = None

    if input_method == translate_text("📁 Upload from Gallery"):
        uploaded_file = st.file_uploader(
            translate_text("Upload Crop Leaf Image"),
            type=["jpg", "jpeg", "png"]
        )
    else:
        uploaded_file = st.camera_input(
            translate_text("Capture Crop Leaf Image")
        )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                image,
                caption=translate_text("Uploaded Crop Image"),
                width="stretch"
            )

        with col2:
            # Only show inputs if final recommendation hasn't been rendered yet
            if not st.session_state.final_recommendation:
                st.success(
                    translate_text("✓ Image ready for analysis")
                )

                
                farmer_question = st.text_area(
                    translate_text("❓ Ask anything about your crop"),
                    placeholder=translate_text(
                        "Examples:\n• What disease is this?\n• Suggest fertilizer.\n• Recommend pesticide.\n• How can I increase yield?\n• Is irrigation needed?\n• What precautions should I take?"
                    ),
                    height=180
                )

                analyze_btn = st.button(
                    translate_text("🔍 Analyze Crop"),
                    use_container_width=True
                )
            else:
                st.info(translate_text("📋 Analysis for this crop is displayed below."))

        if not st.session_state.final_recommendation and 'analyze_btn' in locals() and analyze_btn:

            if not farmer_question.strip():
                st.warning(
                    translate_text("Please ask a question.")
                )
            else:
                with st.spinner(translate_text("Analyzing crop...")):
                    crop, disease, confidence = predict_disease(image)
                    st.session_state.crop = crop
                    st.session_state.disease = disease
                    st.session_state.original_question = farmer_question

                st.success(translate_text("Analysis Completed"))
                st.markdown("---")

                st.subheader(translate_text("🌿 Detection Results"))

                m1, m2, m3 = st.columns(3)
                with m1:
                    st.metric(translate_text("Crop"), translate_text(crop))
                with m2:
                    st.metric(translate_text("Disease"), translate_text(disease))
                with m3:
                    st.metric(translate_text("Confidence"), f"{confidence*100:.2f}%")

                st.markdown("---")

                response = analyze_farmer_query(
                    crop,
                    disease,
                    st.session_state.original_question,
                    {},
                    language
                )

                result = parse_ai_json(response)

                st.session_state.current_question = result
                st.session_state.analysis_done = True
                st.session_state.followup_step = 1
                st.session_state.followup_answers = {}
                st.session_state.confidence = confidence

                st.rerun()

    # =====================================================
    # FOLLOWUP QUESTION FLOW
    # =====================================================

    if st.session_state.analysis_done:

        current = st.session_state.current_question

        if st.session_state.followup_step <= 3:

            st.markdown("---")

            st.subheader(
                f"{translate_text('🤖 Question')} {st.session_state.followup_step}"
            )

            # Translate dynamic questions coming from AI
            st.info(
                translate_text(current["question"])
            )

            selected_option = None

            if len(current["options"]) > 0:
                # Translate predefined options dynamically
                translated_options = [translate_text(opt) for opt in current["options"]]
                selected_option = st.radio(
                    translate_text("Select an option"),
                    translated_options,
                    key=f"q_{st.session_state.followup_step}"
                )

            custom_answer = st.text_input(
                translate_text("Or write your own answer"),
                key=f"custom_{st.session_state.followup_step}"
            )

            if st.button(translate_text("Next")):

                answer = (
                    custom_answer.strip()
                    if custom_answer.strip()
                    else selected_option
                )

                st.session_state.followup_answers[
                    current["question"]
                ] = answer

                if st.session_state.followup_step >= 3:

                    with st.spinner(translate_text("Generating AI Recommendation...")):
                        recommendation = (
                            generate_final_recommendation(
                                st.session_state.crop,
                                st.session_state.disease,
                                st.session_state.original_question,
                                st.session_state.followup_answers,
                                language
                            )
                        )
                        # Translate the final comprehensive recommendation response
                        st.session_state.final_recommendation = recommendation
                        st.session_state.analysis_done = False
                        st.rerun()

                else:

                    next_question = analyze_farmer_query(
                        st.session_state.crop,
                        st.session_state.disease,
                        st.session_state.original_question,
                        st.session_state.followup_answers,
                        language
                    )

                    st.session_state.current_question = parse_ai_json(next_question)
                    st.session_state.followup_step += 1
                    st.rerun()

    # =====================================================
    # FINAL RECOMMENDATION
    # =====================================================

    if st.session_state.final_recommendation:

        st.markdown("---")

        st.subheader(
            translate_text("🌾 Final AI Recommendation")
        )

        st.success(
            st.session_state.final_recommendation
        )

        # =====================================
        # PDF REPORT
        # =====================================
        # 1. Define a cached generator function inside or above the block
        @st.cache_data(show_spinner=False)
        def generate_pdf_bytes(crop, disease, confidence, question, recommendation):
            import io
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            # Style tuning for clean formatting
            story.append(Paragraph("<b>AgroMind AI Diagnostic Report</b>", styles["Title"]))
            story.append(Spacer(1, 25))
            story.append(Paragraph(f"<b>Crop:</b> {crop}", styles["BodyText"]))
            story.append(Paragraph(f"<b>Disease Diagnosis:</b> {disease}", styles["BodyText"]))
            story.append(Paragraph(f"<b>Confidence Level:</b> {confidence*100:.2f}%", styles["BodyText"]))
            story.append(Spacer(1, 12))
            story.append(Paragraph(f"<b>Farmer Query:</b> {question}", styles["BodyText"]))
            story.append(Spacer(1, 15))
            story.append(Paragraph("<b>AI Recommendations & Treatment Plan:</b>", styles["Heading3"]))
            story.append(Spacer(1, 8))
            
            # Clean up newlines for ReportLab paragraph compatibility
            clean_rec = recommendation.replace("\n", "<br/>")
            story.append(Paragraph(clean_rec, styles["BodyText"]))

            doc.build(story)
            buffer.seek(0)
            return buffer.getvalue()

        # 2. Safely call the generator function with existing session state values
        try:
            pdf_data = generate_pdf_bytes(
                st.session_state.crop,
                st.session_state.disease,
                st.session_state.confidence,
                st.session_state.original_question,
                st.session_state.final_recommendation
            )

            # 3. Pass the data variable directly to the button
            st.download_button(
                label=translate_text("📥 Download Complete Report"),
                data=pdf_data,
                file_name=f"AgroMind_{st.session_state.crop.replace(' ', '_')}_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as pdf_error:
            st.error(f"Error compiling report data: {pdf_error}")
        if st.button(translate_text("Start New Analysis")):
            st.session_state.followup_step = 0
            st.session_state.followup_answers = {}
            st.session_state.current_question = {}
            st.session_state.analysis_done = False
            st.session_state.final_recommendation = None
            st.rerun()
                     
# =========================================================
# WEATHER
# =========================================================

elif page_translated == nav_weather:
    show_weather_page()

# =========================================================
# CHATBOT
# =========================================================

elif page_translated == nav_chatbot:

    st.title(
        translate_text("🤖 AgroMind AI Chatbot")
    )

    question = st.text_input(
        translate_text("Ask farming-related questions")
    )

    if st.button(translate_text("Ask AI")):

        if question.strip():
            with st.spinner(translate_text("🤖 Thinking...")):
                try:
                    from modules.chatbot import ask_ai

                    response = ask_ai(question)
                    response = translate_text(response)

                    st.markdown("""
                    <style>
                    .chatbot-response {
                        background: white;
                        padding: 25px;
                        border-radius: 18px;
                        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
                        border-left: 6px solid #16a34a;
                        margin-top: 20px;
                        color: #334155;
                        font-size: 18px;
                        line-height: 1.8;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    formatted_response = format_ai_response(response)

                    st.markdown(f"""
                    <div class="chatbot-response">
                        <h3>{translate_text('🌾 AI Response')}</h3>
                        {formatted_response}
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning(translate_text("Please enter a question."))

# =========================================================
# HELP
# =========================================================
elif page_translated == nav_help:
    show_help_page(translate_text)