# coding=gbk
import json
import os
import re
import jieba
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import pandas as pd
from config import TEST_COMPANY

POOL_NUMBER = 2


def count_time(func):
    """类中使用的计时装饰器"""

    def inner(self, *args, **kwargs):
        print('{} 进程数据处理开始'.format(os.getpid()))
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print('{} 进程数据处理完成，处理数据用时:{}'.format(os.getpid(), end_time - start_time))
        return result

    return inner


class HandlerData(object):
    def __init__(self, file):
        self.file = file
        self.remove_list = []
        self.job_info_file = []
        self._load_stopwords()

    def _load_stopwords(self):
        jieba.load_userdict("userdict.txt")
        with open('removewords.txt', 'r', encoding='utf-8')as f:
            content = f.read()
            self.remove_list = content.split('\n')
            self.remove_list.append('\n')
            self.remove_list.append(' ')

    @count_time
    def count_words(self, words_lists):
        """
        数据清洗出现文字重复次数的数据（词频分析）
        :param words_lists:
        :return:
        """
        print('开始数据清洗，统计关键字{}条数据'.format(len(words_lists)))
        df_words = pd.DataFrame(words_lists)
        words_valid_dict = dict(pd.value_counts(df_words[0]))
        words_data = sorted(words_valid_dict.items(), key=lambda x: x[1], reverse=True)
        res_words_data = dict(words_data[:9])
        print(res_words_data)
        return res_words_data

    def read_json(self):
        """
        读取file文件夹下所有json文件
        :param : 文件夹
        :return:所有职业信息列表
      """
        paths = os.listdir(self.file)
        for path in paths:
            if re.match(r'2019', path):
                with open(path, 'r', encoding='gbk')as f:
                    content = json.loads(f.read())
                    for job_info in content:
                        if job_info['job_name']:
                            self.job_info_file.append(job_info)

    # {'job_name': 'Python高级工程师', 'job_salary': '25-50K', 'job_text': '职位要求：\n1、负责外部公',
    # 'company_name': '深圳市星商电子商务有限公司', 'job_location': '深圳龙岗区云里智能园4栋2楼'}

    def company_classification(self):
        """统计公司数据"""
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
        """统计职业信息"""
        participle_data = []
        print('子进程：{} 开始统计'.format(os.getpid()))
        for job_comp in job_div_info:
            a = job_comp.get('job_text')
            participle_data.extend(jieba.lcut(a))
        print('子进程：{} 统计完成'.format(os.getpid()))
        return participle_data

    @count_time
    def multi_job_info(self):
        """多进程解析数据"""
        # TODO 多进程 解析数据
        results = []
        po = Pool(POOL_NUMBER)  # 定义一个进程池
        get_size = len(self.job_info_file)
        print('开始统计{}个职位信息'.format(get_size))
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
    def plot_data(company_data, filenames):
        """
        将信息（公司与职位信息）可视化
        :param company_data: （公司与职位数量）以键值对信息传入
        :param filenames: 保存文件的位置
        :return: None
        """
        company_list = []
        y_core = []
        for key, value in company_data.items():
            company_list.append(key)
            y_core.append(value)
        # plt.figure(figsize=(20, 8), dpi=80)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小
        x_cor = [x for x in range(len(company_list))]
        plt.barh(x_cor, y_core, facecolor='orange', height=0.3, label='职位数量')
        # 添加数字标号
        for score, pos in zip(y_core, x_cor):
            plt.text(score + 2, pos, '%d' % score)
        plt.yticks(x_cor, company_list)
        plt.grid(alpha=0.3)
        # plt.xlabel('公司招聘职位')
        plt.savefig(filenames)
        plt.legend(loc='best')
        plt.show()

    def run(self):
        # 公司数据统计
        self.read_json()
        pr_company_data = self.company_classification()
        print('总共{}家公司'.format(len(pr_company_data)))
        company_data = sorted(pr_company_data.items(), key=lambda x: x[1], reverse=True)
        res_company_data = dict(company_data[:9])
        self.plot_data(res_company_data, './company.jpg')

        # 职位信息统计,取出计数排名前10的关键词
        job_list = self.multi_job_info()
        job_info_data = self.count_words(job_list)
        self.plot_data(job_info_data, './job_info.jpg')


if __name__ == '__main__':
    hd = HandlerData('../data')
    hd.run()
    # hd.plot_data(dict(TEST_COMPANY[:20]), './company.jpg')
