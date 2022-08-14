# surfs_up
Weather analysis using Python, Pandas, Jupyter Notebook, SQLite, and SQLalchemy.

## Overview of the analysis
In this analysis key statistics will be compared in O‘ahu, Hawaii's weather to help determine if a surf and ice cream shop is sustainable year-round. Using a SQLite database, temperature information was extracted using SQLalchemy and converted into a Pandas DataFrame. After the DataFrames were created, I used a Pandas Dataframe method to generate summary statistics of the weather. The two months selected to analyze are June and December.

## Results

### Statistics


June Temperature Statistics          |  December Temperature Statistics
:-------------------------:|:-------------------------:
![June Statistics](/Resources/June_statistics.PNG)  |  ![December Statistics](/Resources/December_statistics.PNG)

Our data consists of temperatures from June and December in O`ahu from 2010 to 2017.

### Key differences
- December has 183 less data points than June. (Around 10.76% Less)
- Junes mean temperature is 3.9° higher than Decembers
- Decembers standard deviation is .489° higher.
- Decembers minimum temperatures is 8° lower than Junes.
- Junes 25th percentile is 8° higher than Decembers.
- Junes median is 4° higher than Decembers.
- Junes 75th percentile is 3° higher than Decembers.
- Junes Maximum temperature is 2° higher than Decembers.

## Summary
Comparing the two sets of statistics, the temperature doesn't seem to fluctuate very far from one another. Hawaii is somewhat close to the equator and is known for having warmer temperatures so it's somewhat to be expected. The mean and median tempurature for both months is above 70°, so I would say from this dataset the surf and ice cream shop would be sustainable year-round. 

### Additional Queries
additional queries that would further help this analysis would be to measure the historical percipitation statistics of June and december.

![Prcp](/Resources/Prcp.PNG)

June PRCP Statistics          |  December PRCP Statistics
:-------------------------:|:-------------------------:
![June prcp statistics](/Resources/June_prcp.PNG)  |  ![December prcp statistics](/Resources/December_prcp.PNG)

A second query I would recommend would be checking each of the stations statistics to select an area on O`ahu to build the shop. Ideally the station that reports the highest temperatures will have the most business. These queries get the average temperature for each station in June and December.

![Average station temps](/Resources/Station_avg_temps.PNG)
