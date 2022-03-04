import  requests
from bs4 import BeautifulSoup
from random import choice


def GetProxy():
    Url = "https://www.sslproxies.org"
    R = requests.get(Url)
    Soup = BeautifulSoup(R.content, "html5lib")
    return {"http":choice(list(map(lambda x: x[0]+":"+x[1],list(zip(map(lambda x: x.text, Soup.find_all("td")[::8]), map(lambda x: x.text, Soup.find_all("td")[1::8]))))))}
def UsePoroxy(Url):
    while True:
        try:
            proxies = GetProxy()
            R = requests.get(Url, proxies=proxies)
            if R.status_code == 200:
                print("Proxy >>" +str(proxies))
                break
        except:
            print("Proxy Error >> "+str(proxies))
            pass
    return R
Link = "http://api.ipify.org"
Req = UsePoroxy(Link)
print(Req.text)
