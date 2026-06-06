# 🌱 AgroMind AI – Smart Agriculture Assistant

## 📌 Project Overview

AgroMind AI is an AI-powered agriculture assistant designed to help farmers detect crop diseases, receive personalized treatment recommendations, access weather insights, and interact with an intelligent farming chatbot.

The system combines Computer Vision, Generative AI, Weather Analytics, and Multilingual Support to assist farmers in making informed agricultural decisions.

---

## 🎯 Problem Statement

Farmers often face challenges such as:

* Identifying crop diseases accurately
* Choosing suitable fertilizers and pesticides
* Understanding weather impacts on crops
* Accessing expert agricultural guidance

AgroMind AI addresses these challenges through AI-driven crop analysis and recommendations.

---

## ✨ Features

### 🦠 Crop Disease Detection

* Upload crop leaf images
* AI-powered crop identification
* Detect crop type
* Identify crop diseases
* Display confidence score
* Analyze crop health

### 🤖 AI-Powered Farming Assistant

* Gemini AI integration
* Conversational crop diagnosis
* Dynamic follow-up questioning
* Personalized farming recommendations
* Context-aware conversations

### 🌦 Weather Forecast Module

* Current weather conditions
* Temperature monitoring
* Humidity tracking
* Rainfall prediction
* Farming weather insights

### 🌐 Multi-Language Support

Supports:

* English
* Hindi
* Marathi
* Gujarati
* Punjabi
* Bengali
* Tamil
* Telugu
* Kannada
* Malayalam

### 📄 PDF Report Generation

Generate downloadable crop analysis reports containing:

* Crop details
* Disease information
* Treatment recommendations
* Weather insights

### 📘 Interactive User Guide

Built-in multilingual help center for farmers.

---

## 🛠 Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Artificial Intelligence

* TensorFlow / Keras
* CNN Model
* Google Gemini AI

### APIs

* Weather API
* Google Translator API

### Libraries

* Streamlit
* TensorFlow
* Pillow
* NumPy
* Pandas
* Deep Translator
* Google Generative AI
* Requests

---

## 📂 Project Structure

```text
AgroMind-AI/
│
├── app.py
│
├── dataset/
│
├── models/
│   └── crop_disease_model.keras
│
├── modules/
│   ├── predict.py
│   ├── translator.py
│   ├── recommendation_engine.py
│   ├── conversation_agent.py
│   ├── chatbot.py
│   ├── memory_manager.py
│   ├── weather.py
│   └── help_page.py
│
├── services/
│   └── weather_service.py
│
├── Training/
│   └── train_model.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yashgangu/AgroMind-AI 

cd AgroMind-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
WEATHER_API_KEY=YOUR_WEATHER_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Workflow

1. Upload Crop Image
2. Ask Farming Question
3. AI Detects Crop and Disease
4. Follow-Up Questions Generated
5. Personalized Recommendations Generated
6. Download Report
7. Weather Insights Displayed
8. Use the AI Farming Chatbot for additional guidance
9. Help & User Guide

---

## 🎓 Academic Information

**Project Title:** AgroMind AI – Smart Agriculture Assistant

**Project Type:** Master's Final Year Project

**Domain:** Artificial Intelligence & Agriculture

---

## 🔮 Future Scope

* Voice-Based Farmer Interaction
* Real-Time Pest Detection
* Satellite-Based Crop Monitoring
* Fertilizer Prediction System
* Mobile Application Deployment
* IoT Sensor Integration

---

## 👨‍💻 Developed By

Yash Gangurde

Master's Final Year Project

---

## ⭐ AgroMind AI

Helping Farmers Make Better Decisions with Artificial Intelligence.
