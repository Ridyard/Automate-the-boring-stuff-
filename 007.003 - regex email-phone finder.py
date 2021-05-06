#! python3

# to run from windows - win + r; finder

# atbs - regex
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard


import re, pyperclip, sys

phoneNo = re.compile(r'''(
    (\d{4}|\(\d{4}\))?              # area code (digits or digits in brackets)
    (\s|-|\.)?                            # separator
    (\d{3})                                    # first 3 digits
    (\s|-|\.)                                # separator
    (\d{4})                                       # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)                   # verbose allows the regex to flow over multiple lines, easier to read


emailAdd = re.compile(r'''(
    [a-zA-Z0-9._%+-]+        #username, combination of these characters
    @
    [a-zA-Z0-9._%+-]+        # domain name
    (\.[a-zA-Z]{2,4})              # dot something
    (\.[a-zA-Z]{2,4})?            # optional dot something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
print(text + '\n')

matches = []
for groups in phoneNo.findall(text):                                            # one tuple for earch match, with the tuple containing strings for each group in the reg ex
    phoneNos = '-'.join([groups[1], groups[3], groups[5]])      # join the phone no sections, standardise with '-' separator
    if groups[8] != '':                 #if there is an extension...
        phoneNos += ' x' + groups[8]
    matches.append(phoneNos)    # add the clensed phone number to matches

for groups in emailAdd.findall(text):
    matches.append(groups[0])           # group[0] return the whole match object

if len(matches) > 0:
    for i in matches:
        print(i)
    print('*matches copied to clipboard')
else:
    print('no matches returned')

output = '\n'.join(matches)
pyperclip.copy(output)


    
    
    
    
