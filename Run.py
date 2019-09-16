from setting import config
from coin import RunInit

def Init():
  List = config.CoinList
  con = config.config

  for i in range(len(List)):
    if i < len(List):

      for j in range(len(List[i]['period'])):
        if j < len(List[i]['period']):
          RunInit.Init(
            List[i]['name'],
            List[i]['period'][j]['time'],
            List[i]['period'][j]['table'],
            con
          )

Init()