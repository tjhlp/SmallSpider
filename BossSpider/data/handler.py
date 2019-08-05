# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt




def count_time(func):
    """��ʱװ����"""

    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('����������ʱ:{}'.format(end_time - start_time))
        return result

    return inner


def remove_invalid_words(words_lists):
    """
    ������ϴ��һ���������Чͣ�ôʣ����ֵ�����
    :param words_lists:
    :return:
    """

    words_dict = {}
    for word in words_lists:
        # TODO ���ͣ�ô�
        if word not in []:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return words_dict


def read_json(file):
    """
    ��ȡfile�ļ���������json�ļ�
    :param file: �ļ���
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


# {'job_name': 'Python�߼�����ʦ', 'job_salary': '25-50K', 'job_text': 'ְλҪ��\n1�������ⲿ��',
# 'company_name': '���������̵����������޹�˾', 'job_location': '������������������԰4��2¥'}
@count_time
def data_classification(job_list):
    """��������"""
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
    ����Ϣ����˾��ְλ��Ϣ�����ӻ�
    :param company_data: ����˾��ְλ�������Լ�ֵ����Ϣ����
    :return: None
    """
    company_list = []
    value_list = []
    for key, value in company_data.items():
        company_list.append(key)
        value_list.append(value)
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # ��ʾ��С
    x_cor = [x for x in range(len(company_list))]
    plt.barh(x_cor, value_list, facecolor='orange', height=0.3, label='ְλ����')
    plt.yticks(x_cor, company_list)
    plt.grid(alpha=0.3)
    plt.xlabel('��˾��Ƹְλ')
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
