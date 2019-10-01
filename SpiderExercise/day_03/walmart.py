# 导入显性等待的API需要的模块
# 1> 等待对象模块
import time
import re
from selenium import webdriver

options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

browser.get('https://www.walmart.com/search/?cat_id=0&query=audio')
browser.execute_script("var q=document.documentElement.scrollTop=100000" )

# time.sleep(2)

li_list = browser.find_elements_by_xpath('//ul[@class="search-result-gridview-items four-items"]/li')
for li in li_list:
    name = li.find_element_by_xpath('.//div[@class="search-result-product-title gridview"]/a').get_attribute("title")
    try:
        price = li.find_element_by_xpath('.//span[@class="price-main-block"]/span/span').text
    except Exception as e:
        price = 'none'
    star_rev = li.find_element_by_xpath('.//div[@class="stars stars-small"]/span').get_attribute("aria-label")
    print(star_rev)
    print(star_rev[:star_rev.find('Stars')])


browser.quit()

