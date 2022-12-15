# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:25:26 2022

This program copoies text files from a folder based on the image files with the same name

@author: Hadi
"""
import os
import shutil

##===============
## parameters
##===============
extension = ".png"
src_img_path = "D:/data/traffic_videos/20221019_US46_SouthBeverwyckRoad/camera1_3/images/val"
src_lbl_path = "D:/data/traffic_videos/20221019_US46_SouthBeverwyckRoad/camera1_3/obj_train_data/"
dst_lbl_path = "D:/data/traffic_videos/20221019_US46_SouthBeverwyckRoad/camera1_3/labels/val/"
##===============


for fileName in os.listdir(src_img_path):
    fileNameNoExt = os.path.splitext(fileName)[0]
    if os.path.exists(os.path.join(src_lbl_path, fileNameNoExt + ".txt")):
        shutil.copyfile(os.path.join(src_lbl_path, fileNameNoExt + ".txt"), os.path.join(dst_lbl_path, fileNameNoExt + '.txt'))