USE test;

SELECT * FROM chicago_climate_dat;
SELECT * FROM detroit_weather_data;

#Before proceeding with our newly scraped CSV files
#lets make sure our data is clean. Our data from the NOAA
#Has already been cleaned of Null and duplicate values
#but we need to ensure our data types were imported correctly 
#and everything is correctly standardized prior to querying and 
#visualizing in Tableau.

#from looking at both our tables, it looks like our 
#chicago dataset has our 'Year' listed as a double type while our 
#Detroit set is listed as a "Int", this can cause challenges in the 
#future if we were to perform Joins in tableau as their data types dont match.

ALTER TABLE chicago_climate_dat
MODIFY COLUMN `Year` INT;

SELECT * FROM chicago_climate_dat;

#Now, From both tables again, I have a column named MyUnknownColumn that is 
#should be my ID column, lets update both tables to change the name to something
#more descriptive and clear.

ALTER TABLE chicago_climate_dat
RENAME COLUMN MyUnknownColumn TO chi_ID;

ALTER TABLE detroit_weather_data
RENAME COLUMN MyUnknownColumn TO det_ID;

#Now lets take a look at both cleaned datasets...

SELECT * FROM chicago_climate_dat;
SELECT * FROM detroit_weather_data;

#First, I want to see when average temperatures in jan were the same 
#between chicago and detroit, I'll use a subquery for this

SELECT *
FROM chicago_climate_dat AS chi 
WHERE `Jan` IN(
	SELECT `Jan`
    FROM detroit_weather_data AS det);
    
#it looks as though 2001,2005,2010,and 2018 we had the exact same average temperatures!

#Just for comparison, I could also do the same process with an inner join

SELECT * 
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.Jan = det.Jan;

#Now lets find all Years and Months where averages were the exact same between the two cities
#to do this ill utilize inner joins and unions to return one table.

SELECT chi.`Year` AS chi_1, chi.`Jan`, det.`Year`, det.`Jan`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Jan` = det.`Jan`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_2, chi.`Feb`, det.`Year`, det.`Feb`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Feb` = det.`Feb`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_3, chi.`Mar`, det.`Year`, det.`Mar`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Mar` = det.`Mar`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_4, chi.`Apr`, det.`Year`, det.`Apr`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Apr` = det.`Apr`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_5, chi.`May`, det.`Year`, det.`May`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`May` = det.`May`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_6, chi.`Jun`, det.`Year`, det.`Jun`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Jun` = det.`Jun`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_7, chi.`Jul`, det.`Year`, det.`Jul`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Jul` = det.`Jul`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_8, chi.`Aug`, det.`Year`, det.`Aug`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Aug` = det.`Aug`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_9, chi.`Sep`, det.`Year`, det.`Sep`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Sep` = det.`Sep`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_10, chi.`Oct`, det.`Year`, det.`Oct`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Oct` = det.`Oct`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_11, chi.`Nov`, det.`Year`, det.`Nov`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Nov` = det.`Nov`
    WHERE chi.`Year` = det.`Year`
UNION
SELECT chi.`Year`AS chi_12, chi.`Dec`, det.`Year`, det.`Dec`
FROM chicago_climate_dat AS chi
INNER JOIN detroit_weather_data AS det
	ON chi.`Dec` = det.`Dec`
    WHERE chi.`Year` = det.`Year`
    ORDER BY `Year`;

#In 2018 there were 3 months where the average temperature was the exact same between both cities!

#Lets query through our tables to get a pulse on temperature change over our 20 year period 
#to see if we can identify an increase or decrease over time.

WITH CTE_chicago AS(
SELECT `Year`,`Avg` AS chi_avg
FROM chicago_climate_dat
WHERE `Year` = 2000 OR
`Year` = 2020
),
CTE_detroit AS(
SELECT `Year`,`Avg` AS det_avg
FROM detroit_weather_data
WHERE `Year` = 2000 OR
`Year` = 2020)
SELECT * FROM
CTE_chicago AS chi
JOIN CTE_detroit AS det
	ON chi.Year = det.Year;
    
#It appears that both chicago and detroit have slighlty increased in annual temperature on average 
#with chicago at a +3.5 temp increase, and detroit at a +2.1 temp increase across 20 years
#We can visualize this in Tableau to see if this change is a linear increase or if the change is 
#more random over 20 years
    
#Now let's find What Month and Year was the coldest on average?
#I'll start by taking our typical winter months
#and retrieving the minimum with a CTE

WITH CTE AS(
SELECT Year,MIN(`Jan`) AS jan, 
MIN(`Feb`)AS feb, 
MIN(`Dec`) AS december 
FROM 
detroit_weather_data
GROUP BY Year)
SELECT MIN(feb)
FROM CTE;

#It looks like february was our coldest month on average across 20 years
#in 2015 at a chilling 14.1 degrees.

#Now lets identifty when some of our warmest months occured

SELECT * 
FROM detroit_weather_data AS D
JOIN chicago_climate_dat AS C
	ON D.det_ID = C.chi_ID
    WHERE D.Jul > 78;
    
#It looks as though back to back 2011 and 2012 had some of the hottest recorded averages
#with july 2012 in chicago reaching an average of 81 degrees 


