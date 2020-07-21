#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 15:59
@Author  : 鲍凯辰
@File    : connect_img.py
"""
from PIL import Image
from os import listdir

# f = Image.open('asset1/003.bmp')
order = [8, 14, 12, 15, 3, 10, 2, 16, 1, 4, 5, 9, 13, 18, 11, 7, 17, 0, 6]
img_ordered = []
for i in order:
    if i < 10:
        im = Image.open('asset1/00{}.bmp'.format(str(i)))
        img_ordered.append(im)
    else:
        im = Image.open('asset1/0{}.bmp'.format(str(i)))
        img_ordered.append(im)
width, height = img_ordered[0].size
result = Image.new(img_ordered[0].mode, (width * len(img_ordered), height))
print(result.size)
for j, jm in enumerate(img_ordered):
    result.paste(jm, box=(j * width, 0))
result.save('img_after_connect.bmp')
