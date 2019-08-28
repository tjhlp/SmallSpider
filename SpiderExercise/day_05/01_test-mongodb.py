from pymongo import *

client = MongoClient(host='192.168.146.134', port=27017)

db = client.mysql

db.stu.insert({"name": "hello"})
