# atbs - practice question
# date detection - pulls dates from given text and identifies whether it is a valid date

import re


def dateCheck(day, month, year):        # returns true if a valid date, otherwise false
    print('\n' + day, month, year)
    if int(day) > 31:       # group returns the string version, hence use of int()
        print('invalid date')
        return False
    elif month == '04' or month == '06' or month == '09' or month == '11': # 30-day months
        if int(day) > 30:
            print('invalid date')
            return False
    elif month == '02':
        if int(day) > 29:
            print('invalid date')
            return False
        elif day == '29':          # see if it is a leap year / 29 is a valid day 
            if int(year) % 4 == 0 or int(year) % 100 != 0 and int(year) % 400 == 0:
                print('valid date - leap year')
                return True
            else:
                print('invalid date')
                return False
    else:
        print('valid date')
        return True
    
# text to be checked for dates
text = 'hello there, here are some dates to check: 30.05.3000, 29.02.2000, 29.02.2005, 29.02.2008, 29-02-2020, 31.04.2021, 31/12/2019, 31/02/2020, 13-05-1989, 13/01/1992, 32/03/2020, 31/09/2020, 29/02/2020 hope all ok'

#date regex
dateReg = re.compile(r'''(
        ([0-3]\d)               # day
        (\s|-|\/|\.)?       # match zero or 1 of the given separator
        ([0-1]\d)               # month
        (\s|-|\/|\.)?
        ([0-2][0-9][0-9][0-9])    # year
        )''', re.VERBOSE)


dateMO = dateReg.findall(text)
dates = []  # will contain the valid dates

for groups in dateMO:
    validDate = dateCheck(groups[1], groups[3], groups[5])  # send the returned match objects into dateCheck()
    if validDate == False:
        continue    # if not a valid date, skip to next item in loop & don't add to dates[]
    elif validDate == True:
        d = '/'.join([groups[1], groups[3], groups[5]]) # clense each date into a standard format; / separated
        dates.append(d)
    
print('\nthe following dates were returned:')
print(', '.join(dates))     # print valid dates in a readable format
print()




