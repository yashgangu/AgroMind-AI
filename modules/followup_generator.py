# modules/followup_generator.py

import json
import re

def parse_ai_json(text):

    try:

        # Remove markdown blocks

        text = text.replace("```json", "")
        text = text.replace("```", "")

        # Extract JSON object

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:
            text = match.group()

        data = json.loads(text)

        return {
            "need_followup": data.get(
                "need_followup",
                True
            ),
            "question": data.get(
                "question",
                ""
            ),
            "options": data.get(
                "options",
                []
            )
        }

    except Exception as e:

        print(
            "JSON Parse Error:",
            e
        )

        print(
            "Raw Gemini Response:",
            text
        )

        return {
            "need_followup": True,
            "question": "Could you provide more details about the crop condition?",
            "options": [
                "Leaves affected",
                "Stem affected",
                "Fruit affected",
                "Whole plant affected"
            ]
        }