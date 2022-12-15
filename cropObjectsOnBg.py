"""
2 things happening here:
    1) remove everything outside roi from the images
    2) remove everything outside roi from the txt files
"""


import os
import cv2 as cv
import re

##===============
## parameters
##===============
extension = ".png"
data_path = r"G:/.shortcut-targets-by-id/1DjqpVpkinJDyr2Guv28OWFE-8JNpNHVc/2022DOT_SBIR/20220909_rt21_3ave/cam2_local_0_10"
src_img_path = data_path + "/images/"
src_lbl_path = data_path + "/labels/"
bg = cv.imread(data_path + "/bg.png")
roi = cv.imread(data_path + "/roi.png", 0)
BaseFileName = "cam1_1"
#BaseFileName = re.search('parts/(.+?)/frames', data_path).group(1)
##===============


lines = []
cnt = len([entry for entry in os.listdir(src_img_path) if os.path.isfile(os.path.join(src_img_path, entry))])
for fileName in os.listdir(src_lbl_path):
    if fileName in "desktop.ini" or fileName in "train" or fileName in "val": continue
    fileNameNoExt = os.path.splitext(fileName)[0]
    txtFile = os.path.join(src_lbl_path, fileNameNoExt + ".txt")
    with open(txtFile, 'r') as fp:
        lines = fp.readlines()
    if len(lines) == 0: continue
    
    
    # read image
    imgFile = os.path.join(src_img_path, fileNameNoExt + extension)
    if not os.path.exists(imgFile): continue
    img = cv.imread(os.path.join(src_img_path, fileNameNoExt + extension))
    imgW, imgH = img.shape[1], img.shape[0]
    
    #cv.imshow("before", img)
    
    # replace regions outside the roi with bg
    fg = cv.bitwise_or(img, img, mask=roi)        
    mask_inv = cv.bitwise_not(roi)    
    fg_back_inv = cv.bitwise_or(bg, bg, mask=mask_inv)
    modifiedImg = cv.bitwise_or(fg, fg_back_inv)
    
    #cv.imshow("middle", modifiedImg)
    
    wrong_lines = []
    lineCount = 0
    for line in lines:
        lst = line.split()
            
        category = lst[0]
        xCenter, yCenter = int(float(lst[1]) * imgW), int(float(lst[2]) * imgH)
        w, h = int(float(lst[3]) * imgW), int(float(lst[4]) * imgH)
        x1, y1 = xCenter - w // 2, yCenter - h // 2
        x2, y2 = x1 + w, y1 + h
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = min(x2, imgW)
        y2 = min(y2, imgH)
        if x1 >= x2 or y1 >= y2: continue
        
        # detect boxes outside roi in txt
        roiCropped = roi[y1:y2, x1:x2]
        if cv.countNonZero(roiCropped) == 0:
            wrong_lines.append(lineCount)
            
        # if a box is partially inside the roi add it in all back to the img
        elif cv.countNonZero(roiCropped) < w * h:
            modifiedImg[y1:y2, x1:x2] = img[y1:y2, x1:x2]
            
        lineCount += 1
        
    #cv.imshow("end", modifiedImg)
    
    cv.imwrite(imgFile, modifiedImg)
                
    
    # remove boxes outside roi from txt
    with open(txtFile, 'w') as fp:
        for number, line in enumerate(lines):
            if number not in wrong_lines:
                fp.write(line)