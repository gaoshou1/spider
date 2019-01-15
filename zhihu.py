import requests
from lxml import etree
import re
import json
import time
import random
import collections
from pymongo import MongoClient

# 爬取知乎网站用户的昵称、行业、关注人数、粉丝人数

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def spider(user_url):
    # 1、发起网页请求，
    r = requests.get(user_url, headers=head)
    time.sleep(random.randint(5, 10))
    # r.status_code
    # 2、建立正则表达式找到json数据
    pat = re.compile('<script id="js-initialData" type="text/json">(.*)</script><script src="https://static.zhihu.com/heifetz/vendor.4709996994b6c965ecab.js">')
    # 3、提取json数据
    r_json = re.findall(pat, r.text)[0]
    # 4、解析json数据，用户关注的人的名称
    user_following = list(json.loads(r_json).get('initialState')['entities']['users'].keys())[1:]
    # 5、构建用户关注人的url
    next_urls = ['https://www.zhihu.com/people' + username + '/following' for username in user_following]
    sel = etree.HTML(r.text)
    # 6、提取用户名字，职业，关注人，粉丝数据
    name = sel.xpath('//*[@class="ProfileHeader-name"]/text()')[0]
    try:
        prefession = sel.xpath('//*[@class="ProfileHeader-infoItem"]/text()')[0]
    except:
        prefession = ''
    try:
        following = sel.xpath('//*[@class="Card FollowshipCard"]/div/a[1]/div/strong/text()')[0]
    except:
        following = 0
    try:
        follower = sel.xpath('//*[@class="Card FollowshipCard"]/div/a[2]/div/strong/text()')[0]
    except:
        follower = 0
    print(name)
    # collectino1.insert_one({'name': name, 'prefession': prefession, 'following': following, 'follower': follower})
    return next_urls


need_crawl_urls = collections.deque()
need_crawl_urls.append('https://www.zhihu.com/people/qi-wen-guang/following')
# client = MongoClient()
# db = client.zhihu1
# collectino1 = db.user
have_crawled_urls = set()


while True:
    url = need_crawl_urls.popleft()
    try:
        next_urls = spider(url)
        have_crawled_urls.add(url)
        pre_crawl_urls = set(next_urls) - have_crawled_urls
        need_crawl_urls.extend(pre_crawl_urls)
        print("--------------1-----------")
        print(need_crawl_urls)

    except:
        pass






