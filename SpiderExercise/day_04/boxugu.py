"""
打开博学谷
截全屏
获取验证码的图片
输入
"""
from selenium import webdriver
import time
from PIL import Image
from io import BytesIO
from YDMHTTP import *
# 无界面
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
#
# browser = webdriver.Chrome('../html_files/chromedriver',chrome_options=options)
browser = webdriver.Chrome('../html_files/chromedriver')
# 登录
browser.get('http://ntlias-stu.boxuegu.com/#/login')
# 输入账号密码
user_element = browser.find_element_by_xpath('//input[@name="username"]').send_keys('A190306623')
password_element = browser.find_element_by_xpath('//input[@name="password"]').send_keys('wei0906')

# 截取全屏
time.sleep(1)
full_image_data = browser.get_screenshot_as_png()
full_image = Image.open(BytesIO(full_image_data))
full_image.save('full.png')
# 获取部分
piture_element = browser.find_element_by_class_name('code-msg')

# 实际图片像素
# 1476 608  1600 660
# x,y 表示元素
rate = 1.25
x1 = piture_element.location['x'] * rate
y1 = piture_element.location['y'] * rate

x2 = x1 + piture_element.size["width"] * rate
y2 = y1 + piture_element.size['height'] * rate
cut_info = (x1, y1, x2, y2)
print("cut_info:", cut_info)
# 保存截屏后的图片
cut_img = full_image.crop(cut_info)
cut_img.save('partion.png')

# 调用打码平台
result = boxuegu('partion.png')
print(result)
code_element = browser.find_element_by_xpath('//input[@name="verify"]').send_keys(result)
#
# 点击登录按钮
button_element = browser.find_element_by_class_name('login-btn').click()
time.sleep(5)
# 切换界面
browser.switch_to.window(browser.window_handles[(len(browser.window_handles) - 1)])
# 点击反馈
# fankui_button_element = browser.find_element_by_link_text('去反馈').click()
fankui_button_element = browser.find_element_by_class_name('redD1').click()

# 切换到反馈答题界面
browser.switch_to.window(browser.window_handles[(len(browser.window_handles) - 1)])

# 所有列表
li_lists = browser.find_elements_by_xpath('//ul[@class="subject-list"]/li')
print('共有{}道题'.format(len(li_lists)))

# print(li_lists)
time.sleep(2)
for li in li_lists:
    time.sleep(3)
    # 点击B元素
    li_element = li.find_element_by_xpath('.//input[@value="b"]')
    print(li.find_element_by_class_name('title').text)
    browser.execute_script("arguments[0].click();", li_element)

# 提交
tijiao_element = browser.find_element_by_class_name('sub').click()
# 关闭
close_element = browser.find_element_by_partial_link_text('关闭')


