from datetime import datetime

now = datetime.now()
print(now)
print(type(now))
date = datetime(2016,4,3,12,20)
print(date)
print(date.timestamp())
t = 1429417200.0
print(date.fromtimestamp(t))
print(date.utcfromtimestamp(t))

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)