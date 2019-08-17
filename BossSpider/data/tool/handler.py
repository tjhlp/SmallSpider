# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import pandas as pd
from config import KEY_LANGUAGE

POOL_NUMBER = 2


def count_time(func):
    """����ʹ�õļ�ʱװ����"""

    def inner(self, *args, **kwargs):
        print('{} �������ݴ�����ʼ'.format(os.getpid()))
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print('{} �������ݴ�����ɣ�����������ʱ:{}'.format(os.getpid(), end_time - start_time))
        return result

    return inner


class HandlerData(object):
    def __init__(self, file):
        self.file = file
        self.remove_list = []
        self.job_info_file = []
        self.key_language = []
        self._load_words()

    @staticmethod
    def _load_words():
        jieba.load_userdict("userdict.txt")

    @count_time
    def count_words(self, words_lists):
        """
        ������ϴ���������ظ����������ݣ���Ƶ������
        :param words_lists:���зִʵ��б�
        :return:�ؼ����б�
        """
        # TODO �����������
        print('��ʼ������ϴ��ͳ�ƹؼ���{}������'.format(len(words_lists)))
        df_words = pd.DataFrame(words_lists)
        # ����Ƶ�η���
        df_key_words = df_words[df_words[0].isin(KEY_LANGUAGE)]
        words_key_count = pd.value_counts(df_key_words[0])
        # ����Ƶ�η���
        words_count = pd.value_counts(df_words[0])
        words_count.to_csv('{}.csv'.format('count_words'), encoding="utf-8")
        # ת��Ϊ�ֵ�
        words_valid_dict = dict(words_key_count)
        words_valid_dict = self.merge_letter(words_valid_dict)
        words_data = sorted(words_valid_dict.items(), key=lambda x: x[1], reverse=True)
        res_words_data = dict(words_data)
        return res_words_data

    @staticmethod
    def merge_letter(letter_dict):
        """

        :param letter_dict:
        :return:����Сд��ĸ��ɵ�����
        """
        new_dict = {}
        for key, value in letter_dict.items():
            if key.lower() in new_dict:
                new_dict[key.lower()] += value
            else:
                new_dict[key.lower()] = value
        go_lang_count = new_dict.get('golang')
        if go_lang_count is not None:
            del new_dict['golang']
            new_dict['go'] += go_lang_count
        # print(new_dict)
        return new_dict

    def read_json(self):
        """
        ��ȡfile�ļ���������json�ļ�
        :param : �ļ���
        :return:����ְҵ��Ϣ�б�
      """
        paths = os.listdir(self.file)
        for path in paths:
            if re.match(r'2019', path):
                with open('../' + path, 'r', encoding='gbk')as f:
                    content = json.loads(f.read())
                    for job_info in content:
                        if job_info['job_name']:
                            self.job_info_file.append(job_info)

    # {'job_name': 'Python�߼�����ʦ', 'job_salary': '25-50K', 'job_text': 'ְλҪ��\n1�������ⲿ��',
    # 'company_name': '���������̵����������޹�˾', 'job_location': '������������������԰4��2¥'}

    def data_classification(self, search_info):
        """ͳ�ƹ�˾���ݺ�нˮͳ��"""
        company_dict = {}
        for job_comp in self.job_info_file:
            company_name = job_comp.get(search_info)
            if company_name in company_dict:
                company_dict[company_name] += 1
            else:
                company_dict[company_name] = 1
        return company_dict

    @staticmethod
    def salary_classification(salary_dict):
        """
        ��нˮ���ݽ�����ϴ��15-24K    ͳһ����20-25K��һ��
        :param salary_dict: {��нˮ��ע����ְλ��}
        :return: ���У�ͳ�ƺõ�����
        """
        salary_standard_dict = {'0-5k': 0, '5-10k': 0, '10-15k': 0, '15-20k': 0, '20-25k': 0, '25k-30k': 0, '30k����': 0}
        index_list = ['0-5k', '5-10k', '10-15k', '15-20k', '20-25k', '25k-30k', '30k����']

        for key, value in salary_dict.items():
            if not re.match('.*?[��]', key):
                re_key = re.match('^([0-9]{0,3})-([0-9]{0,3})', key)
                data = re_key.group()
                data_spl = data.split('-')
                lower_salary = int(data_spl[0])
                upper_salary = int(data_spl[1])
                level = int(lower_salary / 5)
                if upper_salary - lower_salary > 5:
                    level += 1
                if level > 6:
                    level = 6
                salary_standard_dict[index_list[level]] += value
        return salary_standard_dict

    @staticmethod
    def job_info_classification(job_div_info):
        """ͳ��ְҵ��Ϣ"""
        participle_data = []
        print('�ӽ��̣�{} ��ʼͳ��'.format(os.getpid()))
        for job_comp in job_div_info:
            job_text = job_comp.get('job_text')
            cut_words = jieba.lcut(job_text)
            participle_data.extend(cut_words)
        print('�ӽ��̣�{} ͳ�����'.format(os.getpid()))
        return participle_data

    @count_time
    def multi_job_info(self):
        """����̽�������"""
        results = []
        po = Pool(POOL_NUMBER)  # ����һ�����̳�
        get_size = len(self.job_info_file)
        print('��ʼͳ��{}��ְλ��Ϣ'.format(get_size))
        for index in range(1, POOL_NUMBER + 1):
            data_size_back = int(get_size / POOL_NUMBER * index)
            data_size_forward = int(get_size / POOL_NUMBER * (index - 1))
            divided_data = self.job_info_file[data_size_forward:data_size_back]
            res = po.apply_async(self.job_info_classification, (divided_data,))
            results.append(res)
        po.close()
        po.join()
        job_list = []
        for result in results:
            job_list.extend(result.get())
        return job_list

    @staticmethod
    def plot_data(company_data, filenames, index):
        """
        ����Ϣ����˾��ְλ��Ϣ�����ӻ�
        :param company_data: ����˾��ְλ�������Լ�ֵ����Ϣ����
        :param filenames: �����ļ���λ��
        :return: None
        """
        # ��ע
        label_dict = {
            '��ע': ['ְλ����', '��������', 'ְλ����'],
            '����': ['��˾ְλ��Ŀ�ֲ�ͼ', '�������Էֲ�ͼ', 'нˮ�ֲ�ͼ']
        }
        company_list = []
        y_core = []
        for key, value in company_data.items():
            company_list.append(key)
            y_core.append(value)
        # plt.figure(figsize=(20, 8), dpi=80)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)  # ��ʾ��С
        x_cor = [x for x in range(len(company_list))]
        plt.barh(x_cor, y_core, facecolor='orange', height=0.3, label=label_dict['��ע'][index])
        # �������ֱ��
        for score, pos in zip(y_core, x_cor):
            plt.text(score + 2, pos, '%d' % score)
        plt.yticks(x_cor, company_list)
        plt.grid(alpha=0.3)
        plt.xlabel(label_dict['����'][index])
        plt.savefig(filenames)
        plt.legend(loc='best')
        plt.show()

    def run(self):
        # ��ȡ����
        self.read_json()
        # ��˾����ͳ��
        pr_company_data = self.data_classification('company_name')
        print('�ܹ�{}�ҹ�˾'.format(len(pr_company_data)))
        company_data = sorted(pr_company_data.items(), key=lambda x: x[1], reverse=True)
        res_company_data = dict(company_data[:9])

        # нˮͳ��
        pr_company_salary = self.data_classification('job_salary')
        order_salary = self.salary_classification(pr_company_salary)
        res_salary_data = dict(order_salary)

        # ְλ��Ϣͳ��,ȡ����������ǰ10�Ĺؼ���
        job_list = self.multi_job_info()
        job_info_data = self.count_words(job_list)

        # ��ͼ
        self.plot_data(res_company_data, 'jpg/company.jpg', 0)
        self.plot_data(job_info_data, 'jpg/job_info.jpg', 1)
        self.plot_data(res_salary_data, 'jpg/job_salary.jpg', 2)


if __name__ == '__main__':
    hd = HandlerData('../../data/')
    hd.run()
    # hd.plot_data(dict(TEST_COMPANY[:20]), './company.jpg')