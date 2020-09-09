from datetime import datetime, timedelta

now = datetime.now()

cur_day = now.day
today_lastnum = int(str(cur_day)[-1])
print (today_lastnum+1)
#
