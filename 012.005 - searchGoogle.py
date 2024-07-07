#! python3
# script to search a topic and open the search result links in separate tabs
# take a string from the cmd argument and carries out a Google search; opening the top 5 search result links

import bs4, requests, sys, webbrowser, random

# simple scraping will be blocked by most sites - see this link for guidance to get around this: https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/
# this is a list of fake user agents, used to bypass anti-scraping functionality a site may have
# ie the website can't tell if the request is coming from a scraper or real user
# the called website will think one of the following devices is calling, intead of a py script
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]


print('searching... ' + ' '.join(sys.argv[1:]))

url = 'https://www.google.com/search?q='
res = requests.get(url +' '.join(sys.argv[1:]),headers={'User-Agent': random.choice(user_agents_list)})
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find all <a> tags with the attribute jsname="UWckNb"
linkElements = soup.find_all('a', attrs={'jsname': 'UWckNb'})

# Extract the desired information from each element (e.g., the href attribute or text)
results = [{'href': element.get('href'), 'text': element.get_text()} for element in linkElements]

#print(linkElements)

numOpen = min(5, len(linkElements))
for i in range(numOpen):
    urlToOpen = linkElements[i].get('href')
    print('opening ' + urlToOpen)
    webbrowser.open(urlToOpen)
    
print('end')
