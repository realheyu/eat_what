#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

list1 = ['猪杂', '牛杂', '维克']
list_res = []
print('今天吃什么.py 开始运行')
print('今天的菜单有', end='  ')
print(list1)
count = 5

print("计算结果如下: ")
for x in range(count):
    a = random.choice(list1)
    list_res.append(a)
print(list_res)
for x in list1:
    print("%s 出现了: %d 次" % (x, list_res.count(x)))
