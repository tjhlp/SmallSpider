# coding=gbk
import threading
from concurrent.futures import ThreadPoolExecutor

import requests, os, json
import random
import time
from datetime import datetime

from html_control import parse_one_job, parse_one_page
from file_control import save_job_json, save_text_file
from config import BOOS_URL, REQUEST_HEADERS, TEST_IP_HTML

JOB_INFO_POOL_NUM = 2
SAVE_HTML_DIR = 'html/job/'


class RunBossSpider(object):

    def __init__(self, is_proxy=False):
        self.proxy_list = []
        self.__load_proxy()
        self.is_proxy = is_proxy

    def __load_proxy(self):
        basic_path = 'proxy_pool/valid_ip.json'
        with open(basic_path, 'r')as r:
            self.proxy_list = json.loads(r.read())
        # print(self.proxy_list)

    def get_html(self, url):
        while True:
            re_proxy_ip = random.choice(self.proxy_list)
            proxy_ip = re_proxy_ip[0] + ':' + re_proxy_ip[1]
            # 本机代理
            # proxy_ip = '127.0.0.1:1080'
            proxies = {
                'http': 'http://' + proxy_ip,
                'https': 'http://' + proxy_ip,
            }
            try:
                if self.is_proxy:
                    response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
                    print(proxy_ip)
                else:
                    response = requests.get(url, headers=REQUEST_HEADERS)
            except:
                print('无效ip：{}'.format(proxy_ip))
                continue
            else:
                if response.status_code == 200:
                    return response.text
            finally:
                if self.is_proxy:
                    self.proxy_list.remove(re_proxy_ip)
                    if not len(self.proxy_list):
                        break
        return RuntimeError('ip用完，拒绝访问')

    def parse_one_url(self, url_list):
        present_name = threading.current_thread().name
        _job_list = []
        index = 1
        for url in url_list:
            time.sleep(random.randint(2, 6))
            print('{}正在搜索第{}个：{}'.format(present_name, index, url))
            job_html = self.get_html(url)

            # 保存html
            filename = SAVE_HTML_DIR + str(index) + present_name[-2:] + "_html.txt"
            save_text_file(filename, job_html)

            job_info = parse_one_job(job_html)
            _job_list.append(job_info)
            save_job_json(_job_list, datetime.now().strftime('%Y%m%d-%H-%M') + '_job_info.json')
            index += 1
        return _job_list

    def multi_thread(self, url_list):
        pool = ThreadPoolExecutor(max_workers=JOB_INFO_POOL_NUM)
        get_data = len(url_list)
        # 使用线程池
        for index in range(1, JOB_INFO_POOL_NUM + 1):
            data_size_back = int(get_data / JOB_INFO_POOL_NUM * index)
            data_size_forward = int(get_data / JOB_INFO_POOL_NUM * (index - 1))
            th_data = url_list[data_size_forward:data_size_back]
            future = pool.submit(self.parse_one_url, th_data)
        pool.shutdown()

    def run(self):
        html_content = self.get_html(BOOS_URL)
        url_list = parse_one_page(html_content)
        print(url_list[:10])
        self.multi_thread(url_list[:10])


if __name__ == '__main__':
    boss_spi = RunBossSpider(is_proxy=True)
    # # print(boss_spi.get_html(TEST_IP_HTML))
    boss_spi.run()
