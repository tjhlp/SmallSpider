import requests
from pyquery import PyQuery as pq
import re

PAGE_NUM = 10
url = 'https://www.zhipin.com/job_detail/?query=python&city=101280600&page=1&ka=1'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8')as w:
        w.write(content)


def get_one_page(url):

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    url_list = []
    doc = pq(html)
    doc_1 = doc('#main div .job-list ul')
    doc_2 = doc_1.find('li div .info-primary h3 a').items()
    for urls in doc_2:
        # print(urls)
        get_url = re.findall(r'<a href="(.*?)"', str(urls))
        url_list.append(get_url[0])

    return url_list


def generate_one_page(url):
    # https://www.zhipin.com/job_detail/67aad9d660dec84e1XN52t21FFI~.html
    url = 'https://www.zhipin.com' + url
    return url


html_content = get_one_page(url)
url_list = parse_one_page(html_content)
for url in url_list:
    requests.get(url, headers=headers)

save_file('1.txt', html_content)
