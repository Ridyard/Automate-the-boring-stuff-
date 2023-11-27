#! python3
# atbs - opening all search results

# script to open the top links of a search result on pypi.org

import requests, sys, webbrowser, bs4

print('searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])) # essentially joining the user-cmd parameter with the search addresses
#res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:])) # essentially joining the user-cmd parameter with the search addresses
res.raise_for_status() # check for connections issues

print(sys.argv)
#print(str(res.text))

soup = bs4.BeautifulSoup(res.text, 'html.parser') # retrieve top search result links
linkElements = soup.select('.package-snippet') # get the search result links / all elements that have a css att called package-snippet
                                                # all links have a class="package-snippet" variable ie and not sidebar links
#print(soup)
print(linkElements)

numOpen = min(5, len(linkElements)) # elegantly specify the number of links to open
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElements[i].get('href')
    print('opening ', urlToOpen)
    webbrowser.open(urlToOpen)


