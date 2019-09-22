# coding=gbk
import threading
from concurrent.futures import ThreadPoolExecutor

import requests, os, json
import random
import time
from datetime import datetime

from pyquery import PyQuery as pq
from html_control import parse_one_job, parse_one_page, RejectedException
from file_control import save_job_json, save_text_file
from config import BOOS_URL, REQUEST_HEADERS, BOOS_URL_FOLLOW, BOSS_PAGE_NUM

JOB_INFO_POOL_NUM = 4
SAVE_HTML_DIR = 'html/job/'
PROXY_PATH = 'proxy_pool/valid_ip.json'


class RunBossSpider(object):

    def __init__(self, is_proxy=False):
        self.proxy_list = []
        self.is_proxy = is_proxy
        self.url_joblist = []
        self.current_ip = None
        self.__generate_url()
        if self.is_proxy:
            self.__load_proxy()

    def __load_proxy(self):
        try:
            with open(PROXY_PATH, 'r')as r:
                self.proxy_list = json.loads(r.read())
        except:
            self.proxy_list = []
        print('导入代理ip:{}个'.format(len(self.proxy_list)))

    def __generate_url(self):
        #  page=2&ka=page-2
        self.url_joblist.append(BOOS_URL)
        for index in range(BOSS_PAGE_NUM):
            self.url_joblist.append(BOOS_URL_FOLLOW + 'page=' + str(index) + '&ka=page-' + str(index))

    def choose_proxy(self):
        re_proxy_ip = random.choice(self.proxy_list)
        proxy_ip = re_proxy_ip[0] + ':' + re_proxy_ip[1]
        # 本机代理
        proxies = {
            'http': 'http://' + proxy_ip,
            'https': 'http://' + proxy_ip,
        }
        return re_proxy_ip, proxies

    def get_html(self, url):
        """爬虫部分核心程序"""
        if self.is_proxy:
            # 测试代理ip次数
            count = 1
            re_proxy_ip, proxies = self.choose_proxy()
            while True:
                try:
                    response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
                except Exception as e:
                    print('第{}次无效：{}'.format(count, re_proxy_ip))
                    if count >= 3:
                        self.proxy_list.remove(re_proxy_ip)
                        save_job_json(self.proxy_list, PROXY_PATH, update=True)
                        if not len(self.proxy_list):
                            # raise RejectedException('拒绝次数过多，代理ip用完')
                            self.proxy_list.append(["127.0.0.1", "1008"])
                            print('拒绝次数过多，代理ip用完,启用本机代理ip')
                        re_proxy_ip, proxies = self.choose_proxy()
                        count = 1
                        continue
                    else:
                        count += 1
                else:
                    if response.status_code == 200:
                        self.current_ip = re_proxy_ip
                        return response.text
                    else:
                        return '{}数据被拦截'.format(re_proxy_ip)

        else:
            # 本机代理
            proxy_ip = '127.0.0.1:1080'
            proxies = {
                'http': 'http://' + proxy_ip,
                'https': 'http://' + proxy_ip,
            }
            response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
            if response.status_code == 200:
                return response.text
            else:
                raise RejectedException('访问被拒绝')

    def parse_one_url(self, url_list):
        present_name = threading.current_thread().name
        _job_list = []
        index = 1
        for url in url_list:
            time.sleep(random.randint(2, 6))
            print('{}正在搜索第{}个页面：{}'.format(present_name, index, url))
            job_html = self.get_html(url)

            # 保存html
            filename = SAVE_HTML_DIR + str(index) + present_name[-2:] + "_html.txt"
            save_text_file(filename, job_html)

            job_info = parse_one_job(job_html)
            _job_list.append(job_info)
            save_job_json(_job_list, datetime.now().strftime('%Y%m%d-%H-%M') + '_job_info.json')
            index += 1
        return _job_list

    def test_proxy(self):
        # 本机代理
        re_proxy_ip, proxies = self.choose_proxy()
        response = requests.get(TEST_IP_HTML, headers=REQUEST_HEADERS, proxies=proxies)
        return response.text

    @staticmethod
    def read_html(file):
        """手动读取job的html文件"""
        _job_list = []
        paths = os.listdir(file)
        for path in paths:
            path = file + '/' + path
            with open(path, 'r', encoding='utf-8')as r:
                job_html = r.read()
                job_info = parse_one_job(job_html)
                _job_list.append(job_info)
                save_job_json(_job_list, datetime.now().strftime('%Y%m%d-%H-%M') + '_job_info.json')

    def multi_thread(self, url_list):
        """多线程"""
        pool = ThreadPoolExecutor(max_workers=JOB_INFO_POOL_NUM)
        get_data = len(url_list)
        # 使用线程池
        for index in range(1, JOB_INFO_POOL_NUM + 1):
            time.sleep(random.randint(1, 4))
            # 切割数据 等分成n份
            data_size_back = int(get_data / JOB_INFO_POOL_NUM * index)
            data_size_forward = int(get_data / JOB_INFO_POOL_NUM * (index - 1))
            divided_data = url_list[data_size_forward:data_size_back]
            future = pool.submit(self.parse_one_url, divided_data)
        pool.shutdown()

    def generate_url_list(self):
        """先得到页面关于job职位信息的网址"""
        temp_list = []
        # 如果失败 继续爬取数据
        for job_url in self.url_joblist:
            while True:
                time.sleep(random.randint(2, 6))
                html_content = self.get_html(job_url)
                url_list = parse_one_page(html_content)
                if len(url_list):
                    temp_list.extend(url_list)
                    break
                else:
                    time.sleep(1)
        return temp_list

    def run(self):
        """运行BOSS招聘的爬虫"""
        url_list = self.generate_url_list()
        # 开启多线程爬取 temp list
        self.multi_thread(url_list)


if __name__ == '__main__':
    boss_spi = RunBossSpider()
    boss_spi.run()
    # print(boss_spi.test_proxy())
