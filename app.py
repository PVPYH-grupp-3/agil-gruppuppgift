from dotenv import load_dotenv
from flask import Flask, render_template
import os

load_dotenv()
app = Flask(__name__)


app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG", "0") == "1"

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)