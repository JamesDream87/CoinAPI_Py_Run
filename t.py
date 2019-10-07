import datetime

def main(year, month):
  a = datetime.datetime(year, month, 13, 16, 00, 00)
  a = datetime.datetime.strftime(a,'%Y-%m-%dT%H:%M:%S')
  print(a)

def count():
  year = 2011
  month = 8
  end = False

  while True:
    if month == 12:
      year += 1
      month = 1
    else:
      month += 1
    
    if year == 2019 and month == 10 :
      break
    
    main(year,month)

count()
