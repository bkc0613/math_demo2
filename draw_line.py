#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/22 22:15
@Author  : 鲍凯辰
@File    : draw_line.py
"""
import pandas as pd

f = open('KMeans_result.txt')
aline = f.readline()
aline = aline.split()
int_aline = []
for i in aline:
    int_aline.append(int(i))
edge_dic = dict()
second_number = pd.read_csv('second_line.csv', header=None)
print(second_number.loc[1, 1])
for j in int_aline:
    data = pd.read_table('question2_Ch/matrix{}.txt'.format(j), sep=' ', header=None)
    s_index = second_number.loc[j, 1]
    left = data.iloc[s_index:s_index+50, 0]
    right = data.iloc[s_index:s_index+50, 71]
    count_left = 0
    count_right = 0
    for il in left:
        if il == 0:
            count_left += 1
    for ir in right:
        if ir == 0:
            count_right += 1
    edge_dic[j] = [count_left, count_right]
print(edge_dic)
arr = []
for m in edge_dic:
    add = []
    for n in edge_dic:
        if edge_dic[m][1] == 0 and edge_dic[n][0] == 0:
            degree = 0
        else:
            degree = min(edge_dic[m][1], edge_dic[n][0]) / max(edge_dic[m][1], edge_dic[n][0])
        add.append(degree)
    arr.append(add)
print(arr)
index = 1
order = [1]
while index != 17:
    max_value = 0
    max_index = -1
    for i in range(0, 19):
        if arr[index][i] > max_value:
            max_index = i
            max_value = arr[index][i]
    order.append(max_index)
    index = max_index
print(order)
