title: Matlab Calcium Signal Extraction
date: 2015-11-04
published: True
tags: programming
image: img/posts/4.jpg
featured: True

We are not able to record the the activity of 100s of cells at the same time. Within a day of experiments there are thousand of images collected that make extracting the shapes and time course of areas of interest by hand very tidious. 

Automated segmentation is therefore a goal, and has been for years, to deal with the Gigabytes of data. 

This Matlab program allows the user to upload single three dimensional image stacks as well as a folder containing several of those stack. 

![alt text](https://camo.githubusercontent.com/764d4282e5f72a647df6bf272889ed644c177d33/687474703a2f2f692e696d6775722e636f6d2f4f696d577161672e6a7067 "CalciumSignalExtract")

The user can select different thresholds, particle sizes, smoothing and averaging method to tailor the automated extraction to the needs of the individual data. The data gets then manipulated using cross correlation, thresholding, segmentation, smoothing and curve fitting to find each indiviual cell, extract the activity pattern of each, add it to a database, normalize it, plot it and then correlate each cell's activity to each other. 

As collect data while the animal is performing a task and would like to know when events as a choice by the animal, a presentation of a stimulus or movement of the animals happens, these events can also be plotted alongside the data for easy comparison.

The whole program is available [at Github](https://github.com/ninehundred1/CalciumSignalExtract), see a corresponding Labrigger entry [here](http://labrigger.com/blog/2015/08/21/calcium-imaging-analysis-gui-for-matlab/).


