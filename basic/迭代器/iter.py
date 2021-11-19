#!/usr/bin/python3
import sys

# 迭代器与生成器
list = [1, 2, 3, 4]
it = iter(list)

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()