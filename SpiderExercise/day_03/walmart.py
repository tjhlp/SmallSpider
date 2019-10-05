# 导入显性等待的API需要的模块
import time
import re
from selenium import webdriver

from day_03.csv_control import write_csv


options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
options.add_argument('--headless') # 开启无界面模式
options.add_argument('--disable-gpu') # 禁用gpu，解决一些莫名的问题
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

# time.sleep(2)
html = 'https://www.walmart.com/search/?cat_id=0&page={}&ps=40&query={}'
search = 'LED Stage lights'
mult_data = []
page = 25
filename = search + '.csv'

count = 1
while count <= page:
    try:
        browser.get(html.format(count,search))
    except:
        break
    browser.execute_script("var q=document.documentElement.scrollTop=100000")
    li_list = browser.find_elements_by_xpath('//ul[@class="search-result-gridview-items four-items"]/li')
    for li in li_list:
        name = li.find_element_by_xpath('.//div[@class="search-result-product-title gridview"]/a').get_attribute(
            "title")
        try:
            price = li.find_element_by_xpath('.//span[@class="price-main-block"]/span/span').text
        except Exception as e:
            price = 'none'
        star_rev = li.find_element_by_xpath('.//div[@class="stars stars-small"]/span').get_attribute("aria-label")
        pattern = re.match('(.*?)Stars. (.*?)reviews', star_rev)
        star = pattern.group(1)
        reviews = pattern.group(2)
        id_http = li.find_element_by_xpath('.//div[@class="search-result-productimage gridview"]/div/a').get_attribute(
            "href")
        wal_id = id_http[id_http.rfind('/') + 1:]
        page_id = count
        data = [wal_id, name, price, star, reviews, page_id]
        mult_data.append(data)

    print('第{}页爬取完成'.format(count))
    count += 1
    time.sleep(0.5)

indexes = ['id', 'name', 'price', 'star', 'review', 'page']
print(mult_data)
write_csv(indexes, mult_data, filename)
browser.quit()
