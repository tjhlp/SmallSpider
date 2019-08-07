import pandas as pd
import time
import random
import os


def count_time(func):
    """类中使用的计时装饰器"""

    def inner(*args, **kwargs):
        print('{} 进程数据处理开始'.format(os.getpid()))
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('{} 进程数据处理完成，处理数据用时:{}'.format(os.getpid(), end_time - start_time))
        return result

    return inner


c = ['cdadf', '法撒旦', '我', '哈哈', 'werwq', 'asfweq', 'qwerqwe', 'asfdas', 'asdf', 'asdfas', '她与他', 'werewolf', 'safd',
     '委任为', '五七二']


@count_time
def generate_str_list():
    a = []
    for i in range(10000000):
        d = random.choice(c)
        a.append(d)
    return a


@count_time
def func(str_list):
    str_dict = {}
    str_set = set(str_list)
    for i in str_set:
        str_dict[i] = str_list.count(i)
    print(str_dict)


@count_time
def pd_func(str_list):
    df_a = pd.DataFrame(str_list)
    # df_b = pd.value_counts(df_a[0])
    df_c = dict(pd.value_counts(df_a[0]))
    print(df_c)


a = generate_str_list()
pd_func(a)
func(a)
