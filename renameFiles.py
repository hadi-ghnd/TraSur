# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:05:29 2022

@author: Hadi
"""

import os


folder = r"C:/Users/Hadi/Desktop/New folder (3)"

for fileName in os.listdir(folder):
    #if fileName.startswith("frame"):
        newName = fileName[10:]
        os.rename(folder + "/" + fileName, folder + "/" + newName)