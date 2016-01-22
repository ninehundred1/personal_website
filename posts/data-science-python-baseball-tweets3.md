title: Python Data Science - World Series Tweets
date: 2015-08-17
published: True
tags: programming
image: img/posts/3.jpg
featured: True

Comparison of scraped tweets sent over the course of the World Series Baseball game NY Mets vs Kansas City Royals in 2015.




##### Preview:

![alt text](http://i.imgur.com/rgHpZaG.jpg "Tweets1")

![alt text](http://i.imgur.com/KiLgzpx.jpg "Tweets2")


Tweets are saved in a MongoDB database, then split into two groups and compared to how many tweets were made over the time the data was collected, where they were sent, what the top words were and how those words change over the timecourse of the data.
The script works for any two search terms.
The steps to be done are these:
1. Import the data from MongoDB into Pandas dataframes.
2. Count the number of tweets for both sets over the time of the data set
3. Find the top words tweeted at different times of the data
4. Show the location of the tweets of the two data sets






See the files here at [Github](https://github.com/ninehundred1/DataScience_Baseball_Tweets).

