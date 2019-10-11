import datetime

def main(year, month):

  # if year == 2019 and month == 9:
  #   print('end....')
  # else:
  if(month == 12):
    newYear = year + 1
    newMonth = 1
  else:
    newYear = year
    newMonth = month + 1

  a = datetime.datetime(year, month, 13, 16, 00, 00)
  b = datetime.datetime(newYear, newMonth, 13, 16, 00, 00)
  a = datetime.datetime.strftime(a,'%Y-%m-%dT%H:%M:%S')
  b = datetime.datetime.strftime(b,'%Y-%m-%dT%H:%M:%S')
  print(a,'-------',b)

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
    
    if year == 2019 and month == 9 :
      break
    
    main(year,month)

count()