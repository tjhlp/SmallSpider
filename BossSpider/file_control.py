import csv


def save_text_file(filename, content):
    with open(filename, 'w', encoding='utf-8')as w:
        w.write(content)


def save_csv_file(filename, content):
    with open(filename, 'w', encoding='gbk')as csv_file:
        filenames = ['job_name', 'job_salary', 'job_text',
                     'company_name', 'job_location']
        writer = csv.DictWriter(csv_file, fieldnames=filenames)
        writer.writerows(content)

