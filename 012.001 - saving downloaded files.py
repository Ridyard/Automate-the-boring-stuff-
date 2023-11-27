
# atbs - saving downloaded files to the hdd

import requests, os
from pathlib import Path

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
targetDir = Path.cwd()/'Web Scraping'
print(f'path is {targetDir}... type is {type(targetDir)}')
#os.mkdir(targetDir)

playFile = open(targetDir/'RomeoAndJuliet.txt', 'wb') # downloaded files need to be written as 'write binary' (even plaintext files)

for block in res.iter_content(100000): # iter_content returns chunks of the content; 100,000 bytes is usually a good size
    playFile.write(block)
playFile.close()

