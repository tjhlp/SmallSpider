# 输入关键词
# search = input("请输入关键词：")
# 需要爬取的页面数量
# page = int(input("请输入获取页数："))

# 关键词
SEARCH_NAME = "Party Lights"
# 采集的页面总数
PAGE = 4
# 每页最大的商品详情采集数量
PAGE_DETAIL_MAX = 3
# 存储的文件名
FILE_NAME = '1008-' + SEARCH_NAME + '.csv'
# 页面路径样本（按照关键词）
HTML = 'https://www.walmart.com/search/?cat_id=0&page={}&ps=40&query={}'
INDEXES = ['Rank', 'Id', 'Url', 'Name', 'Price', 'Star', 'Review', 'Page', 'Shop_name', 'Main_Image_url', 'Brand',
           'Category', 'Highlights', 'Key_World', 'Time']
"""
搜索关键词不用改，搜索分类的话需要更换网址，第一步注释掉38行和52行的代码，打开44行和54行的代码然后填入分类的网址
"""
# 页面路径样本（按照分类）
# html = 'https://www.walmart.com/browse/musical-instruments/par-cans/7796869_3896240_1725737?page={}'

