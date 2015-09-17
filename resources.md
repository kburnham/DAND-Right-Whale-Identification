<h2>Resources</h2>

<h4>Right Whales & Whale Identification</h4>
 <li>[How to identify](http://www.neaq.org/conservation_and_research/projects/endangered_species_habitats/right_whale_research/right_whale_projects/monitoring_individuals_and_family_trees/identifying_with_photographs/how_it_works/callosity_patterns.php)
 <li>[Individual Recognition of Cetaceans](BackgroundInfo/methods of photo identification for small cetaceans.pdf)
 <li>[Computer Aided Recognition of Whale Sharks](BackgroundInfo/computer aided recognition of whale sharks.pdf)


<h4>Convolutional Neural Networks/Image Recognition</h4>
<h5>General</h5>
<li>[Wikipedia article on CNNs](https://en.wikipedia.org/wiki/Convolutional_neural_network) - see also the references at the bottom
<li>[Description and basic implementation with Theano](http://deeplearning.net/tutorial/lenet.html)
<li>[Good description of CNNs](http://cs231n.github.io/convolutional-networks/)
<li>[Unsupervised Feature Learning and Deep Learning](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial)

<h5>Case Studies</h5>
<li>[Detecting Diabetic Retinopathy in Eye Images](http://blog.kaggle.com/2015/08/10/detecting-diabetic-retinopathy-in-eye-images/)
<li>[Classifying Plankton With Deep Neural Networks](http://benanne.github.io/2015/03/17/plankton.html) - [	notes](Notes/Notes from Plankton winners.md)
<li>[My Solution for the Galaxy Zoo Competition](http://benanne.github.io/2014/04/05/galaxy-zoo.html)

<h5>Academic Papers</h5>
<li>[Delving Deep Into Rectifiers](BackgroundInfo/Delving Deep into rectifiers.pdf)
<li>[Distilling the Knowledge in a Neural Network](BackgroundInfo/Distilling the Knowledge in a Neural Network.pdf)
<li>[ImageNet Classification with Deep Convolutional Neural Networks](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf)
<li>[Rotation-invariant convolutional neural networks for galaxy morphology prediction](http://arxiv.org/pdf/1503.07077v1.pdf) - from Galaxy Zoo challenge
<li>[Rapid Object Detection using a Boosted Cascade of Simple Features](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf)
<li>[An Extended Set of Haar-like Features for Rapid Object Detection](http://www.lienhart.de/Prof._Dr._Rainer_Lienhart/Source_Code_files/ICIP2002.pdf)
<li>[Learning Multi-scale Block Local Binary Patterns for Face Recognition](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CB8QFjAAahUKEwiugbjh_N3HAhVFEJIKHXnsDi0&url=http%3A%2F%2Fwww.cbsr.ia.ac.cn%2Fusers%2Flzhang%2Fpapers%2FICB07%2FICB07_Liao.pdf&usg=AFQjCNGT1oe12V2Cf8fJ-Kf5r_iKkkp-0Q&sig2=sb4D6J4JgR7bwuni-pN-dw)
<li>[Multiresolution Gray Scale and Rotation Invariant Texture Classification with Local Binary Patterns](http://vision.stanford.edu/teaching/cs231b_spring1415/papers/lbp.pdf)
<li>[Histograms of Oriented Gradients for Human Detection](https://hal.inria.fr/inria-00548512/document)



<h4>Software</h4>
<h5>Tools</h5>
<li>[Theano](http://deeplearning.net/software/theano/) - used by previous image processing winners - makes certain computations faster by using GPU. See link for download and tutorials.
 	 - [short talk on Theano](https://archive.org/details/Scipy2010-JamesBergstra-TransparentGpuComputingWithTheano)
 <li>~~[MathWorks](http://www.mathworks.com/academia/student-competitions/kaggle/?refresh=true) - free copy of MatLab for use in the competiton (I think the license is for 1 year). There is a [tutorial](https://www.kaggle.com/c/noaa-right-whale-recognition/details/creating-a-face-detector-for-whales) for the competition that uses this software. Contact me for a license key.~~
 <li>~~[Label Images for Classification Model Training](http://www.mathworks.com/help/vision/ug/label-images-for-classification-model-training.html) - instructions for labeling images for training an object classifier with MatLab. See also [here](http://www.mathworks.com/help/vision/ug/train-a-cascade-object-detector.html) which talks about how MatLab's ObjectDetector works and how to give it good data for training.~~
 <li>[trainCascadeObjectDetector](http://www.mathworks.com/help/vision/ref/traincascadeobjectdetector.html?refresh=true) - used to train an object detector given a list of images with the object highlighted and a list of negative images not containing the object.
 <li>[keras](https://github.com/fchollet/keras) - Theano-based Deep Learning library (convnets, recurrent neural networks, and more)
 <li>[pylearn2](https://github.com/lisa-lab/pylearn2) - A Machine Learning library based on Theano
 <li>[OpenCV-Python tutorials](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html)
 <li>[Installing OpenCV-Python on a MAC](http://www.mobileway.net/2015/02/14/install-opencv-for-python-on-mac-os-x/)
 <li>[Sloth](https://github.com/cvhciKIT/sloth) - we may be able to use this for our image labeling
 <li>[Repository of labelled annotations from other particpants](https://github.com/Smerity/right_whale_hunt)
 <li>[Python script for sorting images by whale](https://www.kaggle.com/c/noaa-right-whale-recognition/forums/t/16275/python-script-to-sort-images/91274#post91274)
 <li>[Train Your Own OpenCV Haar Classifier](https://github.com/mrnugget/opencv-haar-classifier-training) - this repository appears to contain everything we might need to train our own whale classifier, we just need to make some positive and negative images to feed into it.
 <li>[How to do OpenCV Haar training](http://www.technolabsz.com/2011/08/how-to-do-opencv-haar-training.html)
 <li>[Analysis and optimization of parameters used in training a cascade classifier](http://scholarpublishing.org/index.php/AIVP/article/view/1152)
 <li>[Training Haar cascade in the cloud](http://computer-vision-talks.com/articles/cloud-haartaining/) - tutorial on using DigitalOcean to train a classifier in the cloud
 <li>[Cascade Classifier Q/A](http://answers.opencv.org/question/7141/about-traincascade-paremeters-samples-and-other/) - good post from OpenCV Q&A about parameter tuning in a cascade classifier
 <li>[More advice on haar cascade parameter settings](http://answers.opencv.org/question/39160/opencv_traincascade-parameters-explanation-image-sizes-etc/)
 <li>[Using AWS to train a whale classifier](https://github.com/kburnham/DAND-Right-Whale-Identification/blob/master/Using%20AWS%20to%20Train%20a%20Cascade%20Classifier.md) - I wrote this one, but I haven't tested it myself yet, so let me know if you run into any problems.

<h4>Miscellany</h4>




