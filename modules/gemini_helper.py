import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def analyze_farmer_query(
        crop,
        disease,
        confidence,
        farmer_question,
        memory
):
    """
    Determines whether more information is needed
    before generating a recommendation.
    """

    prompt = f"""
You are an expert Agriculture AI Assistant.

Crop:
{crop}

Detected Disease:
{disease}

Confidence:
{confidence}

Farmer Question:
{farmer_question}

Previous Context:
{memory}

Your task:

1. Understand the farmer's question.
2. Decide if enough information exists.
3. If information is missing:
   Ask ONLY ONE follow-up question.
4. Provide 4 possible options.
5. Allow custom answer.

Return ONLY valid JSON.

Example:

{{
    "need_followup": true,
    "question": "What is the age of the crop?",
    "options": [
        "0-30 days",
        "30-60 days",
        "60-90 days",
        "90+ days"
    ]
}}

OR

{{
    "need_followup": false,
    "question": "",
    "options": []
}}

Return JSON only.
"""

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)

    except Exception:

        return {
            "need_followup": False,
            "question": "",
            "options": []
        }


def generate_final_recommendation(
        crop,
        disease,
        confidence,
        farmer_question,
        memory
):
    """
    Generates final answer after enough
    information is collected.
    """

    prompt = f"""
You are an expert Agriculture Consultant.

Crop:
{crop}

Detected Disease:
{disease}

Confidence:
{confidence}

Farmer Question:
{farmer_question}

Collected Information:
{memory}

Generate a complete recommendation.

Include only relevant information.

If farmer asks:

Disease →
Explain disease.

Fertilizer →
Recommend fertilizer.

Pesticide →
Recommend pesticide.

Yield →
Suggest yield improvement.

Irrigation →
Suggest irrigation schedule.

Response format:

Disease:
Cause:
Treatment:
Fertilizer:
Pesticide:
Prevention:
Irrigation:
Additional Advice:

Keep answer practical and farmer friendly.
"""

    response = model.generate_content(prompt)

    return response.text