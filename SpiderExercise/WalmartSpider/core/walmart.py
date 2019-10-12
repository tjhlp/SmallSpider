import gevent.monkey

gevent.monkey.patch_all()
from gevent.pool import Pool

import time
import re
import random
from queue import Queue
from core.walmart_details import getitemdetai
from core.config import SEARCH_NAME, FILE_NAME, PAGE, HTML, PAGE_DETAIL_MAX, INDEXES
from core.init import _init_Chrome
from core.tool import write_csv, generate_url, count_time


class WalmartSpider:

    def __init__(self):

        # 创建线程池，初始化线程数量
        self.pool = Pool(5)
        # 头部用户
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        # 专门存放 url 容器
        self.url_queue = Queue()
        # 存放数据
        self.res_data = Queue()

    def generate_url(self):
        """生成url容器"""
        url_list = generate_url(HTML, PAGE, SEARCH_NAME)
        for url in url_list:
            self.url_queue.put(url)

    @count_time
    def exec_task(self):
        get_data = self.url_queue.get()
        browser = _init_Chrome()
        cur_page = get_data[0]
        url = get_data[1]
        print('第{}页开始采集数据'.format(cur_page))
        mult_data = []
        item_range = 0
        try:
            # 页面路径样本（按照关键词）
            browser.get(url)
        except:
            return 0
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
            if item_range <= PAGE_DETAIL_MAX:
                item_detail = getitemdetai(id_href)
            else:
                item_detail = {'brand': '-', 'category': '-', 'highlights': '-'}
            item_range = item_range + 1

            # try:
            #     shop_name = li.find_element_by_xpath('.//span[@class="marketplace-sold-by-company-name"]').text
            # except Exception as e:
            #     shop_name = 'none'

            wal_id = id_href[id_href.rfind('/') + 1:]
            data = [item_range, wal_id, id_href, name, price, star, reviews, cur_page, main_image,
                    item_detail['brand'], item_detail['category'], item_detail['highlights']]
            mult_data.append(data)
        browser.quit()
        set_data = {str(cur_page): mult_data}
        self.res_data.put(set_data)
        time.sleep(random.randint(1, 3))
        self.url_queue.task_done()
        return cur_page

    def exec_task_finished(self, result):
        if result != 0:
            print("第{}页数据采集完成:".format(result))
        else:
            print("第{}页数据采集失败:".format(result))
        self.pool.apply_async(self.exec_task, callback=self.exec_task_finished)

    def save_data(self):
        mult_data = []
        res_dict = {}
        while self.res_data.empty() is False:
            get_data = self.res_data.get().popitem()
            res_dict[get_data[0]] = get_data[1]
        print(res_dict)
        for i in range(1, PAGE + 1):
            mult_data.append(str(res_dict[i]))
        write_csv(INDEXES, mult_data, FILE_NAME)

    def run(self):
        self.generate_url()
        for i in range(5):
            self.pool.apply_async(self.exec_task, callback=self.exec_task_finished)
        time.sleep(1)
        self.url_queue.join()
        print("第{}页爬取完成:".format(PAGE))
        self.save_data()


if __name__ == '__main__':
    walmart = WalmartSpider()
    walmart.run()
