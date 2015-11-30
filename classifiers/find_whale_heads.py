#! find whale_heads.py

## uses opencv to estimate the location of the whale head
## Adapted from Alex's Ipython Notebook...

## outputs in a json format to the annotaions folder
## output is the same format as sloth, allowing for
## easy input to existing image_parser program

import os
import time
import json
import numpy as np
import cv2
from PIL import Image, ImageDraw
import pandas as pd

path_to_img_folder="../../imgs/"
## get training images
train_files=np.array(pd.read_csv("../../train.csv")["Image"])
print train_files
##get all file in image directory
files = os.listdir(path_to_img_folder)
##extract the files that are images
test_files = [img for img in files if img[(len(img)-4):]==".jpg" and not img in train_files]
##load the classifier
whale_cascade = cv2.gpu.CascadeClassifier('cascade_1.xml')

classifications=[]

for ind in range(len(test_files)):
	print float(ind)/len(test_files)
	try:
		img_path=path_to_img_folder+test_files[ind]
		img = cv2.imread(img_path)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		attributes = whale_cascade.detectMultiScale(gray, 1.2, 7, 0, (280, 280))
		attributes_array=[attr for attr in attributes[0]]
		attributes_dict={
		"class":"Head",
		"x":int(attributes_array[0]),
		"y":int(attributes_array[1]),
		"height":int(attributes_array[3]),
		"width":int(attributes_array[2])
		}
		classifications.append({"annotations":[attributes_dict],"filename":test_files[ind]})
	except:
		a=1

with open("../ImageAnnotation/predictive_annotations.json","w") as f:
	json.dump(classifications,f)
