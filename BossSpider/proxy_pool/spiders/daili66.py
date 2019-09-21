#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree

class Daili66ProxySpider(object):

    def get_url_list(self):
        return ["http://www.66ip.cn/{}.html".format(i) for i in range(1,100)]


    def get_proxies(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Referer":"http://www.66ip.cn/1.html",
            'Cookie':"yd_cookie=255a3b09-5568-45172e7787d693f61d1d3b254a0a3045a976; _ydclearance=4d377e346fce8ff9dd1fbcef-5871-4a4c-823d-c23832da17fa-1548377811; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1548370612; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1548370612"
        }
        for url in self.get_url_list():
            response = requests.get(url,headers=headers)
            print(response.text)
            edata = etree.HTML(response.text)
            rows = edata.xpath('//table//tr')
            for idx in range(2,len(rows)):
                row = rows[idx]
                ip = row.xpath('./td[1]/text()')[0]
                port = row.xpath('./td[2]/text()')[0]
                yield "http://{}:{}".format(ip,port)
                yield "https://{}:{}".format(ip,port)