import requests


# 1、爬取商品排名和详情页链接
url_page1 = 'https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_electronics_home_all?pf_rd_p=65f3ea14-1275-4a7c-88f8-1422984d7577&p'  # 01-50名商品
 # 51-100名商品

item_info = []    # 存储商品详细信息的列表
item_links = []   # 存储商品详情页链接的列表
def get_item_info(url):
    # wb_data = requests.get(url,headers=headers,proxies=proxies)
    wb_data = requests.get(url)
    print(wb_data.text)

get_item_info(url_page1)