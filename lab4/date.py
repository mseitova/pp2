#1. Write a Python program to subtract five days from current date.
from datetime import date, timedelta, datetime

today = date.today()
fiveago = today - timedelta(days=5)
print(fiveago)

#2. Write a Python program to print yesterday, today, tomorrow.
today = date.today()
print(f'yesterday: {today - timedelta(days = 1)}\ntoday: {today}\ntomorrow: {today + timedelta(days = 1)}')

#3. Write a Python program to drop microseconds from datetime.
data = datetime.now()
data = data.replace(microsecond=0)
print(data, '.000000', sep = '')

#4. Write a Python program to calculate two date difference in seconds.
def difference_in_seconds(date1, date2):
  # Convert dates to timestamps in seconds
  timestamp1 = date1.timestamp()
  timestamp2 = date2.timestamp()

  #
  difference = abs(timestamp1 - timestamp2)

  return difference

#Example
date1 = datetime(2024, 3, 19, 10, 22, 0)
date2 = datetime(2024, 3, 18, 15, 22, 0)
difference = difference_in_seconds(date1, date2)
print(f"The difference between {date1} and {date2} is {difference} seconds.")