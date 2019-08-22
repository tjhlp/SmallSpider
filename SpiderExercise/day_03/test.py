import time
import selenium

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建对象
browser = webdriver.Chrome('./chromedriver.exe')
# 打开百度页面
browser.get('https://www.baidu.com')
# 输入斗鱼
input_element = browser.find_element_by_xpath('//input[@id="kw"]')
input_element.send_keys('斗鱼')
# 点击确定
input_element = browser.find_element_by_xpath('//input[@id="su"]')
input_element.click()

# # 进入斗鱼平台
browser.implicitly_wait(1)
# time.sleep(2)
# enter_element = browser.find_element_by_xpath('//h3[@class="t"]/a').click()
enter_element = browser.find_element_by_partial_link_text('每个人的直播平台').click()

# 切换窗体 来到斗鱼窗体
browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])
# 点击分类
# print(browser.window_handles)
browser.implicitly_wait(1)
# print(browser.current_window_handle)
print(browser.title)
fenlei_element = browser.find_element_by_link_text('分类').click()

# 点击英雄联盟

browser.implicitly_wait(1)
browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])
print(browser.title)
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
lol_element = browser.find_element_by_xpath('//a[@class="layout-Classify-card secondCateCard"]').click()
time.sleep(1)

browser.quit()