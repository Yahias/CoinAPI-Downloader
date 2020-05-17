### CoinAPI Downloader Version 2.0

#### This Script for fetching data from coinAPI and writing it to a database Postgres based on the last record at the database if there is no records will start from the January 1st of 2016.



##### Prerequisties:
- Pandas : 
pip install pandas
- Psycopg:
pip install psycopg2  
Or:  
pip install psycopg2-binary

#### Input variables: 
- cryptocurrency code example : Bitcoin --> BTC
- API Key

#### Configuration File:
db_config.ini 
This file conatain all the parameter for the database connection.

db_user: Databse account

db_password: The Password

hostname: The hostname of the database server

db_port= The port of postgres defualt is 5432

db_name=database name of the data for example : coin_api


#### How to RUN :

$ python coinAPI_Downloader_vr2.py -c < CurrencySymbol> -k your-API_KEY

Example:

$ python coinAPI_Downloader_vr2.py -c ETH -k 58457C88

Starting of fetching historical data of ETH starting from 2016-01-01T00:00:00
Writting to the Datbase 
1437 records have been written


