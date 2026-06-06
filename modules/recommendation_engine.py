# modules/recommendation_engine.py

import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_final_recommendation(
        crop,
        disease,
        farmer_question,
        farmer_answers,
        language):

    try:

        answers_text = ""

        for question, answer in farmer_answers.items():

            answers_text += (
                f"\nQuestion: {question}"
                f"\nAnswer: {answer}\n"
            )

        prompt = f"""
You are a Senior Agriculture Consultant.

Generate the entire report in:

Language = {language}

IMPORTANT:
Return 100% of the report in this language.
Do not mix English and any other language.

Crop:
{crop}

Disease:
{disease}

Farmer Original Question:
{farmer_question}

Follow-up Answers:
{answers_text}

Generate a COMPLETE recommendation report.

Include:

# Disease Analysis

# Severity Assessment

# Root Cause

# Fertilizer Recommendation

- Product
- Dosage
- Application Method

# Fungicide / Pesticide Recommendation

- Product
- Dosage
- Spray Frequency

# Irrigation Advice

# Prevention Measures

# Recovery Timeline

# Additional Expert Tips

Use the farmer's answers while generating recommendations.

Provide detailed practical advice.

Do not give generic suggestions.
"""

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:

            return response.text

        return """
Unable to generate recommendation.

Please try again.
"""

    except Exception as e:

        return f"""
Recommendation generation failed.

Error:
{str(e)}
"""