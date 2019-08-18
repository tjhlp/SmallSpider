import requests
import json
import jsonpath

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
proxies = {
    'https': 'http://127.0.0.1:1080'
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "25",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "user_trace_token=20190719140632-21c2fd82-541c-43d2-885c-f8888f1c4bb4; _ga=GA1.2.1013674605.1563516393; LGUID=20190719140633-5bf71dc8-a9eb-11e9-80fc-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c08d72656ea-0902e8c0eb6017-c343162-1049088-16c08d726573cc%22%2C%22%24device_id%22%3A%2216c08d72656ea-0902e8c0eb6017-c343162-1049088-16c08d726573cc%22%7D; _gid=GA1.2.305935484.1566039505; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA554ECFB0DEB6926B935DC5158AEF4208; WEBTJ-ID=20190818092010-16ca24f6e9a100-0e466266e5c2f6-7373e61-1049088-16ca24f6e9b4bc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565256520,1566039502,1566043542,1566091211; LGSID=20190818092012-53c4132b-c156-11e9-8a59-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%25E5%25BC%2580%25E5%258F%2591%3Fcity%3D%25E5%2585%25A8%25E5%259B%25BD%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gat=1; X_MIDDLE_TOKEN=facace93dcf8ad0470bd0152ad512691; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566091529; LGRID=20190818092530-113f4ecc-c157-11e9-8a59-525400f775ce; X_HTTP_TOKEN=17ad8e4313c6e42364519066519f5a70620be3d979; SEARCH_ID=caf99249725748e5bf6a6f74e9286174",
    "Host": "www.lagou.com",
    "Origin": "https//www.lagou.com",
    "Referer": "https//www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
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
    "kd": "python",
}
params = {
    "needAddtionalResult": "false"
}
html = requests.post(url=url, proxies=proxies, headers=headers, params=params, data=data)
# print(html.text)
data = json.loads(html.text)
name = jsonpath.jsonpath(data, '$..positionName')
print(name)

# with open('lagou.json', 'w', encoding='utf-8') as w:
#     print(html.text)
#     w.write(html.text)
