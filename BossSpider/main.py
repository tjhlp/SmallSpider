from core import RunBossSpider
from data.tool.handler import HandlerData


def run_proxy():
    pass


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
