%extraciting negatives for training the object detector
formatStr = 'neg%d.jpg';   % Output format for negatives
for i=1:images.Count 
 imginp = read(images,i);  % Read an image 
 imcropped = imcrop(imginp,[1 1 1078 670]); % Crop
 fileName = sprintf(formatStr,i);
 imwrite(imcropped,fileName); % Save negative images
end

%training the object detector
 whaleFinder = trainCascadeObjectDetector('detectorFile.xml', ... positiveInstances, negativeFolder)