#! python3
# atbs - automate opening the top n pages on pypi.org
# run from command line; "py [script name] [search term]"
# example: py '012.003 - searchpypi.py' boring stuff 

import webbrowser, requests, sys, bs4

# command line args will determine the term(s) to search for
# requests module will then download the resultant search page
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# we create a bs object from the downloaded page's html text
soup = bs4.BeautifulSoup(res.text, 'html.parser') 

# using select on 'package-snippet' will find all of the <a> elements that are within elements that has the package-snippet css class
# package-snippet refers to the class referenced within each search result link on pypi.org
# it doesn't matter what this class does, it is just a marker for the <a> element that we're looking for
# soup.select will return a list of all of the elements that matched the 'package-snippet'
linkElems = soup.select('.package-snippet') 

# placeholder test: the top 5 links from this page should open within the for loop further below
webbrowser.open('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

numOpen = min(5, len(linkElems)) # open the top 5x links (or all of the links if fewer than 5x returned) 
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print(f'opening {urlToOpen}...')
    webbrowser.open(urlToOpen)
