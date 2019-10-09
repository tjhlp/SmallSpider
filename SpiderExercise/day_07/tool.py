import csv


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
            writer.writerow(data)


def generate_url(url, page, search_name=None):
    if search_name is None:
        return [url.format(i) for i in range(1, page + 1)]
    else:
        return [url.format(i, search_name) for i in range(1, page + 1)]
