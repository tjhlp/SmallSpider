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
# list_a = ['职位', '要求', '：', '\n', '1', '、', '负责', '外部', '公开', '数据', '的', '抓取', '及', '可视化', '\n', '2', '、', '根据', '业务', '需求', '进行', '数据', '整合', '\n', '3', '、', '实现', '数据业务', '基础', '计算', '逻辑', '\n', '岗位职责', '：', '\n', '1', '、', '熟悉', 'requests', '、', 'lxml', '、', 'xpath', '等', '爬虫', '框架', '及', '网页内容', '解析', '知识', '\n', '2', '、', '熟悉', '文本', '模式匹配', '，', '获取', '特定', '内容', '\n', '3', '、', '有', '两个', '以上', '独自', '数据', '爬取', '项目', '经验', '\n', '4', '、', '熟悉', '、', 'numpy', '、', 'scipy', '、', 'matplotlib', '等', '数据分析', '包', '\n', '5', '、', '熟悉', '自然语言', '处理', '、', '深度', '学习', '技术', '，', '包括', '：', '中文', '分词', '、', '主题', '分析', '、', '图像识别', '、', '视频', '分析', '、', '智能', '对话', '、', '情感', '分析', '等', '方面', '算法', '有', '深刻', '的', '了解', '；', '\n', '6', '、', '了解', '机器', '学习', '、', '神经网络', '等', '相关', '算法', '，', '包括', '但', '不', '限于', 'SVM', '、', 'KNN', '、', 'RNN', '、', 'CNN', '、', '随机', '森林', '以及', '聚类分析', '等', '；', ' ', '企业简介', '：', '\n', '\n', '深圳', '牧原', '数字', '技术', '有限公司', '位于', '深圳市', '南山区', '三湘', '海尚', '，', '毗邻', '深圳湾', '超级', '总部', '基地', '和', '深圳市', '人才', '公园', '，', '人才', '聚集', '，', '交通', '便利', '，', '风景优美', '。', '深圳', '牧原', '数字', '技术', '有限公司', '属于', '牧原', '集团', '(', '股票代码', '002714', ')', '全资', '子公司', '，', '为', '集团', '提供', '大', '数据', '、', '数字化', '、', '智能化', '技术', '服务', '，', '支撑', '公司', '数字化', '和', '智能化', '发展', '，', '并']
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
# plt.plot(x,y2)#进行画图
# plt.xlim(-1,2)
# plt.ylim(-2,3)
# plt.xlabel("I'm x")
# plt.ylabel("I'm y")
# new_ticks=np.linspace(-1,2,5)#小标从-1到2分为5个单位
# print(new_ticks)
# #[-1.   -0.25  0.5   1.25  2.  ]
# plt.xticks(new_ticks)#进行替换新下标
# plt.yticks([-2,-1,1,2,],
#            [r'$really\ bad$','$bad$','$well$','$really\ well$'])
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = {'深圳牧原数字技术有限公司': 5, '深圳市星商电子商务有限公司': 9,
        '深圳市客路网络科技有限公司': 8, '深圳平安综合金融服务有限公司上海分公司': 7,
        '软通动力信息技术（集团）有限公司': 6, '深圳小步网络科技有限公司': 5,
        '深圳市联合信通科技有限公司': 4, '深信服科技股份有限公司': 3}


def plot_data(data):
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小
    company_list = []
    value_list = []
    for key, value in data.items():
        company_list.append(key)
        value_list.append(value)
    x_cor = [x for x in range(len(company_list))]
    plt.barh(x_cor, value_list, facecolor='orange', height=0.3)
    plt.yticks(x_cor, company_list)
    plt.grid(alpha=0.3)
    plt.xlabel('公司招聘职位')
    plt.show()
