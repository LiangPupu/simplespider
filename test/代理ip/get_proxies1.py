import requests
import json
import time


def get_proxies():
    url = "http://http.tiqu.alicdns.com/getip3?num=1&type=3&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions="
    response = requests.get(url)
    time.sleep(1)
    # proxies = json.loads(response.text, encoding='utf-8')
    print(response.text)
    return response.text

