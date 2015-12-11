from __future__ import absolute_import
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

'''
    Train a simple convnet on the MNIST dataset.
    Run on GPU: THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python mnist_cnn.py
    Get to 99.25% test accuracy after 12 epochs (there is still a lot of margin for parameter tuning).
    16 seconds per epoch on a GRID K520 GPU.
'''

batch_size = 128

nb_epoch = 12

# input image dimensions
img_rows, img_cols = 50, 50
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3

# the data, shuffled and split between tran and test sets
#(X_train, y_train), (X_test, y_test) = mnist.load_data()
import json
import numpy as np
print("loading data...")
with open("../../nn_train_datav3.json","r") as f:
	data = json.load(f)

print("processing data...")
X = np.array(data["X"])
X = X.astype("float32")
X /= 255.
X = X.reshape(X.shape[0],1,50,50)

Y = np.array(data["Y"]).transpose()[0]
nb_classes=np.max(Y)+1


## create an array of all different images and their classes, 
## only include those classes with more than 1 image...
## do this by first extracting every 8th element of the 
## labels and then appending that to an index if there are 
## more than 1 with that class
id_array=np.array([Y[i*8] for i in range(len(Y)/8)])
train_test_ind=[]
for i in range(len(id_array)):
	if sum(id_array==id_array[i])>1:
		train_test_ind.append(i*8)

train_test_array=Y[np.array(train_test_ind)]

from sklearn.cross_validation import StratifiedShuffleSplit
sss = StratifiedShuffleSplit(train_test_array,n_iter=1,test_size=0.3)

### extract the train and test images from the dataset...
for train_index, test_index in sss:
	print("TRAIN:", train_index, "TEST:", test_index)
	## get each of the 7 images (of the same whale) following that of the index.
	## this syntax allows for single line iterative concatenation of the arrays.
	Train_index= sum([[x+i for i in range(8)] for x in [train_test_ind[j] for j in train_index]],[]) 
	Test_index= sum([[x+i for i in range(8)] for x in [train_test_ind[j] for j in test_index]],[])
#	X_train, X_test = X[Train_index], X[Test_index]
	y_train, y_test = Y[Train_index], Y[Test_index]
#print(X_train)
#print(y_train)

## test to make sure no images are shared...
#print("testing...")
#for i in range(len(y_train)/8):
#	for j in range(8):
#		if not y_train[8*i+j]==y_train[8*i]:
#			print("fail!")
#print("end test...")


#print('X_train shape:', X_train.shape)
#print(X_train.shape[0], 'train samples')
#print(X_test.shape[0], 'test samples')
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

model.add(Convolution2D(nb_filters, nb_conv, nb_conv,
                        border_mode='full',
                        input_shape=(1, img_rows, img_cols)))
model.add(Activation('relu'))
model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
print("compiling...")
model.compile(loss='categorical_crossentropy', optimizer='adadelta')
print("training...")
model.fit(X_train, Y_train, nb_epoch=nb_epoch, show_accuracy=True, verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
