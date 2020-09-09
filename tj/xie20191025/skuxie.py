import os
from math import ceil
import time
import random
import string
from datetime import date, datetime, timedelta
from pprint import pprint
import requests


rooms = {

    # Mono
    'mono1br': '36898405',
    'monost1br': '36901129',

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

}

# Xie Login Info

user_id = "54a3906c-fa1d-43e4-984f-aa5a307dffaa"
login_string = "cb76192c3b0dd77c814e5a837f035eb0fa6e4935"

# Xie waka sku id

lpn1br_waka = ["e0b9e05b-cd70-4330-aea7-4bd4cbe2ddea"]
lpnsm2br_waka = ["5628047d-dc25-47f0-bd4c-2cf95f057093","bcb034d4-2798-47c4-8b10-2b448b19e03a"]
lpnla2br_waka = ["344ded6b-681a-402c-b3e1-09eb932d1b42"]
blsm1br_waka = ["b5fbb3bb-61a9-4a15-8b8c-aee55963b9dc"]
blsmlo1br_waka = ["0f1150d8-ed88-489a-b5cc-efa2f6114f62"]
blsm2br_waka = ["6c28cf36-3a95-417d-92cc-0eb455910c4d"]
vtr1br_waka = ["df59d2a1-6273-40d5-b885-1570a9f470cf","9e20db30-78b0-498a-a0a0-2e507f489dea"]
vtr2br_waka = ["e3ad5c9e-a24d-4ccc-9eee-995837056ec4"]
mono1br_waka = ["becdcf1e-4daa-4fa8-bad0-122769da073c"]
monost1br_waka = ["7f19d32f-0b85-49ee-baae-68e08f1b2ada"]


# Xie ical id url

ical_id_url = '31183'

icals = {

# lpn1br
'e0b9e05b-cd70-4330-aea7-4bd4cbe2ddea' : '31182',

# lpnsm2br
'5628047d-dc25-47f0-bd4c-2cf95f057093' : '31183',
'bcb034d4-2798-47c4-8b10-2b448b19e03a' : '31112',

# lpnla2br
'344ded6b-681a-402c-b3e1-09eb932d1b42' : '31181',

# blsm1br
'b5fbb3bb-61a9-4a15-8b8c-aee55963b9dc' : '31236',

# blsmlo1br
'0f1150d8-ed88-489a-b5cc-efa2f6114f62' : '31111',

# blsm2br
'6c28cf36-3a95-417d-92cc-0eb455910c4d' : '31235',

# vtr1br
'df59d2a1-6273-40d5-b885-1570a9f470cf' : '31092',
'9e20db30-78b0-498a-a0a0-2e507f489dea' : '31108',

# vtr2br
'e3ad5c9e-a24d-4ccc-9eee-995837056ec4' : '31091',

# mono1br
'becdcf1e-4daa-4fa8-bad0-122769da073c' : '31106',

# monost1br
'7f19d32f-0b85-49ee-baae-68e08f1b2ada' : '31238',

}

def randnum8() -> str:
    chars = random.sample(string.digits, 8)
    return ''.join(chars)


def gen_reqid() -> str:
    return '15667{}'.format(randnum8())

now = datetime.now()
timestamp = now.strftime('%Y%m%dT%H%M%SZ')
cur_year, cur_month = now.year, now.month
today = datetime(now.year, now.month, now.day)
# Start
cur_day = now.day
today_lastnum = int(str(cur_day)[-1])
# End

url_abb = "https://www.airbnb.cn/api/v2/homes_pdp_availability_calendar"
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
        resp = requests.get(url_abb, params={
            'currency': currency,
            'key': key,
            'locale': 'zh',
            'listing_id': _id,
            'year': cur_year,
            'month': cur_month,
            'count': count,
        })
        
#        print ("JSON: "+str(resp.json()))
        pdates = []
        bnbprices = []

       # month = cur_month
        
        for month in resp.json().get('calendar_months', []):
           # print ("month: "+str(month))      
            for day in month.get('days', []):
                pdate = datetime.strptime(day['date'], '%Y-%m-%d')
                bnbprice = int(day['price']['local_price_formatted'][1:])
                if pdate > today:
                    pdates.append(pdate)
                    bnbprices.append(bnbprice)

#        print ("pdates: "+str(pdates))
#        print ("bnbprices: "+str(bnbprices))

#       
       
        updates = []
        upprices = []
#       if len(bnbprices) != 0:
#       i = 1
        for i in range(1, len(bnbprices)):
                pdiff = bnbprices[i] - bnbprices[i - 1]

                if i ==1:
                    updates.append(pdates[i-1])
                    upprices.append(bnbprices[i-1])

                if pdiff != 0:
                    updates.append(pdates[i])  
                    upprices.append(bnbprices[i])
                

                if i == len(bnbprices)-1:
                    updates.append(pdates[i])
                    upprices.append(bnbprices[i])

#        print ("uprices: "+str(upprices))
#        print ("updates: "+str(updates))
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
                  print("\n")
                 # print("pri: "+str(pri))
                 # print("dates: "+str(dates))

                  url = "http://waka.tujia.com/api/v4/date_prices"
                  headers = {
                      'Content-Type': "application/json",
                      'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                      'Accept': "*/*",
                      'Cache-Control': "no-cache",
                      'Host': "waka.tujia.com",
                      'Accept-Encoding': "gzip, deflate",
                      'Connection': "keep-alive",
                      'cache-control': "no-cache"
                      }

                  wakarooms = []
                  if name == "lpn1br":
                       wakarooms = lpn1br_waka
                  elif name == "lpnsm2br":
                       wakarooms = lpnsm2br_waka
                  elif name == "lpnla2br":
                       wakarooms = lpnla2br_waka
                  elif name == "blsm1br":
                       wakarooms = blsm1br_waka
                  elif name == "blsmlo1br":
                       wakarooms = blsmlo1br_waka
                  elif name == "blsm2br":
                       wakarooms = blsm2br_waka
                  elif name == "vtr1br":
                       wakarooms = vtr1br_waka
                  elif name == "vtr2br":
                       wakarooms = vtr2br_waka
                  elif name == "mono1br":
                       wakarooms = mono1br_waka
                  elif name == "monost1br":
                       wakarooms = monost1br_waka
                  else:
                       wakarooms = lpnla2br_waka
                
                #  print ("WakaRooms: " + str(wakarooms))
                 
                #  new_price = int(int(int(pri/10)*10) - 20 + today_lastnum )
                #  can not /1.06 , can /1.05 and plus 10, 
                  new_price = int(int(int(pri/1.05/10)*10) + 10 + today_lastnum )
 
                  for ie in range(0, len(wakarooms)):
                       reqid = gen_reqid()
                       print ("reqid: "+reqid)
                       payload = {"new_price":new_price,"dates":dates,"room_uuid":wakarooms[ie]}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                       response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
                       print(response.text)
                       print("Done!\n")
                      # break
                       time.sleep(60)
                
              ### End




#12345678912345678break
                 # break
                                
        time.sleep(10)
#2345678break - Must Break Here
       # break
