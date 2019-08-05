# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt




def count_time(func):
    """计时装饰器"""

    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('处理数据用时:{}'.format(end_time - start_time))
        return result

    return inner


def remove_invalid_words(words_lists):
    """
    数据清洗第一步，清除无效停用词，数字的数据
    :param words_lists:
    :return:
    """

    words_dict = {}
    for word in words_lists:
        # TODO 添加停用词
        if word not in []:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return words_dict


def read_json(file):
    """
    读取file文件夹下所有json文件
    :param file: 文件夹
    :return:
    """
    job_info_file = []
    paths = os.listdir(file)
    for path in paths:
        if re.match(r'2019', path):
            with open(path, 'r', encoding='gbk')as f:
                content = json.loads(f.read())
                for job_info in content:
                    if job_info['job_name']:
                        job_info_file.append(job_info)
    else:
        return job_info_file


# {'job_name': 'Python高级工程师', 'job_salary': '25-50K', 'job_text': '职位要求：\n1、负责外部公',
# 'company_name': '深圳市星商电子商务有限公司', 'job_location': '深圳龙岗区云里智能园4栋2楼'}
@count_time
def data_classification(job_list):
    """分类数据"""
    company_dict = {}
    for job_comp in job_list:
        a = job_comp.get('job_text')
        participle_data = jieba.lcut(a)
        process_data1 = remove_invalid_words(participle_data)
        process_data2 = sorted(process_data1.items(), key=lambda x:x[1], reverse=True)
        print(process_data2)
        company_name = job_comp.get('company_name')
        if company_name in company_dict:
            company_dict[company_name] += 1
        else:
            company_dict[company_name] = 1

    return company_dict


def plot_data(company_data, filename):
    """
    将信息（公司与职位信息）可视化
    :param company_data: （公司与职位数量）以键值对信息传入
    :return: None
    """
    company_list = []
    value_list = []
    for key, value in company_data.items():
        company_list.append(key)
        value_list.append(value)
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小
    x_cor = [x for x in range(len(company_list))]
    plt.barh(x_cor, value_list, facecolor='orange', height=0.3, label='职位数量')
    plt.yticks(x_cor, company_list)
    plt.grid(alpha=0.3)
    plt.xlabel('公司招聘职位')
    plt.savefig(filename)
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    job_info_list = read_json('../data')
    # print(job_info_list)
    get_company = data_classification(job_info_list)
    # print(get_company)
    # plot_data(job_info, './job_info.jpg')
    # plot_data(get_company)
