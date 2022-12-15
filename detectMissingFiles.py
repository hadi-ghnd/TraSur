# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:27:54 2022

@author: Hadi
"""

import os

data_path = r"D:/data/AUAIR/classes/bus"
src_lbl_path = data_path + "/labels/trainAug/"
src_img_path = data_path + "/images/trainAug/"

#file1 = open(data_path + "/missingLabels.txt", "w")

# cntImg = len([entry for entry in os.listdir(src_img_path) if os.path.isfile(os.path.join(src_img_path, entry))])
# cntLbl = len([entry for entry in os.listdir(src_lbl_path) if os.path.isfile(os.path.join(src_lbl_path, entry))])

# print(cntImg, " images")
# print(cntLbl, " labels")

cnt = 0
for fileName in os.listdir(src_lbl_path): 
    if fileName in "desktop.ini": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    imgFile = os.path.join(src_img_path, fileNameNoExt + '.jpg')
    
    if not os.path.exists(imgFile):
        cnt += 1
        print(fileName)
        os.remove(imgFile)
        #file1.write(fileName + "\n")
        
print(cnt)
