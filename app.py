from flask import Flask
from flask import send_from_directory
from time import sleep
from client.downloader import launch 

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '/static/'


@app.route("/")
def send_data():
    path = "<a href = \"/continuous\">test</a>"
    return path

@app.route("/test")
def send_file():
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)

@app.route("/continuous")
def cont_transf():
    sleep(300)
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)


@app.route('/download')
def launch_client():
    sleep(300)
    return launch()
    
