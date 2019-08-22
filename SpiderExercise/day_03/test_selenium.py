# 导入显性等待的API需要的模块
# 1> 等待对象模块
from selenium.webdriver.support.wait import WebDriverWait
# 2> 导入等待条件模块
from selenium.webdriver.support import expected_conditions as EC
# 3> 导入查询元素模块
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys('百度一下')
browser.find_element_by_id('su').click()

# time.sleep(1)
# browser.find_element_by_xpath('//div[@id="2"]//h3//a').click()
wait = WebDriverWait(browser, 60, 0.1)
url_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="2"]//h3//a')))
url_element.click()

print(browser.title)
browser.switch_to.window(browser.window_handles[1])
print(browser.title)
# time.sleep(3)
browser.quit()
