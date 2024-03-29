#!/usr/bin/python3

# Set（集合）

# 集合（set）是一个无序的不重复元素序列。

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)


# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素


thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
thisset2 = set(("Google"))


print("thisset", thisset)
print("thisset2", thisset2)
