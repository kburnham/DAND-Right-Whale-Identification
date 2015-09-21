<h2>Image Annotation</h2>

The purpose of this document is to organize the process of image annotation. To train our classifier (aka recognizer) we need to provide our model with lots of images of whales (more specifically we will use whale heads) and lots of images that are not whales. These later images should be backgrounds on which whales might occur and objects that are likely to be confused for whales (sea spray, wave patterns, etc.). The more images we have the better, so I hope that everyone on the team can do a good chunk of images (about 500) so that we can train a good classifier. Note that we must run our final whale idenitying model on the test data on unannotated images. It is not permissible to submit results based on hand annotated images.

These are the steps to annotating a batch of images:

1. Install the Sloth program on your computer. (Obviously you only need to do this once.)
2. Get a list of files to annotate. 
3. Annotate the files with Sloth.
4. Check the annotated images (by looking at them) to make sure we aren't giving bad data to our algorithms.
5. Put your .json in the Annotations folder with a descriptive name and submit a pullrequest
6. Repeat 2-5 with another batch!

<h4>1. Install Sloth</h4>

Sloth should be simple to install. You need to clone the [github repo](https://github.com/cvhciKIT/sloth) and then install it. You can find installation instructions [here](http://sloth.readthedocs.org/en/latest/), but if you have Python, [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download) and [PIL](http://www.pythonware.com/products/pil/) or okapy, and are signed in with administrator privileges, this should work:

<kbd>git clone https://github.com/cvhciKIT/sloth</kbd><br>
<kbd>python setup.py install</kbd>

You should play around with Sloth a little bit to get an idea how it works. See [here](http://sloth.readthedocs.org/en/latest/first_steps.html) for a brief intro to how it works. Basically, it allows you to annotate an image (or images) and output an xml file that describes that image. We will use it to identify whale heads in our images, and also areas of images without whales.

When you are confortable annotation images with Sloth, go on to step 2.


<h4>2. Get a list of files to annotate.</h4>

To make sure that we don't duplicate effort, you first want to generate a list of files to annotate that have not already been annotated. 

Use the `AnnotateImages.ipynb` file in this directory to generate a temporary folder of images that can be imported into sloth for annotation.

<h4>3. Annotate the files with sloth</h4>

From within the `ImageAnnotation` folder on the github repo, these commands should launch sloth with your new batch of files to annotate.  

<kbd>find ../../files_for_annotation/* -iname "*.jpg"| xargs sloth appendfiles annotations/new_file_name.json</kbd><br>
<kbd>ln -s annotations/new_file_name.json .</kbd><br>
<kbd>sloth --config sloth_configuration.py annotations/new_file_name.json</kbd><br>

Please keep the following in mind when annotation images:

 - for all images you should make a square around the head of the whale using the 'head' tag. The square should include the full head and, when possible, the blowhole. I can't find a way for force a square, but do your best to make the aspect ratio 1:1.
 - you should also try to tag some negative areas with the 'neg; tag. These should either be background - like the water - or areas that might be confused for whales - wave patterns, foam, spray etc. You do not necesarrily need to identify negatives on all images.
 - Be sure that you are labelling heads 'head' and negatives 'neg'. It's tricky because the boxes are the same color. Press `esc` to get out of the editor and click on a box to see its tag. Also, please be sure to proofread your annotations (see below).
 - pressing `ctrl-F` should center the image on the sloth palette.
 - the space bar will load the next image

Check out some sample annotations [here](sample_annotations/sample_annotations.md). Note that when you view them in sloth, all the boxes will be yellow.


When you have completed your annotations, close sloth and you will find the new file you created in the `annotations` folder.

<h4>4. Check your work</h4>

Use the `check_annotations` function in `AnnotateImages.ipynb` to create a group of images with your boxes marked on them. Use your favorite viewer to quickly look at all of the images. Are all of the whale heads in yellow? Are all of the negative areas in red? If not, be sure to delete the entry from your json file.

 **It is very important to check your work. If we give bad data to our trainer, it can't do its job!**

 Once you have checked them you should delete the marked files and the temporary files created for annotation. If you are in the `ImageAnnotation` folder:

<kbd>rm -r ../../files_for_annotation</kbd><br>
<kbd>rm -r ../../marked_images</kbd>

<h4>5. Submit a pull request.</h4>

When you are confident your annotations are clean, submit a pull request so they can be merged.

<h4>6. Wasn't that fun? Now you can repeat steps 2-6 to annotate another batch.</h4>



