#! python3

# atbs - version control zip back-up
# chapter 10 - backing up a folder to a zip file whose filename increments

import os, zipfile
from pathlib import Path

def backupToZip(folder):
    #backup the entire contents of a folder to a zipfile
    folder = os.path.abspath(folder)
    print(f'target filepath is {folder}\n')
    n = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(n) + '.zip'
        #print(zipFilename)
        if not os.path.exists(os.path.join(folder,zipFilename)):     # if zipFilename doesn't exist then break
            break
        n +=1
    
    # create the zip file
    print(f'creating {zipFilename}...')
    backupZip = zipfile.ZipFile(os.path.join(folder, zipFilename), 'w') # create the zipfile in the subfolder 'testing files/backupToZip'

    # to do - walk entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder): # each iter through the loop will return the iteration's current folder, subfolders & files in the folder
        print(f'adding files from \"{foldername}\" to the zip archive')
        backupZip.write(foldername) # add current folder to the zip
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up any existing zip file
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    
    print('done') 


folder = Path.cwd()/'testing files/backupToZip'
backupToZip(folder)
