import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "Origin": 'https://www.lagou.com',
    'Cookie': '_ga=GA1.2.139620168.1546609487; user_trace_token=20190104214448-e71c5a52-1026-11e9-bbaa-525400f775ce; LGUID=20190104214448-e71c5ed0-1026-11e9-bbaa-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216939dfb99a76-0853f52dfd4035-1333062-2073600-16939dfb99b992%22%2C%22%24device_id%22%3A%2216939dfb99a76-0853f52dfd4035-1333062-2073600-16939dfb99b992%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAABEEAAJA1E0AD5F1C9C44D1B4BA8336DD3298285; _gid=GA1.2.1523433660.1554554971; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552762148,1553699663,1554203667,1554554971; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=0dfb97c40bf166050bef7816ba98f432; _gat=1; LGSID=20190406215421-7ae8e75b-5873-11e9-a47f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252F5783372.html%26t%3D1554558859%26_ti%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F5783372.html; X_HTTP_TOKEN=dba213767b1edd9a49295545512003acfbdf1dd590; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554559259; LGRID=20190406220134-7cf56513-5874-11e9-802f-5254005c3644; SEARCH_ID=4b29a84494ab4b9d8ab5b6a85344901a',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'}

def get_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        "first" :" false",
        "pn":2,
        "kd":'python'
    }

    #
    for x in range(1,14):
        data['pn'] = x
        respones = requests.post(url, headers=headers, data=data)
        result = respones.json()
        print(result)
        positions = result["content"]["positionResult"]['result']
        for position in positions:
            positionID = positions['positionID']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionID
            parse_postion_detail(position_url)
            break
        break

def parse_postion_detail(url):
    respones = requests.get(url, headers=headers)
    print(respones.text)





def main():
    get_page()

if __name__ == '__main__':
    main()