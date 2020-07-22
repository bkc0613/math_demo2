#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 22:38
@Author  : 鲍凯辰
@File    : Q2_get_left.py
"""
import pandas as pd

result = []
for i in range(0, 209):
    data = pd.read_table('question2_Ch/matrix{}.txt'.format(str(i)), sep=' ', header=None)
    data_left = data.iloc[:, 0]
    count = 0
    for j in data_left:
        if j == 1:
            count += 1
            if count == 180:
                result.append(i)
                break
            continue
        else:
            break
print(result)
