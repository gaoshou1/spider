import requests
from retrying import retry

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'}


@retry(stop_max_attempt_number=3)  #允许报错3次
def _parse_url(url, method, data,proxies):
    if method == "POST":
        response = requests.post(url, data=data, headers=headers, proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(parse_url(url))