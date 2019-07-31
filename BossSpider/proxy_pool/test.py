import pandas as pd
import json

data = pd.read_csv('ip.csv', index_col=0)
ip_data1 = {
    'ip': [['123.123.123.124', '5000']]
}
ip_data2 = {
    'ip': ['123.123.123.124', '123.123.123.125'],
    'port': ['5000', '244']
}

# def a_append_b(ip_data1, ip_data2):
#     ip_a = ip_data1['ip']
#     port_b = ip_data1['ip']
# df_ip1 = pd.DataFrame(ip_data1)
# df_ip2 = pd.DataFrame(ip_data2)
# print(df_ip1)
# print(df_ip2)
# data = data.append(df_ip1)
# data = data.append(df_ip2)
# data = pd.merge(data, df_ip1)
# print(data)

# data_a = pd.concat([data, df_ip1], axis=0)
# # print(data_a)
# data_b = pd.concat([data_a, df_ip2], axis=0)
# df = data_b.reset_index(drop=True)
# # print(df)
#
# print(data.size)
# print(len(data))
# ip_list = data.iloc[:12]
# print(ip_list)
# list_ip = eval(ip)
# print(list_ip[0])
# print(list_ip[1])
# for i in range(len(ip_list)):
#     ip = ip_list.iloc[i][0]
#     list_ip = eval(ip)
#     print(list_ip[0])
#     print(list_ip[1])

# print(df)

# my_dict = {
# #     'ip_ports': {'123.123.123.432': '214'}
# # }
# with open('1.json', 'a')as w:
#     w.write(json.dumps(my_dict))
# ip = '123.123.123.434'
# port = '2332'
# ip_ports1 = [["123.123.123.432", "2332"], ["123.123.123.434", "2332"]]
# ip_ports2 = [["123.213.123.432", "24"], ["132.123.123.434", "80"]]
# try:
#     with open('1.json', 'r')as r:
#         content = json.loads(r.read())
#         print(content)
#         # print(type(content))
#     count = 0
#     for index in ip_ports2:
#         list_data = ip_ports2[count]
#         content.append(list_data)
#         count += 1
#
# except:
#     content = ip_ports1
#
# with open('1.json', 'w')as w:
#     res = json.dumps(content)
#     w.write(res)
    # print(res)
# for i in range(2):
#     print(i)

import os
if os.path.exists('valid'):
    print('1')
else:
    os.mkdir('valid')



