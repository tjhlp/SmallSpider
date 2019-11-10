#将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N

# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"

'''
# 个人解决
res1 = 'LEETCODEISHIRING'
len_str = len(res1)
count = 0
list1 = []
list2 = []
list3 = []
for i in range(0, len_str, 4):
    list1.append(res1[i])
    list2.append(res1[i+1])
    list2.append(res1[i+3])
    list3.append(res1[i+2])

list1.extend(list2)
list1.extend(list3)
print(''.join(list1))

'''


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    r, j, k = [''] * numRows, 0, 1
    for i in s:
        r[j] += i
        print(r)
        j += k
        if j == 0 or j == numRows - 1:
            k = -k
    return "".join(r)

res  = convert('LEETCODEISHIRING' , 3)

# print(res)




