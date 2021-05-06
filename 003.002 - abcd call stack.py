# atbs, chapter 3

# abcd call stack

def a():
    print('the a() function begins...')
    b()
    d()
    print('the a() function finishes & returns')

def b():
    print('the b() function begins...')
    c()
    print('the b() function finishes & returns')

def c():
    print('the c() function starts...')
    print('the c() function finishes & returns')

def d():
    print('the d() function begins...')
    print('the d() function finishes & returns')

a()

# functions can use global variables, without being passed them
# global scope (ie not a function) cannot access a variable declared in a function (ie local scope)


# def test1():
#       print(eggs)
#       eggs = 'i'
#
# eggs = 'y'
# test1()

# this function will cause an error as eggs is defined in test1() after the print call
# python see that egs is defined in the local scope so considers eggs to be local & ignores the global variable
# script crashes as the test1() print call is made before eggs is defined locally
# python won't fall back to using the global variable
