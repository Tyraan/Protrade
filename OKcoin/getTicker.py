
import requests

class getTicker():
    def __init__(self,url):
        __url = url
        r = requests.get(url)
        response = r.json()




