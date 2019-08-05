# coding=gbk
import csv, os
import pandas as pd
import json


def save_text_file(filename, content):
    """����txt�ļ�"""
    with open(filename, 'w', encoding='utf-8')as w:
        w.write(content)


def save_csv_file(filename, content):
    with open(filename, 'w', encoding='gbk')as csv_file:
        filenames = ['job_name', 'job_salary', 'job_text',
                     'company_name', 'job_location']
        writer = csv.DictWriter(csv_file, fieldnames=filenames)
        writer.writerows(content)


def save_pd_csv(filename, df):
    try:
        df.to_csv(filename)
    except:
        raise ValueError('ת��csvʧ��')


def save_job_json(job_info, filename, update=False):
    if not os.path.exists('data'):
        os.mkdir('data')
    if not update:
        filename = 'data/' + filename
        try:
            with open(filename, 'r', encoding='utf-8')as r:
                job_content = json.loads(r.read())
            for index in range(len(job_info)):
                list_data = job_info[index]
                job_content.append(list_data)
        except:
            job_content = job_info
    else:
        job_content = job_info

    with open(filename, 'w', encoding='utf-8')as w:
        res = json.dumps(job_content)
        w.write(res)


def read_json(filename):
    if os.path.exists('data'):
        filename = 'data/' + filename
        try:
            with open(filename, 'r', encoding='gbk')as r:
                return json.loads(r.read())
        except:
            raise RuntimeError('�ļ�δ�ҵ�')
    else:
        raise RuntimeError('�ļ���δ�ҵ�')


if __name__ == '__main__':
    info = [{'job_name': 'Python����ʦ', 'job_salary': '12-24K',
             'job_text': "����λְ��\n1������KLOOK Affiliateҵ���ߵĺ���з�����\n2���������������Ŀ����������ȼ�����ʱ����������\n3�����Ʒ����ͨ���󣬽�����صļ����ĵ���д���������\n4������ģ�黯���ֲ��ϵͳ���˼����п�������������������������Ϸ�����м�غ����ܵ���\n5��ѧϰ�о�ҵ���Ƚ����������ּ�������\n����ְ�ʸ�\n1����������Python/Java/Go�ȱ�����ԣ�������ʵ�ļ���������ͱ����������Ϥ�������㷨�����ݽṹ, ��������������, HttpЭ��, �ܹ��������������������, ��������MySQL���ݿ�\n2���������ճ�����Linux����������, ����Nginx, Mysql,��ϤRESTful API��ƣ��й�������ҵ��ϵͳ����ؼ�����Ʒ��������\n3���н�ǿ�Ĺ��������ĺ����õĹ�ͨЭ���������ܹ����ٶ�λ���Ⲣ�������\n4����Դ���������ȣ�GitHubԴ�������ȣ���������������\n��KLOOK������\n1�����ʡ����������Ի��İ칫������\n2����ƽ�����Ŷӹ���ҵ����ٷ�չ����������ͼ�ֵ�ܿ�ᱻ��ҿ�����\n3�����źͳ�������Ĺ��ʻ��Ŷӣ���Ů����ֵ���ұ���Э����ÿ���˶�����ôһ�㴫�棻\n4�����صĴ�ҵ�Ŷӷ�Χ����������ɹ���֮�࣬�����Լ���ʱ��ѧϰ���ɳ���\n5����Ҫ��Homieͬ���Σ��Ŷ��㼣̤�����50+��������һ��ռ�����\n6���Ŷ���������裬����С�۲ͣ��������ﲻ���Ρ� ��KLOOK��·�Ŷӡ�\n\n- ��2014���������ۣ�����ۣ��ܲ��������ڣ�ȫ�����з����ģ���̨�����¼��¡��׶������ȡ���¡�¡�����������������־���С��żӴ�ϰݡ��������񼰰�ķ˹�ص��ȵ�����20�����ذ칫�ң�\n- ���ʻ��Ŷӣ�����1000���Ŷӳ�Ա�����Գ���25�����Ҽ�������\n- ֧��30���ֻ��ҽ��׼�8�����ԡ� ��KLOOK��˭��\nKLOOK��·������ȫ�����ȵ���������Ԥ��ƽ̨�� �ṩ270���Ŀ�ĵص�����������񣬰���������Ʊ��һ���Ρ��������顢�س���ʳ��WiFi�����ؽ�ͨ�ȡ�KLOOK�볬��10,000λ��Ӧ�̻����������ǳ���270��Ŀ�ĵأ��ṩ����100,000�ֻ�����з����Դ���������KLOO",
             'company_name': '�����п�·����Ƽ����޹�˾',
             'job_location': '������ ������ �����찲�Ƽ���ҵ԰A�� 9¥902'}]

    # save_job_json(info, '1.json')
    content = read_json('1.json')
    for index in content:
        print(index)
