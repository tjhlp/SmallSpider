import csv
from multiprocessing.dummy import Pool
import requests
from lxml import etree
from threading import Thread
from queue import Queue
import time


def time_counter(func):
    def inner(self, *args, **kwargs):
        start_time = time.time()
        res = func(self, *args, **kwargs)
        end_time = time.time()
        print('总共用时: ', (end_time - start_time))
        return res

    return inner


class WangYISpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.proxies = {'https': 'http://127.0.0.1:1080'}
        self.filename = 'data1.csv'
        self.pool = Pool(5)
        self.url_queue = Queue()

    def get_url_list(self):
        for page in range(1, 13):
            url = self.url.format(page)
            self.url_queue.put(url)

    def exec_task(self):

        url = self.url_queue.get()
        html = requests.get(url, headers=self.headers, proxies=self.proxies)
        eroot = etree.HTML(html.text)
        li_elements = eroot.xpath('//a[@class="recmd-content"]/text()')
        for li_element in li_elements:
            item = {}
            item['title'] = li_element
            # print(item)
        self.url_queue.task_done()

    def exec_task_finished(self, result):
        print("执行任务完成")
        return self.pool.apply_async(self.exec_task, callback=self.exec_task_finished)

    @time_counter
    def run(self):
        self.get_url_list()

        for i in range(5):
            self.pool.apply_async(self.exec_task, callback=self.exec_task_finished)

        self.url_queue.join()
        time.sleep(1)

if __name__ == '__main__':
    spider = WangYISpider()
    spider.run()
