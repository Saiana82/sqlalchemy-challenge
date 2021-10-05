# sqlalchemy-challenge

## Step 1 - Climate Analysis and Exploration

To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database. All of the following analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.




### Precipitation Analysis

* I started by finding the most recent date in the data set.

* Using this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data. 

* Only the `date` and `prcp` values was selected.

* The query results was loaded into a Pandas DataFrame and set the index to the date column.

* The DataFrame values was sorted by `date`.

* The results ploted using the DataFrame `plot` method.


* Using Pandas I printed the summary statistics for the precipitation data.

### Station Analysis

* I designed a query to calculate the total number of stations in the dataset.

* I designed a query to find the most active stations (i.e. which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * Using the most active station id, calculate the lowest, highest, and average temperature.

 

* I designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Query the last 12 months of temperature observation data for this station.

  * Plot the results as a histogram with `bins=12`.

    

* Closed out a session.

- - -

## Step 2 - Climate App

* Used Flask to create your routes.

### Routes

* `/`

  * Home page.

  * Listed all routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.



  