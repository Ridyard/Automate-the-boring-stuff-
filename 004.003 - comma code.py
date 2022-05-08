# atbs - comma code: take a list of strings and return a comma separated string with AND inserted before final item

words = ['cat', 'dog', 'monkey', 'chicken']

# method 1
def comma1(words):
    for i in range(len(words)-2):
        print(words[i], end=', ')
    print(words[-2] + ' & ' + words[-1])


# method 2
def comma2(words):
    sentence = ', '.join(words[:-1])
    sentence += ' & ' + words[-1]
    print(sentence)


comma1(words)
comma2(words)


