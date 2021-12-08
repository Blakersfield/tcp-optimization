from flask import Flask
from flask import send_from_directory
from time import sleep
from synchronization import *
import time
from datetime import datetime
from client.downloader import autonomous_testing 

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '/static/'
setting_startup()

@app.route("/")
def send_data():
    path = "<a href = \"/continuous\">test</a>"
    return path

@app.route("/test")
def send_file():
    return send_from_directory(app.config['STATIC_FOLDER'], 'arch.tar', as_attachment=True)

@app.route("/sync-transfer")
def sync_transfer():
    connection_wait()
    print(f'beginning transfer at: {datetime.now().strftime("%H:%M:%S")}')
    return send_from_directory(app.config['STATIC_FOLDER'], 'arch.tar', as_attachment=True)

@app.route("/continuous")
def cont_transf():
    #add to
    sleep(300)
    return send_from_directory(app.config['STATIC_FOLDER'], 'arch.tar', as_attachment=True)
    
@app.route("/start-trials")
def start_trials():
    trials = read_settings()['number_of_trials']
    return trials


@app.route('/sync-transfer-autonomous/<trial>')
def sync_transfer_autonomous(trial):
    # as soon as everyboyd starts, we reset to zero
    connection_wait()
    connection_start()
    print(f'beginning transfer at: {datetime.now().strftime("%H:%M:%S")}')
    return send_from_directory(app.config['STATIC_FOLDER'], 'arch.tar', as_attachment=True)