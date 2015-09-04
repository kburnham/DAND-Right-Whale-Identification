<h3>Notes on Galaxy Zoo winner's blog</h3>

The task - 
>build a model of how “the crowd” perceive and classify these images.

This means that we’re looking at a regression problem, not a classification problem: we don’t have to determine which classes the galaxies belong to, but rather the fraction of people who would classify them as such.

>Transfer learning by pre-training a deep neural network on another dataset (say, ImageNet), chopping off the top layer and then training a new classifier, a popular approach for the recently finished Dogs vs. Cats competition, is not really viable either.

>During the contest, I frequently referred to [Krizhevsky et al.’s seminal 2012 paper](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf) on ImageNet classification for guidance. Asking myself “What would Krizhevsky do?” usually resulted in improved performance.

>As Geoffrey Hinton has been known to say, if you’re not overfitting, your network isn’t big enough. My main objective during the competition was avoiding overfitting. My models were significantly overfitting throughout the entire competition, and most of the progress I attained came from finding new ways to mitigate that problem.

>I tackled this problem with three orthogonal approaches:

    <li>data augmentation
    <li>dropout and weight norm constraints
    <li>modifying the network architecture to increase parameter sharing

>The best model I found has about 42 million parameters. It overfits significantly, but it’s still the best despite that. There seems to be a lot of room for improvement there.

As is customary in Kaggle competitions, I also improved my score quite a bit by averaging the predictions of a number of different models. Please refer to the “Model averaging” section below for more details.

>I used Python, NumPy and Theano to implement my solution. I also used the Theano wrappers for the cuda-convnet convolution implementation that are part of pylearn2. They provided me with a speed boost of almost 3x over Theano’s own implementation. I wrote [a guide on how to use them](http://benanne.github.io/2014/04/03/faster-convolutions-in-theano.html), because their documentation is limited.

>For this post I will assume that Python, numpy and Theano are installed and working, and that you have access to a CUDA-enabled GPU.

See post for detailed implementation for Galaxy Zoo.

See [academic write up of same](http://arxiv.org/pdf/1503.07077v1.pdf)



