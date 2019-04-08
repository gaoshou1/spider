# import re
#
# text = "apple's price $99, orange's price is $10"

# ret = re.findall('\$\d+', text)
#
# print(ret)
# html = """<dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div class="job-detail">
#         岗位职责：
# 1、数据分析、采集、挖掘、清洗、整合、入库及备份等数据日常工作；
# 2、能够根据项目的实际需要，进行技术方案的分析、选型；
# 3、研究各种网页探寻特点和规律，负责网页信息抽取、数据清洗等研发和优化工作；
# 4、负责抽取算法和数据库建模的调研和设计，保证抽取、去重、分类、解析、增量融合入库等流程之后的数据结果；
# 5、研究反爬机制，破解复杂图片验证码、账号限制、IP限制等。
# 任职要求：
# 1、统招大专及以上学历，计算机相关专业；
# 2、熟悉Python脚本语言，至少有两年以上爬虫、搜索、数据库建模的开发经验，有Scrapy项目经验加分；
# 3、熟悉多种网络协议，HTML、XML，熟悉基于Cookie的网站登录原理，熟悉基于正则表达式、Xpath表达式，CSS选择器等网页信息抽取技术，熟悉JS、Ajax、网页消重；
# 4、熟悉Scrapy、PySpider、Crawley、Portia、Newspaper、BeautifulSoup、Grab、Cola等爬虫技术；
# 5、熟练掌握爬虫策略和防屏蔽规则，解决封账号、封IP、验证码，登录等问题；
# 6、熟悉MySQL数据库及性能优化，熟悉MongoDB、redis等nosql；
# 7、熟悉前端开发技术，熟悉Bootstrap，Vuejs等前端框架；
# 8、具有分布式、多线程、协程、进程的编程经验，有可证明的良好编码习惯；
# 9、责任心强，具有良好的对外沟通和团队协作能力，主动、好学。
#
# 福利待遇：
# 提供有竞争力的薪酬待遇；
# 上班时间双休，法定节假日休息；
# 统一购买五险一金；
# 入职满一年，享有5天的带薪年假；
# 节日福利等神马的自然是不在话下；
# 不定期可以参加一些外训的技能类专题论坛会；
# 不定期组织各种团建活动......
#         </div>
#     </dd>"""
# ret = re.sub('<.*?>', '', html)


# text = "hello world ni hao 20.50"
# # ret =re.split(' ', text)
#
# r = re.compile(r"""
#     \d+ # 小数点前的数
#     \.? # 小数点本身
#     \d* # 小数点后面的数
# """, re.VERBOSE)
# ret = re.search(r, text)
# print(ret.group())



import re

content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*(\d+)\s.*s$',content)
print(res.group(1))