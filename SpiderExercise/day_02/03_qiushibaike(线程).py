import requests
from lxml import etree
import csv
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
        self.url_list = Queue()
        self.html = Queue()
        self.item = Queue()

    def get_url_list(self):
        for page in range(1, 13):
            url = self.url.format(page)
            self.url_list.put(url)

    def get_html(self):
        while True:
            url = self.url_list.get()
            html = requests.get(url, headers=self.headers, proxies=self.proxies)
            self.html.put(html.text)
            self.url_list.task_done()

    def get_item(self):

        while True:
            html = self.html.get()
            eroot = etree.HTML(html)
            li_elements = eroot.xpath('//a[@class="recmd-content"]/text()')
            for li_element in li_elements:
                item = {}
                item['title'] = li_element
                # print(item)
                # item_list.append(item)
                self.item.put(item)
            self.html.task_done()

    def save_item(self):
        while True:
            item_list = self.item.get()
            print(item_list)
            # print("*" * 100)
            # f = open(self.filename, 'w', encoding='utf-8')
            # csv_writer = csv.writer(f)
            # print(item_list)
            # csv_writer.writerow(item_list[0].keys())
            # for item in item_list:
            #     csv_writer.writerow(item.values())
            # f.close()
            self.item.task_done()

    @time_counter
    def run(self):
        tasks = []
        tasks.append(Thread(target=self.get_url_list))
        for i in range(3):
            tasks.append(Thread(target=self.get_html))
        for i in range(5):
            tasks.append(Thread(target=self.get_item))
        for i in range(6):
            tasks.append(Thread(target=self.save_item))

        for task in tasks:
            task.setDaemon(True)
            task.start()

        time.sleep(1)
        self.url_list.join()
        self.html.join()
        self.item.join()


if __name__ == '__main__':
    spider = WangYISpider()
    spider.run()
