# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import cv2 as cv

##===============
## parameters
##===============
train_or_val = "val" # train, val
dataset = "AUAIR"
category = '1' # 0:person, 1:cyclist, 2:car, 3:bus, 4:truck
class_name = "cyclist"
##===============

src_img_path = "D:/data/" + dataset + "/images/" + train_or_val
src_lbl_path = "D:/data/" + dataset + "/labels/" + train_or_val
dst_img_path = "D:/data/" + dataset + "/classes/" + class_name + "/images/" + train_or_val
dst_lbl_path = "D:/data/" + dataset + "/classes/" + class_name + "/labels/" + train_or_val

# src_img_path = "D:/data/COCO/train2017/"
# src_lbl_path = "D:/data/COCO/labels/train/"


cnt = 0
for fileName in os.listdir(src_lbl_path):
    fileNameNoExt = os.path.splitext(fileName)[0]
    
    # only for MIO
    ####
    #fileNameNoExt = str(int(fileNameNoExt) - 1)
    #fileNameNoExt = fileNameNoExt.zfill(8)
    ####
    
    with open(os.path.join(src_lbl_path, fileName)) as f:
        for line in f:
            lst = line.split()
            if lst[0] == category:
                if os.path.exists(os.path.join(src_img_path, fileNameNoExt + '.jpg')):
                    img = cv.imread(os.path.join(src_img_path, fileNameNoExt + '.jpg'))
                    imgW, imgH = img.shape[1], img.shape[0]
                    xCenter, yCenter = int(float(lst[1]) * imgW), int(float(lst[2]) * imgH)
                    w, h = int(float(lst[3]) * imgW), int(float(lst[4]) * imgH)
                    x1, y1 = xCenter - w // 2, yCenter - h // 2
                    x2, y2 = x1 + w, y1 + h
                    x1 = max(x1, 0)
                    y1 = max(y1, 0)
                    x2 = min(x2, imgW)
                    y2 = min(y2, imgH)
                    if x1 >= x2 or y1 >= y2:
                        continue
                    imgCropped = img[y1:y2, x1:x2] 
                    imgName = dataset + "_" + class_name + "_" + "{:06d}".format(cnt)
                    cnt += 1
                    #print(x1, " ", x2, " " , y1, " ", y2)
                    cv.imwrite(os.path.join(dst_img_path, imgName + '.jpg'), imgCropped)
                    with open(os.path.join(dst_lbl_path, imgName + '.txt'), 'w') as f1:
                              f1.write(category + " " + "{:06f}".format(0.5) + " " + "{:06f}".format(0.5) +
                                       " " + "{:06f}".format(1) + " " + "{:06f}".format(1))
                    
                    #cv.imshow("cropped", imgCropped)
                    #cv.waitKey(0)
                    #break
                    
        