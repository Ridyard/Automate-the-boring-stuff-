# atbs
# renaming files to a European date format

import os, re, shutil
from pathlib import Path

p = Path.cwd()/'testing files'/'date regex test files'



# create date regex
datePattern = re.compile(r"""^(.*?) # all text before the date
        ((0|1)?\d)-         # 1 or 2 digits for the month
        ((0|1|2|3)?\d)-     # 1 or 2 digits for the day
        ((19|20)\d\d)           # 4 digits for the year
        (.*?)$                             # all text after date
        """,re.VERBOSE) # verbose allows allows whitespace, ie makes it easier to read



# loop over files in directory & identify the date parts of the filename
for amFilename in os.listdir(p):
    mo = datePattern.search(amFilename)
    if mo == None:
        continue # ie if amFilename doesn't contain a date then skip to next filename
    beforePart = mo.group(1) 
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8) # read the groups by incrementing the group(no) by 1 each time you open a parenthesis in the regex above
    #print(beforePart + monthPart + dayPart)

    euroDate = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart # store new concat string in euroDate
    print(f'renaming {amFilename} to {euroDate}') # sense check before proceeding with the renaming
    shutil.move(p/amFilename, p/euroDate) # rename src (p/amFilename) to dest (p/euroDate)
    










