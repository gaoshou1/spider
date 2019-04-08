from selenium import webdriver
from lxml import etree
import time
import csv


class BossSpider(object):
    driver_path = r'D:/chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position='
        self.positions = []


    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.Parse_list(source)
            next_bin = self.driver.find_element_by_xpath("//div[@class='page']/a[last()]")
            if 'next disabled' in next_bin.get_attribute('class'):
                break

            else:
                next_bin.click()
            time.sleep(1)



    def Parse_list(self, source):
        html = etree.HTML(source)
        lis = html.xpath("//div[@class='info-primary']//a/@href")
        for li in lis:
            li_url = 'https://www.zhipin.com' + li
            self.OpenNew(li_url)


    def OpenNew(self, url):
        self.driver.execute_script('window.open("%s")' % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.List_Page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def List_Page(self, source):
        html = etree.HTML(source)
        postition = {}
        postition['name'] = html.xpath("//div[@class='name']/h1/text()")[0]
        postition['salary'] = html.xpath("//span[@class='salary']/text()")[0].strip()
        postition['city'] = html.xpath("//p/text()")[0]
        postition['work_years'] = html.xpath("//p/text()")[1]
        postition['education'] = html.xpath("//p/text()")[2]
        postition['job-sec'] = "".join(html.xpath("//div[@class='job-sec']//div[@class='text']/text()")).strip()
        self.positions.append(postition)
        header = ['name','salary','city','work_years','education','job-sec']
        with open('boos.csv', 'w',encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, header)
            writer.writeheader()
            writer.writerows(self.positions)







if __name__ == '__main__':
    boss = BossSpider()
    boss.run()