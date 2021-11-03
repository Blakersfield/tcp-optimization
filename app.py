from flask import Flask
from flask import send_from_directory
from time import sleep
from synchronization import *
import threading
from scripts import server_metrics

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '/static/'
setting_startup()

thr = threading.Thread(target=server_metrics.record_metrics)
thr.start()


@app.route("/")
def send_data():
    path = "<a href = \"/continuous\">test</a>"
    return path


@app.route("/test")
def send_file():
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)


@app.route("/sync-transfer")
def sync_transfer():
    connection_wait()
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)


@app.route("/continuous")
def cont_transf():
    #add to
    sleep(300)
    return send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)


    
