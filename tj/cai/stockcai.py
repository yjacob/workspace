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

# Cai Login Info 
user_id = "eaf62f6f-723b-463d-9b37-894af3c8b93e"
login_string = "ec3725d62db4dcae59af09a02163056cc8f3a92a"

# Cai waka sku id

lpn1br_waka = ["ee88733d-540b-4d41-8e1f-6053ed37687a"]
lpnsm2br_waka = ["c1962626-a323-49e8-b111-49f549e76dc3","52816f8c-000a-49db-aa6d-8ff9b86e044f"]
lpnla2br_waka = ["50e699af-78ba-4ec6-8d0c-7152099404d2"]
blsm1br_waka = ["7674daf0-f7ce-4f0a-b09c-a30ee7b019f8","5d45d1fa-7162-4ee0-9d7b-796f8d99e8d8"]
blsmlo1br_waka = ["e80b763d-000a-4643-82c0-da591a8ce552"]
blsm2br_waka = ["cf38c7d0-f44b-440c-aae7-ebf5ba60cb87"]
vtr1br_waka = ["9df0b35a-ca25-4b91-9ecd-53723d354050"]
vtr2br_waka = ["d2f03471-b9a9-41b6-b5d1-ebba5dc487bb"]
mono1br_waka = ["fcfac85c-cf80-41b3-8464-07b1b532516a"]
monost1br_waka = ["b6ffeba9-2554-4831-9221-dec5ea041128"]


# Cai ical id url

ical_id_url = '31229'

icals = {

# lpn1br
'ee88733d-540b-4d41-8e1f-6053ed37687a' : '31230',

# lpnsm2br
'c1962626-a323-49e8-b111-49f549e76dc3' : '31229',
'52816f8c-000a-49db-aa6d-8ff9b86e044f' : '31522',

# lpnla2br
'50e699af-78ba-4ec6-8d0c-7152099404d2' : '31231',

# blsm1br
'7674daf0-f7ce-4f0a-b09c-a30ee7b019f8' : '31185',
'5d45d1fa-7162-4ee0-9d7b-796f8d99e8d8' : '31121',

# blsmlo1br
'e80b763d-000a-4643-82c0-da591a8ce552' : '31517',

# blsm2br
'cf38c7d0-f44b-440c-aae7-ebf5ba60cb87' : '31184',

# vtr1br
'9df0b35a-ca25-4b91-9ecd-53723d354050' : '31524',

# vtr2br
'd2f03471-b9a9-41b6-b5d1-ebba5dc487bb' : '31118',

# mono1br
'fcfac85c-cf80-41b3-8464-07b1b532516a' : '31122',

# monost1br
'b6ffeba9-2554-4831-9221-dec5ea041128' : '31178',

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
                       time.sleep(79)
                
              ### End

#00000000002345678break - Must Break Here
                 # break
