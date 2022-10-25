# atbs - saving downloads to hard drives

import requests, os
from pathlib import Path

os.chdir(Path.cwd()/'other') # change to the test folder on my machine; file will be saved here

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status() # raise exception if there was an error downloading

playFile = open('RomeoAndJuliet.txt', 'wb') # need to open this file in wb to maintain the downloads unicode encoding of the text

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()