import numpy as np
import pandas as pd
import cv2 as cv2
import os

path = 'the directory of train.csv file'
os.chdir(path)

train = pd.read_csv('train.csv', index_col='Image')

path = 'the directory of .... /annotated_imgs/whales'
os.chdir(path)

train['label'] = 0

whaleID = np.unique(train['whaleID'])

ind = 0

for i in whaleID:
    train['label'][train['whaleID'] == i] = ind
    ind += 1

labels = train.label.values

# Make a dictionary and list to save the samples
imgStack = {}
imgStack_size = []
ind = 0
y = np.empty([])

# Doing a loop over all images in the directory
for img in os.listdir(path):
    a = train['label'][train.index == img.strip('_annotated.png') + '.jpg']
    y = np.append(y, a.values)
    image = cv2.imread(img, 0)
    raw = image.flatten()
    imgStack[ind] = raw
    imgStack_size.append(raw.size)
    ind += 1

# Find the maximum sized image of the entire resized dataset
maxInd = imgStack_size.index(max(imgStack_size))
maxImg = imgStack[maxInd]

data = np.empty([ind, imgStack_size[maxInd]])

# zero padding
for i in xrange(ind):
    data[i, 0:len(imgStack[i])] = imgStack[i]

X = data
