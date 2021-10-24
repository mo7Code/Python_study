#!/usr/bin/python3
# while 语句

n = 100
sum = 0
counter = start = 1

while counter <= n:
    sum = sum + counter
    counter += 1

print("%d 到 %d 之和为： %d" % (start, n, sum))
