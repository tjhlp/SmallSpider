from html_control import *
from file_control import *
from config import *
from proxy_pool.core import RunProxy


class RunBossSpider(object):
    def __init__(self):
        self.proxy = RunProxy

    def run(self):
        pass


if __name__ == '__main__':

    proxy_per = RunProxy('ip.csv')
    ip_port = proxy_per.run()
    job_list = []
    html_content = get_html(BOOS_URL)
    url_list = parse_one_page(html_content)
    for url in url_list:
        job_info = parse_one_job(url)
        job_list.append(job_info)
    save_csv_file('job.csv', job_list)
