# atbs - web requests

import webbrowser, requests

addr = 'https://automatetheboringstuff.com/files/rj.txt'
res = requests.get(addr)
webbrowser.open(str(addr))

print(type(res))
print(len(res.text))
print(res.status_code == requests.codes.ok) # if this is True then the request was successful

print('\n' + res.text[:250])