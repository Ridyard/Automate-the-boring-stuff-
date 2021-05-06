# atbs - regex

import re

# pass the desired pattern to re.compile & store the returned regex obj in phoneNo
phoneNo = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
# search() searches the string it is passed for any matches to the regex object
mo = phoneNo.search('my umber is 0161-301-1000. thanks') 

print('phone number found: ' + mo.group()) # group() returns a string of the returned text




mobileNo = re.compile(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)') # brackets allow us to group
mo2 = mobileNo.search('my mobile number is +447976882819')
print('mobile number found: ' + mo2.group())

print(mo2.groups()) # print each returned group
print(mo2.group(1)) # passing 0 would return the entire group
areaCode, number = mo2.groups() # multi assignment using groupS() *note the plural
print('mobile area code is: '+ areaCode + '\nbody of mobile number is: 0'+ number)
