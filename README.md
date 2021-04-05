Covid-19-API
-------------
An API and JSON list that contains countries covid cases. 

-------------
Using the API
-------------
Fetching API request from https://api.covid19api.com/ through our app https://covid19-qm-grp7.herokuapp.com/

-------------
Summary Data
------------
A summary of new and total cases per country updated daily.


Request:
Get summary

 {
      "Country": "United Kingdom",
      "CountryCode": "GB",
      "Slug": "united-kingdom",
      "NewConfirmed": 3788,
      "TotalConfirmed": 42477,
      "NewDeaths": 709,
      "TotalDeaths": 4320,
      "NewRecovered": 7,
      "TotalRecovered": 215,
      "Date": "2020-04-05T06:37:00Z"
    },
....

--------------
Countries Name
--------------
Returns all the available countries and provinces, as well as the country slug for per country requests.

Request: 
Get countries

 {
    "Country": "Barbados",
    "Slug": "barbados",
    "ISO2": "BB"
  },
  {
    "Country": "Gibraltar",
    "Slug": "gibraltar",
    "ISO2": "GI"
  },
  {
    "Country": "Lithuania",
    "Slug": "lithuania",
    "ISO2": "LT"
.... 

---------------------------
Individual Countries Cases
---------------------------
Returns all live cases by case type for a country after a given date. These records are pulled every 10 minutes and are ungrouped. Country must be the slug from /countries or /summary. Cases must be one of: confirmed, recovered, deaths


Request API from https://api.covid19api.com/live/country/{country-name}/status/confirmed/date/{date}
{country-name} = United Kingdom
{date} = 2020-01-31

{
    "Active": 2, 
    "City": "", 
    "CityCode": "", 
    "Confirmed": 2, 
    "Country": "United Kingdom", 
    "CountryCode": "GB", 
    "Date": "2020-01-31T00:00:00Z", 
    "Deaths": 0, 
    "ID": "a8482d5e-9a24-4dcd-bb6f-f07872dde610", 
    "Lat": "55.38", 
    "Lon": "-3.44", 
    "Province": "", 
    "Recovered": 0
  }, 
.....

------------------
Run the project
----------------
Setup and activate your virtual enviornment

install requirements pip install -r requirements.txt

run server python server.py

Create user and password on the main page. 
