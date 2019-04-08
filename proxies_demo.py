import requests

proxies = {
    'http': '111.177.186.149:9999'
}


resp = requests.get("http://httpbin.org/ip", proxies=proxies)
print(resp.text)