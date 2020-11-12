import calendar
import datetime

print(calendar.weekheader(3))
print("--------------------")

print(calendar.month(2020, 5))
print("--------------------")


print(calendar.monthcalendar(2020, 5))
print("--------------------")

print(calendar.calendar(2021))
print("--------------------")

day_of_week = calendar.weekday (2020,11,9)
print(day_of_week)
print("--------------------")

is_leap = calendar.isleap(2020)
print(is_leap)
print("--------------------")

how_many_leap_days = calendar.leapdays(1000, 3000)
print(how_many_leap_days)
print("--------------------")

hora = datetime.time(15, 2, 11)
print(hora)