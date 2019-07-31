import pandas as pd
import numpy as np
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import time

from config import PROXY_URL_BASIC, PAGE_NUM, PROXY_URLS

from proxy_pool.control import get_html, get_page_ip, test_ip


class RunProxy(object):
    """获取代理ip，先运行run方法，以后拿ip可以直接运行get_ip方法"""

    def __init__(self, filename, model=False):
        self.model = model
        self.filename = filename
        self.df_ip = None
        self.ip = None
        self.port = None
        self.__generate_url()

    @staticmethod
    def __generate_url():
        for page in range(1, PAGE_NUM):
            result_page = ''
            if page:
                result_page = str(page)
            PROXY_URLS.append(PROXY_URL_BASIC + result_page)

    def run(self):
        if self.model:
            for proxy_url in PROXY_URLS:
                time.sleep(2)
                print('正在搜索:{}'.format(proxy_url))
                ip_lists = get_page_ip(proxy_url)
                df_ip_ports = pd.DataFrame(ip_lists)
                raw_data = pd.concat([self.df_ip, df_ip_ports], axis=0)
                self.df_ip = raw_data.reset_index(drop=True)
            self.df_ip.to_csv(self.filename)
        else:
            self.df_ip = pd.read_csv(self.filename, index_col=0)
            # print(self.df_ip)

    def get_ip(self):
        """返回ip和端口地址"""
        if self.df_ip is not None:
            rd_num = random.randint(0, self.df_ip.size)
            ip_list = eval(self.df_ip.iloc[rd_num][0])
            self.ip = ip_list[0]
            self.port = str(ip_list[1])
            get_ip_port = self.ip + ':' + self.port
            return get_ip_port
        return ReferenceError('你必须先运行run方法')

    def process(self):
        # args是关键字参数，需要加上名字，写成args=(self,)
        th1 = threading.Thread(target=RunProxy.run, args=(self,))
        th1.start()
        th1.join()

    @staticmethod
    def run_test_ip():
        """双线程测试ip"""
        # 创建一个包含2条线程的线程池
        pool = ThreadPoolExecutor(max_workers=2)
        get_data = pd.read_csv('ip.csv', index_col=0)
        # print(get_data)
        data_size = int(get_data.size/2)
        th1_data = get_data[:data_size]
        th2_data = get_data[data_size:]
        future1 = pool.submit(test_ip, th1_data)
        future2 = pool.submit(test_ip, th2_data)
        pool.shutdown()


if __name__ == '__main__':
    proxy_per = RunProxy('ip.csv')
    # proxy_per = RunProxy('ip.csv', model=True)
    proxy_per.run()
    proxy_per.run_test_ip()
