from flask import Flask

app = Flask(__name__)

@app.route("/")
def send_data():
    return "text out for harambe"