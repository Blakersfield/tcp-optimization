import asyncio
from flask import Flask
from flask import send_from_directory
from time import sleep
from scripts.server_metrics import *
from synchronization import *

async def main():
    await asyncio.gather(recordMetrics())

app = Flask(__name__)
app.config['STATIC_FOLDER'] = app.root_path + '/static/'
setting_startup()

@app.route("/")
async def send_data():
    path = "<a href = \"/continuous\">test</a>"
    return path

@app.route("/test")
async def send_file():
    data = await send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)
    return data

@app.route("/sync-transfer")
async def sync_transfer():
    connection_wait()
    data = await send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)
    return data

@app.route("/continuous")
async def cont_transf():
    #add to
    await asyncio.sleep(300)
    data = await send_from_directory(app.config['STATIC_FOLDER'], 'harambe.jpg', as_attachment=True)
    return data

asyncio.run(main())
