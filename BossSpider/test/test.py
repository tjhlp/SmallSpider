# coding=gbk
import jieba
import random
from datetime import datetime
import json

# print(type(datetime.now().strftime('%Y-%m-%d %H:%M')))
# t = datetime.now().strftime('%Y%m%d-%H-%M')
# n = 1
# print(t + '_job.json')
# with open(t + '_job.json', 'w')as r:
#     r.write(json.dumps(n))
# print(random.randint(1, 5))
#
# list1 = [1,2,3]
# print(list1[:1])

# from pyquery import PyQuery as pq
# with open('0_html.txt' ,'r', encoding='utf-8')as r:
#     html = r.read()
#     doc = pq(html)
#     doc_1 = doc('#tips')
#     if doc_1:
#         print('11')
#
# list_a = ['ְλ', 'Ҫ��', '��', '\n', '1', '��', '����', '�ⲿ', '����', '����', '��', 'ץȡ', '��', '���ӻ�', '\n', '2', '��', '����', 'ҵ��', '����', '����', '����', '����', '\n', '3', '��', 'ʵ��', '����ҵ��', '����', '����', '�߼�', '\n', '��λְ��', '��', '\n', '1', '��', '��Ϥ', 'requests', '��', 'lxml', '��', 'xpath', '��', '����', '���', '��', '��ҳ����', '����', '֪ʶ', '\n', '2', '��', '��Ϥ', '�ı�', 'ģʽƥ��', '��', '��ȡ', '�ض�', '����', '\n', '3', '��', '��', '����', '����', '����', '����', '��ȡ', '��Ŀ', '����', '\n', '4', '��', '��Ϥ', '��', 'numpy', '��', 'scipy', '��', 'matplotlib', '��', '���ݷ���', '��', '\n', '5', '��', '��Ϥ', '��Ȼ����', '����', '��', '���', 'ѧϰ', '����', '��', '����', '��', '����', '�ִ�', '��', '����', '����', '��', 'ͼ��ʶ��', '��', '��Ƶ', '����', '��', '����', '�Ի�', '��', '���', '����', '��', '����', '�㷨', '��', '���', '��', '�˽�', '��', '\n', '6', '��', '�˽�', '����', 'ѧϰ', '��', '������', '��', '���', '�㷨', '��', '����', '��', '��', '����', 'SVM', '��', 'KNN', '��', 'RNN', '��', 'CNN', '��', '���', 'ɭ��', '�Լ�', '�������', '��', '��', ' ', '��ҵ���', '��', '\n', '\n', '����', '��ԭ', '����', '����', '���޹�˾', 'λ��', '������', '��ɽ��', '����', '����', '��', '����', '������', '����', '�ܲ�', '����', '��', '������', '�˲�', '��԰', '��', '�˲�', '�ۼ�', '��', '��ͨ', '����', '��', '�羰����', '��', '����', '��ԭ', '����', '����', '���޹�˾', '����', '��ԭ', '����', '(', '��Ʊ����', '002714', ')', 'ȫ��', '�ӹ�˾', '��', 'Ϊ', '����', '�ṩ', '��', '����', '��', '���ֻ�', '��', '���ܻ�', '����', '����', '��', '֧��', '��˾', '���ֻ�', '��', '���ܻ�', '��չ', '��', '��']
# dicta = {'a':1}
# if 'b' in dicta:
#     print('2')
# if 'pandas' in list_a:
#     print('1')

# x=np.linspace(-3,3,50)
# y1=2*x+1
# y2=x**2
# plt.figure(num=2,figsize=(8,5))
# plt.plot(x,y1,color='red',linewidth=2,linestyle='-')
# plt.plot(x,y2)#���л�ͼ
# plt.xlim(-1,2)
# plt.ylim(-2,3)
# plt.xlabel("I'm x")
# plt.ylabel("I'm y")
# new_ticks=np.linspace(-1,2,5)#С���-1��2��Ϊ5����λ
# print(new_ticks)
# #[-1.   -0.25  0.5   1.25  2.  ]
# plt.xticks(new_ticks)#�����滻���±�
# plt.yticks([-2,-1,1,2,],
#            [r'$really\ bad$','$bad$','$well$','$really\ well$'])
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = {'������ԭ���ּ������޹�˾': 5, '���������̵����������޹�˾': 9,
        '�����п�·����Ƽ����޹�˾': 8, '����ƽ���ۺϽ��ڷ������޹�˾�Ϻ��ֹ�˾': 7,
        '��ͨ������Ϣ���������ţ����޹�˾': 6, '����С������Ƽ����޹�˾': 5,
        '������������ͨ�Ƽ����޹�˾': 4, '���ŷ��Ƽ��ɷ����޹�˾': 3}


def plot_data(data):
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # ��ʾ��С
    company_list = []
    value_list = []
    for key, value in data.items():
        company_list.append(key)
        value_list.append(value)
    x_cor = [x for x in range(len(company_list))]
    plt.barh(x_cor, value_list, facecolor='orange', height=0.3)
    plt.yticks(x_cor, company_list)
    plt.grid(alpha=0.3)
    plt.xlabel('��˾��Ƹְλ')
    plt.show()
