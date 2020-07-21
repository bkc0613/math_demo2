#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/21 15:59
@Author  : 鲍凯辰
@File    : connect_img.py
"""
from PIL import Image

order = [3, 6, 2, 7, 15, 18, 11, 0, 5, 1, 9, 13, 10, 8, 12, 14, 17, 16, 4]
img_ordered = []
for i in order:
    if i < 10:
        im = Image.open('asset2/00{}.bmp'.format(str(i)))
        img_ordered.append(im)
    else:
        im = Image.open('asset2/0{}.bmp'.format(str(i)))
        img_ordered.append(im)
width, height = img_ordered[0].size
result = Image.new(img_ordered[0].mode, (width * len(img_ordered), height))
for j, jm in enumerate(img_ordered):
    result.paste(jm, box=(j * width, 0))
result.save('img_after_connect_Eg.bmp')
