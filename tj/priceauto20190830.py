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

    # Asoke
    # 'ask1br': '33140478',
    # 'asklo1br': '35168362',
    # 'ask2br': '31588234',
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
        
        print ("JSON: "+str(resp.json()))
        pdates = []
        bnbprices = []

       # month = cur_month
        
        for month in resp.json().get('calendar_months', []):
            print ("month: "+str(month))      
            for day in month.get('days', []):
                pdate = datetime.strptime(day['date'], '%Y-%m-%d')
                bnbprice = int(day['price']['local_price_formatted'][1:])
                if pdate > today:
                    pdates.append(pdate)
                    bnbprices.append(bnbprice)

        print ("pdates: "+str(pdates))
        print ("bnbprices: "+str(bnbprices))

#       
       
        updates = []
        upprices = []
     #  if len(bnbprices) != 0:
        i = 1
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
        print ("uprices: "+str(upprices))
        print ("updates: "+str(updates))
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
                  print("pri: "+str(pri))
                  print("dates: "+str(dates))

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
                  user_id = "194835a0-731f-4ea2-b0d0-1100ae354d2b"
                  login_string = "5dffc19ce4c7ed2894cedebc7a5e463c8e2f50d3"

              ### Start
                  lpn1br_waka = ["490395d6-6f4d-4a27-9e3f-b10689c81532","3d014680-b991-4e3a-8e50-c4e578aee131"]
                  lpnsm2br_waka = ["5ad8be1c-3a69-4e6f-9561-fc110dd409e4","1cfe903c-dcf9-48dd-8adb-a3770ba0e4a2","3a2533f7-2e6b-42ff-8663-77a83ec50b2b"]
                  lpnla2br_waka = ["05d74890-53a2-48f1-bc80-0749074184dd","ce15f1bf-f58b-415c-9901-2d4978ede4d1"]
                  blsm1br_waka = ["0d0bf1f4-15a7-462f-916d-6ee1955607cc",
                                  "e5472a6a-fbb4-4330-95cd-b91320c405a4",
                                  "ea889dce-016c-429d-b201-54c685eb89b0",
                                  "06720953-acc5-418d-b9f6-2dc64b5a39d3",
                                  "f6a9b139-c546-4115-ad1e-67f409d8562b",
                                  "6fa4360f-4f3a-4748-b35c-fffac4fd2148",
                                  "31f90050-b54b-4d66-a34f-c830e553b8ee",
                                  "a30067f3-2432-4df2-9cb0-f002c4bb169d",
                                  "46281721-1fbd-4844-b5ae-fa5e26f1635d",
                                  "613ab658-664e-4347-a2b0-35bc3b0c6c04",
                                  "91aed72c-9a15-4d66-a63f-e6eaa982329b"]
                  blsmlo1br_waka = ["e3c4fc1d-20bc-4c78-bee5-04a272e3ca2f"]
                  blsm2br_waka = ["314848c4-a812-4914-9114-6e570f29d2d5","9da55c4a-4868-492b-9aae-f26818329bfb","c7388581-3d55-4734-806f-5df7f7108d96","dec6b42d-7b45-4d1d-8468-a9a2ca870196","b1eab4fa-a6bf-45c1-ade2-489a6755751d"]
                  vtr1br_waka = ["99a74f01-a27c-466f-829c-b3effc596e8b","efbdef05-cffb-4b1f-bed8-f7bad59d9442","5b47d93f-0032-4bab-9951-6a7e8bb2d020","1baa782b-44fa-4e7b-a687-0af487ed3a07","801126c3-5086-4866-abe5-62dbed0bba84","8686411c-a059-4410-a43b-775192b285e8"]
                  vtr2br_waka = ["63310e9a-6b93-486b-80da-4a4d9d382d69","1a87a6a7-fc22-4b5a-be1d-fdbe894b226a"]
                  mono1br_waka = ["1a61e3fb-7b55-44f9-8e4c-d43b78582b42"]
                  monost1br_waka = ["d4c3a5a4-3686-48a4-a00e-c0e8f2662254"]

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
                
                  print ("WakaRooms: " + str(wakarooms))
                 
                  new_price = int(int(pri/10)*10)+1
                 
                  for ie in range(0, len(wakarooms)):
                       reqid = gen_reqid()
                       print ("reqid: "+reqid)
                       payload = {"new_price":new_price,"dates":dates,"room_uuid":wakarooms[ie]}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                       response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
                       print(response.text)
                       print("Done!")
                      # break
                       time.sleep(70)
                
              ### End




#12345678912345678break
#      break
                                
        time.sleep(70)
#2345678break - Must Break Here
#     break
