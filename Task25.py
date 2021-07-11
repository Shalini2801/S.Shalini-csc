#1.Write a Python program to convert a string to datetime 

from datetime import datetime
x= datetime.strptime('Jul 11 2021 2:43PM', '%b %d %Y %I:%M%p')
print(x)

#2.Write a Python program to subtract five days (last working day) from current date

from datetime import date,timedelta
y = date.today() - timedelta(4)
print('Current Date :',date.today())
print('4 days before Current Date :',y)

#3.Write a Python program to convert the date to datetime using a function 

from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt,datetime.min.time()))

#4.Write a Python program to print next 7 days (week) starting from today

import datetime
y = datetime.datetime.today()
for x in range(0, 7):
      print(y+datetime.timedelta(days=x))