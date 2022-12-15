# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:18:10 2022

@author: Hadi
"""

import os
import shutil

##===============
## parameters
##===============
extension = ".png"
data_path = r"D:/data/custom2"
src_img_path = data_path + "/images/"
src_lbl_path = data_path + "/labels/"
train_img_path = data_path + "/images/train/"
train_lbl_path = data_path + "/labels/train/"
val_img_path = data_path + "/images/val/"
val_lbl_path = data_path + "/labels/val/"
test_img_path = data_path + "/images/test/"
test_lbl_path = data_path + "/labels/test/"
##===============

if not os.path.exists(train_img_path): os.makedirs(train_img_path)
if not os.path.exists(train_lbl_path): os.makedirs(train_lbl_path)
if not os.path.exists(val_img_path): os.makedirs(val_img_path)
if not os.path.exists(val_lbl_path): os.makedirs(val_lbl_path)
if not os.path.exists(test_img_path): os.makedirs(test_img_path)
if not os.path.exists(test_lbl_path): os.makedirs(test_lbl_path)

cnt = 1
for fileName in os.listdir(src_img_path):
    if fileName in "desktop.ini" or fileName in "train" or fileName in "val" or fileName in "test": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    imgFile = os.path.join(src_img_path, fileNameNoExt + extension)
    
    if not os.path.exists(txtFile): continue
    if 1 <= cnt <= 7:
        shutil.move(imgFile, os.path.join(train_img_path, fileNameNoExt + extension))
        shutil.move(txtFile, os.path.join(train_lbl_path, fileNameNoExt + '.txt'))
    elif 8 <= cnt <= 9:
        shutil.move(imgFile, os.path.join(val_img_path, fileNameNoExt + extension))
        shutil.move(txtFile, os.path.join(val_lbl_path, fileNameNoExt + '.txt'))
    elif cnt == 10:
        shutil.move(imgFile, os.path.join(test_img_path, fileNameNoExt + extension))
        shutil.move(txtFile, os.path.join(test_lbl_path, fileNameNoExt + '.txt'))
        
    cnt += 1
    if cnt > 10: cnt = 1
        