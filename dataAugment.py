# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:19:49 2022

@author: Hadi
"""

import os
import numpy as np
import cv2 as cv
import albumentations as A
import shutil

##===============
## parameters
##===============
train_or_val = "train" # train, val
dataset = "AUAIR"
category = '1' # 0:person, 1:cyclist, 2:car, 3:bus, 4:truck
class_name = "cyclist"
extension = '.jpg'

src_img_path = "D:/data/" + dataset + "/classes/" + class_name + "/images/" + train_or_val
src_lbl_path = "D:/data/" + dataset + "/classes/" + class_name + "/labels/" + train_or_val
dst_img_path = "D:/data/" + dataset + "/classes/" + class_name + "/images/" + train_or_val + "Aug"
dst_lbl_path = "D:/data/" + dataset + "/classes/" + class_name + "/labels/" + train_or_val + "Aug"

if not os.path.exists(dst_img_path): os.makedirs(dst_img_path)
if not os.path.exists(dst_lbl_path): os.makedirs(dst_lbl_path)

##===============
## transformations
##===============
transforms = []
t1 = A.Compose([A.HorizontalFlip(p=0.5)])
t2 = A.Compose([A.RandomBrightnessContrast(p=0.2)])
t3 = A.Compose([A.CLAHE()])
t4 = A.Compose([A.ColorJitter ()])
t5 = A.Compose([A.FancyPCA()])
t6 = A.Compose([A.GaussNoise ()])
t7 = A.Compose([A.HueSaturationValue ()])
t8 = A.Compose([A.ISONoise ()])
t9 = A.Compose([A.MultiplicativeNoise ()])
#t10 = A.Compose([A.RandomFog ()])
t11 = A.Compose([A.RandomGamma ()])
#t12 = A.Compose([A.RandomRain()])
#t13 = A.Compose([A.RandomShadow ()])
#t14 = A.Compose([A.RandomSnow()])
#t15 = A.Compose([A.SafeRotate()])
t16 = A.Compose([A.RandomToneCurve ()])
t17 = A.Compose([A.RandomContrast()])
t18 = A.Compose([A.RGBShift()])
t19 = A.Compose([A.RingingOvershoot()])
t20 = A.Compose([A.Sharpen()])
#t21 = A.Compose([A.Spatter ()])
#t22 = A.Compose([A.Superpixels ()])
t23 = A.Compose([A.RandomBrightness()])
t24 = A.Compose([A.ToSepia ()])
t25 = A.Compose([A.UnsharpMask ()])

transforms.append(t1)
transforms.append(t2)
transforms.append(t3)
transforms.append(t4)
transforms.append(t5)
transforms.append(t6)
transforms.append(t7)
transforms.append(t8)
transforms.append(t9)
#transforms.append(t10)
transforms.append(t11)
#transforms.append(t12)
#transforms.append(t13)
#transforms.append(t14)
#transforms.append(t15)
transforms.append(t16)
transforms.append(t17)
transforms.append(t18)
transforms.append(t19)
transforms.append(t20)
#transforms.append(t21)
#transforms.append(t22)
transforms.append(t23)
transforms.append(t24)
transforms.append(t25)
##===============



# src_img_path = "D:/data/COCO/train2017/"
# src_lbl_path = "D:/data/COCO/labels/train/"


for fileName in os.listdir(src_lbl_path):
    fileNameNoExt = os.path.splitext(fileName)[0]
    
    # only for MIO
    ####
    #fileNameNoExt = str(int(fileNameNoExt) - 1)
    #fileNameNoExt = fileNameNoExt.zfill(8)
    ####
    if os.path.exists(os.path.join(src_img_path, fileNameNoExt + extension)):
        image = cv.imread(os.path.join(src_img_path, fileNameNoExt + extension))
        #image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        for i in range(len(transforms)):
            transformed = transforms[i](image=image)
            transformed_image = transformed["image"]
            imgName = fileNameNoExt + "_" + str(i)
            cv.imwrite(os.path.join(dst_img_path, imgName + extension), transformed_image)
            shutil.copyfile(os.path.join(src_lbl_path, fileName), os.path.join(dst_lbl_path, imgName + '.txt'))
        
        #cv.imshow("cropped", imgCropped)
        #cv.waitKey(0)
        #break
                    
        