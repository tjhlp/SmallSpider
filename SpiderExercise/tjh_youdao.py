# -*- coding: utf-8 -*-

import requests
import hashlib
import time
import random


def make_md5(string):
    t = hashlib.md5()
    t.update(string.encode('utf-8'))
    return t.hexdigest()


word = 'tiger'
string = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
t = make_md5(string)
r = str(time.time())
i = r + str(random.randint(0, 10))
salt = i
sign = make_md5("fanyideskweb" + word + i + "n%A-rKaT5fb[Gy?;N5@Tj")
ts = r
bv = t

url = "http://fanyi.youdao.com/translate_o"
proxies = {
    'http': 'http://127.0.0.1:1080'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-684719233@113.116.177.74; OUTFOX_SEARCH_USER_ID_NCOO=1797061351.2474163; JSESSIONID=aaa-vy--UIsZg8yX7tEYw; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcDBq61PFgvS-hD-tEYw; _ntes_nnid=a6ce119d4e4fec83da15da24bfa3aea6,1566024142296; ___rl__test__cookies=1566033183462'
}
data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt,
    "sign": sign,
    "ts": ts,
    "bv": bv,
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
}
params = {
    "smartresult": "dict",
    "smartresult": "rule"
}

response = requests.post(url, data=data, params=params, headers=headers, proxies=proxies)

print(response.text)
