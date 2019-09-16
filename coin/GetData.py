import requests
import json
import datetime

def WriteJson(name, time, con):
  base = f'https://rest.coinapi.io/v1/ohlcv/{name}/history?'
  period = time
  limit = '100'

  # Set the Start time and End time
  now = datetime.datetime.now()
  end = now + datetime.timedelta(hours = -now.hour-8,minutes = -now.minute, seconds = -now.second, microseconds = -now.microsecond)
  start = end + datetime.timedelta(-1)

  # format the time
  end = end.strftime('%Y-%m-%dT%H:%M:%S')
  start = start.strftime('%Y-%m-%dT%H:%M:%S')

  # GetData
  url = base + 'period_id=' + period + '&time_start=' + start + '&time_end=' + end + '&limit=' + limit
  headers = {'X-CoinAPI-Key': con['key']}
  response = requests.get(url, headers=headers)
  json_str = json.dumps(response.json())

  # WriteData
  fo = open("data.json", "w", encoding='utf-8')
  fo.write(json_str)
  return True

def CheckJson(name,time):
  fo = open("data.json")
  json_str = json.loads(fo.read())

  if(time == '1DAY'):
    TimeLen = 1
  elif (time == '1HRS'):
    TimeLen = 1 * 24
  elif (time == '15MIN'):
    TimeLen = 1 * 24 * (60/15)

  # 判断总数目是否足够
  num = len(json_str)

  # 如果数据数目小于应该写入条数，显示出缺失数据
  if num < TimeLen:
    print(f'{name}-{time}:数据缺失')
    num = num - 1
    # 循环显示缺失数据
    for i in range(len(json_str)):
      if i < num:
        json_str[i]['time_period_start'] = json_str[i]['time_period_start'].replace('0000000Z', '000000Z')
        json_str[i+1]['time_period_start'] = json_str[i+1]['time_period_start'].replace('0000000Z', '000000Z')
        d1 = datetime.datetime.strptime(json_str[i]['time_period_start'], '%Y-%m-%dT%H:%M:%S.%fZ')
        d2 = datetime.datetime.strptime(json_str[i+1]['time_period_start'], '%Y-%m-%dT%H:%M:%S.%fZ')

        if time == '1HRS':
          d4 = (d2-d1).seconds
          if(d4 > 3600):
            print(f'缺失位置:{d1}  至  {d2},时长:{(d4-3600)/3600}小时')
        elif time == '15MIN':
          d3 = (d2-d1).seconds
          if(d3 > 900):
            print(f'缺失位置:{d1}  至  {d2},时长:{(d3-900)/900}分钟')
        elif time == '1DAY':
          d3 = (d2-d1).days
          if(d3 > 1):
            print(f'缺失位置:{d1}  至  {d2},时长:{d3-1}天')

  # 如果数据数目大于应写入数目，返回错误
  elif num > TimeLen:
    print(f'{name}-{time}:数据冗余，出现异常')
  elif num == TimeLen:
    return True


def Main(name, time, table, con):
  Res = WriteJson(name, time, con)
  print(Res)
  # if Res == True:
  #   Count = CheckJson(name, time)
  #   print(Count)