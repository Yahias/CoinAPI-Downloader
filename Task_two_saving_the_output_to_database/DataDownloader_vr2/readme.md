### CoinAPI Downloader Version 2.0

#### This Script for fetching data from coinAPI and writing it to a database Postgres.

#### New changes :
1. Dynamic start date: 
in version one the start date was set static to the first of Januray 2016, in this version this parameter have been changed to be dynamic,
in order to avoid duplication with itration of running the script based on the last record at the database if there is no records will start from the January 1st of 2016.

2. Database Integration: to be able to store the data to the datbase some changed has been made to the script, to open connection with database and write the data.

### How it Work:
1. The script will query the database to get the most update date related to the input currency to avoid data duplication and keep consistent data records
2. If the no records in the database for this currency, the script will set the default value (2016-01-01) as start date for fetching the historical data.

3. run the request from API to get the data.
4. Have the data in panadas dataframe.
5. send the dataframe to the database.


### Prerequisties:
- Pandas : 
pip install pandas
- Psycopg:
pip install psycopg2  
Or:  
pip install psycopg2-binary

### Input variables: 
- cryptocurrency code example : Bitcoin --> BTC
- API Key

### Configuration File: db_config.ini 
This file conatain all the parameter for the database connection.

Definition of the parameters:
- db_user: Databse account

- db_password: The Password
- hostname: The hostname of the database server

- db_port= The port of postgres defualt is 5432

- db_name=database name of the data for example : coin_api


### How to RUN :
1. Set the proper configuration for the database on the parameter file **db_config.ini**
2. Run the script with the required variables as below:

    $ python coinAPI_Downloader_vr2.py -c < CurrencySymbol> -k your-API_KEY

Example:

    $ python coinAPI_Downloader_vr2.py -c ETH -k 58457C88-XXXXXX-XXXXX

#### Sample output of successfull run :
Starting of fetching historical data of ETH starting from 2016-01-01T00:00:00
Writting to the Datbase 
1437 records have been written


