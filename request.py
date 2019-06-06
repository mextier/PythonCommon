#https://www.youtube.com/watch?v=KnBntO0wayk
#https://www.youtube.com/watch?v=sbYXa6HJJ5M
#https://www.youtube.com/watch?v=tb8gHvYlCFs

#https://httpbin.org/

import requests

try:
    r=requests.get('https://code.visualstudio.com/')
    if r.ok:
        print('Everything is fine!')
    else:
        print('Error ',r.status_code)
except e:
    print('Error ',e)

r=requests.get("https://httpbin.org/get")
print(r.json())
