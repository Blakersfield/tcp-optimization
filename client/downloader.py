import urllib.request
import shutil

def launch(): 
    print('Launching client app...')
    url = 'localhost:5000/download'
    file_name = 'harambe.jpg'
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


