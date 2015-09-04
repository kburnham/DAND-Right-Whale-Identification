Notes from Plankton winners(http://benanne.github.io/2015/03/17/plankton.html)

>Judicious use of techniques to prevent overfitting such as dropout, weight decay, data augmentation, pre-training, pseudo-labeling and parameter sharing, has enabled us to train very large models with up to 27 million parameters on this dataset.

What are each of the techniques he mentions above?

>We used Python, NumPy and Theano to implement our solution, in combination with the cuDNN library. We also used PyCUDA to implement a few custom kernels.

>Our code is mostly based on the Lasagne library, which provides a bunch of layer classes and some utilities that make it easier to build neural nets in Theano. This is currently being developed by a group of researchers with different affiliations, including Aäron and myself. We hope to release the first version soon!

What is Theano?

>We also used scikit-image for pre-processing and augmentation, and ghalton for quasi-random number generation. During the competition, we kept track of all of our results in a Google Drive spreadsheet. Our code was hosted on a private GitHub repository, with everyone in charge of their own branch.

>We performed very little pre-processing, other than rescaling the images in various ways and then performing global zero mean unit variance (ZMUV) normalization, to improve the stability of training and increase the convergence speed.

What is global zero mean unit variance?

What are the characteristics of our data set? - It is relatively small - only 4544 images, lots of whales with only a single data point, we are identifying individuals, not types (as with plankton, galaxies)

>We augmented the data to artificially increase the size of the dataset. We used various affine transforms, and gradually increased the intensity of the augmentation as our models started to overfit more. We ended up with some pretty extreme augmentation parameters:

>rotation: random with angle between 0° and 360° (uniform)</br>
>translation: random with shift between -10 and 10 pixels (uniform)</br>
>rescaling: random with scale factor between 1/1.6 and 1.6 (log-uniform)</br>
>flipping: yes or no (bernoulli)</br>
>shearing: random with angle between -20° and 20° (uniform)</br>
>stretching: random with stretch factor between 1/1.3 and 1.3 (log-uniform)</br>

</br>
>We augmented the data on-demand during training (realtime augmentation), which allowed us to combine the image rescaling and augmentation into a single affine transform. The augmentation was all done on the CPU while the GPU was training on the previous chunk of data.
>
We experimented with various variants of rectified linear units (ReLUs), as well as maxout units (only in the dense layers). We also tried out smooth non-linearities and the ‘parameterized ReLUs’ that were recently introduced by He et al., but found networks with these units to be very prone to overfitting. 

>However, we had great success with (very) leaky ReLUs. Instead of taking the maximum of the input and zero, y = max(x, 0), leaky ReLUs take the maximum of the input and a scaled version of the input, y = max(x, a*x). Here, a is a tunable scale parameter. Setting it to zero yields regular ReLUs, and making it trainable yields parameterized ReLUs.

<br>
>Spatial pooling

>We started out using networks with 2 or 3 spatial pooling layers, and we initially had some trouble getting networks with more pooling stages to work well. Most of our final models have 4 pooling stages though.

What is spatial pooling?

>Here are some examples of types of features we evaluated (the ones we ended up using are in bold)</br>
    >**Image size in pixels**</br>
    >**Size and shape estimates based on image moments**</br>
    >Hu moments</br>
    >Zernike moments</br>
    >Parameter Free Threshold Adjacency Statistics</br>
    >Linear Binary Patterns</br>
    >**Haralick texture features**</br>
    >Features from the competition tutorial</br>
    >Combinations of the above</br>


>We trained all of our models with stochastic gradient descent (SGD) with Nesterov momentum. We set the momentum parameter to 0.9 and did not tune it further. Most models took between 24 and 48 hours to train to convergence.

What is stochastic gradient descent (SGD) with Nesterov momentum?

>Another way we exploited the information in the test set was by a combination of pseudo-labeling and knowledge distillation (Hinton et al.).

>In total we trained over 300 models, so we had to select how many and which models to use in the final blend. For this, we used cross-validation on our validation set. On each fold, we optimized the weights of all models to minimize the loss of the ensemble on the training part.

>The models selected by this process were not necessarily the ones with the lowest TTA score. Some models with relatively poor scores were selected because they make very different predictions than our other models
</br>
>Here are a few other things we tried, with varying levels of success:

<li>untied biases: having separate biases for each spatial location in the convolutional layer seemed to improve results very slightly.</br>
<li>winner take all nonlinearity (WTA, also known as channel-out) in the fully connected layers instead of ReLUs / maxout.</br>
<li>smooth nonlinearities: to increase the amount of variance in our blends we tried replacing the leaky rectified linear units with a smoothed version. Unfortunately this worsened our public leaderboard score.</br>
<li>specialist models: we tried training special models for highly confusable classes of chaetognaths, some protists, etc. using the knowledge distillation approach described by Hinton et al.. We also tried a self-informed neural network structure learning (Warde-Farley et al.), but in both cases the improvements were negligible.</br>
<li>batch normalization: unfortunately we were unable to reproduce the spectacular improvements in convergence speed described by Ioffe and Szegedy for our models.</br>
<li>Using FaMe regularization as described by Rudy et al. instead of dropout increased overfitting a lot. The regularizing effect seemed to be considerably weaker.</br>
<li>Semi-supervised learning with soft and hard bootstrapping as described by Reed et al. did not improve performance or reduce overfitting.</br>

Still need to read comments and replies.