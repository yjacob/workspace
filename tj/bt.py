from datetime import date, timedelta

sdate = date(2019, 9, 1)   # start date
edate = date(2019, 9, 10)   # end date

delta = edate - sdate       # as timedelta

dates = []
datesstr = ""
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates.append(day)
    datesstr = datesstr+str(day)+","
print(dates)
print (datesstr)

