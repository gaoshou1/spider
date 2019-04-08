from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait  # 等待
from selenium.webdriver.support import expected_conditions as EC  # until条件
from selenium.webdriver.common.by import By


class LagouSpider(object):
    driver_path = r'D:/chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='  # start_url
        self.positions = []

    def run(self):
        self.driver.get(self.url)  # 发送请求
        while True:
            source = self.driver.page_source  # 获取网页源码
            # WebDriverWait(driver=self.driver, timeout=10).until(
            #     EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            # )
            self.parse_list_page(source)  # 获取详情页url
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")  # 获取下一页url
            if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):  # 判断是否最后一页
                break
            else:
                next_btn.click()
            time.sleep(1)


    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)  # 进入到详情页
            time.sleep(1)



    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)  # 新窗口打开详情页
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到详情页新窗口
        # WebDriverWait(driver=self.driver, timeout=10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[@class='name']"))
        # )
        source = self.driver.page_source  # 获取详情页源码
        self.parse_detail_page(source)  # 提取页面信息
        self.driver.close()  # 关掉详情页
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换回列表页


    def parse_detail_page(self, source):
        html = etree.HTML(source)
        postition_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spns = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spns[0].xpath(".//text()")[0].strip()
        city = job_request_spns[1].xpath(".//text()")[0].strip()
        city = re.sub(r'[\s/]', "", city)
        work_years = job_request_spns[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r'[\s/]', "", work_years)
        education = job_request_spns[3].xpath(".//text()")[0].strip()
        education = re.sub(r'[\s/]', "", education)
        desc = "".join(html.xpath("//div[@class='job-detail']//text()")).strip()
        postition ={
            'name':postition_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }

        self.positions.append(postition)
        print(postition)
        print('='*30)






if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()