# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:25:26 2022

This program extracts every n frame from a video

@author: Hadi
"""
import os
import cv2
import re

##===============
## parameters
##===============
minutes = 5 # extract until this minute
n = 60 # extract every n frame
#vid_name = "vlc-record-2022-11-22-13h09m13s-Rt130_PrincetonHights_south_dilemma_no_jump__result.mp4-"
src_vid_path = "G:/.shortcut-targets-by-id/1DjqpVpkinJDyr2Guv28OWFE-8JNpNHVc/2022DOT_SBIR/20221019_US46_South Beverwyck Road/parts/camera2/"
dst_img_path = src_vid_path + "frames/"
vid_format = 'mp4'
##===============


if not os.path.exists(dst_img_path):
    os.makedirs(dst_img_path)
    
vidName = re.search('parts/(.+?)/', src_vid_path).group(1)
#print(vidName)


cnt = 0
for vid_name in os.listdir(src_vid_path):

    video = cv2.VideoCapture(src_vid_path + vid_name)
    success,image = video.read()
    
    fps = video.get(cv2.CAP_PROP_FPS)
    print('frames per second =',fps)
    
    count = 0
    while success:
        if count % n == 0:
            name = vidName + "_frame_" + f"{cnt:06d}"
            cv2.imwrite(dst_img_path + name + ".png", image)     # save frame as JPEG file 
            cnt += 1
        success,image = video.read()
        count += 1
        #if count == 60 * minutes * fps:
        #    break