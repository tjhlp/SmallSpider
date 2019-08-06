# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt

jieba.load_userdict("userdict.txt")
POOL_NUMBER = 2
po = Pool(POOL_NUMBER)  # ����һ�����̳أ���������2

def count_time(func):
    """��ʱװ����"""

    def inner(self,*args, **kwargs):
        start_time = time.time()
        result = func(self,*args, **kwargs)
        end_time = time.time()
        print('����������ʱ:{}'.format(end_time - start_time))
        return result

    return inner


class HandlerData(object):
    def __init__(self, file):
        self.file = file
        self.remove_list = []
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
        job_info_file = []
        paths = os.listdir(self.file)
        for path in paths:
            if re.match(r'2019', path):
                with open(path, 'r', encoding='gbk')as f:
                    content = json.loads(f.read())
                    for job_info in content:
                        if job_info['job_name']:
                            job_info_file.append(job_info)
        return job_info_file

    # {'job_name': 'Python�߼�����ʦ', 'job_salary': '25-50K', 'job_text': 'ְλҪ��\n1�������ⲿ��',
    # 'company_name': '���������̵����������޹�˾', 'job_location': '������������������԰4��2¥'}

    @count_time
    def data_classification(self, job_info_file):
        """��������"""
        company_dict = {}
        for job_comp in job_info_file:
            a = job_comp.get('job_text')
            participle_data = jieba.lcut(a)
            company_name = job_comp.get('company_name')
            process_data1 = self.count_words(participle_data)
            if company_name in company_dict:
                company_dict[company_name] += 1
            else:
                company_dict[company_name] = 1

        return company_dict

    @staticmethod
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

    def run(self):
        # ��ȡ����
        job_info_file = self.read_json()
        pr_company_data = self.data_classification(job_info_file)
        company_data = sorted(pr_company_data.items(), key=lambda x: x[1], reverse=True)
        res_company_data = dict(company_data[:9])
        self.plot_data(res_company_data, './company.jpg')

        # ����� ��������
        # result = []
        # for index in range(POOL_NUMBER):
        #     result.append(po.apply_async(self.data_classification, (job_info_file,)))
        #
        # print(len(company_data))
        # print(company_data)
        # po.close()  # �رս��̳أ��رպ�po���ٽ����µ�����
        # po.join()


        # ȡ����������ǰ10��Ԫ��
        # words_data = sorted(self.words_valid_dict.items(), key=lambda x: x[1], reverse=True)
        # res_words_data = dict(words_data[:9])
        # print(res_words_data)
        # self.plot_data(res_words_data, './job_info.jpg')


if __name__ == '__main__':
    hd = HandlerData('../data')
    hd.run()


