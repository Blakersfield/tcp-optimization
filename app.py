from flask import Flask
from flask import send_from_directory
import time

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '/static/'


@app.route("/")
def send_data():
    return app.config['STATIC_FOLDER'] #"text out for harambe"

@app.route("/test")
def send_file():
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)

@app.route("/continuous")
def cont_transf():
    time.sleep(300)
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)