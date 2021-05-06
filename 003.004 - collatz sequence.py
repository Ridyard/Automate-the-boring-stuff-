# atbs, chapter 3 practice questions

# collatz sequence
# input number will eventually evaluate to 1 based on collatz sequence

def collatz(number):
    if number % 2 == 0:         # if choice number is even
        cNumber = number // 2
        print(cNumber)
        return cNumber
    elif number % 2 == 1:       # if choice number is odd
        cNumber = 3 * number + 1
        print(cNumber)
        return cNumber


print('enter a number to run the collatz sequence...')
try:
    choice = int(input())

    while choice != 1:
        print('current value is ' + str(choice))
        choice = collatz(choice) # assign choice the value of choice once sent through collatz function

except:
    print('encountered issue... ensure input character is a number')
