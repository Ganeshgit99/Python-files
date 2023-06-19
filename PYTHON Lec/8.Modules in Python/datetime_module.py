'''

datetime module
===============
'''


import datetime as dt
'''
print(dt.MINYEAR)
print(dt.MAXYEAR)

dt1=dt.datetime(2023,2,2)
print(dt1)
dt2=dt.datetime(2023,2,2,15,30,45)
print(dt2)
print(type(dt2))
'''

#current date and time
curdt=dt.datetime.today()
print('Usinf today:',curdt)

cdt=dt.datetime.now()
print('Using now:',cdt)

print('Year:',cdt.year)
print("Month:",cdt.month)
print("Day:",cdt.day)
print("Hour:",cdt.hour)
print("Minute:",cdt.minute)
print("Second:",cdt.second)


