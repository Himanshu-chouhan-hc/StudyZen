# ================================
# 🔥 IMPORTS
# ================================
import os

# Optional OpenAI import (safe mode)
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except:
    client = None


# ================================
# 🧠 MEMORY (OPTIONAL - TEMPORARY)
# ================================
messages = [
    {
        "role": "system",
        "content": "You are a smart voice assistant. Reply in short and clear sentences."
    }
]


# ================================
# 🤖 AI RESPONSE FUNCTION
# ================================
def get_ai_response(user_text):
    """
    User input lega → AI response return karega
    """

    # 🔹 Add user message to history
    messages.append({
        "role": "user",
        "content": user_text
    })

    # 🔹 Agar OpenAI available hai
    if client:
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            reply = completion.choices[0].message.content

            # 🔹 Add AI reply to history
            messages.append({
                "role": "assistant",
                "content": reply
            })

            return reply

        except Exception as e:
            return f"AI Error: {str(e)}"

    # 🔹 Fallback (No API key)
    else:
        reply = f"You said: {user_text}"

        # Store reply (optional)
        messages.append({
            "role": "assistant",
            "content": reply
        })

        return reply