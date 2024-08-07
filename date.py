#import datetime
from datetime import datetime
# datetime modulunden sadece datetime sinifini import lar
from datetime import time
from datetime import date
from datetime import timedelta

result=dir(datetime)
print(result)

suan=datetime.today()
suan=datetime.now()

result=datetime.now()
result=suan.year
result=suan.month
result=suan.day
result=suan.hour
result=suan.minute
result=suan.second

result=datetime.ctime(suan)
# suanki zamani daha detayli gosterir ay gun yil saat vesaire
result=datetime.strftime(suan,"%Y") # sadece yili yazdirir
print(result)

result=datetime.strftime(suan,"%X") 
print(result)

result=datetime.strftime(suan,"%d") 
print(result)

result=datetime.strftime(suan,"%A") 
print(result)

result=datetime.strftime(suan,"%B ") 
print(result)

result=datetime.strftime(suan,"%Y %B %A") 
print(result)

t="21 Nisan 2019"

gun,ay,yil =t.split(" ")
print(gun)
print(ay)
print(yil)

t="19 April 2019 hour 10:12:30"
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)
dt=dt.year

birthday=datetime(1983,5,9,12,30,10)
print(birthday)

dt=datetime.fromtimestamp(dt)
print(dt)

result=datetime.timestamp(birthday) # saniye
print(result)

result=datetime.fromtimestamp(result) # saniye to datetime
print(result)

result=datetime.fromtimestamp(0) 
print(result)

result=suan - birthday # timedelta objesi
print(suan)

result=suan+timedelta(days=10)
print(result)
result=suan+timedelta(days=720,minutes=10)
print(result)

