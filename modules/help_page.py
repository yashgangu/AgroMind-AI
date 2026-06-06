import streamlit as st

def show_help_page(translate_text):

    st.title(translate_text("📘 AgroMind AI User Guide"))

    st.success(
        translate_text("🌱 Welcome to AgroMind AI! Follow the steps below to detect crop diseases, ")
        + translate_text("get personalized farming recommendations, check weather forecasts, and use the AI chatbot.")
    )

    st.markdown("---")

    # =====================================
    # CROP DISEASE DETECTION
    # =====================================

    with st.expander(translate_text("🦠 Crop Disease Detection"), expanded=True):

        st.markdown(translate_text("""
### Step 1: Select Image Source

Choose one option:

- 📁 Upload Crop Image from Gallery
- 📷 Capture Live Photo using Camera

### Step 2: Upload a Clear Crop Image

For best results:

✅ Use good lighting

✅ Capture affected leaves clearly

✅ Avoid blurry images

✅ Focus on damaged areas

### Step 3: Ask Your Farming Question

Examples:

- What disease is affecting my crop?
- Which fertilizer should I use?
- Recommend pesticide treatment
- How can I increase crop yield?
- Is irrigation required?

### Step 4: Click **Analyze Crop**

AgroMind AI will:

🔍 Identify Crop

🦠 Detect Disease

📊 Calculate Confidence Score

🌱 Analyze Crop Health

### Step 5: Answer Follow-Up Questions

You may be asked:

- Crop Age
- Irrigation Status
- Weather Conditions
- Symptom Severity
- Farming Practices

### Step 6: Receive AI Recommendations

You will receive:

✅ Disease Explanation

✅ Treatment Plan

✅ Fertilizer Suggestions

✅ Pesticide Recommendations

✅ Irrigation Advice

✅ Prevention Measures

✅ Yield Improvement Tips

### Step 7: Download Report

Click:

📥 **Download Report**

to save the analysis as PDF.
"""))  # <--- FIXED: Added the missing closing parenthesis here

    # =====================================
    # WEATHER
    # =====================================

    with st.expander(translate_text("🌦 Weather Forecast Module")):

        st.markdown(translate_text("""
Navigate to **Weather** section.

Features:

- 🌡 Current Temperature
- 💧 Humidity
- 🌧 Rain Forecast
- 🌦 Weather Conditions
- 🚜 Farming Weather Insights

💡 Always check weather before applying fertilizers or pesticides.
"""))

    # =====================================
    # CHATBOT
    # =====================================

    with st.expander(translate_text("🤖 AI Farming Chatbot")):

        st.markdown(translate_text("""
Navigate to **AI Chatbot** section.

Ask questions such as:

- Best fertilizer for tomato?
- How to prevent leaf curl disease?
- Organic farming techniques
- Pest management solutions
- Irrigation practices

The AI assistant provides instant farming guidance.
"""))

    # =====================================
    # LANGUAGES
    # =====================================

    with st.expander(translate_text("🌐 Multi-Language Support")):

        st.markdown(translate_text("""
Supported Languages:

- English
- Hindi
- Marathi
- Gujarati
- Punjabi
- Bengali
- Tamil
- Telugu
- Kannada
- Malayalam

Select your preferred language from the sidebar.
"""))

    # =====================================
    # TIPS
    # =====================================

    st.markdown("---")

    st.info(translate_text("""
### 💡 Tips for Best Results

✅ Upload high-quality crop images

✅ Answer follow-up questions accurately

✅ Check weather before spraying chemicals

✅ Download reports for future reference

✅ Use AI Chatbot for additional farming guidance
"""))

    st.success(
        translate_text("🌱 AgroMind AI – Your Smart Farming Companion\n\n")
        + translate_text("Helping Farmers Make Better Decisions with Artificial Intelligence.")
    )