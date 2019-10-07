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

html = 'https://www.walmart.com/ip/Ball-Projector-DJ-Remote-7-3w-Activated-Control-Ktaxon-Party-Lights-Light-Lighting-Stage-Lamp-Color-bulb-Led-Sound-Change-Wedding-Disco-Effect-Show-S/125275699'

browser.get(html)

li_list = browser.find_elements_by_xpath('.//ol[@class="breadcrumb-list"]//li')
shop_name = browser.find_element_by_xpath('./a[@class="prod-brandName"]/span').text
shop_highlights = browser.find_element_by_xpath('.//div[@data-tl-id="ProductPage-ProductHighlights"]/div/ul//li')

highlight_list = [highlight.text for highlight in shop_highlights]
name_list = [li.find_element_by_xpath('./a/span').text for li in li_list]
print(highlight_list)
print(name_list)
print(shop_name)
browser.quit()
