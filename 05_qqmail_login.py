from selenium import webdriver
import time


driver = webdriver.Chrome('d:/chromedriver.exe')
driver.set_window_size(1366, 1080)


driver.get('https://mail.qq.com/')

# 切换到iframe
driver.switch_to.frame('login_frame')

driver.find_element_by_id('u').send_keys('')
driver.find_element_by_id('p').send_keys('')
driver.find_element_by_id('login_button').click()

time.sleep(3)

driver.quit()
