#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree

class KuaidailiSpider():
    '''
    针对快代理进行爬取免费
    
    '''

    def __init__(self):
        pass

    def get_url_list(self):
        return ["https://www.kuaidaili.com/free/inha/{}/".format(i) for i in range(1,100)]


    def get_proxies(self):

        '''
        内部需要 yield 向上层提交IP代理
        
        :return: 
        '''
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        for url in self.get_url_list():

            response = requests.get(url,headers=headers)
            eroot = etree.HTML(response.text)
            tr_list = eroot.xpath('//table[@class="table table-bordered table-striped"]//tr')

            for tr in tr_list:
                td_list = tr.xpath('./td/text()')
                if td_list is None or len(td_list) == 0:
                    continue
                type = td_list[3]
                ip = td_list[0]
                port = td_list[1]
                yield "{}://{}:{}".format(type.lower(),ip, port)


