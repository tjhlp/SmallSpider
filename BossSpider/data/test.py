list_a = [1,2,3,4,5,1,2,3,2,3,8,5,4,32,9,75,4,3,4,5,4345,]

set_a = set(list_a)
print(set_a)
dict_a = {}
for i in set_a:
    dict_a[i] = list_a.count(i)
print(dict_a)



