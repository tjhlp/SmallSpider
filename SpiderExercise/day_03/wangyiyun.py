# 导入显性等待的API需要的模块
# 1> 等待对象模块
import time

from selenium.webdriver.support.wait import WebDriverWait
# 2> 导入等待条件模块
from selenium.webdriver.support import expected_conditions as EC
# 3> 导入查询元素模块
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

browser.get('https://www.baidu.com')

browser.find_element_by_id('kw').send_keys('网易云音乐')
browser.find_element_by_id('su').click()

wait = WebDriverWait(browser, 60, 0.5)
url_element = wait.until(EC.presence_of_element_located((By.ID, '1')))
url_element.find_element_by_xpath('.//h3[@class="t"]/a').click()

# 切换窗口
browser.switch_to.window(browser.window_handles[1])

url_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-module="playlist"]')))
url_element.find_element_by_xpath('//a[@data-module="playlist"]').click()

# 切换iframe窗口
iframe_element = browser.find_element_by_id('g_iframe')
browser.switch_to.frame(iframe_element)
li_elements = browser.find_elements_by_xpath('//ul[@id="m-pl-container"]//li')
for li_element in li_elements:
    item ={}
    item['title'] = li_element.find_element_by_xpath('.//p[@class="dec"]/a').text
    item['author'] = li_element.find_element_by_xpath('.//a[@class="nm nm-icn f-thide s-fc3"]').text
    print(item)
browser.quit()












