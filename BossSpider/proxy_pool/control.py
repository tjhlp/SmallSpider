import requests
from pyquery import PyQuery as pq
import telnetlib
import threading
import json, os, time
from multiprocessing import Pool

from config import REQUEST_HEADERS

test_list = []


def read_text():
    with open('html_' + str(len(test_list)) + '.txt', 'r')as f:
        test_list.append(1)
        html = f.read()
    return html


def save_text(content):
    with open('html_' + str(len(test_list)) + '.txt', 'w')as f:
        test_list.append(1)
        f.write(content)


def save_json(ip_ports, filename):
    # ip_ports = [["123.213.123.432", "24"], ["132.123.123.434", "80"]]
    if os.path.exists('valid_ip'):
        try:
            with open(filename, 'r')as r:
                content = json.loads(r.read())
            for index in range(len(ip_ports)):
                list_data = ip_ports[index]
                content.append(list_data)
        except:
            content = ip_ports

        with open(filename, 'w')as w:
            res = json.dumps(content)
            w.write(res)
    else:
        os.mkdir('valid_ip')


def get_html(url):
    proxy_ip = '127.0.0.1:1080'
    proxies = {
        'http': 'http://' + proxy_ip,
        'https': 'http://' + proxy_ip,
    }
    response = requests.get(url, headers=REQUEST_HEADERS, proxies=proxies, verify=False)
    if response.status_code == 200:
        return response.text
    return None


def get_page_ip(url):
    html = get_html(url)
    # save_text(html)
    # print(html)
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
    """对pd的dataframe里面的ip进行测试"""
    # 线程
    present_name = threading.current_thread().name
    # 进程
    # present_name = os.getpid()

    valid_list = []
    for index in range(len(ip_lists)):
        ip_port = []
        df_ip = ip_lists.iloc[index][0]
        ip_list = eval(df_ip)
        try:
            # 连接Telnet服务器
            # 判断响应时间
            tn = telnetlib.Telnet(ip_list[0], port=int(ip_list[1]), timeout=100)
            # pass
        except:
            print('第{}个代理IP:{}:{}无效,当前：{} '.format(index+1, ip_list[0], int(ip_list[1]), present_name))
        else:
            ip_port.append(ip_list[0])
            ip_port.append(ip_list[1])
            valid_list.append(ip_port)
            print('第{}个代理IP:{}有效,当前：{}'.format(index+1, ip_list[0], present_name))

    name = 'valid_ip/' + 'valid_ip' + present_name[-2:]
    save_json(valid_list, name + '.json')
