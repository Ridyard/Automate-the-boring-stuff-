
# atbs - parsing html with bs4
# works with example.html file

import bs4, requests, os

res = requests.get('https://nostarch.com')
res.raise_for_status() # this will raise an exception if there wa an error downloading the url file; it will do nothing if it succeeded
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

print('=============================')

os.chdir('Web Scraping')
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)
print()

print('=================================')

pElems = exampleSoup.select('p')
for i in range(len(pElems)):
    print(pElems[i].getText())

print('=================================')

# find any span elements, store the first matched element to spanElem & pass the att name to return the att value
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.attrs)




print()








