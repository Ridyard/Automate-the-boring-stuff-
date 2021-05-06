# atbs, chapter 3

# print a continuous zigzag

import time, sys

indent = 0 # how many spaces to indent
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end = '')
        print('*******')
        time.sleep(0.1) # pause for 1/10th of a second

        if indentIncreasing == True:
            indent += 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
