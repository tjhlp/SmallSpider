from core import RunBossSpider
from data.tool.handler import HandlerData
from flask import Flask


def run_proxy():
    pass


def run_web():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    app.run()


def main():
    # 开启爬虫
    boss_spi = RunBossSpider()
    boss_spi.run()

    # 开启数据分析
    hd = HandlerData('../../data/')
    hd.run()


if __name__ == '__main__':
    # run_proxy()
    # main()
    run_web()