from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome('d:/chromedriver.exe')
# driver.set_window_size(1366, 1080)
#
#
# driver.get('https://www.baidu.com/')
# #  行为链
# # inputTag = driver.find_element_by_id('kw')
# # submitBtn = driver.find_element_by_id('su')
# #
# # actions = ActionChains(driver)
# # actions.move_to_element(inputTag)
# # actions.send_keys_to_element(inputTag, 'python')
# # actions.move_to_element(submitBtn)
# # actions.click(submitBtn)
# # actions.perform()
#
# # 打开一个新页面
# driver.execute_script("window.open('https://www.douban.com')")
# print(driver.window_handles)
# # 切换新窗口
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)


# 代理
driver_path = r'D:/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://59.32.37.25:3128")

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)


driver.get('http://www.baidu.com')
submitBtn = driver.find_element_by_id('su')
print(submitBtn.get_attribute('value'))
driver.save_screenshot()



