from urllib import request 
import shutil
from datetime import datetime

'''
    automation algorithm
    1.) loop through number of trials
    2.) hit a route each trial, instead of sync transfer
    3.) for each trial, do x number of tests
    4.) in those tests, hit sync transfer  
    5.) keep going until all trials are done
'''


def autonomous_testing(target):
    url = 'http://' + target + ':5000/start-trials'
    with request.urlopen(url) as response:
        content = int(response.read().decode(response.headers.get_content_charset()))
        for i in range(content):
            fake_launch(target, i)

def fake_launch(target, index): 
    print('Launching (fake) client app..')
    file_name = f'trial{index}.tar'
    url = 'http://' + target + f':5000/sync-transfer-autonomous'
    with request.urlopen(url) as response: 
        content = response.read().decode(response.headers.get_content_charset())
        print(content)

def launch(target):
    print('Launching client app...')
    url = 'http://' + target + ':5000/sync-transfer'
    file_name = 'arch.tar'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print(f'transfer finished at: {datetime.now().strftime("%H:%M:%S")}')



