#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/20 23:30
@Author  : 鲍凯辰
@File    : picture_to_matrix.py
"""
import cv2
import os
import numpy as np

for i in range(0, 209):
    if i < 10:
        file_name = 'asset5/00' + str(i) + 'b.bmp'
    elif i < 100:
        file_name = 'asset5/0' + str(i) + 'b.bmp'
    else:
        file_name = 'asset5/' + str(i) + 'b.bmp'
    img = cv2.imread(file_name, 0)
    height, width = img.shape
    f = open('question3/matrix{}b.txt'.format(str(i)), 'w')
    for k in range(height):
        for j in range(width):
            if img[k, j] > 150:
                f.write('1')
            else:
                f.write('0')
            f.write(' ')
        f.write('\n')
    f.close()
