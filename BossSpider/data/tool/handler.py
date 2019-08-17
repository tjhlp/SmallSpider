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
        self.key_language = []
        self._load_words()

    @staticmethod
    def _load_words():
        jieba.load_userdict("userdict.txt")

    @count_time
    def count_words(self, words_lists):
        """
        数据清洗出现文字重复次数的数据（词频分析）
        :param words_lists:所有分词的列表
        :return:关键词列表
        """
        # TODO 工作年龄分析
        print('开始数据清洗，统计关键字{}条数据'.format(len(words_lists)))
        df_words = pd.DataFrame(words_lists)
        # 语言频次分析
        df_key_words = df_words[df_words[0].isin(KEY_LANGUAGE)]
        words_key_count = pd.value_counts(df_key_words[0])
        # 所有频次分析
        words_count = pd.value_counts(df_words[0])
        words_count.to_csv('{}.csv'.format('count_words'), encoding="utf-8")
        # 转化为字典
        words_valid_dict = dict(words_key_count)
        words_valid_dict = self.merge_letter(words_valid_dict)
        words_data = sorted(words_valid_dict.items(), key=lambda x: x[1], reverse=True)
        res_words_data = dict(words_data)
        return res_words_data

    @staticmethod
    def merge_letter(letter_dict):
        """

        :param letter_dict:
        :return:返回小写字母组成的数字
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
        读取file文件夹下所有json文件
        :param : 文件夹
        :return:所有职业信息列表
      """
        paths = os.listdir(self.file)
        for path in paths:
            if re.match(r'2019', path):
                with open('../' + path, 'r', encoding='gbk')as f:
                    content = json.loads(f.read())
                    for job_info in content:
                        if job_info['job_name']:
                            self.job_info_file.append(job_info)

    # {'job_name': 'Python高级工程师', 'job_salary': '25-50K', 'job_text': '职位要求：\n1、负责外部公',
    # 'company_name': '深圳市星商电子商务有限公司', 'job_location': '深圳龙岗区云里智能园4栋2楼'}

    def data_classification(self, search_info):
        """统计公司数据和薪水统计"""
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
        将薪水数据进行清洗：15-24K    统一算作20-25K这一档
        :param salary_dict: {‘薪水标注’：职位数}
        :return: 排列，统计好的数据
        """
        salary_standard_dict = {'0-5k': 0, '5-10k': 0, '10-15k': 0, '15-20k': 0, '20-25k': 0, '25k-30k': 0, '30k以上': 0}
        index_list = ['0-5k', '5-10k', '10-15k', '15-20k', '20-25k', '25k-30k', '30k以上']

        for key, value in salary_dict.items():
            if not re.match('.*?[天]', key):
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
        """统计职业信息"""
        participle_data = []
        print('子进程：{} 开始统计'.format(os.getpid()))
        for job_comp in job_div_info:
            job_text = job_comp.get('job_text')
            cut_words = jieba.lcut(job_text)
            participle_data.extend(cut_words)
        print('子进程：{} 统计完成'.format(os.getpid()))
        return participle_data

    @count_time
    def multi_job_info(self):
        """多进程解析数据"""
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
    def plot_data(company_data, filenames, index):
        """
        将信息（公司与职位信息）可视化
        :param company_data: （公司与职位数量）以键值对信息传入
        :param filenames: 保存文件的位置
        :return: None
        """
        # 标注
        label_dict = {
            '标注': ['职位数量', '语言数量', '职位数量'],
            '标题': ['公司职位数目分布图', '其他语言分布图', '薪水分布图']
        }
        company_list = []
        y_core = []
        for key, value in company_data.items():
            company_list.append(key)
            y_core.append(value)
        # plt.figure(figsize=(20, 8), dpi=80)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小
        x_cor = [x for x in range(len(company_list))]
        plt.barh(x_cor, y_core, facecolor='orange', height=0.3, label=label_dict['标注'][index])
        # 添加数字标号
        for score, pos in zip(y_core, x_cor):
            plt.text(score + 2, pos, '%d' % score)
        plt.yticks(x_cor, company_list)
        plt.grid(alpha=0.3)
        plt.xlabel(label_dict['标题'][index])
        plt.savefig(filenames)
        plt.legend(loc='best')
        plt.show()

    def run(self):
        # 读取数据
        self.read_json()
        # 公司数据统计
        pr_company_data = self.data_classification('company_name')
        print('总共{}家公司'.format(len(pr_company_data)))
        company_data = sorted(pr_company_data.items(), key=lambda x: x[1], reverse=True)
        res_company_data = dict(company_data[:9])

        # 薪水统计
        pr_company_salary = self.data_classification('job_salary')
        order_salary = self.salary_classification(pr_company_salary)
        res_salary_data = dict(order_salary)

        # 职位信息统计,取出计数排名前10的关键词
        job_list = self.multi_job_info()
        job_info_data = self.count_words(job_list)

        # 画图
        self.plot_data(res_company_data, 'jpg/company.jpg', 0)
        self.plot_data(job_info_data, 'jpg/job_info.jpg', 1)
        self.plot_data(res_salary_data, 'jpg/job_salary.jpg', 2)


if __name__ == '__main__':
    hd = HandlerData('../../data/')
    hd.run()
    # hd.plot_data(dict(TEST_COMPANY[:20]), './company.jpg')
