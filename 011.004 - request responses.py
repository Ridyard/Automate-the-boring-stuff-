# atbs - raise for status
# checking for errors
import requests

res = requests.get('https://inventwithpython.com/not_a_real_page')

try:
    res.raise_for_status() # call method on response object; 
                        # will raise exception if there ewas an error downloading the file

except Exception as exc:
    print(f'\n>>>there was a problem with the link / connection / download: \n{exc} \n')


