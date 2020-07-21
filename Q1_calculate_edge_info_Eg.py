#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 16:53
@Author  : 鲍凯辰
@File    : Q1_calculate_edge_info_Eg.py
"""
import pandas as pd

for j in range(0, 19):
    arr = [list() for i in range(30)]
    count = 0
    img = pd.read_table('question1_Eg/matrix{}.txt'.format(j), sep=' ', header=None)
    right = img.iloc[:, 71]
    left = img.iloc[:, 0]
    for i in range(0, 30):
        right_split = right.iloc[17 + 64 * i: 17 + 64 * (i + 1)]
        for k in right_split:
            if k == 0:
                count += 1
        arr[i].append(count)
        count = 0
        left_split = left.iloc[17 + 64 * i: 17 + 64 * (i + 1)]
        for k in left_split:
            if k == 0:
                count += 1
        arr[i].append(count)
        count = 0
    print(arr)
    f = open('question1_edge_Eg/' + str(j) + '.txt', 'w')
    for height in range(0, 30):
        for width in range(0, 2):
            f.write(str(arr[height][width]))
            f.write(' ')
        f.write('\n')
    f.close()
