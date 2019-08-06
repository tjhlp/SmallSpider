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
from config import BOOS_URL, REQUEST_HEADERS, TEST_IP_HTML, BOOS_URL_FOLLOW, BOSS_PAGE_NUM

JOB_INFO_POOL_NUM = 4
SAVE_HTML_DIR = 'html/job/'
PROXY_PATH = 'proxy_pool/valid_ip.json'


class RunBossSpider(object):

    def __init__(self, is_proxy=False):
        self.proxy_list = []
        self.is_proxy = is_proxy
        self.url_joblist = []
        self.current_ip = None
        self.__load_proxy()
        self.__generate_url()

    def __load_proxy(self):
        try:
            with open(PROXY_PATH, 'r')as r:
                self.proxy_list = json.loads(r.read())
        except:
            self.proxy_list = []
        print('�������ip:{}��'.format(len(self.proxy_list)))

    def __generate_url(self):
        #  page=2&ka=page-2
        self.url_joblist.append(BOOS_URL)
        for index in range(BOSS_PAGE_NUM):
            self.url_joblist.append(BOOS_URL_FOLLOW + 'page=' + str(index) + '&ka=page-' + str(index))

    def choose_proxy(self):
        # re_proxy_ip = random.choice(self.proxy_list)
        # proxy_ip = re_proxy_ip[0] + ':' + re_proxy_ip[1]
        # ��������
        proxy_ip = '127.0.0.1:1080'
        re_proxy_ip = ["127.0.0.1", "1008"]
        proxies = {
            'http': 'http://' + proxy_ip,
            'https': 'http://' + proxy_ip,
        }
        return re_proxy_ip, proxies

    def get_html(self, url):
        if self.is_proxy:
            # ���Դ���ip����
            count = 1
            re_proxy_ip, proxies = self.choose_proxy()
            while True:
                try:
                    response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
                except:
                    print('��{}����Ч��{}'.format(count, re_proxy_ip))
                    if count >= 3:
                        self.proxy_list.remove(re_proxy_ip)
                        save_job_json(self.proxy_list, PROXY_PATH, update=True)
                        if not len(self.proxy_list):
                            # raise RejectedException('�ܾ��������࣬����ip����')
                            self.proxy_list.append(["127.0.0.1", "1008"])
                            print('�ܾ��������࣬����ip����,���ñ�������ip')
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
                        return '{}���ݱ�����'.format(re_proxy_ip)

        else:
            response = requests.get(url, headers=REQUEST_HEADERS)
            if response.status_code == 200:
                return response.text
            else:
                raise RejectedException('���ʱ��ܾ�')

    def parse_one_url(self, url_list):
        present_name = threading.current_thread().name
        _job_list = []
        index = 1
        for url in url_list:
            time.sleep(random.randint(2, 6))
            print('{}����������{}��ҳ�棺{}'.format(present_name, index, url))
            job_html = self.get_html(url)

            # ����html
            filename = SAVE_HTML_DIR + str(index) + present_name[-2:] + "_html.txt"
            save_text_file(filename, job_html)

            job_info = parse_one_job(job_html)
            _job_list.append(job_info)
            save_job_json(_job_list, datetime.now().strftime('%Y%m%d-%H-%M') + '_job_info.json')
            index += 1
        return _job_list

    def test_proxy(self):
        # ��������
        re_proxy_ip, proxies = self.choose_proxy()
        response = requests.get(TEST_IP_HTML, headers=REQUEST_HEADERS, proxies=proxies)
        return response.text

    @staticmethod
    def read_html(file):
        """�ֶ���ȡjob��html�ļ�"""
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
        """���߳�"""
        pool = ThreadPoolExecutor(max_workers=JOB_INFO_POOL_NUM)
        get_data = len(url_list)
        # ʹ���̳߳�
        for index in range(1, JOB_INFO_POOL_NUM + 1):
            time.sleep(random.randint(1, 4))
            data_size_back = int(get_data / JOB_INFO_POOL_NUM * index)
            data_size_forward = int(get_data / JOB_INFO_POOL_NUM * (index - 1))
            divided_data = url_list[data_size_forward:data_size_back]
            future = pool.submit(self.parse_one_url, divided_data)
        pool.shutdown()

    def run(self):
        """�ȵõ�ҳ�����jobְλ��Ϣ����ַ"""
        temp_list = []
        for job_url in self.url_joblist:
            while True:
                time.sleep(random.randint(2, 4))
                html_content = self.get_html(job_url)
                # print(html_content)
                url_list = parse_one_page(html_content)
                if len(url_list):
                    # print('{}���joblist���ݳɹ�'.format(self.current_ip))
                    temp_list.extend(url_list)
                    break
                else:
                    pass
                    # print('{}���joblist����ʧ��'.format(self.current_ip))
        # print(temp_list)
        # �������߳���ȡ temp list
        self.multi_thread(temp_list)


if __name__ == '__main__':
    boss_spi = RunBossSpider(is_proxy=True)
    boss_spi.run()
    # print(boss_spi.test_proxy())

