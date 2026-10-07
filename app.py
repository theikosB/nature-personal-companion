from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import errors
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    environment = data["environment"]
    time = data["time"]
    mood = data["mood"]
    company = data["company"]

    prompt = f"""
You are the AI behind "Nature's Personal Companion", a small outdoor
adventure game.

Your job is to create a short, interesting real-world field assignment
based on the user's situation.

USER SITUATION:
- Environment: {environment}
- Time available: {time}
- Mood: {mood}
- Company: {company}

Create a field assignment that makes the user pay attention to and interact
with their surroundings.

The assignment should:
- Feel like a small adventure, not a generic list of things to do.
- Be achievable within the available time.
- Suit the user's mood and whether they are alone or with others.
- Use things the user can reasonably find in the specified environment.
- Encourage observation, movement, curiosity, or interaction with surroundings.
- Require little or no technology once the mission begins.

SAFETY RULES:
- Never ask the user to enter dangerous, restricted, or isolated places.
- Never ask them to approach strangers.
- Never ask them to touch unknown plants, animals, insects, or objects.
- Never require crossing roads unsafely.
- Never require spending money.
- Never require identifying a species with certainty.
- Keep the activity within the general area the user described.

Return ONLY valid JSON in exactly this structure:

{{
    "persona": "A memorable role the user will play",
    "mission_title": "A short, fun title",
    "mission": "A 1-2 sentence description of the mission",
    "objectives": [
        "First objective",
        "Second objective",
        "Third objective",
        "Fourth objective"
    ],
    "special_rule": "One interesting constraint for the mission",
    "completion": "A clear description of when the mission is complete"
}}
"""

    try:
        response = client.models.generate_content(
            model="gemma-4-26b-a4b-it",
            contents=prompt
        )

        return jsonify({
            "result": response.text
        })

    except errors.APIError as e:
        return jsonify({
            "error": f"AI service error: {e}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)