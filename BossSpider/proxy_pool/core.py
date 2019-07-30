import pandas as pd
import random
import threading

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
        for page in range(PAGE_NUM):
            result_page = ''
            if page:
                result_page = str(page)
            PROXY_URLS.append(PROXY_URL_BASIC + result_page)
        # print(PROXY_URLS)

    def run(self):
        if self.model:
            for proxy_url in PROXY_URLS:
                # print(proxy_url)
                ip_ports = self.download_ip(proxy_url)
                ch_df = pd.DataFrame(ip_ports)
                # 如果有数据就合并数据帧
                if self.df_ip is None:
                    self.df_ip = ch_df
                else:
                    # self.df_ip = pd.concat([self.df_ip, ch_df],axis=0, keys=['ip', 'port'],join='inner')
                    self.df_ip.append(ch_df)
                    # print(ch_df)
            self.df_ip.to_csv(self.filename)
        else:
            self.df_ip = pd.read_csv(self.filename, index_col=0)

    @staticmethod
    def download_ip(proxy_url):
        return get_page_ip(proxy_url)

    def get_ip(self):
        """返回ip和端口地址"""
        if self.df_ip is not None:
            sign = random.randint(0, self.df_ip.size / 2)
            self.ip = self.df_ip.ix[sign][0]
            self.port = str(self.df_ip.ix[sign][1])
            get_ip_port = self.ip + ':' + self.port
            return get_ip_port
        return ReferenceError('你必须先运行run方法')

    def process(self):
        # args是关键字参数，需要加上名字，写成args=(self,)
        th1 = threading.Thread(target=RunProxy.run, args=(self,))
        th1.start()
        th1.join()

    # def test_ip(self):
    #     for test_ip in self.

if __name__ == '__main__':
    # proxy_per = RunProxy('ip.csv', model=True)

    proxy_per = RunProxy('ip.csv')
    proxy_per.run()
    print(proxy_per.get_ip())
    test_ip(proxy_per.ip, proxy_per.port)
    # print(type(ip_port))
