# -*- coding: utf-8 -*-
import scrapy
from itcast.items import YgItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    base_url = 'http://wz.sun0769.com/index.php/question/report?page={}'

    def start_requests(self):
        for page in range(0, 150, 30):
            yield scrapy.Request(
                url=self.base_url.format(page)
            )

    def parse(self, response):
        tr_list = response.xpath('//td[@class="t12wh"]/..')
        for tr in tr_list:
            item = YgItem()
            item['num'] = tr.xpath('./td[1]/text()').extract_first()
            item['title'] = tr.xpath('./td[2]/a[2]/text()').extract_first()
            item['status'] = tr.xpath('./td[3]/span/text()').extract_first()
            item['author'] = tr.xpath('./td[4]/text()').extract_first()
            item['time'] = tr.xpath('./td[5]/text()').extract_first()
            yield item
