import numpy as np
import pandas as pd
import cv2 as cv2
import os
from sklearn import cross_validation
from sklearn import svm

path = '/.. directory of train.csv'
os.chdir(path)

train = pd.read_csv('train.csv', index_col='Image')

path = '/.. directory of annotated images (only whales)'
os.chdir(path)

train['label'] = 0
train['num'] = 0

whaleID = np.unique(train['whaleID'])
whaleNum = whaleID.shape[0]

ind = 0

for i in whaleID:
    train['label'][train['whaleID'] == i] = ind
    ind += 1

labels = train.label.values
labels_unique_sort = np.sort(np.unique(labels))

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
    train['num'][ind] = ind
    ind += 1
    
# Find the maximum sized image of the entire resized dataset
maxInd = imgStack_size.index(max(imgStack_size))
maxImg = imgStack[maxInd]
m = int(imgStack_size[maxInd])

data = np.empty([ind, m+1])

# zero padding
for i in xrange(ind):
    data[i, 0:len(imgStack[i])] = imgStack[i]
    data[i, m] = i

X = data

# SVM identifier
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)

clf = svm.SVC(probability = True)
clf.fit(X_train[:,0:m], y_train)
clf.predict_proba(X_test[0,0:m])

Image = []
result = np.zeros([X_test.shape[0], whaleNum])
y_train_unique_sort = np.sort(np.unique(y_train))

# Probability predictions 
for i in xrange(X_test.shape[0]):
    Image.append(train.index[train['num'] == X_test[i,m]][0])
    z = clf.predict_proba(X_test[i,0:m])
    for j in xrange(z.shape[1]):
        result[i, labels_unique_sort == y_train_unique_sort[j]] = z[0,j]      

# Writing csv file
features = list(whaleID)
df = pd.DataFrame(result, columns = features, index = Image)
df.index.name = 'Image'
path = '/.. directory you want to creat the result.csv file in'
os.chdir(path)
df.to_csv('result.csv')
