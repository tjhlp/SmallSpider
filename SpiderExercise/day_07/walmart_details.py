from selenium import webdriver


def getitemdetai(html):
    # 初始化驱动程序
    options = webdriver.ChromeOptions()
    # 切换User-Agent
    options.add_argument(
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
    options.add_argument('--headless')  # 开启无界面模式
    options.add_argument('--disable-gpu')  # 禁用gpu，解决一些莫名的问题  有界面注释这两行
    # 导入驱动程序
    # browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    browser1 = webdriver.Chrome(chrome_options=options)
    browser1.get(html)

    try:
        item_highlights = browser1.find_elements_by_xpath('.//div[@class="prod-ProductHighlights-content"]/div/ul//li')
        highlight_list = [highlight.text for highlight in item_highlights]
        highlights = '\n'.join(highlight_list)
    except Exception as e:
        highlights = 'none'

    try:
        item_brand = browser1.find_element_by_xpath('.//span[@itemprop="brand"]').text
    except Exception as e:
        item_brand = 'none'

    try:
        item_store = browser1.find_element_by_xpath('.//a[@class="seller-name"]').text
    except Exception as e:
        item_store = 'none'

    item_breadcrumbs = browser1.find_elements_by_xpath('.//ol[@class="breadcrumb-list"]//li')
    breadcrumbs_list = [breadcrumb.find_element_by_xpath('./a/span').text for breadcrumb in item_breadcrumbs]
    breadcrumbs = '/'.join(breadcrumbs_list)

    item = {'category': breadcrumbs, 'brand': item_brand, 'highlights': highlights, 'store': item_store}

    print(item)
    browser1.quit()
    return item


