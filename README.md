# surfs_up 

## overview
The purpose of this challenge was to work wit SqlAlchemy and pandas to look into a database and analize weather data for a business planning to open in florda. The business needed to know if they weather would be good for a surf shop and icecream shop since their previous business failed likely due to bad weather in the area. Along with this the business would like to use this on multiple locations or databases with the same structure. The code I have done uses functions that can be used on different cities and timeframes with minor adjustment so it should help in the future aswell. It sends the information into a flask application.

## Analysis 
The flask application first shows you a list of paths you can take for different information. This is displayed below

> Welcome to the Climate Analysis API! <br>
> Available Routes: <br>
> /api/v1.0/precipitation <br>
> /api/v1.0/stations <br>
> /api/v1.0/tobs <br>
> /api/v1.0/temp/start/end <br>


The most important thing for the businesses was the temperature, coming in second was the precipitation. For this I have created pages for both of these on the application where you can get the data from the previous year. you can also get a list of stations and since weather is the most important piece of information, you are able to get summary statistics for any timeframe that is in the dataframe with /api/v1.0/temp/start/end.  This is very useful to see if the weather will cooperate with a store. 

When it comes to the location they wanted tested first, they were curious if an icecream shop would still be able to stay open all year. They wanted the summary statistics for June and December. I used a jupyter notebook to create a small function that you can pull the weather data from any specific month from all years. I checked these years and the results are displayed below. 

![image](https://user-images.githubusercontent.com/81537476/142919169-aef5af2f-a8e8-4dc5-94f1-96148dd49cca.png)![image](https://user-images.githubusercontent.com/81537476/142919232-3f4aaf2c-1261-4c0d-bb08-ec699fe42d88.png)

## Summary

The scripts created in this project should be useful for doing basic weather analysis for any location that you can get a simmilar database. When it comes to the data we were working with this time it seems that the location consistently has good weather and will be a good location for a shop since the weather is consistently warm with an avg temperature of 71 even in December. 

