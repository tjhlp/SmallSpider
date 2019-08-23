# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from PIL import Image
from io import BytesIO

from selenium.webdriver import ActionChains

from day_04.YDMHTTP import decode

browser = webdriver.Chrome('./chromedriver.exe')

fs = "武汉,WHN"
ts = "深圳,SZQ"
date = "2019-09-03"
base_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={}&ts={}&date={}&flag=N,N,Y'
browser.get(base_url.format(fs, ts, date))

time.sleep(3)
li_elements = browser.find_elements_by_xpath('//tbody[@id="queryLeftTable"]//tr[starts-with(@id,"ticket_")]')
for li_element in li_elements:
    name = li_element.find_element_by_class_name('number').text
    cdz = li_element.find_element_by_class_name('cdz').text
    try:
        revers_obj = browser.find_element_by_class_name('btn72')
        revers_obj.click()
    except:
        continue

time.sleep(2)

browser.find_element_by_class_name('login-hd-account').click()
time.sleep(2)

browser.find_element_by_id('J-userName').send_keys('r374586186')
browser.find_element_by_id('J-password').send_keys('t8306418')

img_element = browser.find_element_by_id('J-loginImg')
full_image = browser.get_screenshot_as_png()
img = Image.open(BytesIO(full_image))

scale = 0.7
# 354 207
x1 = img_element.location.get("x") * scale
y1 = img_element.location.get("y")

x2 = x1 + img_element.size.get('width')
y2 = y1 + img_element.size.get('height')

cut_info = (x1, y1, x2, y2)
cut_img = img.crop(cut_info)

cut_img.save('cut.png')
time.sleep(1)
result = decode('cut.png', 6701)
print(result)
positions = [
    (40, 70),
    (120, 70),
    (180, 70),
    (260, 70),
    (40, 140),
    (120, 140),
    (180, 140),
    (260, 140)
]
for num in result:
    position = positions[int(num) - 1]
    print(position)
    ActionChains(browser).move_to_element_with_offset(img_element, position[0],
                                                      position[1]).click().perform()

browser.find_element_by_id('J-login').click()
time.sleep(3)
# browser.quit()
