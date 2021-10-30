from flask import Flask
from flask import send_from_directory

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '\static\'


@app.route("/")
def send_data():
    return app.config['STATIC_FOLDER'] #"text out for harambe"

@app.route("/test")
def send_file():
    return send_from_directory(app.config['STATIC_FOLDER'], 'static/harambe.jpg', as_attachment=True)
