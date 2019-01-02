import requests
from lxml import etree
import re
import json


url = 'https://www.zhihu.com/people/qi-wen-guang/following'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(url, headers=head)
pat = re.compile('<script id="js-initialData" type="text/json">(.*)</script><script src="https://static.zhihu.com/heifetz/vendor.7c9abc3e398528f8abf1.js')
resp = re.findall(pat, r.text)[0]
json.loads(resp)
