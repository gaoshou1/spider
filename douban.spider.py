import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
          'Referer': 'https://movie.douban.com/'}

url = 'https://movie.douban.com/cinema/nowplaying/maoming/'

response = requests.get(url, headers=headers)
text = response.text


html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")

movies = []
for li in lis:
    item = {}
    item["title"] = li.xpath("@data-title")[0]
    item["score"] = li.xpath("@data-score")[0]
    item["duration"] = li.xpath("@data-duration")[0]
    item["director"] = li.xpath("@data-director")[0]
    item["poster"] = li.xpath(".//img/@src")[0]

    movies.append(item)
print(movies)
