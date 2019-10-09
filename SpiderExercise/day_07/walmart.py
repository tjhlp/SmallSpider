import gevent.monkey
import time
import re
from queue import Queue

gevent.monkey.patch_all()
from gevent.pool import Pool

from walmart_details import getitemdetai
from config import SEARCH_NAME, FILE_NAME, PAGE, HTML, PAGE_DETAIL_MAX
from init import browser
from tool import write_csv, generate_url


url_list = generate_url(HTML, PAGE, SEARCH_NAME)


class WalmartSpider:

    def __init__(self):

        self.pool = Pool(5)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

        # 专门存放 url 容器
        self.url_queue = Queue()

    def generate_url(self):
        return generate_url(HTML, PAGE, SEARCH_NAME)

    def main(html):
        item_range = 0
        try:
            # 页面路径样本（按照关键词）
            browser.get(html)
            # 页面路径样本（按照分类）
            # browser.get(html.format(count))
        except:
            pass
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
            main_image = li.find_element_by_xpath('.//div[@class="search-result-productimage gridview"]/div/a/img'). \
                get_attribute("data-image-src")
            star = pattern.group(1)
            reviews = pattern.group(2)
            id_href = li.find_element_by_xpath(
                './/div[@class="search-result-productimage gridview"]/div/a').get_attribute(
                "href")
            # 限制爬取详情信息的数量，只爬取item_detail_max条
            if item_range < PAGE_DETAIL_MAX:
                item_detail = getitemdetai(id_href)
            else:
                item_detail = {'brand': '-', 'category': '-', 'highlights': '-'}
            item_range = item_range + 1

            # try:
            #     shop_name = li.find_element_by_xpath('.//span[@class="marketplace-sold-by-company-name"]').text
            # except Exception as e:
            #     shop_name = 'none'

            wal_id = id_href[id_href.rfind('/') + 1:]
            data = [item_range, wal_id, id_href, name, price, star, reviews, page_id, item_detail['store'], main_image,
                    item_detail['brand'], item_detail['category'], item_detail['highlights']]
            mult_data.append(data)

        time.sleep(1)

    def exec_task_finished(self, result):
        print("result:", result)
        print("执行任务完成")
        self.pool.apply_async(self.exec_task, callback=self.exec_task_finished)

    def run(self):
        for i in range(5):
            pool.apply_async(self.exec_task_finished, callback=self.exec_task_finished)
        url_queue.join()


indexes = ['Range', 'Id', 'Url', 'Name', 'Price', 'Star', 'Review', 'Page', 'Shop name', 'Main image url', 'brand',
           'category', 'highlights']
print(mult_data)
write_csv(indexes, mult_data, FILE_NAME)
browser.quit()
