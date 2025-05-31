import groq
import os
from dotenv import load_dotenv

client = groq.Groq(api_key="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")
#or

print("🤖 Welcome to your  AI Chatbot! Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers in a friendly tone."},
            {"role": "user", "content": user_input}
        ]
    )

    # 6. Get the chatbot's reply
    reply = response.choices[0].message.content
    print("AI:", reply)
