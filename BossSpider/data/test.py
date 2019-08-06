#encodig=utf-8
from __future__ import print_function, unicode_literals
import jieba


test_sent = "李小福是创新办主任也是云计算方面的专家，云计算云计算云计算，云计算是我国新技术"
words1 = jieba.cut(test_sent)
print('/'.join(words1))

print("="*40)

jieba.load_userdict("userdict.txt")
words2 = jieba.cut(test_sent)
print('/'.join(words2))




