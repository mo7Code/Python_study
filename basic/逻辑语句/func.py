#!/usr/bin/python3

# 函数

# def hello():
#     print("hello")


# hello()

# a = [123]
# a = "123"

# print(a)


# def change(a):
#     print(id(a))   # 指向的是同一个对象
#     a = 10
#     print(id(a))   # 一个新对象


# a = 1
# print(id(a))
# change(a)

v = 1


def change(v):
    v = 123
    print("func-out", id(v))


change(v)

print("out", id(v))
