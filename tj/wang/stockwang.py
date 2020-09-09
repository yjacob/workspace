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


# Wang Hui Login Info

user_id = "e7bfb49a-6046-4967-be45-a2326c7cd601"
login_string = "55632115a47cf9ab82a898977eead3fd38c50bed"

# Wang Hui waka sku id

lpn1br_waka = ["35c5808b-66ad-488f-a956-6d115bc1b527"]
lpnsm2br_waka = ["033cb718-740f-438b-aaae-52c9c6c7b3ef"]
lpnla2br_waka = ["387d9bbd-25f5-4de7-a9f5-d9a526067c46"]
blsm1br_waka = ["809d619c-8172-47b9-9ff6-f66102aa1539"]
blsmlo1br_waka = ["697cf17e-5204-4645-8f92-52d04aed15ae"]
blsm2br_waka = ["8b412623-29ad-4858-a1d2-7a9c60b7b079"]
vtr1br_waka = ["43aa5c85-2f7c-4f11-bd58-775975a33bc9"]
vtr2br_waka = ["20f85f21-0f20-4c2b-b107-e0e0d1987431"]
mono1br_waka = ["67ac9b43-11a1-433e-9533-960a159d2a80"]
monost1br_waka = ["c801243b-9ec7-4990-be63-19a787237302"]


# Wang Hui ical id url

ical_id_url = '30984'

icals = {

# lpn1br
'35c5808b-66ad-488f-a956-6d115bc1b527' : '30987',

# lpnsm2br
'033cb718-740f-438b-aaae-52c9c6c7b3ef' : '30984',

# lpnla2br
'387d9bbd-25f5-4de7-a9f5-d9a526067c46' : '30988',

# blsm1br
'809d619c-8172-47b9-9ff6-f66102aa1539' : '31095',

# blsmlo1br
'697cf17e-5204-4645-8f92-52d04aed15ae' : '31094',

# blsm2br
'8b412623-29ad-4858-a1d2-7a9c60b7b079' : '31096',

# vtr1br
'43aa5c85-2f7c-4f11-bd58-775975a33bc9' : '31089',

# vtr2br
'20f85f21-0f20-4c2b-b107-e0e0d1987431' : '31090',

# mono1br
'67ac9b43-11a1-433e-9533-960a159d2a80' : '31180',

# monost1br
'c801243b-9ec7-4990-be63-19a787237302' : '31179',

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

#url_abb = "https://www.airbnb.cn/api/v2/homes_pdp_availability_calendar"
#currency = 'THB'
#key = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'
#count = 3

nginx_path = "/usr/share/nginx/html/waka"
#New coding by  Jacob -  Start
available_path = "/usr/share/nginx/html/available"
myprice_path = "/usr/share/nginx/html/jrate"
agent_path = "/usr/share/nginx/html/agent"
#End

#endday = datetime(now.year, now.month+2%12, 28)
endday = datetime(2020, 2, 29)
sdate = today + timedelta(days=1)   # start date
edate = endday  # end date
delta = edate - sdate + timedelta(days=1)
dates = []

for ic in range(delta.days):
    day = sdate + timedelta(days=ic)
    day2 = day.strftime("%Y-%m-%d")
    dates.append(day2)

#print("\n") 
#print("dates: "+str(dates))
#print("\n")



if __name__ == '__main__':
    for name, _id in rooms.items():

   
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
                  cfmtype = 1
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
                       cfmtype = 0
                       wakarooms = mono1br_waka
                  elif name == "monost1br":
                       cfmtype = 0
                       wakarooms = monost1br_waka
                  else:
                       wakarooms = lpnla2br_waka
                
                #  print ("WakaRooms: " + str(wakarooms))
                 
                  for ie in range(0, len(wakarooms)):
                       url_stock = "http://waka.tujia.com/api/v5/sku_stocks"
                       reqid = gen_reqid()
                       print ("reqid_stockset: "+reqid)
                     # payload = {"new_price":new_price,"dates":dates,"room_uuid":wakarooms[ie]}
                       payload = {"new_stock":1,"room_uuid":wakarooms[ie],"confirm_type":cfmtype,"dates":dates}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                       response = requests.request("POST", url_stock, json=payload, headers=headers, params=querystring)
                       print(response.text[:150])
                       print("Stock Set Done!\n")
                       time.sleep(5)
                       
                       for sku_id, ical_id in icals.items():
                                 if sku_id == wakarooms[ie]:
                                           ical_id_url = ical_id
         
                     # Smart Me

                       url_ical = "http://waka.tujia.com/api/v3/calendars/"+wakarooms[ie]+"/icals/"+ical_id_url
                       payload_ical = "{}"
                       reqid_ical = gen_reqid()
                       print ("reqid_ical: "+reqid_ical)
                       print ("url_ical: "+url_ical[7:])
                       querystring_ical = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid_ical,"user_id":user_id,"login_string":login_string}
                       response_ical = requests.request("POST", url_ical, json=payload_ical, headers=headers, params=querystring_ical)
                       print(response_ical.text)
                       print("iCal Sync Done!" + str(now) +"\n")
                    #   break
                       time.sleep(71)
                
              ### End

#00000000002345678break - Must Break Here
                 # break
