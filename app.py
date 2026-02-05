from random import choice
from dotenv import load_dotenv
from flask import Flask, redirect, render_template
import os
import requests
from datetime import datetime

load_dotenv()

app = Flask(__name__)


app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG", "0") == "1"

@app.route('/', methods=("POST", "GET"))
def home():
    words = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/main/words").text.splitlines()
    word = choice(words)
    return render_template("index.html", word=word)
    words = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/main/words")\
    .text.splitlines()
    word = words[datetime.now().day]
    return render_template("index.html", word=word)



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
        
        