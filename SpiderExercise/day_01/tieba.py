from pprint import pprint
from lxml import etree
import requests


class TiebaSpider(object):
    def __init__(self, kw, max_pn):
        self.kw = kw
        self.max_pn = max_pn
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36",
        }

    def generate_url(self):
        return [self.url.format(self.kw, page) for page in range(0, self.max_pn, 30)]

    def run(self):
        page_url_list = self.generate_url()
        for page_url in page_url_list:
            html = requests.get(url=page_url, headers=self.headers)
            eroot = etree.HTML(html.content.decode('utf-8'))
            li_elements = eroot.xpath('//li[@class="tl_shadow tl_shadow_new "]')
            for li_element in li_elements:
                item = {}
                item['title'] = li_element.xpath('.//div[@class="ti_title"]/span/text()')
                item['author'] = li_element.xpath('.//span[@class="ti_author"]/text()')
                item['img'] = li_element.xpath('.//div[@class="medias_wrap ordinary_thread clearfix"]//@data-url')
                print(item)
            break


if __name__ == '__main__':
    spider = TiebaSpider('抗压', 150)
    spider.run()
