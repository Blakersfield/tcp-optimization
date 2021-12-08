from urllib import request 
import shutil
from datetime import datetime
import os
import json

'''
    automation algorithm
    1.) loop through number of trials
    2.) hit a route each trial, instead of sync transfer
    3.) for each trial, do x number of tests
    4.) in those tests, hit sync transfer  
    5.) keep going until all trials are done
'''

def multiple_file_transfer(target):
    getFiles = 'http://' + target + ':5000/start-files'
    getTrials = 'http://' + target + ':5000/start-trials'
    files = 0
    trials = 0
    with request.urlopen(getFiles) as response:
        content = int(response.read().decode(response.headers.get_content_charset()))
        files = content
    with request.urlopen(getTrials) as response:
        content = int(response.read().decode(response.headers.get_content_charset()))
        trials = content
    print(f'files {files} trials {trials}')
    for i in range(trials):
        launch_autonomous(target, 0)
        for j in range(1, files):
            launch_mft(target, i) 

def launch_mft(target, trial):
    start_trial_text = f':: TRIAL{trial}:: direct transfer started at: {datetime.now().strftime("%H:%M:%S")}\n'
    print(start_trial_text)
    trialTXT = open(f'trial{trial}.txt', 'w+')
    trialTXT.write(start_trial_text)

    file_name = f'trial{trial}.tar'
    url = 'http://' + target + f':5000/direct-transfer/<{trial}>'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file: 
        shutil.copyfileobj(response, out_file)
    end_trial_text = f':: TRIAL{trial}:: direct transfer finished at: {datetime.now().strftime("%H:%M:%S")}\n'
    print(end_trial_text)
    trialTXT.write(end_trial_text)
    trialTXT.close()


def autonomous_testing(target):
    url = 'http://' + target + ':5000/start-trials'
    trials = 0
    with request.urlopen(url) as response:
        content = int(response.read().decode(response.headers.get_content_charset()))
        trials = content
        for i in range(content):
            launch_autonomous(target, i)
    # delete all tars
    for i in range(trials):
        os.remove(f'trial{i}.tar')


def launch_autonomous(target, index): 
    start_trial_text = f':: TRIAL{index}:: transfer started at: {datetime.now().strftime("%H:%M:%S")}\n'
    print(start_trial_text)
    trialTXT = open(f'trial{index}.txt', 'w+')
    trialTXT.write(start_trial_text)

    file_name = f'trial{index}.tar'
    url = 'http://' + target + f':5000/sync-transfer-autonomous/<{index}>'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file: 
        shutil.copyfileobj(response, out_file)
    end_trial_text = f':: TRIAL{index}:: transfer finished at: {datetime.now().strftime("%H:%M:%S")}\n'
    print(end_trial_text)
    trialTXT.write(end_trial_text)
    trialTXT.close()

def launch(target):
    start_trial_text = f'transfer started at: {datetime.now().strftime("%H:%M:%S")}'
    print(start_trial_text)
    url = 'http://' + target + ':5000/sync-transfer'
    file_name = 'arch.tar'
    with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print(f'transfer finished at: {datetime.now().strftime("%H:%M:%S")}')



