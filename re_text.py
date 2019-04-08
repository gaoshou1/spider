import requests
from lxml import etree
import re


def parse_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
               'referer': 'https://www.gushiwen.org/default_2.aspx'
               }
    respones = requests.get(url, headers=headers)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', respones.text, re.DOTALL)  # Dotall代表.匹配\n
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',respones.text, re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', respones.text, re.DOTALL)
    contents = re.findall(r'<div\sclass="contson".*?>(.*?)</div>',respones.text, re.DOTALL)
    item = []
    for i in contents:
        x = re.sub(r'<.*?>',"", i)
        item.append(x.strip())
    poems = []
    for value in zip(titles,dynasties,authors,item):
        title,dynasty,author,content = value
        pome = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content

        }
        poems.append(pome)
    for poem in poems:
        print(poem)



def main():
    for x in range(1,22):
        url = 'https://www.gushiwen.org/default_%s.aspx' %x
        parse_page(url)


if __name__ == '__main__':
    main()