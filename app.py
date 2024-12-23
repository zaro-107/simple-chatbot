from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I assist you?",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a program, but I'm doing well! How about you?",
    "your name": "I'm ChatBot, your helpful assistant.",
    "what is your name": "You can call me ChatBot.",
    "bye": "Goodbye! Take care!",
    "hello": "Hi there! How can I assist you?",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a program, but I'm doing well! How about you?",
    "your name": "I'm ChatBot, your helpful assistant.",
    "what is your name": "You can call me ChatBot.",
    "time": "I can't tell time yet, but you can try asking me in a different version!",
    "bye": "Goodbye! Take care!",
    "what's up": "I'm good! What about you?",
    "who is your creator": "My creator is none other than human ingenuity!",
    "which religion is best": "Sorry, I don't have a relevant answer for that.",
    "thank you": "You're welcome!",
    "how_are_you": "I'm just a bot, but I'm functioning perfectly!",    
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    user_input = request.args.get("msg").lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    app.run(debug=True)
