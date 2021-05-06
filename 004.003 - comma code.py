# ATBS, chapter 4 - lists

# practice question 1
#comma code - function takes a given list and returns a string with correct comma separated grammar

grammarList = ['cats','dogs','fish','racoons','monkeys']

def grammar(gl):
    print(gl)
    
    gl = ', '.join(gl)             # add commas with join, which returns a string
    print(gl)
    
    gl = gl.split()                 # split the string of words into a list
    print(gl)

    x = gl[-2]                      # pull the penultimate word from the list and remove the trailing comma
    print(x)
    gl[-2] = x[:-1]             # re-add the penultimate list item, with the comma removed
    print(gl)
    
    gl.insert(-1, 'and')
    print(gl)

    
    print(' '.join(gl))
    

    
    



grammar(grammarList)
