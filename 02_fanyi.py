import requests
import json
import sys

# 借助手机百度接口做的翻译小程序


# query_string = sys.argv[1]
query_string = input("请输入要翻译的内容")

headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

data = {
    "query": query_string,
    "from": "zh",
    "to": "en"

}

post_url = 'https://fanyi.baidu.com/basetrans'

r = requests.post(post_url, data=data, headers=headers)
# print(r.content.decode())
dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("翻译结果为：", ret)
