import requests
from pyquery import PyQuery as pq
import telnetlib
import threading

from config import REQUEST_HEADERS

proxy = '111.230.203.211:8118'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}


def get_html(url):
    response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies)
    if response.status_code == 200:
        return response.text
    return None


def get_page_ip(url):
    html = get_html(url)
    if html:
        doc = pq(html)
        doc_infos = doc.find('#ip_list .odd').items()

        ip_list = []

        for doc_info in doc_infos:

            ip_time = doc_info('.country .bar').attr('title')
            ev_seconds = eval(ip_time[:-1])
            # print(eval(re_seconds))

            # 判断响应时间小于1秒的
            if ev_seconds < 1:
                ip_info = doc_info.text()
                split_info = ip_info.split('\n')

                # ['222.89.32.178', '9999', '河南济源', '高匿', 'HTTPS', '29天', '19-07-29 16:20']
                sur_life = split_info[5]
                if sur_life[-1:] == '天':
                    ip_port = []
                    ip_address = split_info[0]
                    port_num = split_info[1]
                    ip_port.append(ip_address)
                    ip_port.append(port_num)
                    ip_list.append(ip_port)
                    # print('ip:port = {}:{} time:{}'.format(ip_address, ip_port, ip_time))

        return {'ip': ip_list}
        # return ip_list, port_list
    else:
        raise RuntimeError('没有html数据')


def test_ip(ip_lists):
    valid_ip = []
    valid_port = []
    for index in range(len(ip_lists)):
        ip_list = ip_lists[index]
        try:
            # 连接Telnet服务器
            tn = telnetlib.Telnet(ip_list[0], port=int(ip_list[1]), timeout=100)
        except:
            print('该代理IP:{}无效,当前线程：{}'.format(ip_list[0], threading.current_thread().name))
        else:
            valid_ip.append(ip_list[0])
            valid_port.append(ip_list[1])
            print('该代理IP:{}有效,当前线程：{}'.format(ip_list[0]), threading.current_thread().name)
    return {'ip': valid_ip, 'port': valid_port}
