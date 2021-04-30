#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#sunday on the 1st of every month?
from time import time
import datetime

def sunday_count(s,e): #date = "dd:mm:yyyy"
    day, month, yr = s.split(":")
    start_date = datetime.date(int(yr), int(month), int(day))

    day, month, yr = e.split(":")
    end_date = datetime.date(int(yr), int(month), int(day))

    delta = datetime.timedelta(days=1)

    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sunday_count = 0
    while start_date <= end_date:
        day_index = start_date.weekday()
        if start_date.day == 1 and day_name[day_index] == 'Sunday':
            sunday_count += 1
        start_date += delta

    return sunday_count

sol = sunday_count('01:01:1901','31:12:2000')
print('There are {} sundays in the start of every month between the given dates'.format(sol))
