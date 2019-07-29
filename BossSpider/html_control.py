import requests, re
from pyquery import PyQuery as pq

from config import REQUEST_HEADERS


def get_html(url):
    response = requests.get(url, headers=REQUEST_HEADERS)
    if response.status_code == 200:
        return response.text
    return None


def generate_one_page(url):
    # https://www.zhipin.com/job_detail/67aad9d660dec84e1XN52t21FFI~.html
    url = 'https://www.zhipin.com' + url
    return url


def parse_one_page(html):
    url_list = []
    doc = pq(html)
    doc_1 = doc('#main div .job-list ul')
    doc_2 = doc_1.find('li div .info-primary h3 a').items()
    for urls in doc_2:
        get_url = re.findall(r'<a href="(.*?)"', str(urls))
        url_html = generate_one_page(get_url[0])
        url_list.append(url_html)
    return url_list


def parse_one_job(url):
    job_html = get_html(url)
    doc = pq(job_html)
    doc_main = doc('#main')
    doc_info = doc_main.find('.smallbanner div .name')
    doc_cominfo = doc_main.find('.job-box div .detail-content')
    job_name = doc_info.find('h1').text()
    job_salary = doc_info('span').text()
    job_text = doc_cominfo.find('.job-sec .text').text()
    company_name = doc_cominfo.find('.job-sec .name').text()
    job_location = doc_cominfo.find('.job-sec .job-location .location-address').text()
    return {
        'job_name': job_name,
        'job_salary': job_salary,
        'job_text': job_text,
        'company_name': company_name,
        'job_location': job_location,
    }
