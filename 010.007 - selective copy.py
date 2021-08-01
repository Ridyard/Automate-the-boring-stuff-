# atbs - chapter 10

##Selective Copy
##
##Write a program that walks through a folder tree and searches for files with a certain file extension
##(such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

# initial issues around permissions in windos dir; ensure files and folders aren't set to READ ONLY


import os, shutil
from pathlib import Path



def clearContents(d):
    print(f'clearing the contents of \n\"{dest}\"\n') 
    try: 
        for i in d:
            os.unlink(dest/i) # join filename to filepath & delete
    except Exception as e:
        print(e)

def copyPDFs(src, dest): # this will copy all PDFs from the src folder to dest
    for foldername, subfolders, filenames in os.walk(src):
        print(f'copying PDFs from:\n\"{foldername}\"')
        for filename in filenames:
            if filename.endswith('.pdf'):
                try:
                    path_file = os.path.join(foldername, filename) # avoids errors with subfolders; ie without ths line, any pdfs in a subfolder would cause an error
                    shutil.copy2(path_file,dest)
                except Exception as e:
                    print(f'\nunable to copy {filename}\n')
                    print(e)


p = Path.cwd()
src = p/'Testing files\selective copy src' 
dest = p/'Testing files\selective copy dest'

d = os.listdir(dest)
if len(d) > 0: # clear the contents of dest folder
    clearContents(d)
copyPDFs(src, dest)



