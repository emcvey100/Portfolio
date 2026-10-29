url = 'https://www.netflix.com/browse?jbv=70140403'
url2 = 'https://www.netflix.com/browse?jbv=7014040'
##import validators
##print(validators.url(url))
##print(validators.url(url2))
##import requests
##r = requests.head(url)
##redirect_url = r.url
##print(redirect_url)
##print(redirect_url == url)
##print(url)
##print()
##import time
##r = requests.head(url2)
##time.sleep(10)
##redirect_url = r.url
##print(redirect_url)
##print(url2)
##print(redirect_url==url2)
from urllib.request import urlopen
try:
    data = urlopen(url2).read()
#print(data)

    data=str(data)
    x=data.find("<title>")
    print(x)
    y=data.find("</title>")
    print(y)
    print(data[x+7:y])
except:
    print("N/a")
