# coding=gbk
import csv, os
import pandas as pd
import json


def save_text_file(filename, content):
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
        raise ValueError('转化csv失败')


def save_job_json(job_info, filename, update=False):
    if os.path.exists('data'):
        # print(filename)
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
    else:
        os.mkdir('data')


def read_json(filename):
    if os.path.exists('data'):
        filename = 'data/' + filename
        try:
            with open(filename, 'r', encoding='gbk')as r:
                return json.loads(r.read())
        except:
            raise RuntimeError('文件未找到')
    else:
        raise RuntimeError('文件夹未找到')


if __name__ == '__main__':
    info = [{'job_name': 'Python工程师', 'job_salary': '12-24K',
             'job_text': "【岗位职责】\n1、参与KLOOK Affiliate业务线的后端研发工作\n2、负责管理自身项目和需求的优先级、按时高质量交付\n3、与产品经理沟通需求，进行相关的技术文档编写，方案设计\n4、运用模块化、分层等系统设计思想进行开发工作，对自身所负责的线上服务进行监控和性能调优\n5、学习研究业界先进技术，保持技术进步\n【任职资格】\n1、熟练掌握Python/Java/Go等编程语言，具有扎实的计算机基础和编程能力，熟悉常见的算法与数据结构, 熟练掌握网络编程, Http协议, 能够解决常见的网络编程问题, 熟练掌握MySQL数据库\n2、熟练掌握常见的Linux服务器配置, 比如Nginx, Mysql,熟悉RESTful API设计，有过互联网业务系统或相关技术产品开发经验\n3、有较强的工作责任心和良好的沟通协调能力，能够快速定位问题并解决问题\n4、开源贡献者优先，GitHub源码者优先，技术博客者优先\n【KLOOK福利】\n1、舒适、健康、人性化的办公环境；\n2、扁平化的团队管理，业务飞速发展，你的能力和价值很快会被大家看到；\n3、开放和充满激情的国际化团队，男女高颜值并且比例协调，每个人都有那么一点传奇；\n4、独特的创业团队氛围会让你在完成工作之余，还有自己的时间学习、成长；\n5、还要跟Homie同富游：团队足迹踏遍国家50+，等你来一起占领地球；\n6、团队天天下午茶，周周小聚餐，月胖三斤不是梦。 【KLOOK客路团队】\n\n- 于2014年成立于香港，在香港（总部）、深圳（全球技术研发中心）、台北、新加坡、首尔、曼谷、吉隆坡、东京、马尼拉、胡志明市、雅加达、迪拜、孟买、宿务及阿姆斯特丹等地设有20个当地办公室；\n- 国际化团队，超过1000名团队成员，来自超过25个国家及地区；\n- 支持30余种货币交易及8种语言。 【KLOOK是谁】\nKLOOK客路旅行是全球领先的旅游体验预订平台， 提供270多个目的地的旅游体验服务，包括景点门票、一日游、独特体验、必吃美食、WiFi及当地交通等。KLOOK与超过10,000位供应商伙伴合作，覆盖超过270个目的地，提供超过100,000种活动及旅行服务。自创立以来，KLOO",
             'company_name': '深圳市客路网络科技有限公司',
             'job_location': '深圳市 福田区 福田天安科技创业园A座 9楼902'}]

    # save_job_json(info, '1.json')
    content = read_json('1.json')
    for index in content:
        print(index)
