from urllib import request 
import shutil
from datetime import datetime

def launch(target):
    print('Launching client app...')
    url = 'http://' + target + ':5000/sync-transfer'
    file_name = 'arch.tar'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print(f'transfer finished at: {datetime.now().strftime("%H:%M:%S")}')



