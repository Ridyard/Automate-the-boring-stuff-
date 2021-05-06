# zigzag

# 2nd attempt from memory // make use of function & user input
# 1st attempt is more elegant


indent = 0
increaseIndent = True

def printSymbol(symbol, symbolCount, indent):
    print(' ' * indent, end = '')
    print(symbol * symbolCount)

print('enter the character to use for zigzag')
symbol = input()
print('repeat character how many times?')
symbolCount = int(input())


try:
    while True:
        printSymbol(symbol, symbolCount, indent)
        indent += 1
        if indent > 20:
            increaseIndent = False
            while increaseIndent == False:
                printSymbol(symbol, symbolCount, indent)
                indent -= 1
                if indent == 0:
                    increaseIndent = True

except:
    print('')

        
        
