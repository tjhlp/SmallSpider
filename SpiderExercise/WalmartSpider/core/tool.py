import csv
import time


def write_csv(index, mult_data, filename):
    """
            :param index: 列名（list）
            :param mult_data: 写入的数据（二维列表）
            :return:
            """
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(index)
        for data in mult_data:
            for index_data in data:
                writer.writerow(index_data)


def generate_url(url, page, search_name=None):
    if search_name is None:
        return [[i, url.format(i)] for i in range(1, page + 1)]
    else:
        return [[i, url.format(i, search_name)] for i in range(1, page + 1)]


def count_time(func):
    """计时"""

    def inner(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print('处理数据用时:{}'.format(end_time - start_time))
        return result

    return inner


if __name__ == '__main__':
    INDEXES = ['Rank', 'Id', 'Url', 'Name', 'Price', 'Star', 'Review', 'Page', 'Shop name', 'Main image url', 'Brand',
               'Category', 'Highlights']

