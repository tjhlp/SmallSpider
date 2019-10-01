import requests
from pprint import pprint

url = "https://www.walmart.com/search/?cat_id=0&query=audio"
# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
response = requests.get(
    url=url,
    headers=headers,
)
print(response.text)
