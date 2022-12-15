# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:52:40 2022

@author: Hadi
"""

import os

src_img_path = r"D:/data/custom2/trucks"
dst_img_path = r"D:/data/custom2/images/train"

for fileName in os.listdir(src_img_path):
    srcFile = src_img_path + "/" + fileName
    dstFile = dst_img_path + "/" + fileName
    if os.path.exists(dstFile):
        os.replace(srcFile, dstFile)
        print("file " , dstFile, " was replaced with ", srcFile)