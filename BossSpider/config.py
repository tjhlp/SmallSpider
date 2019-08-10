# 访问页面总数
BOSS_PAGE_NUM = 9
BOOS_URL = 'https://www.zhipin.com/job_detail/?query=python%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101280600&industry=&position='
BOOS_URL_FOLLOW = 'https://www.zhipin.com/c101280600/?query=python%E5%B7%A5%E7%A8%8B%E5%B8%88&'
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
PROXY_URL_BASIC = 'https://www.xicidaili.com/wn/'
PROXY_URLS = []

# 测试是否使用代理的网站
TEST_IP_HTML = 'http://httpbin.org/get'

# 测试ip开启的线程池的数目
TEST_POOL_NUM = 10

TEST_COMPANY = [('腾讯科技（深圳）有限公司', 354), ('深圳市客路网络科技有限公司', 351), ('深信服科技股份有限公司', 305), ('深圳小步网络科技有限公司', 272),
                ('深圳市联合信通科技有限公司', 262), ('深圳牧原数字技术有限公司', 258), ('平安科技（深圳）有限公司', 258), ('深圳平安综合金融服务有限公司上海分公司', 245),
                ('北京国双科技有限公司', 227), ('广州市万齐网络科技有限公司', 165), ('中软国际科技服务有限公司', 162), ('华为技术有限公司', 145),
                ('深圳前海优管信息技术有限公司', 144), ('软通动力信息技术（集团）有限公司', 144), ('富途网络科技（深圳）有限公司', 140), ('深圳市观麦网络科技有限公司', 139),
                ('深圳茂源资本资产管理有限公司', 131), ('上海速强信息技术股份有限公司', 129), ('安吉康尔（深圳）科技有限公司', 129), ('深圳市星商电子商务有限公司', 127),
                ('深圳战吼网络科技有限公司', 125), ('深圳逻辑汇科技有限公司', 121), ('深圳市安之天信息技术有限公司', 119), ('深圳市彬讯科技有限公司', 114),
                ('上海币胜网络科技有限公司', 109), ('深圳晶泰科技有限公司', 108), ('长园深瑞继保自动化有限公司', 107), ('新译信息科技（深圳）有限公司', 105),
                ('妙印云科技（深圳）有限公司', 102), ('欣旺达电子股份有限公司', 98), ('深圳市金未来信息技术有限公司', 97), ('深圳市火乐科技发展有限公司', 92),
                ('深圳市杉岩数据技术有限公司', 82), ('深圳市三颗子弹科技有限公司', 75), ('量基（深圳）科技有限公司', 74), ('深圳萨摩耶互联网金融服务有限公司', 73),
                ('成都华为技术有限公司', 73), ('行云智能（深圳）技术有限公司', 72), ('深圳脉图精准技术有限公司', 72), ('深圳米筐科技有限公司', 71),
                ('深圳市丰远国际货运代理有限公司', 71), ('安克创新科技股份有限公司', 69), ('深圳市美迪尔实业有限公司', 68), ('深圳市街角电子商务有限公司', 68),
                ('深圳市亿龙达物流有限公司', 67), ('深圳创景世界科技有限公司', 67), ('北京志凌海纳科技有限公司', 66), ('深圳市走路捡钱科技有限公司', 66),
                ('云鲸智能科技（东莞）有限公司', 65), ('深圳市贝多分金融科技有限公司', 64), ('深圳智通财经信息科技服务有限公司', 63), ('深圳市雷赛信息科技有限公司', 62),
                ('深圳市多保文化传播科技有限公司', 60), ('深圳前海农产品交易所股份有限公司', 59), ('OPPO广东移动通信有限公司', 58), ('深圳市衍盛资产管理有限公司', 58),
                ('深圳点赞互娱科技有限公司', 58), ('深圳众趣文化传播有限公司', 57), ('深圳市超群光科技有限公司', 57), ('深圳市有芯电子有限公司', 57),
                ('深圳江南月科技有限公司', 56), ('深圳前海达飞金融服务有限公司', 56), ('深圳大师科技有限公司', 56), ('深圳视见医疗科技有限公司', 55),
                ('深圳市悦动天下科技有限公司', 55), ('达而观信息科技（上海）有限公司', 54), ('深圳市华富洋供应链有限公司', 54), ('深圳市微埃智能科技有限公司', 54), ('', 53),
                ('南京绛门信息科技股份有限公司', 53), ('深圳市鼎鼎赞科技有限公司', 53), ('深圳市前海源伞科技有限公司', 52), ('深圳度创科技有限公司', 52),
                ('深圳市魔方安全科技有限公司', 51), ('金贝塔网络金融科技（深圳）有限公司', 51), ('深圳市运维软件有限公司', 50), ('深圳市达深智能科技（有限合伙）', 49),
                ('湖北玉立砂带集团股份有限公司', 48), ('百度在线网络技术（北京）有限公司', 47), ('深圳市乐易网络股份有限公司', 47), ('深圳广田云万家科技有限公司', 47),
                ('深圳市得瑟文化传媒有限公司', 46), ('深圳贝尔信息科技有限公司', 45), ('深圳达脉科技有限公司', 45), ('深圳市科迈爱康科技有限公司', 44),
                ('深圳市明源云科技有限公司', 43), ('深圳市普特生物医学工程有限公司', 42), ('青牛智胜（深圳）科技有限公司', 42), ('百度国际科技（深圳）有限公司', 41),
                ('深圳爱财科技有限公司', 40), ('深圳市前海数据服务有限公司', 39), ('安徽绿舟科技有限公司', 39), ('深圳前海优麦科技有限公司', 38),
                ('深圳佑驾创新科技有限公司', 38), ('深圳码隆科技有限公司', 37), ('深圳市大疆创新科技有限公司', 37), ('深圳淘乐网络科技有限公司', 36),
                ('腾讯音乐娱乐科技（深圳）有限公司', 36), ('引领发展（深圳）有限公司', 36), ('深圳市韵达速递有限公司', 35), ('联觉（深圳）科技有限公司', 35),
                ('深圳市方舟云数信息科技有限公司', 35), ('深圳市冲潮科技有限公司', 34), ('深圳市微赢世纪网络科技有限公司', 33), ('深圳房讯通信息技术有限公司', 32),
                ('深圳市达深信息科技有限公司', 31), ('浪潮通用软件有限公司', 30)]
