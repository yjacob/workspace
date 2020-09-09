import os
import json
import time
import random
import string
from datetime import datetime, timedelta

import requests


rooms = {
    # blsm
    'blsm1br': '34457284',
    'blsmlo1br': '35842498',
    'blsm2br': '35923088',
    #
    # lpn
    #DELETED 'lpn1br': '32007323',
    'lpnsm2br': '33509908',
    'lpnla2br': '32904357',
    #
    # ask
    # 'ask1br': '33140478',
    # 'asklo1br': '35168362',
    # 'ask2br': '31588234',
    #
    # vtr
    'vtr1br': '35786821',
    'vtr2br': '35789467',
    #
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
#New coding by  Jacob -  Start
available_path = "/usr/share/nginx/html/available"
myprice_path = "/usr/share/nginx/html/jrate"
agent_path = "/usr/share/nginx/html/agent"
#End

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

        
        months0 =  resp.json()
        months = resp.json().get('calendar_months', [])
        data = []

        for month in months:
            m = {
                'year': month['year'],
                'month': month['month'],
                'days': []
            }
            days = month['days']
            for day in days:
                m['days'].append({
                    'date': day['date'],
                    'available': day['available'],
                    'price': day['price']['local_price_formatted'][1:]
                })
            data.append(m)
        datajson = json.dumps(months0)
#        datajson = json.dumps(months0, sort_keys=True, indent=5, separators=(',', ': '))
#        data = str(data)
        mypricepath = os.path.join(myprice_path, f"{name}.json")
        with open(mypricepath, 'w') as fs:
           fs.write(datajson)
#       print(data)
#2345678break
        break
