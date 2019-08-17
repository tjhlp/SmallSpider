from core import RunBossSpider
from data.tool.handler import HandlerData
from proxy_pool.scheduler import RunProxy


def run_proxy():
    proxy_per = RunProxy('ip.csv', model=True)
    proxy_per.run()
    proxy_per.run_test_ip()
    proxy_per.merge_json_file()


def main():
    # 开启爬虫
    boss_spi = RunBossSpider()
    boss_spi.run()

    # 开启数据分析
    hd = HandlerData('../../data/')
    hd.run()


if __name__ == '__main__':
    run_proxy()
    # main()
