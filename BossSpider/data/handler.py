# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
from config import TEST_COMPANY

jieba.load_userdict("userdict.txt")
POOL_NUMBER = 2


def count_time(func):
    """��ʱװ����"""

    def inner(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print('����������ʱ:{}'.format(end_time - start_time))
        return result

    return inner


class HandlerData(object):
    def __init__(self, file):
        self.file = file
        self.remove_list = []
        self.job_info_file = []
        self._load_stopwords()
        self.words_valid_dict = {}

    def _load_stopwords(self):
        with open('removewords.txt', 'r', encoding='utf-8')as f:
            content = f.read()
            self.remove_list = content.split('\n')
            self.remove_list.append('\n')
            self.remove_list.append(' ')

    def count_words(self, words_lists):
        """
        ������ϴ���������ظ����������ݣ���Ƶ������
        :param words_lists:
        :return:
        """
        for word in words_lists:
            if word not in self.remove_list:
                if word in self.words_valid_dict:
                    self.words_valid_dict[word] += 1
                else:
                    self.words_valid_dict[word] = 1
        return self.words_valid_dict

    def read_json(self):
        """
        ��ȡfile�ļ���������json�ļ�
        :param : �ļ���
        :return:����ְҵ��Ϣ�б�
      """
        paths = os.listdir(self.file)
        for path in paths:
            if re.match(r'2019', path):
                with open(path, 'r', encoding='gbk')as f:
                    content = json.loads(f.read())
                    for job_info in content:
                        if job_info['job_name']:
                            self.job_info_file.append(job_info)

    # {'job_name': 'Python�߼�����ʦ', 'job_salary': '25-50K', 'job_text': 'ְλҪ��\n1�������ⲿ��',
    # 'company_name': '���������̵����������޹�˾', 'job_location': '������������������԰4��2¥'}

    def company_classification(self):
        """ͳ�ƹ�˾����"""
        company_dict = {}
        for job_comp in self.job_info_file:
            company_name = job_comp.get('company_name')
            if company_name in company_dict:
                company_dict[company_name] += 1
            else:
                company_dict[company_name] = 1

        return company_dict

    @staticmethod
    def job_info_classification(job_div_info):
        """ͳ��ְҵ��Ϣ"""
        participle_data = []
        for job_comp in job_div_info:
            a = job_comp.get('job_text')
            participle_data = jieba.lcut(a)
        return participle_data

    @count_time
    def multi_job(self):
        """����̽�������"""
        # TODO ����� ��������
        result = []
        po = Pool(POOL_NUMBER)  # ����һ�����̳أ���������2
        get_size = len(self.job_info_file)
        for index in range(POOL_NUMBER):
            data_size_back = int(get_size / POOL_NUMBER * index)
            data_size_forward = int(get_size / POOL_NUMBER * (index - 1))
            divided_data = self.job_info_file[data_size_forward:data_size_back]
            res = po.apply_async(self.job_info_classification, (divided_data,))
            print(res)
            # result.append()
        po.close()
        po.join()

    @staticmethod
    def plot_data(company_data, filenames):
        """
        ����Ϣ����˾��ְλ��Ϣ�����ӻ�
        :param company_data: ����˾��ְλ�������Լ�ֵ����Ϣ����
        :param filenames: �����ļ���λ��
        :return: None
        """
        company_list = []
        y_core = []
        for key, value in company_data.items():
            company_list.append(key)
            y_core.append(value)
        plt.figure(figsize=(20, 8), dpi=80)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)  # ��ʾ��С
        x_cor = [x for x in range(len(company_list))]
        plt.barh(x_cor, y_core, facecolor='orange', height=0.3, label='ְλ����')
        # ������ֱ��
        for score, pos in zip(y_core, x_cor):
            plt.text(score + 2, pos, '%d' % score)
        plt.yticks(x_cor, company_list)
        plt.grid(alpha=0.3)
        plt.xlabel('��˾��Ƹְλ')
        plt.savefig(filenames)
        plt.legend(loc='best')
        plt.show()

    def run(self):
        # ��ȡ����
        self.read_json()
        pr_company_data = self.company_classification()
        company_data = sorted(pr_company_data.items(), key=lambda x: x[1], reverse=True)
        res_company_data = dict(company_data[:9])
        self.plot_data(res_company_data, './company.jpg')

        # ȡ����������ǰ10��Ԫ��
        # words_data = sorted(self.words_valid_dict.items(), key=lambda x: x[1], reverse=True)
        # res_words_data = dict(words_data[:9])
        # print(res_words_data)
        # self.plot_data(res_words_data, './job_info.jpg')


if __name__ == '__main__':
    hd = HandlerData('../data')
    hd.run()
    # hd.plot_data(dict(TEST_COMPANY[:20]), './company.jpg')
