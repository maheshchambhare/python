import calendar

#----------------Weakheader-------------

print(calendar.weekheader(1))
print()

#----------------firstweekday()-------------
print(calendar.firstweekday())
print()

#----------------month(2020,4)-------------
print(calendar.month(2020,4))
print()

print(calendar.monthcalendar(2020 , 2))
print()

# *****whole year *************
print()
print(calendar.calendar(2020))

#************weakday*************

print(calendar.weekday(2020 ,4 ,19))

print()

#*****************is_leap***********

print(calendar.isleap(2020))
print()

#**************calculate leap years *************
print(calendar.leapdays(2020 ,3020))
