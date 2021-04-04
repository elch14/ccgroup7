Covid-19-API
-------------
An API and JSON list that contains countries covid cases. 

-------------
Using the API
-------------

API Base: https://covid19-qm-grp7.herokuapp.com/

-------------
Summary Data
------------

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

Input country string name into Country:<name> on main page.

Request API from https://api.covid19api.com/dayone/country/<name>

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
