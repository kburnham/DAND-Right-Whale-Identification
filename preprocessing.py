import numpy as np
import os
import cv2
from matplotlib import pyplot as plt

# Set the directory
path = '/media/reza/OS/Kaggle/Right Whale Recognition/annotated_imgs/whales'
os.chdir(path)

# Make a dictionary and list to save the samples
imgStack = {}
imgStack_size = []
ind = 0

# Doing a loop over all images in the directory
for img in os.listdir(path):
    image = cv2.imread(img, 0)
    raw = image.flatten()
    imgStack[ind] = raw
    imgStack_size.append(raw.size)
    ind += 1

# Find the maximum sized image of the entire resized dataset
maxInd = imgStack_size.index(max(imgStack_size))
maxImg = imgStack[maxInd]
