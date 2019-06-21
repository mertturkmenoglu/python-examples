# Example 046: Time

import datetime

# Get current date and time
current = datetime.datetime.now()
print(current)

print('\n' * 3)

# Get current date
today_date = datetime.date.today()
print(today_date)

print('\n' * 3)

# List possible usages
print(dir(datetime))

print('\n' * 3)

# Create a date object
date_obj = datetime.date(2019, 4, 13)
print(date_obj)

print('\n' * 3)

# Create a timestamp
timestamp = datetime.date.fromtimestamp(1326244364)
print("Date =", timestamp)

print('\n' * 3)

# Create a date obj
today_date = datetime.date.today() 
print("Current year:", today_date.year)
print("Current month:", today_date.month)
print("Current day:", today_date.day)

print('\n' * 3)

# Create time object
a = datetime.time()
print("a =", a)

# Create time object with params
b = datetime.time(11, 34, 56)
print("b =", b)

# Create time object with params
c = datetime.time(hour = 11, minute = 34, second = 56)
print("c =", c)

# Create time object with params
d = datetime.time(11, 34, 56, 234566)
print("d =", d)

print('\n' * 3)

# Create time object and get fields
a = datetime.time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

print('\n' * 3)

# datetime(year, month, day)
a = datetime.datetime(2018, 11, 28)
print(a)

print('\n' * 3)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

print('\n' * 3)

# Create datetime object and get fields
a = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())