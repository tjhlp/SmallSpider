from selenium import webdriver

# 初始化驱动程序
options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
options.add_argument('--headless')  # 开启无界面模式
options.add_argument('--disable-gpu')  # 禁用gpu，解决一些莫名的问题  有界面注释这两行
# 导入驱动程序
# browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
browser = webdriver.Chrome(chrome_options=options)








