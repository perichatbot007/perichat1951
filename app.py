from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import chat_with_groq

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Empty message received."}), 400
    try:
        bot_reply = chat_with_groq(user_message)
        return jsonify({"response": bot_reply})
    except Exception as e:
        import traceback
        print("[Flask Error]")
        traceback.print_exc()
        return jsonify({"response": "An error occurred on the server."}), 500

if __name__ == "__main__":
    app.run(debug=True)
