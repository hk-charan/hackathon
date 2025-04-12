from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyDZ043N77K_9Um8WajmMmSm06822tzUxHs"

@app.route("/")
def home():
    return render_template("index.html")  # Landing Page

@app.route("/chat")
def chat():
    return render_template("chat.html")   # Chat Interface

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message", "")
    
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {
            "contents": [{"parts": [{"text": user_input}]}]
        }
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, json=payload, headers=headers)
        result = res.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)

