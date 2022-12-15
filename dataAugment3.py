"""
this file only cares about the minority classes
data augmentation keeping the entire image instead of cropping the object out
if it's a minority class create a new image with only that object in it
augment the image with other techniques as well
categories:
    US130: 0) person 1) car 2) bus 3) cyclist 4) truck
    US46: 0) person 1) cyclist 2) car 3) bus 4) truck 5) motor
"""

import os
import cv2 as cv
import re
import albumentations as A
import shutil

##===============
## parameters
##===============
extension = ".png"
data_path = r"G:/.shortcut-targets-by-id/1DjqpVpkinJDyr2Guv28OWFE-8JNpNHVc/2022DOT_SBIR/20221110Rt130/undistorted/parts/Rt130_Dutch_south_dilemma_looking_south/frames"
src_img_path = data_path + "/images/"
src_lbl_path = data_path + "/labels/"
dst_img_path = data_path + "/minority/images/"
dst_lbl_path = data_path + "/minority/labels/"

if not os.path.exists(dst_img_path):
    os.makedirs(dst_img_path)
    
if not os.path.exists(dst_lbl_path):
    os.makedirs(dst_lbl_path)
    
bg = cv.imread(data_path + "/bg1.png")
roi = cv.imread(data_path + "/roi.png", 0)
BaseFileName = re.search('parts/(.+?)/frames', data_path).group(1)
##===============


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

lines = []
cnt = len([entry for entry in os.listdir(src_img_path) if os.path.isfile(os.path.join(src_img_path, entry))])
for fileName in os.listdir(src_lbl_path):
    if fileName in "desktop.ini": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    with open(txtFile, 'r') as fp:
        lines = fp.readlines()
    if len(lines) == 0: continue
    
    
    # read image
    imgFile = os.path.join(src_img_path, fileNameNoExt + extension)
    if not os.path.exists(imgFile): continue
    image = cv.imread(os.path.join(src_img_path, fileNameNoExt + extension))
    imgW, imgH = image.shape[1], image.shape[0]
    

    for line in lines:
        lst = line.split()
            
        category = lst[0]
        if category == '1': continue # we have enough cars
        
        xCenter, yCenter = int(float(lst[1]) * imgW), int(float(lst[2]) * imgH)
        w, h = int(float(lst[3]) * imgW), int(float(lst[4]) * imgH)
        x1, y1 = xCenter - w // 2, yCenter - h // 2
        x2, y2 = x1 + w, y1 + h
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = min(x2, imgW)
        y2 = min(y2, imgH)
        if x1 >= x2 or y1 >= y2: continue
    
        if category == '4': # if it's a truck just add one image
            newImage = bg.copy()
            newImage[y1:y2, x1:x2] = image[y1:y2, x1:x2] 
            imgName = BaseFileName + "_" + "frame" + "_" + "{:06d}".format(cnt)
            cnt += 1
            cv.imwrite(os.path.join(dst_img_path, imgName + extension), newImage)
            with open(os.path.join(dst_lbl_path, imgName + '.txt'), 'w') as f1:
                f1.write(line)
                
        else: # for person, bus, cyclist add a lot more
            newImage = bg.copy()
            newImage[y1:y2, x1:x2] = image[y1:y2, x1:x2] 
            for i in range(len(transforms)):
                transformed = transforms[i](image=newImage)
                transformed_image = transformed["image"]
                imgName = BaseFileName + "_" + "frame" + "_" + "{:06d}".format(cnt)
                cnt += 1
                cv.imwrite(os.path.join(dst_img_path, imgName + extension), transformed_image)
                with open(os.path.join(dst_lbl_path, imgName + '.txt'), 'w') as f1:
                    f1.write(line)
        

