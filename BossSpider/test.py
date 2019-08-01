import jieba
import random
from datetime import datetime
import json
print(type(datetime.now().strftime('%Y-%m-%d %H:%M')))
t = datetime.now().strftime('%Y%m%d-%H-%M')
n = 1
print(t + '_job.json')
with open(t + '_job.json', 'w')as r:
    r.write(json.dumps(n))
print(random.randint(1, 5))

list1 = [1,2,3]
print(list1[:1])
