import requests
from pyquery import PyQuery as pq
import telnetlib

from config import REQUEST_HEADERS

proxy = '120.83.121.73:808'
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
    doc = pq(html)
    doc_infos = doc.find('#ip_list .odd').items()

    ip_list = []
    port_list = []

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
                ip_address = split_info[0]
                port_num = split_info[1]
                ip_list.append(ip_address)
                port_list.append(port_num)
                # print('ip:port = {}:{} time:{}'.format(ip_address, ip_port, ip_time))

    ip_ports = {'ip': ip_list, 'port': port_list}

    return ip_ports


def test_ip(ip, port):
    print('------------------------connect---------------------------')
    # 连接Telnet服务器
    try:
        tn = telnetlib.Telnet(ip, port=port, timeout=20)
    except:
        print('该代理IP:{}无效'.format(ip))
    else:
        print('该代理IP:{}:{}有效'.format(ip, port))

    print('-----------end-----------')
