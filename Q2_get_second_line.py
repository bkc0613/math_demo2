#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/22 17:40
@Author  : 鲍凯辰
@File    : Q2_get_second_line.py
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

arr = [list() for k in range(209)]
for i in range(0, 209):
    data = pd.read_table('question2_Ch/matrix{}.txt'.format(i), sep=' ', header=None)
    for j in range(0, 180):
        count = 0
        for content in data.iloc[j, :]:
            if content == 1:
                count += 1
                continue
            else:
                break
        if count == 72:
            arr[i].append(1)
        else:
            arr[i].append(0)

second_line = []
# init_center = [7, 14, 29, 38, 49, 61, 71, 89, 94, 125, 168]
for x in range(0, 209):
    curr_arr = arr[x]
    for i in range(0, 180):
        if curr_arr[i] == 0 and curr_arr[i + 1] == 1:
            if i > 69:
                add = i - 40
            else:
                add = i + 31
            second_line.append(add)
            break
second_line_matrix = np.array([second_line])
second_line_matrix = second_line_matrix.T
# print(second_line_matrix)
DF = pd.DataFrame(second_line_matrix)
DF.to_csv('second_line.csv')
# km = KMeans(n_clusters=11, n_init=1, init=np.array([[58], [93], [30], [46], [37], [64], [68], [79], [52], [75], [89]])).fit(second_line_matrix)
# # print(km.labels_)
# result = km.labels_.tolist()
# dic = dict()
# for i in range(0, 209):
#     if result[i] not in dic:
#         dic[result[i]] = [i]
#     else:
#         dic[result[i]].append(i)
#
# f = open('KMeans_result.txt', 'w')
# for a in range(0, 11):
#     for b in dic[a]:
#         f.write(str(b))
#         f.write(' ')
#     f.write('\n')
# f.close()
