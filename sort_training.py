import os
import pandas as pd
import shutil

path = "....the path including trani.csv and imgs folder"
os.chdir(path)

train = pd.read_csv('train.csv', index_col='Image')

os.makedirs('train_set')

src = path + '/imgs/'
dst = path + '/train_set'

for image in train.index:
    if os.path.exists(src + image):
        shutil.move(src + image, dst)
