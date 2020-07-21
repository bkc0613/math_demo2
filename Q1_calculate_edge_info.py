#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 9:30
@Author  : 鲍凯辰
@File    : Q1_calculate_edge_info.py
"""
import pandas as pd

for j in range(0, 19):
    arr = [list() for i in range(28)]
    count = 0
    img = pd.read_table('question1_ch/matrix{}.txt'.format(j), sep=' ', header=None)
    right = img.iloc[:, 71]
    left = img.iloc[:, 0]
    for i in range(0, 28):
        right_split = right.iloc[25 + 68 * i: 25 + 68 * (i + 1)]
        for k in right_split:
            if k == 0:
                count += 1
        arr[i].append(count)
        count = 0
        left_split = left.iloc[25 + 68 * i: 25 + 68 * (i + 1)]
        for k in left_split:
            if k == 0:
                count += 1
        arr[i].append(count)
        count = 0
    print(arr)
    f = open('question1_edge/'+str(j)+'.txt', 'w')
    for height in range(0, 28):
        for width in range(0, 2):
            f.write(str(arr[height][width]))
            f.write(' ')
        f.write('\n')
    f.close()
