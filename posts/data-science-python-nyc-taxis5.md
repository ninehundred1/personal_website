title: Python Data Science - NYC taxis
date: 2015-12-01
published: True
tags: programming
image: img/posts/5.jpg
featured: True

Mapping of NYC cab hailing behavior, locations, times, revenue, trip length and passenger number of over 20 million NYC cab rides in January 2015.


##### Preview:

![alt text](http://i.imgur.com/rTZu1a0.jpg "Cabs1")

![alt text](http://imgur.com/RWIwMrv.jpg "Cabs2")

![alt text](http://i.imgur.com/99eOVpK.jpg "Cabs3")



Use the publicly available NYC cab data csv datasets for January 2015. Available here: http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
We will compare two sets, the yellow (Manhattan bound) and the green (outer borough) cabs as well as their pickup and drop off data for the first Wednesday and Sunday that month for over 20 million entries.

####These are the steps:


##### A. DROP OF AND PICKUP LOCATION DIFFERENCES BETWEEN YELLOW AND GREEN CABS.


To enable better access to the boroughs outside of Manhattan, green cabs are not allowed to pick up passengers within Manhattan, which we plan to visualize here

A1. Parse the CSV file into a MongoDB database to allow for different query of the large dataset (20 million cab tours)

A2. Query the database and load the geo coordinates for pickup and dropoff data into a Pandas dataframe from a selected date range

A3. Clean and sort the data within Pandas and split into pickup and dropoff coordinates

A4. Plot the whole month data as scatter plot in Pandas using Matplotlib to compare pickup and dropoff location between yellow and green

#####B. DISTRIBUTION OF PICKUPS AND DROP OFFS OVER A 24H ON A WEDNESDAY AND SUNDAY

To visualize changes of passenger behavior between a normal workday and a weekend day, we visualize where passengers are being picked up and dropped off over a 24h period and compare the difference between a Wednesday and Sunday

B1. Sort and bin data into 24 one hour long bins

B2. Visualize distribution of drop offs at different times of day between green and yellow cabs

#####C. DISTRIBUTION OF PASSENGER NUMBER, TRIP LENGTH AND REVENUE ACROSS A WEDNESDAY AND SUNDAY

To assess how many cab are being hailed, how much money is earned, how many passengers use cabs and how all that changes over a word day as compared to a weekend day, we will compare those parameters

C1. Sort and bin data into 24 one hour long bins extracting the mean, standard errors and sums of passengers, trip lengths and revenue.


#####D. ORIGIN AND DESTINATION OF CAB TRAFFIC INTO WILLIAMSBURG ON A SATURDAY

Williamsburg in Brooklyn being a popular destination for nightly events outside of Manhatten, we will visualize where the passengers hail the cabs that go into Williamsburg and similarly where passengers are dropped off when leaving Williamsburg on a Saturday until Sunday early morning. We will visualize how these ride location change throughout a 24 hour perid.

D1. Query MongoDB database for Saturday data and load into Pandas dataframe

D2. Clean data and extract only traffic starting or ending within GPSs bounds of Williamsburg

D3. Sort and bin data into 24 one hour long bins


See the files here at [Github](https://github.com/ninehundred1/DataScience_NYC_taxis).

