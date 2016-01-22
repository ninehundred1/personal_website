title: Matlab ScanImage Navigator Extension
date: 2015-05-01
published: True
tags: programming
image: img/posts/1.jpg
featured: True


When we installed ScanImage to run our Two Photon Microscope it was lacking a way to actually now where you are in space. You can move the stage around and track the x,y,z coordinates, but you were mainly lost in numbers. 

I put together an extension to Scan Image that will query the motors to get the current position, translate that to a coordinate system and display that in a GUI within the exisitng ScanImage software.

![alt text](https://camo.githubusercontent.com/c02462a57abb8bd663936da6279db09f2ddab476/687474703a2f2f692e696d6775722e636f6d2f4552646365374b2e6a7067 "ScanImageNavigator")

The GUI will allow you to record where you are, mark it in the coordinate system, track your movement, click on saves positions to return to them and also annotate. You can also export the map as a vector as well as all the coordinates to use in Matlab.

See also here for a Labrigger post [Labrigger post](http://labrigger.com/blog/2014/05/08/meyernavigator/comment-page-1/).

The whole extension is available [at Github](https://github.com/ninehundred1/ScanImage_Navigator)