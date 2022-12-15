# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:05:43 2022

@author: Hadi
"""

import os
import shutil

##===============
## parameters
##===============
extension = ".png"
data_path = r"G:/.shortcut-targets-by-id/1DjqpVpkinJDyr2Guv28OWFE-8JNpNHVc/2022DOT_SBIR/20221110Rt130/undistorted/parts/Rt130_PrincetonHights_south_dilemma/frames"
src_img_path = data_path + "/images/test/"
src_lbl_path = data_path + "/labels/test/"
dst_img_path = "D:/data/custom2/trucks/test/"
##===============

if not os.path.exists(dst_img_path):
    os.makedirs(dst_img_path)
    
lines = []
for fileName in os.listdir(src_lbl_path):
    if fileName in "desktop.ini": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    with open(txtFile, 'r') as fp:
        lines = fp.readlines()
    if len(lines) != 1: continue # we want images with only one truck or bus
    
    # read image
    imgFile = os.path.join(src_img_path, fileNameNoExt + extension)
    if not os.path.exists(imgFile): continue

    line = lines[0]
    lst = line.split()
        
    category = lst[0]
    if category == '3' or category == '4':
        shutil.copy(imgFile, os.path.join(dst_img_path, fileNameNoExt + extension))