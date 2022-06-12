# atbs - version control back-up script

import os, zipfile
from pathlib import Path

userPath = Path(r"C:\Users\alexa\Documents\Workspace\Python\Test Files") # use a raw string to avoid issues with escape chars

def backupToZip(userPath): 
    userPath = os.path.abspath(userPath) # make sure path is absolute
    print()

    num = 1 # used for the zip version control
    
    # create a zipfile; 
    while True:
        zipName = os.path.basename(userPath) + '_' + str(num) + '.zip'
        if not os.path.exists(Path(userPath)/zipName):# if 'Test_files n .zip' exists in the target location, we loop through until num equals a new version
            break
        num += 1
    print(zipName)
    print(userPath)

    print('creating back-up...\n')
    backup = zipfile.ZipFile((Path(userPath)/zipName), 'w') # create the zipfile in the target loaction (userPath)

    # walk folder tree and compress each file
    for folder, subs, files in os.walk(userPath):
        # print(subs, files)
        
        print(f'\nadding files in {folder}...\n')
        backup.write(folder) # add current folder to the zip
        
        # add the files in this folder to the zip
        for file in files:
            newBase = os.path.basename(userPath) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue # don't backup the backup-zip files
            backup.write(os.path.join(folder, file))
    
    print('done')
    backup.close()

backupToZip(userPath)



