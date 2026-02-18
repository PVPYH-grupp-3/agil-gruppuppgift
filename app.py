from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from logic import check_word
import os

load_dotenv()

app = Flask(__name__)
app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG", "0") == "1"

with open("words.txt") as f:
    WORDS = f.read().splitlines()

def get_daily_word():
    day_of_year = datetime.now().timetuple().tm_yday
    return WORDS[day_of_year % len(WORDS)]


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/play")
def play():
    word = get_daily_word()
    return render_template("index.html", word=word)

@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    user_guess = data.get("guess", "").lower()
    word = get_daily_word()

    result = check_word(word, user_guess)

    if result is None:
        return jsonify({"error": "Ogiltig gissning"}), 400

    won = result == "11111"
    return jsonify({"result": result, "won": won})


if __name__ == "__main__":
    app.run(debug=True)