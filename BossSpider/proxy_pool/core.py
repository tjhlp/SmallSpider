import pandas as pd
import random

from proxy_pool.config import *
from proxy_pool.control import get_html, get_page_ip


class RunProxy(object):
    """获取代理ip，先运行run方法，以后拿ip可以直接运行get_ip方法"""

    def __init__(self, filename, model=False):
        self.model = model
        self.filename = filename
        self.df_ip = None

    def run(self):
        if self.model:
            html = get_html(proxy_url)
            ip_ports = get_page_ip(html)
            self.df_ip = pd.DataFrame(ip_ports)
            self.df_ip.to_csv(self.filename)
        else:
            self.df_ip = pd.read_csv(self.filename, index_col=0)

        return self.get_ip()

    def get_ip(self):
        if self.df_ip is not None:
            sign = random.randint(0, self.df_ip.size / 2)
            get_ip_port = self.df_ip.ix[sign][0] + ':' + str(self.df_ip.ix[sign][1])
            return get_ip_port
        return ReferenceError('你必须先运行run方法')


if __name__ == '__main__':
    proxy_per = RunProxy('ip.csv')
    ip_port = proxy_per.run()
    print(ip_port)
    print(proxy_per.get_ip())
    print(proxy_per.get_ip())
    # print(type(ip_port))
