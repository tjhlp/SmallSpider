import requests
import js2py

context = js2py.EvalJs()
with open('md5.js', 'r', encoding='utf-8') as f:
    context.execute(f.read())

url = 'https://logindict.youdao.com/login/acc/login'
username = "m18003915297@163.com"
password = "8593365"
pwd = context.hex_md5(password)

proxies = {
    'http': 'http://127.0.0.1:1080'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

data = {
    "app": "web",
    "tp": "urstoken",
    "cf": "3",
    "fr": "1",
    "ru: http": "//dict.youdao.com/search?q=as&tab=#keyfrom=${keyfrom}",
    "product": "DICT",
    "type": "1",
    "um": "true",
    "username": username,
    "password": pwd, }

resp = requests.post(url, data=data, headers=headers, proxies=proxies)
with open('md5.html', 'wb') as w:
    w.write(resp.content)

# print(resp.cookies)
