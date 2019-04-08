from selenium import webdriver
import time

driver = webdriver.Chrome('d:/chromedriver.exe')
driver.set_window_size(1366, 1080)


driver.get('https://www.bilibili.com/v/game/esports/?spm_id_from=333.8.b_7375626e6176.3#/')
print(driver.find_element_by_xpath('//ul[@class="vd-list mod-2"]/li//a[@class="title"]').text)

# 翻页
driver.find_element_by_xpath('//button[@class="nav-btn iconfont icon-arrowdown3"]').click()


# 数据加载需要时间
time.sleep(3)

print(driver.find_element_by_xpath('//ul[@class="vd-list mod-2"]/li//a[@class="title"]').text)

driver.quit()