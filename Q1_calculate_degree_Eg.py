#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 16:53
@Author  : 鲍凯辰
@File    : Q1_calculate_degree_Eg.py
"""
import pandas as pd

arr = [list() for k in range(19)]
for i in range(0, 19):
    root_data = pd.read_table('question1_edge_Eg/' + str(i) + '.txt', sep=' ', header=None)
    root = root_data.iloc[:, 0]
    for others in range(0, 19):
        degree = 0
        target_data = pd.read_table('question1_edge_Eg/' + str(others) + '.txt', sep=' ', header=None)
        target = target_data.iloc[:, 1]
        for j in range(0, 30):
            if root[j] == 0 and target[j] == 0:
                add = 0
            else:
                add = min(root[j], target[j]) / max(root[j], target[j])
            degree = degree + add
        arr[i].append(degree)
f = open('pic_value_Eg.txt', 'w')
for height in range(0, 19):
    for width in range(0, 19):
        f.write(str(arr[height][width]))
        f.write(' ')
    f.write('\n')
f.close()
