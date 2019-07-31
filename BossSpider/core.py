import requests, os, json
import random
import time

from html_control import parse_one_job, parse_one_page
from file_control import save_text_file
from config import BOOS_URL, REQUEST_HEADERS, TEST_IP_HTML


class RunBossSpider(object):

    def __init__(self):
        self.proxy_list = []
        self.__start_proxy()

    def __start_proxy(self):
        basic_path = 'proxy_pool/valid_ip/'
        for filename in os.listdir(basic_path):
            with open(basic_path + filename, 'r')as r:
                content = json.loads(r.read())
                for ip_port in content:
                    self.proxy_list.append(ip_port)
        # print(self.proxy_list)

    def get_html(self, url):
        while True:
            re_proxy_ip = random.choice(self.proxy_list)
            proxy_ip = re_proxy_ip[0] + ':' + re_proxy_ip[1]
            proxies = {
                'http': 'http://' + proxy_ip,
                'https': 'http://' + proxy_ip,
            }
            try:
                # response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
                response = requests.get(url, headers=REQUEST_HEADERS)
            except:
                print('无效ip：{}'.format(proxy_ip))
                continue
            else:
                print(proxy_ip)
                if response.status_code == 200:
                    return response.text
            finally:
                self.proxy_list.remove(re_proxy_ip)
                if not len(self.proxy_list):
                    break
        return RuntimeError('ip用完，拒绝访问')

    def run(self):
        html_content = self.get_html(BOOS_URL)
        url_list = parse_one_page(html_content)
        self.parse_one_url(url_list)

    def parse_one_url(self, url_list):
        _job_list = []
        for url in url_list:
            time.sleep(2)
            print('正在搜索：{}'.format(url))
            job_html = self.get_html(url)
            job_info = parse_one_job(job_html)
            _job_list.append(job_info)
        save_text_file('job_info.txt', _job_list)
        return _job_list


if __name__ == '__main__':
    boss_spi = RunBossSpider()
    # print(boss_spi.get_html(TEST_IP_HTML))
    print(boss_spi.run())
