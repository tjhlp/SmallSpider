import time

from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

el = browser.get('https://www.douyu.com/directory/all')
time_out =3000
while True:
    time.sleep(1)
    li_elements = browser.find_elements_by_xpath('//section[@class="layout-Module js-ListContent"]//ul[@class="layout-Cover-list"]/li')
    for li in li_elements:
        item = {}
        item['title'] = li.find_element_by_xpath('.//h3[@class="DyListCover-intro"]').text
        item['author'] = li.find_element_by_xpath('.//h2[@class="DyListCover-user"]').text
        print(item)
        print('*'*100)
    browser.execute_script("var q=document.documentElement.scrollTop=100000" )
    try:
        browser.find_element_by_xpath('//span[text()="下一页"]').click()
    except:
        break

    # browser.find_element_by_xpath('//li[@class="dy-Pagination-item dy-Pagination-item-3"]').click()
browser.quit()






