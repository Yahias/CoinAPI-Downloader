### CoinAPI Downloader

#### This Script is for fetching the historical data for cryptocurrencies from CoinAPI.io since the January 1st of 2016.
#### List of cryptocurrencies: [Bitcoin (BTC), Ethereum (ETH), Ripple (XRP),Litecoin (LTC) ]
#### Input variables: 
    - cryptocurrency symbol example : Bitcoin --> BTC
    - API Key
#### Output format:
    - Json file with the result, named as result_start_date - end_date.json

#### How to Run:
    $ python coinAPI_Downloader_vr1.py -c <curency_symbol> -k <API_KEY>
     
##### Example:
     $ python coinAPI_Downloader_vr1.py -c BTC -k 58457C88-XXXXXX-XXXXXX