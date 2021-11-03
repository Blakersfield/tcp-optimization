from urllib import request 
import shutil

print('Launching client app...')
url = 'http://127.0.0.1:5000/test'
file_name = 'harambe.jpg'
with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    


