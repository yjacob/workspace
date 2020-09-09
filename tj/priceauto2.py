import os
from math import ceil
import time
import random
import string
from datetime import date, datetime, timedelta
from pprint import pprint
import requests


rooms = {
    # 1st One Before Break
    #

    # Lumpini
    'lpn1br': '32007323',
    'lpnsm2br': '33509908',
    'lpnla2br': '32904357',

    # Blossom
    'blsm1br': '34457284',
    'blsmlo1br': '35842498',
    'blsm2br': '35923088',

    # Vtara
    'vtr1br': '35786821',
    'vtr2br': '35789467',

    # Mono
    'mono1br': '36898405',
    'monost1br': '36901129',

    # Asoke
    # 'ask1br': '33140478',
    # 'asklo1br': '35168362',
    # 'ask2br': '31588234',
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


def randnum8() -> str:
    chars = random.sample(string.digits, 8)
    return ''.join(chars)


def gen_reqid() -> str:
    return '15667{}'.format(randnum8())

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

        dates = []
        pdates = []
        bnbprices = []

        for month in resp.json().get('calendar_months', []):
            start, end = None, None
            pstart, pend = None, None

            for day in month.get('days', []):
                pdate = datetime.strptime(day['date'], '%Y-%m-%d')
                bnbprice = int(day['price']['local_price_formatted'][1:])
                if pdate > today:
                    pdates.append(pdate)
                    bnbprices.append(bnbprice)
#        pprint (str(bnbprices))
#        print ("\n\n")
#        pprint (str(pdates))
#        print ("\n\n")
        


#       
       
        updates = []
        upprices = []
        if len(bnbprices) != 0:
#            pstart, pndays = pdates[0], 1
            for i in range(1, len(bnbprices)):
                pdiff = bnbprices[i] - bnbprices[i - 1]

                if i ==1:
                    updates.append(pdates[i-1])
                    upprices.append(bnbprices[i-1])

                if pdiff != 0:
                   # pndays += 1
                    updates.append(pdates[i])
                   # print (bnbprices[i])
                   # print (bnbprices[i-1])
                    upprices.append(bnbprices[i])
                   # print (pdates[i])
                   # print ("\n-\n")

                if i == len(bnbprices)-1:
                    updates.append(pdates[i])
                    upprices.append(bnbprices[i])
            print (str(upprices))
            print ("\n")
            print (str(updates))
#
#
            for ib in range(0, len(upprices)-1):

                  sdate = updates[ib]   # start date
                  edate = updates[ib+1]   # end date
                  pri = upprices[ib]
                  if ib == len(upprices)-2:
                        delta = edate - sdate + timedelta(days=1)       # as timedelta
                  else:
                        delta = edate - sdate
                  dates = []
                  for ic in range(delta.days):
                       day = sdate + timedelta(days=ic)
                       day2 = day.strftime("%Y-%m-%d")
                       dates.append(day2)
                  print(pri)
                  print(dates)

                  url = "http://waka.jia.com/api/v4/date_prices"
                  headers = {
                      'Content-Type': "application/json",
                      'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                      'Accept': "*/*",
                      'Cache-Control': "no-cache",
                      'Host': "waka.jia.com",
                      'Accept-Encoding': "gzip, deflate",
                      'Connection': "keep-alive",
                      'cache-control': "no-cache"
                      }
                  user_id = "194835a0-731f-4ea2-b0d0-1100ae354d2b"
                  login_string = "5dffc19ce4c7ed2894cedebc7a5e463c8e2f50d3"

              ### Start
                  lpn1br_waka = ["490395d6-6f4d-4a27-9e3f-b10689c81532","3d014680-b991-4e3a-8e50-c4e578aee131"]
                  for ie in range(0, len("{name}_waka")):
                       reqid = gen_reqid()
                       print ("reqid: "+reqid)
                       payload = {"new_price":pri,"dates":dates,"room_uuid":"{name}_waka"[ie]}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                      # response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
                      # print(response.text)
                       cool = "{name}_waka"[ie]
                       print("\n"+str(ie)+str(cool))
                      # break
                       time.sleep(6)
                
              ### End




#12345678912345678break
#                  break
                                

#2345678break - Must Break Here
        break
