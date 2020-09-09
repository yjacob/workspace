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


now = datetime.now()
cur_year, cur_month = now.year, now.month
today = datetime(now.year, now.month, now.day)

url = "https://www.airbnb.cn/api/v2/homes_pdp_availability_calendar"
currency = 'THB'
key = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'
count = 3

nginx_path = "/usr/share/nginx/html/price"
#nginx_path = "rates"

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
        prices = []
        data = []
        rates = ''
        months =  resp.json().get('calendar_months')
        prices = []
        for month in months:
            m = {
                'year': month['year'],
                'month': month['month'],
                'days': []
            }
            days = month['days']
            for day in days:
                    rate = str(day['available'])+"_"+str(day['price']['local_price_formatted'][1:])+"_____"+str(day['date'])+"_____"+str(int(int(day['price']['local_price_formatted'][1:])/0.9))
                    rates = rates + rate + "\n"
        fpath = os.path.join(nginx_path, f"{name}.txt")
        with open(fpath, 'w') as fs:
           fs.write(rates)
        print(name+"'s price list is ready")
        time.sleep(20)

