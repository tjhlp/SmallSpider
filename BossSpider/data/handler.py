# coding=gbk
import json
import os
import re
import jieba
import time
import matplotlib.pyplot as plt


def count_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('处理数据用时:{}'.format(end_time - start_time))
        return result

    return inner


def read_json(file):
    paths = os.listdir(file)
    for path in paths:
        if re.match(r'2019', path):
            with open(path, 'r', encoding='gbk')as f:
                content = json.loads(f.read())
                return content
    else:
        return RuntimeError('没有json文件')


# {'job_name': 'Python高级工程师', 'job_salary': '25-50K', 'job_text': '职位要求：\n1、负责外部公',
# 'company_name': '深圳市星商电子商务有限公司', 'job_location': '深圳龙岗区云里智能园4栋2楼'}
@count_time
def data_classification(job_list):
    """分类数据"""
    # valid_list = []
    company_list = {}
    for job_info in job_list:
        # a = job_info.get('job_text')
        # process_data = jieba.lcut(a)
        company_name = job_info.get('company_name')
        if company_name in company_list:
            company_list[company_name] += 1
        else:
            company_list[company_name] = 1
            # if 'pandas' in process_data:
            #     valid_list.append(job_info)
    return company_list


def plot_data(company_data):
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小
    company_list = []
    value_list = []
    for key, value in company_data.items():
        company_list.append(key)
        value_list.append(value)
    x_cor = [x for x in range(len(company_list))]
    plt.barh(x_cor, value_list, facecolor='orange', height=0.3)
    plt.yticks(x_cor, company_list)
    plt.grid(alpha=0.3)
    plt.xlabel('公司招聘职位')
    plt.show()


if __name__ == '__main__':
    job_info_list = read_json('../data')
    company_list = data_classification(job_info_list)
    plot_data(company_list)
    # print(len(job_info_list))
