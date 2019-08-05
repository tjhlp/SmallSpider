BOSS_PAGE_NUM = 10
BOOS_URL = 'https://www.zhipin.com/job_detail/?query=python%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600&industry=&position='
BOOS_URL_FOLLOW = 'https://www.zhipin.com/c101280600/?query=python%E5%B7%A5%E7%A8%8B%E5%B8%88&'
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

# 使用代理的网页
PROXY_PAGE_NUM = 30

# 代理网站
PROXY_URL_BASIC = 'https://www.xicidaili.com/nn/'
PROXY_URLS = []

# 测试是否使用代理的网站
TEST_IP_HTML = 'http://httpbin.org/get'

# 测试ip开启的线程池的数目
TEST_POOL_NUM = 10
