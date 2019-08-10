# 访问页面总数
BOSS_PAGE_NUM = 9
BOOS_URL = 'https://www.zhipin.com/job_detail/?query=python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600&industry=&position='
BOOS_URL_FOLLOW = 'https://www.zhipin.com/c101280600/?query=python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&'
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
KEY_WORD = ['爬虫', '算法', 'Linux', '人工智能', 'Django', 'Flask', 'MySQL', 'C++', 'linux', 'mysql', 'django', 'flask']
# 取出 python
KEY_LANGUAGE = ['MySQL', 'C++', 'Linux', 'PHP', 'Javascript', 'Java', 'Git', 'Shell', 'Go', 'Golang', 'C', 'Ruby', 'mysql', 'c++', 'linux', 'php', 'javascript', 'java', 'git', 'shell', 'go', 'golang', 'c', 'ruby']

KEY_WORD_YEAR = ['一年以上', '两年以上', '三年以上', '三到五年']
KEY_WORD_BACKGROUND = ['一本', '二本', '985', '211', '本科学历']
# 使用代理的网页
PROXY_PAGE_NUM = 30

# 代理网站
PROXY_URL_BASIC = 'https://www.xicidaili.com/nn/'
PROXY_URLS = []

# 测试是否使用代理的网站
TEST_IP_HTML = 'http://httpbin.org/get'

# 测试ip开启的线程池的数目
TEST_POOL_NUM = 10


