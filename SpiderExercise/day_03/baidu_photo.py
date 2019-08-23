import time
import selenium

from selenium import webdriver

# 创建对象
browser = webdriver.Chrome('./chromedriver.exe')
# 打开百度页面
browser.get('http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0')
time.sleep(3)
li_elements = browser.find_elements_by_xpath('//div[@id="imgid"]/div/ul//li')
for li_element in li_elements:
    print(li_element.get_attribute("data-objurl"))
# print(browser.page_source)


browser.quit()