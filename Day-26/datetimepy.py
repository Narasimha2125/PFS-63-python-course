from datetime import date,time,datetime,timedelta

today = date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday)

t = time(23,6,5)

print(t)
print(t.hour)
print(t.minute)
print(t.second)

dt = datetime.now()
print(dt)

print(dt.strftime('%D-%m-%Y %H:%M:%S'))
print(dt.strftime('%D-%m-%Y %H:%M:%S %p'))
print(dt.strftime('%d %b %Y %H:%M:%S %p'))
print(dt.strftime('%d %B %Y %H:%M:%S %p'))
print(dt.strftime('%a %d %Y %H:%M:%S %p'))
print(dt.strftime('%A %d %Y %H:%M:%S %p'))

