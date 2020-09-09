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

endday = datetime(now.year, now.month+2%12, 28)

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
                  
                  for ie in range(0, len(wakarooms)):
                       url_stock = "http://waka.tujia.com/api/v5/sku_stocks"
                       reqid = gen_reqid()
                       print ("reqid_stockset: "+reqid)
                     # payload = {"new_price":new_price,"dates":dates,"room_uuid":wakarooms[ie]}
                       payload = {"new_stock":0,"room_uuid":wakarooms[ie],"confirm_type":0,"dates":dates}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                       response = requests.request("POST", url_stock, json=payload, headers=headers, params=querystring)
                       print(response.text[:150])
                       print("Stock Set Done!\n")

                     #  time.sleep(5)
                       
                     #  for sku_id, ical_id in icals.items():
                     #            if sku_id == wakarooms[ie]:
                     #                      ical_id_url = ical_id
         
                     # Smart Me

                      # url_ical = "http://waka.tujia.com/api/v3/calendars/"+wakarooms[ie]+"/icals/"+ical_id_url
                      # payload_ical = "{}"
                      # reqid_ical = gen_reqid()
                      # print ("reqid_ical: "+reqid_ical)
                      # print ("url_ical: "+url_ical[7:])
                      # querystring_ical = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid_ical,"user_id":user_id,"login_string":login_string}
                      # response_ical = requests.request("POST", url_ical, json=payload_ical, headers=headers, params=querystring_ical)
                      # print(response_ical.text)
                      # print("iCal Sync Done!" + str(now) +"\n")
                    #   break
                       time.sleep(75)
                
              ### End

#00000000002345678break - Must Break Here
                 # break
