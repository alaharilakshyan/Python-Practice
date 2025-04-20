from datetime import date

fdate = date(2025, 4, 10)
ldate = date(2025, 9, 5)

missing_days = fdate - ldate
print("No.of Days Left: ", missing_days.days)
#datetime module is used to work with dates and times.
#date class is used to work with dates.
#date class is used to create date objects.
#missing_days is used to calculate the difference between two dates.
#fdate and ldate are used to create date objects.