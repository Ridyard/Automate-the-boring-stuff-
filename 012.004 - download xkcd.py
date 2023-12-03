#! python3
# atbs - web scraping: download xkcd comics

import requests, bs4, os

url = 'https://xkcd.com/'
os.chdir('./Web Scraping')
os.makedirs('xkcd', exist_ok=True) # creake xkcd dir, but if it already exists then don't raise exception
#print(os.getcwd())

#while not url.endswith('#'):
for i in range(10):
    # download the page
    print(f'downloading {url}...')
    res = requests.get(url) # download the url page
    res.raise_for_status() # check if something went wrong

    soup = bs4.BeautifulSoup(res.text, 'html.parser') # create bs object from the ext of the downloaded page

    # find url of the comic image
    comicElem = soup.select('#comic img') # get the div with the id attribute set to comic; img will get the img element from the bs object
    if comicElem == []: # if the selector function doesn't find anything, it will return an empty list; skip these
        print('could not find the comic image')
    else:
        comicUrl = 'https:' + comicElem[0].get('src') # otherwise the selector will return a list containing one <img> element; get the src att from the img element and pass to requests.get() to download the image
        print(f'downloading the image {comicElem}...')
        res = requests.get(comicUrl) # store the image file
        res.raise_for_status()

        # save xkcd image to the hdd directory
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # return the last part of the url string to use as the filename

        for chunk in res.iter_content(100000): # to save files we've downloaded with requests, we need to loop over the return values of iter-content()
            imageFile.write(chunk)
        imageFile.close()
    
    # get 'prev' button url
    prevLink = soup.select('a[rel="prev"]')[0] # identify the <a> element with the 'rel' att set to 'prev' button, and use this element's href att to get the url to the prev image  
    url = 'https://xkcd.com' + prevLink.get('href') # the loop resets using this "incremented" link


print('\ndone!\n')


