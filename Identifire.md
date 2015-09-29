# Right Whale Identification: Identifier Section

## Introduction
The cropped images of whales obtained by the Recognizer are used in this step to train an identifier. The identifier should result in a vector of probabilities, one for each whale in the test set images. 

## Preprocessing
### 1. Reading Images
This section includes reading cropped images and their assigned whales and storing them in two 2-dimensional arrays named X and y as the train dataset and their labels. For this purpose, we have already implemented a simple code in Python and used OpenCV tools in a loop over some previously annotated images in gray scale. 
### 2. Resizing, Padding, or?
The read images have different sizes and aspect ratios. To obtain vectors with equal sizes different methods have been proposed. We can try them and check the difference. Resizing, padding, bag-of-words, etc.
### 3. Identifier
I am trying to make predictions with Support Vector Machines, but unfortunately so far I haven't managed to achieve results with the right form with reasonable accuracy. Right now I try to determine the correct SVM settings to analyze the images. However, we are almost sure that the best method to be used in this competition would be a Convolutional Neural Networks. Here you can find a comprehensive tutorial on implementation of a CNN: http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/ . This implementation is dealing with another Kaggle competition; however the basics might be so useful for us.

### 3. Data Augmentation
Data augmentation would be a key factor to increase the precision of convolutional neural networks. Some more info about data augmentation can be found here: http://benanne.github.io/2014/04/05/galaxy-zoo.html
However I do not think it is trivial for the right whale identification challenge.
