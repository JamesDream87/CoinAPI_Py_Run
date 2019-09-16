# 1.Create your setting folder in the root path

# 2.Create your config.py in the setting folder

# 3.write your config data in the config.py
## 3.1. Like this:
  ```
  config ={     
    'host': 'your host',       
    'user': 'your username',              
    'password': 'your PWD',       
    'port': 'your port',                   
    'database': 'your DB name',
    'key': 'your CoinAPI key'
  }

  CoinList = [
    {'name': 'huobi_SPOT_eos_USD', 'period': [{'time':'1DAY','table': 'huobi_eos_1d'},{'time':'1HRS','table':'huobi_eos_1h'}]}
  ]
  ```
  in the CoinList Json, name means the symbol and time is the data period, table is the db table name.