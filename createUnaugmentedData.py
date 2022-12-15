# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:29:52 2022

@author: Hadi

this code creates a dataset from custom2 of only images with no augmentation
"""

import os
import shutil

##===============
## parameters
##===============
extension = ".png"
data_path = r"D:/data/custom2"
train_test_vel = "test"
src_img_path = data_path + "/images/" + train_test_vel + "/"
src_lbl_path = data_path + "/labels/" + train_test_vel + "/"
dst_img_path = "D:/data/custom3/images/" + train_test_vel + "/"
dst_lbl_path = "D:/data/custom3/labels/" + train_test_vel + "/"
##===============

if not os.path.exists(dst_img_path): os.makedirs(dst_img_path)
if not os.path.exists(dst_lbl_path): os.makedirs(dst_lbl_path)
    
lines = []
for fileName in os.listdir(src_lbl_path):
    if fileName in "desktop.ini": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    imgFile = os.path.join(src_img_path, fileNameNoExt + extension)
    
    with open(txtFile, 'r') as fp:
        lines = fp.readlines()
    if len(lines) <= 1: continue # we want images with more than one object (unaugmented)
    if not os.path.exists(imgFile): continue
    
    shutil.copy(imgFile, os.path.join(dst_img_path, fileNameNoExt + extension))
    shutil.copy(txtFile, os.path.join(dst_lbl_path, fileNameNoExt + ".txt"))