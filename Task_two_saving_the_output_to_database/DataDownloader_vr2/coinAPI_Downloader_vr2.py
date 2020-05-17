"""
This Script is for fetching the historical data from cryptocurrencies from CoinAPI.io based on the last record at the database if there is no records will start from the January 1st of 2016.
List of cryptocurrencies: [Bitcoin (BTC), Ethereum (ETH), Ripple (XRP),Litecoin (LTC) ]

Input variables: 
    - cryptocurrency code example : Bitcoin --> BTC
    - API Key
    
"""

import os
import requests
import pandas as pd
#import numpy as np
from io import StringIO
from sqlalchemy import create_engine
import psycopg2
import argparse
from datetime import datetime
import configparser



def gettingThelastdate(db_user,db_password,hostname,db_port,db_name):
    try:
        connection = psycopg2.connect(user=db_user,password=db_password,host=hostname,port=db_port,database=db_name)
        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT DATE(time_period_end) FROM ohlcv_historical_data where currency_code='{currency_code.upper()}' ORDER BY 1 DESC LIMIT 1"
        cursor.execute(postgreSQL_select_Query)
        #print("getting the last record of the database")
        last_date = cursor.fetchall() 
        if last_date != []:
            return last_date[0][0]
        else:
            return datetime(2016, 1, 1).replace(microsecond=0).isoformat()


    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
        #print("PostgreSQL connection is closed")


def writingToDatabase(db_user,db_password,hostname,db_port,db_name,df,table_name):
    try:
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{hostname}:{db_port}/{db_name}')
        df.to_sql(table_name, engine, if_exists='append',index=False)
        print("Writting to the Datbase ")
        print(f'{df.shape[0]} records have been written')
        


    except (Exception, psycopg2.Error) as error :
        print ("Error while writing data to PostgreSQL DB", error)



parser = argparse.ArgumentParser()
parser.add_argument("-c", "--currencysymbol", required=True,help="Currencty Symbol for example BTC,ETH,XRP,LTC")
parser.add_argument("-k", "--key", required=True,help="Your API KEY")
args = parser.parse_args()


config = configparser.ConfigParser()
config.read('db_config.ini')
db_parameters = config['DB_prameters']

db_user=db_parameters['db_user']
db_password=db_parameters['db_password']
hostname=db_parameters['hostname']
db_port=db_parameters['db_port']
db_name=db_parameters['db_name']

currency_code=args.currencysymbol
API_KEY =args.key
headers = {'X-CoinAPI-Key': API_KEY}
#start_date='2016-01-01T00:00:00'
end_date=datetime.today().replace(microsecond=0).isoformat()
period = '1DAY'
limit = '100000'
asset_id_base=currency_code.upper()
asset_id_quote='USD'

if __name__ == "__main__":
    start_date=gettingThelastdate(db_user,db_password,hostname,db_port,db_name)
    
    print(f'Starting of fetching historical data of {currency_code} starting from {start_date}')

    try:

        url = f'https://rest.coinapi.io/v1/ohlcv/{asset_id_base}/{asset_id_quote}/history?period_id={period}&time_start={start_date}&limit={limit}'
        resp = requests.get(url,params={'output_format': 'csv'},headers=headers)
        #print(resp.status_code)
        if resp.status_code == 200:
            #Creating Pandas Dataframe from the response
            data = pd.read_csv(StringIO(resp.text), sep=';')

            #Adding the related currency_code to the Data
            data['currency_code'] = currency_code.upper()
            #print(data)

            #Sending to the datbase:
            writingToDatabase(db_user,db_password,hostname,db_port,db_name,data,'ohlcv_historical_data')
        else: 
            print(f"error message{resp.json()}") 

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from API ", error)