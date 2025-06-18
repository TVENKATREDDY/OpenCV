import calendar
import datetime
day_week=calendar.weekday(2025,2,6)
day_na=calendar.day_name[day_week]
format_string = "%a %d %b %Y %H:%M:%S %z"
date_string = input()
date_string1 = input()
print(day_week)
print(day_na)
d1=datetime.datetime.strptime(date_string,format_string)
d2=datetime.datetime.strptime(date_string1,format_string)
datedff=d1-d2
print(round(datedff.total_seconds()))