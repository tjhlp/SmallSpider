import requests

url = "http://www.eon.com.hk/common/fcg/estroke1.fcg"
proxies = {
    'https': 'http://127.0.0.1:1080'
}
headers = {
    "Referer": "http://www.eon.com.hk/canvas/anim.htmll",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Cookie": "Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1566096476; Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1566096476; __qca=P0-1977758018-1566096478418"
}
params = {
    'task': 'getPhrase'
}
data = {
    "xx": "",
    "uni": "到",
    "screenWidth": "180",
    "bias": "Simplified",
}

resp = requests.post(url=url, headers=headers, data=data, params=params)

with open('font.html', 'wb') as w:
    w.write(resp.content)
