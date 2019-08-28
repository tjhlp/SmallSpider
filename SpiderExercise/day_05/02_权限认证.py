#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 0. pip install pymongo

# 1. 导入模块
from pymongo import *

# 2. 创建客户端对象
'''
client = MongoClient(host='127.0.0.1',port=27017)
# 通过管理员登录
admin = client.admin
admin.authenticate('python','123456')
'''
# 通过uri进行登录
user = 'python'
pwd = '123456'
server = '192.168.146.134'
port = '27017'
db_name = 'mysql'
uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port +'/'+ db_name
client = MongoClient(uri)


# 获取数据对象
db_01 = client.mysql

# 查,返回值是一个游标
# 游标指针指向当前记录
cursor = db_01.stu.find()
print(cursor)

for row in cursor:
    print(row)
