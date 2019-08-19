import requests
import json
import jsonpath
from pprint import pprint

proxies = {
    'https': 'http://127.0.0.1:1080'
}
session = requests.session()
resp = session.get(
    url='https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91?city=%E5%85%A8%E5%9B%BD',
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Refer": "https://www.lagou.com/utrack/trackMid.html?f=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fpython%25E5%25BC%2580%25E5%258F%2591%3Fcity%3D%25E5%2585%25A8%25E5%259B%25BD&t=1566178578&_ti=3",
        "Cookie": "user_trace_token=20190719140632-21c2fd82-541c-43d2-885c-f8888f1c4bb4; _ga=GA1.2.1013674605.1563516393; LGUID=20190719140633-5bf71dc8-a9eb-11e9-80fc-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c08d72656ea-0902e8c0eb6017-c343162-1049088-16c08d726573cc%22%2C%22%24device_id%22%3A%2216c08d72656ea-0902e8c0eb6017-c343162-1049088-16c08d726573cc%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA554ECFB0DEB6926B935DC5158AEF4208; WEBTJ-ID=20190818092010-16ca24f6e9a100-0e466266e5c2f6-7373e61-1049088-16ca24f6e9b4bc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565256520,1566039502,1566043542,1566091211; X_MIDDLE_TOKEN=facace93dcf8ad0470bd0152ad512691; SEARCH_ID=61c39aaeaae7484f91f4ac71e334628e; _gid=GA1.2.1353268621.1566178559; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566178559; LGSID=20190819093600-b33d2968-c221-11e9-8a7f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist%255Fpython%2525E5%2525BC%252580%2525E5%25258F%252591%253Fcity%253D%2525E5%252585%2525A8%2525E5%25259B%2525BD%26t%3D1566178559%26_ti%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%25E5%25BC%2580%25E5%258F%2591%3Fcity%3D%25E5%2585%25A8%25E5%259B%25BD; LGRID=20190819093600-b33d2aef-c221-11e9-8a7f-525400f775ce; X_HTTP_TOKEN=17ad8e4313c6e42308587166519f5a70620be3d979"
    },
    params={
        'city': '全国'
    },
    proxies=proxies

)
pprint(resp.cookies)
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "25",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.lagou.com",
    "Origin": "https//www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest",
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "Python",
}
params = {
    "needAddtionalResult": "false"
}
html = session.post(url="https://www.lagou.com/jobs/positionAjax.json",
                    proxies=proxies,
                    headers=headers,
                    params=params,
                    data=data)
pprint(html.text)
pprint(html.status_code)
data = json.loads(html.text)
name = jsonpath.jsonpath(data, '$..positionName')
pprint(name)

# with open('lagou.json', 'w', encoding='utf-8') as w:
#     print(html.text)
#     w.write(html.text)
