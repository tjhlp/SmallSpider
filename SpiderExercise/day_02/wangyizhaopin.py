import requests
from bs4 import BeautifulSoup
import csv


class WangYISpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        self.url = 'https://hr.163.com/position/list.do?currentPage={}'
        self.proxies = {'http': 'http://127.0.0.1:1080'}
        self.filename = 'data.csv'

    def get_url_list(self):
        return [self.url.format(page) for page in range(1, 134)]

    def get_html(self, url):
        html = requests.get(url, headers=self.headers)
        if html.status_code == 200:
            return html.text
        else:
            return None

    @staticmethod
    def get_item(html):
        soup = BeautifulSoup(html, 'lxml')
        part_info = soup.select(".position-tb")[0].tbody.select("tr")
        item = {}
        item_list = []
        for index in range(0, len(part_info), 2):
            info = part_info[index]
            detail_info = info.select('td')
            item['name'] = detail_info[0].get_text().strip()
            item['department'] = detail_info[1].get_text()
            item['category'] = detail_info[2].get_text()
            item['type'] = detail_info[3].get_text()
            item['location'] = detail_info[4].get_text()
            item['number'] = detail_info[5].get_text().strip()
            item['date'] = detail_info[6].get_text().strip()

            back_info = part_info[index + 1].select(".position-detail")[0]
            item['background'] = back_info.select("ul li")[0].get_text()
            item['year'] = back_info.select("ul li")[1].get_text()
            item['description'] = back_info.select("div > p")[0].get_text().strip()
            item['require'] = back_info.select("div > p")[1].get_text().strip()

            item_list.append(item)
        return item_list

    def save_item(self, item_list):
        f = open(self.filename, 'w', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(item_list[0].keys())
        for item in item_list:
            csv_writer.writerow(item.values())
        f.close()

    def run(self):
        url_list = self.get_url_list()
        item_sum = []
        for url in url_list:
            html = self.get_html(url)
            item_list = self.get_item(html)
            item_sum.extend(item_list)
        self.save_item(item_sum)
            # break


if __name__ == '__main__':
    spider = WangYISpider()
    spider.run()
