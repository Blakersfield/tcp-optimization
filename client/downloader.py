from urllib import request 
import shutil


def launch(target):
    print('Launching client app...')
    url = 'http://' + target + '/sync-transfer'
    file_name = 'arch.tar'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    


