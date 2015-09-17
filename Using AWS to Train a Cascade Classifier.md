<h2>Using (a free) Amazon Web Services EC2 instance to train a whale classifier with OpenCV</h2>

In what follows, I will attempt to explain the process involved in using the computer vision library OpenCV to train a whale classifier. A classifier is an algorithm that scans an image and identifies the subregion (or subregions) that contain specific objects (traditionally faces, but in our case right whales).

Building the classifier involves the following steps:
1. Sign up for an Amazon Web Services account and create a linux instance that you can ssh to from your local machine. (this is free)
2. Install OpenCV (and its many dependencies) on the remote instance
3. Run the `opencv_createsamples` and `opencv_traincascade` utilities to create a cascade.xml file that can be used to find whale new images.
4. ~~Use your new `cascade.xml` to test and validate the trainer.~~ Coming Soon!

It is possible to do this on a local machine too if you don't want to sign up for an AWS account, but in some cases`opencv_traincascade` will take days (or maybe longer) to run.


<h4>Signing up for an Amazon Web Services account</h4>

You can get a free AWS account for 12 months that allows you to create and run an instance.

Go to [this site](https://aws.amazon.com/). You should see a box on the right that says 'Create a Free Account'. (I did this in the US, I am not sure if it works elsewhere).

Once you have your account check out [Setting up with Amazon EC2](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html). There are a number of different steps that you have to take before you can create an instance. I used a Mac with Linux and I see there are also instuctions for Windows users using a program called PuTTY.

Once you are set up, go [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) for Linux and [here](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2Win_GetStarted.html) for Windows to set up an instance. There are links to the steps for setting up and connecting to you instance. 

If you are in a linux terminal, you should be able to connect to the command line of your instance with:

<kbd>scp -i /path/to/keypair.pem ec2-user@public_dns_name</kbd>

You should get a message saying 'The authenticity of host your_public_dns_name' . . . can't be established'. 

Type 'yes' to continue. You will be promted to make update with `sudo yum install`. Do this.

<h4>Install OpenCV</h4>

No we want to download and build OpenCV. 

Start by installing `git` with this command:

<kbd>sudo yum install git</kbd>

Now we use `git` to clone the OpenCV repository:

<kbd>git clone https://github.com/Itseez/opencv.git</kbd>

There are a few steps we need to take before we can install OpenCV.

First, download `cmake` with this command:

<kbd>wget http://www.cmake.org/files/v3.3/cmake-3.3.1.tar.gz</kbd>

Then extract the downloaded file like this:

<kbd>tar -zxvf cmake-3.3.1.tar.gz</kbd>

Now we need `gcc-c++` so we can compile cmake as follows:

<kbd>sudo yum install gcc-c++</kbd>

And now from inside the `cmake-3.1.1` directory, run bootstrap. Because we are on a remote machine we will run into permission errors with out specificying a prefix:

<kbd>./bootstrap --prefix=$HOME</kbd>

When it's done you will get the message 'CMake has bootstrapped.  Now run gmake.' Do that:

<kbd>gmake</kbd>

When that finishes, you are finally ready to install OpenCV. Go into the `opencv` folder you cloned and create and open a folder called `release`:

<kbd>mkdir release</kbd><br>
<kbd>cd release</kbd>

Then use this command to start the build:

<kbd>cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..</kbd>

When that is done use these two commands (make sure you are in the `release` folder):

<kbd>make</kbd><br>
<kbd>sudo make install</kbd>

<h4>Run the `opencv_createsamples` and `opencv_traincascade` utilities</h4>

When the intallation is complete you should find the `opencv_createsamples` and `opencv_traincascade` utitilies in the `opencv/release/bin` folder. Unfortunately we can't use them until we upload the files that it needs for training. To train the classifier, we need to provide it with:

1. Images that contain whales and a file (we'll call it `data.info`) that provides the coordinates, width and height of the subregion containing the whale.
2. Negative images (aka background images) that do not contain whales and a file (`bg.txt`) that lists the names and relative locations of the files.
3. A .vec file created from positive images (we will create this file with the `opencv_createsamples` utility.)

Start by creating a new folder on your home level. Call it `whaleclassifier`. We will put all the files needed for training in this folder.

For instructions on moving files between local and remote machines using `scp` see [here](http://www.computerhope.com/unix/scp.htm). If you are using an instance from AWS, you need to be sure to include `-i /you/keypair.pem` in your scp commands.

Within the `whaleclassifier` folder, create a folder called `positives` and one called `negatives` (or scp entire folders with image files from your local machine).

Into the positives folder you need to upload the full images of images that you (or someone else has annotated to indicate the position of the whale).

You can get the image files from the [competition website](https://www.kaggle.com/c/noaa-right-whale-recognition/data). You can get annotations from [this github repository](https://github.com/Smerity/right_whale_hunt). Or you can just use the file from [our github site](https://github.com/kburnham/DAND-Right-Whale-Identification). If you use this file, you need to make sure you upload all of the corresponding images. 

Into the `negatives` folder, you should upload images that contain anything but whales. I created a bunch of negatives from the annotated images by taking slices of them that did not contain whales. You can find these images [here](https://drive.google.com/folderview?id=0B5TdRGXyaxqWT1RFTWhUUnZIZmM&usp=sharing) and upload them to your negatives folder. 

One level above the `negatives` folder (in the `whaleclassifier` folder) you need your `bg.txt` file that lists all of your negatives like this:

negatives/image1.jpg<br>
negatives/image2.jpg<br>
negatives/image3.jpg<br>
. <br>
.<br>
.<br>

If you use the negatives above, you can also use the [`bg.txt`](https://github.com/kburnham/DAND-Right-Whale-Identification/blob/master/bg.txt) file on our repo.

Inside the `whaleclassifier` folder, create a folder called `output`. When the training finished you will find a cascade.xml file here. You will use this file to find whales in images.

Now you want to move (or copy) the `opencv_createsamples` and `opencv_traincascade` utilities into the `whaleclassifier` folder.

Once you have all these in place you need to create a .vec file with `opencv_createsamples`. Minimally you need to provide -vec, the name of the .vec file it will create, -num, the number of samples it should make (this should equal the number of positives) and -bg, the file that lists the negatives. Type `opencv_createsamples` to get a list of the other parameters or see the heading Positive Samples on [this page](http://docs.opencv.org/doc/user_guide/ug_traincascade.html). If you are using the data.info and bg.txt I have provided, this should work:

<kbd>./opencv_createsamples -vec whale_faces.vec -num 611 -info data.info -bg bg.txt</kbd>

It shouldn't take very long and when it is done, you will find a `whale_faces.vec` file in your `whaleclassifier` folder.

You should be able to see the created images with:

<kbd>opencv_createsamples -vec whale_faces.vec -h 24 -w 24</kbd> (this assumes that you created the .vec with -w 24 and -h 24, the defaults)

Now that you have a .vec file, you can train a classifier. Again, there are many paramenter settings and we need to experiment with them, but this command should work for you:

<kbd>./opencv_traincascade -vec whale_faces.vec -data output/ -numPos 540 -numNeg 100 -bg bg.txt -numStages 5 -featureType LBP</kbd>

This may take a while, but it will output a bunch of information about the training and when it is done, you will find a `cascade.xml` file in the `output` folder. Download this file to your local machine to test your whale classifier. 

Given lots of samples and many training stages (as good classifiers need) means that the training could take some time to complete. If you want to be able to end the ssh session and comeback later, you should be able to do this with:

<kbd>nohup ./opencv_traincascade -vec whale_faces.vec -data output/ -numPos 540 -numNeg 100 -bg bg.txt -numStages 5 -featureType LBP &</kbd>

This will place all terminal output into a file called nohup.out (including error messages, so be sure to check it right away with <kbd>nano nohup.out</kbd>). You should be able to sign out (but do not stop the instance until it is done) and come back later. If you check the nohup.out file and it ends with END, I think that means its finished. I have not actually tried to sign out and come back though, so I am not sure exactly how it works. 

We want to make sure that we capture the output and the cascade.xml file of every classifier that we train so that we can try to figure out what the best parameter settings are and so we do not waste time training classifiers with the same input data and parameter settings. We also might benefit from making an ensemble of whale classifiers. It is good to keep in my that our whale finding task is usefully constrained by the fact that every image we process contains exactly one whale (actually at least some of the photos have multiple whales, but each image is identified with exactly one whale). However, I believe that the nature of the cascade classifier is such that there is no ranking or confidence measure for a hit. So if it returns 3 areas that it thinks contain whales, there is no way for us to choose the best one. I thought then that we might train a bunch of classifiers each of which 'votes' for areas of the image that it thinks has a whale. This in effect would generate a heat map on the image and we could then take the 'hottest' area as our whale. The trick is to have classifiers that are different enough from one another to base their conclusions on different data. So in addition to changing the parameters of `opencv_createsamples` and `opencv_traincascade` we can experiment with different input data (different sets of positive and negative images, different image preprocessing steps, different window sizes, etc.).


There are still have many unanswered questions about training, including:

How many positives do we need? What is the best way to do the image annotations? What kind of image preprocessing should we use? How many negatives do I need? What should they consist of? What are the parameters of opencv_traincascade and how do they influence the performance of the model and the length of training time?

These are all questions that we need to answer in order to build the best possible whale classifier. There are some links on [resources.md](resources.md) on our repo that might help get us started in answering these questions. 







 