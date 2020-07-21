#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 17:37
@Author  : 鲍凯辰
@File    : Q1_greed_algorithm_Eg.py
"""
import pandas as pd

f = pd.read_table('pic_value_Eg.txt', sep=' ', header=None)
data = f.values.tolist()
index = 3
arr = [3]
while index != 4:
    max_value = 0
    max_index = -1
    for i in range(0, 19):
        if data[index][i] > max_value:
            max_index = i
            max_value = data[index][i]
    arr.append(max_index)
    index = max_index
print(arr)