from flask import Flask
import os
#test
app = Flask(__name__)

# debug = os.getenv('FLASK_DEBUG', '0') == '1'
# app.config['FLASK_DEBUG'] = debug

app.route('/')
def home():
    return "hej"

if __name__ == '__main__':
    app.run(debug=True)