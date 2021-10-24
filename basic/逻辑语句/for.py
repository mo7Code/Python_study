#!/usr/bin/python3


sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)

else:
    print("没有循环数据!")


print("完成循环!")


v = range(1, 5)
b = [1, 2, 3, 4, 5]
c = (1, 2, 3, 4, 5)
print(v)
print(b)
print(c)


for i in c:
    print(i)
