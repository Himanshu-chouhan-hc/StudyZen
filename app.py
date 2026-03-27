from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# OpenAI setup
try:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = None
except:
    client = None

app = Flask(__name__)
CORS(app)

def get_ai_response(user_text):
    if not client:
        return "API key not set"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a smart assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    return completion.choices[0].message.content


@app.route('/')
def home():
    return "Voice Assistant Backend Running 🚀"


@app.route('/voice', methods=['POST'])
def voice():
    try:
        data = request.json
        user_text = data.get("text")

        if not user_text:
            return jsonify({"response": "No input received"}), 400

        reply = get_ai_response(user_text)

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)