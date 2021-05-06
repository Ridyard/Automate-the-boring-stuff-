# atbs - regex, findall

import re

phoneNumbers = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbers.findall('hello my home number is 0161-301-1111 & my work number is 0161-371-1491/ thanks')
# findall returns all occurrences of the matched string as a list of strings 
print(mo)


"""

    When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall()
    returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
    When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall()
    returns a list of tuples of strings (one string for each group), such as
    [('415', '555', '9999'), ('212', '555', '0000')]

    
"""
