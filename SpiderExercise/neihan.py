import requests
import re

url = "https://www.neihanba.com/dz/1164399.html"
proxies = {
    'https': 'http://127.0.0.1:1080'
}
headers = {
    "Referer": "https//www.neihanba.com/dz/1164398.html",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

html = requests.get(url=url, headers=headers, proxies=proxies)
print('1')
html.encoding = 'gbk'
print('2')
content = html.text
print('3')
pattern = re.compile('<p>(.*?)</p>')
finds = pattern.findall(content)
print(finds)
