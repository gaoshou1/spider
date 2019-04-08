import requests

url = 'http://www.renren.com/'
data = {'email': '379329230@qq.com', 'password':'3525806.'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
session = requests.Session()
session.post(url=url, data=data, headers=headers)

resp = session.get('http://www.renren.com/880151247/profile')

print(resp.text)

