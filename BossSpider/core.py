import requests

from html_control import parse_one_job, parse_one_page
from config import BOOS_URL, REQUEST_HEADERS,PROXY_TEST_URL
from proxy_pool.core import RunProxy


class RunBossSpider(object):

    def __init__(self):
        self.proxy_per = None
        self.__start_proxy()

    def __start_proxy(self):
        self.proxy_per = RunProxy('proxy_pool/ip2.csv')
        self.proxy_per.run()

    def get_html(self, url):
        # proxy = self.proxy_per.get_ip()
        proxies = {
            'http': 'http://' + PROXY_TEST_URL,
            'https': 'https://' + PROXY_TEST_URL,
        }
        response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None

    def run(self):
        _job_list = []
        html_content = self.get_html(BOOS_URL)
        url_list = parse_one_page(html_content)
        for url in url_list:
            job_html = self.get_html(url)
            job_info = parse_one_job(job_html)
            _job_list.append(job_info)
        return _job_list


if __name__ == '__main__':
    boss_spi = RunBossSpider()
    print(boss_spi.get_html('http://httpbin.org/get'))
    # print(boss_spi.run())
