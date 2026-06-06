# modules/conversation_agent.py

import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_farmer_query(
        crop,
        disease,
        original_question,
        followup_answers,
        language):

    question_count = len(followup_answers)

    prompt = f"""
You are an expert agriculture consultant.

Generate question and options in:
{language}

Crop:
{crop}

Disease:
{disease}

Farmer Question:
{original_question}

Previous Follow-up Answers:
{followup_answers}

Questions Already Asked:
{question_count}

Your task:

Generate ONLY ONE new follow-up question.

Rules:

1. Ask exactly ONE question.
2. Question must help diagnose the problem better.
3. Question must depend on previous answers.
4. Never repeat a previous question.
5. Provide exactly 4 answer options.
6. Farmer may type a custom answer.
7. Return ONLY valid JSON.
8. Do not add explanation.
9. Do not use markdown.

Return:

{{
    "need_followup": true,
    "question": "your question",
    "options": [
        "option1",
        "option2",
        "option3",
        "option4"
    ]
}}
"""

    response = model.generate_content(prompt)

    return response.text