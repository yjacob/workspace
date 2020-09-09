import os
import time
import random
import string
from datetime import datetime, timedelta

import requests


rooms = {
    # lpn
    'lpn1br': '32007323',
    'lpnsm2br': '33509908',
    'lpnla2br': '32904357',
    # ask
    'ask1br': '33140478',
    'asklo1br': '35168362',
    'ask2br': '31588234',
    # blsm
    'blsm1br': '34457284',
    'blsmlo1br': '35842498',
    'blsm2br': '35923088',
    # vtr
    'vtr1br': '35786821',
    'vtr2br': '35789467',
    # mono
    'mono1br': '36898405',
    'monost1br': '36901129',
}

fmt_ics = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Jacob at TripHi dot co//Hosting Calendar 0.0.1//ZH
{}
END:VCALENDAR
"""

fmt_unit = """
BEGIN:VEVENT
DTSTAMP:{timestamp}
SUMMARY:Not available
UID:{uid}@triphi.co
DTSTART;VALUE=DATE:{start}
DTEND;VALUE=DATE:{end}
END:VEVENT
"""


def rand8() -> str:
    chars = random.sample(string.ascii_letters + string.digits, 8)
    return ''.join(chars)


def gen_uid() -> str:
    return '{}-{}-{}-{}'.format(rand8(), rand8(), rand8(), rand8())


now = datetime.now()
timestamp = now.strftime('%Y%m%dT%H%M%SZ')
cur_year, cur_month = now.year, now.month
today = datetime(now.year, now.month, now.day)

url = "https://www.airbnb.cn/api/v2/homes_pdp_availability_calendar"
currency = 'THB'
key = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'
count = 3

nginx_path = "/usr/share/nginx/html/waka"


if __name__ == '__main__':
    for name, _id in rooms.items():
        resp = requests.get(url, params={
            'currency': currency,
            'key': key,
            'locale': 'zh',
            'listing_id': _id,
            'year': cur_year,
            'month': cur_month,
            'count': count,
        })

        dates = []
        for month in resp.json().get('calendar_months', []):
            start, end = None, None
            for day in month.get('days', []):
                if day['available']:
                    continue
                date = datetime.strptime(day['date'], '%Y-%m-%d')
                if date >= today:
                    dates.append(date)

        units = []
        if len(dates) != 0:
            start, ndays = dates[0], 1
            for i in range(1, len(dates)):
                delta: timedelta = dates[i] - dates[i - 1]
                if delta.days == 1:
                    ndays += 1
                else:
                    unit = fmt_unit.format(
                        timestamp=timestamp,
                        uid=gen_uid(),
                        start=start.strftime('%Y%m%d'),
                        end=(start + timedelta(days=ndays)).strftime('%Y%m%d')
                    )
                    units.append(unit)
                    start, ndays = dates[i], 1
            unit = fmt_unit.format(
                timestamp=timestamp,
                uid=gen_uid(),
                start=start.strftime('%Y%m%d'),
                end=(start + timedelta(days=ndays)).strftime('%Y%m%d')
            )
            units.append(unit)

        doc = fmt_ics.format(''.join(units)).strip()
        fpath = os.path.join(nginx_path, f"{name}.txt")
        with open(fpath, 'w') as fs:
            fs.write(doc)

        print(name+".txt generated")
        time.sleep(20)

