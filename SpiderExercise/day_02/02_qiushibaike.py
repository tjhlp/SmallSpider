import time
import requests
from lxml import etree
import csv
from pprint import pprint


def time_counter(func):
    def inner(self, *args, **kwargs):
        start_time = time.time()
        res = func(self, *args, **kwargs)
        end_time = time.time()
        print('总共用时: ' ,(end_time - start_time))
        return res

    return inner


class WangYISpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.proxies = {'https': 'http://127.0.0.1:1080'}
        self.filename = 'data.csv'

    def get_url_list(self):
        return [self.url.format(page) for page in range(1, 13)]

    def get_html(self, url):
        html = requests.get(url, headers=self.headers, proxies=self.proxies)
        if html.status_code == 200:
            return html.text
        else:
            return None

    @staticmethod
    def get_item(html):
        item_list = []
        eroot = etree.HTML(html)
        li_elements = eroot.xpath('//a[@class="recmd-content"]/text()')
        for li_element in li_elements:
            item = {}
            item['title'] = li_element
            item_list.append(item)
        return item_list

    def save_item(self, item_list):
        # print(item_list)
        pass
        # f = open(self.filename, 'w', encoding='utf-8')
        # csv_writer = csv.writer(f)
        # csv_writer.writerow(item_list[0].keys())
        # for item in item_list:
        #     csv_writer.writerow(item.values())
        # f.close()

    @time_counter
    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html = self.get_html(url)
            item_list = self.get_item(html)
            self.save_item(item_list)


if __name__ == '__main__':
    # 1.1290369033813477
    spider = WangYISpider()
    spider.run()
