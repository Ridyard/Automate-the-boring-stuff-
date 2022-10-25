# atbs - web scraping 1

# return a list of match object from the test html file using beautiful soup module

import bs4, os

os.chdir('./Other') # navigate to the test html file...
#print('cwd is ' + str(os.getcwd()))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author') # stores a list or returned matches in elems; we're searching for '#author' tags
print(type(elems)) # <class 'list'>
print(len(elems)) # 1   # one author tag in the test file

print(type(elems[0])) # <class 'bs4.element.Tag'>
print(str(elems[0])) # '<span id="author">Al Sweigart</span>' 
print(elems[0].getText()) # 'Al Sweigart'
print(elems[0].attrs) # {'id': 'author'}

print('\n')

# pull list of all <p> elements in the test html file

pElems = exampleSoup.select('p')
print(len(pElems))
print(str(pElems) +'\n')
for i in range(len(pElems)):
    print(pElems[i].getText())
print()

