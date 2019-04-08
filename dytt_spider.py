from lxml import etree
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
           'Referer': 'https://www.dytt8.net/html/gndy/dyzz/list_23_191.html'}

BASE_DOMAIN = 'https://www.dytt8.net'

def get_detail_urls(url):
    respones = requests.get(url, headers=HEADERS)
    # text = respones.content.decode('gbk')
    html = etree.HTML(respones.text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def parse_detail_page(deatil_url):
    movie = {}
    respones = requests.get(deatil_url, headers=HEADERS)
    text = respones.content.decode('gbk')
    html = etree.HTML(text)
    movie["title"] = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie["cover"] = html.xpath("//div[@id='Zoom']//img/@src")[0]
    movie["shot"] = html.xpath("//div[@id='Zoom']//img/@src")[1]
    # def parse_info(info, rule):
    #     return info.replace(rule,"").strip()
    movieinfos = html.xpath("//div[@id='Zoom']//text()")
    for index, infos in enumerate(movieinfos):
        # print(infos)
        # print(index)
        # print("="*30)
        if infos.startswith("◎上映日期"):
            movie["year"] = infos.replace("◎上映日期","").strip() # replace替换字符串， strip清除多余字符串
        elif infos.startswith("◎产　　地"):
            movie["country"] = infos.replace("◎产　　地", "").strip()
        elif infos.startswith('◎类　　别'):
            movie["category"] = infos.replace('◎类　　别', "").strip()
    movie["down"] = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    return movie



def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1, 11):

        # print("="*30)
        # print(x)
        # print("="*30)
        url = base_url.format(x)
        # print(url)
        deatil_urls = get_detail_urls(url)
        for deatil_url in deatil_urls:
            movie = parse_detail_page(deatil_url)
            print(movie)




if __name__ == '__main__':
    spider()