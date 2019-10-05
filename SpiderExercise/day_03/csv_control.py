import csv


def write_csv(index, mult_data,filename):
    """

    :param index: 列名（list）
    :param mult_data: 写入的数据（二维列表）
    :return:
    """
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(index)
        for data in mult_data:
            writer.writerow(data)

if __name__ == '__main__':
    pass