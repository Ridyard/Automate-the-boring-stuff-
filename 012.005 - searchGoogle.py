#! python3
# script to search a topic and open the search result links in separate tabs
# take a string from the cmd argument and search on the pypi project resource

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
# https://pypi.org/search/?q=
# mr robot
#<a jsname="UWckNb" href="https://www.imdb.com/title/tt4158110/" data-ved="2ahUKEwj55vjgnpWHAxWVU0EAHYcDAekQFnoECGkQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">Mr. Robot (TV Series 2015–2019)</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJC4xJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3NTU3Nzc1Nzc3Nzc3Nzc1LTUyKzUwNTU3Nzc3NTUxLS04Ny00NTU1NTgtNTU3Nv/AABEIABwAHAMBEQACEQEDEQH/xAAaAAACAgMAAAAAAAAAAAAAAAAABgQFAQMH/8QAJBAAAgEDAwQDAQAAAAAAAAAAAQIDAAQRBQYxEhMhQUNRkSL/xAAbAQABBQEBAAAAAAAAAAAAAAAAAQIDBAUHBv/EACYRAAIBAwIFBQEAAAAAAAAAAAABEQIDBDFRBRIhodETImHB4RX/2gAMAwEAAhEDEQA/AHmuaG+FAgUAFJICpvnWb7SXshYTCPuwXjvlFbJjgZ05HpgDWzwrFtZCr9RTDXdlbIuVURyik28txiC6Z7gRvb2eCe0nmcSxBmHjjpkFar4ZiSmlq+0PwVlkXCyj3hqtlOWumF5DbPfLKuFjaRYmUKcgcjJ4xmq9XDLFxNULlb5Y+JkesipPq51OiIwdFceAwB815yqmKmti+uqkh6npFhqpjN/AJe2sip/TDAdSrcH2CRU1jKvY8q24n6GVW6a9SLPtfRZ0dJbFWV1KsO4wyCUJ9/caflSriWVTHu0/fI12LexrfaWhPCsTWOUXr+V8nrILZOcnOBzTv6eUnPN22E9C3sXYAAAAwAMAVQbbcsm06IzQAUAFABQB/9k=" style="height:26px;width:26px" alt="" data-csiid="rLOKZvngK5WnhbIPh4eEyA4_35" data-atf="4"></div></span><div class="CA5RN"><div><span class="VuuXrf">IMDb</span></div><div class="byrV5b"><cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://www.imdb.com<span class="ylgVCe ob9lvb" role="text"> › title</span></cite></div></div></div></div></a>
