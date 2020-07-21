#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/20 23:30
@Author  : 鲍凯辰
@File    : picture_to_matrix.py
"""
import cv2

for i in range(0, 19):
    if i < 10:
        file_name = 'asset2/00' + str(i) + '.bmp'
    elif i < 100:
        file_name = 'asset2/0' + str(i) + '.bmp'
    else:
        file_name = 'asset2/' + str(i) + '.bmp'
    img = cv2.imread(file_name, 0)
    height, width = img.shape
    f = open('question1_Eg/matrix{}.txt'.format(str(i)), 'w')
    for k in range(height):
        for j in range(width):
            if img[k, j] > 150:
                f.write('1')
            else:
                f.write('0')
            f.write(' ')
        f.write('\n')
    f.close()
