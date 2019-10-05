import time
import re
from selenium import webdriver
import csv


def write_csv(index, mult_data, filename):
    """

    :param index: 列名（list）
    :param mult_data: 写入的数据（二维列表）
    :return:
    """
    with open(filename, 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(index)
        for data in mult_data:
            writer.writerow(data)


# 初始化驱动程序
options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
# options.add_argument('--headless')  # 开启无界面模式
# options.add_argument('--disable-gpu')  # 禁用gpu，解决一些莫名的问题
# 导入驱动程序
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

# 输入关键词
search = 'Party Lights'
# 需要爬取的页面数量
page = 2
# 存储的文件名
filename = search + '.csv'
# 页面路径样本（按照关键词）
html = 'https://www.walmart.com/search/?cat_id=0&page={}&ps=40&query={}'
# 页面路径样本（按照分类）
# html = 'https://www.walmart.com/browse/musical-instruments/par-cans/7796869_3896240_1725737?page={}'


mult_data = []
count = 1
while count <= page:
    try:
        print(html.format(count, search))
        # 页面路径样本（按照关键词）
        browser.get(html.format(count, search))
        # 页面路径样本（按照分类）
        # browser.get(html.format(count))
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
