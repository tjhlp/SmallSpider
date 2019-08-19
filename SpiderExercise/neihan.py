from pprint import pprint

import requests
import re
import html


class Neihan8(object):
    def __init__(self):
        self.url = "https://www.neihan8s.com/e/action/ListInfo/?classid=11&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        }

    def generate_url(self):
        return [self.url.format(page) for page in range(1093)]

    def run(self):
        page_pattern = re.compile('<h3><a href="(.*?)" class="title" title="(.*?)">(.*?)</a></h3>')
        content_pattern = re.compile(r'<div class="detail">(.*?)<div class="tag-share line"', re.DOTALL)
        part_pattern = re.compile(r'<p>(.*?)</p>')

        page_url_list = self.generate_url()
        for page_url in page_url_list:
            page_resp = requests.get(page_url, headers=self.headers)
            article_list = page_pattern.findall(page_resp.text)
            for article_url, title1, title2 in article_list:
                item = {}
                item['content'] = ''
                item['title'] = title1
                article_resp = requests.get("https://www.neihan8s.com" + article_url, headers=self.headers)
                html_article = article_resp.content.decode('utf-8')
                content_list = content_pattern.findall(html_article)
                part_content = part_pattern.findall(content_list[0])
                for part in part_content:
                    part = html.unescape(part)
                    part = part.strip()
                    item['content'] += part + '\n'
                pprint(item)
                print("*" * 100)
            break


if __name__ == '__main__':
    spider = Neihan8()
    spider.run()
