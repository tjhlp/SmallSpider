#!/usr/bin/python3
# -*- coding: utf-8 -*-

REDIS_HOST = '192.168.146.134'
REDIS_PORT = 6379
PROXIES_REDIS_KEY = "proxies"
    
PROXIES_SPIDERS = [
    # "spiders.daili66.Daili66ProxySpider",
    "spiders.kuaidaili.KuaidailiSpider"
]