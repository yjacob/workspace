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
# if the date on 28 is High season or low season price, then probably will be a problem here.
basic_date = datetime(2020, 1, 2)

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

# Find the basic price first:
        for month in resp.json().get('calendar_months', []):
            for day in month.get('days', []):
                basdate = datetime.strptime(day['date'], '%Y-%m-%d')
                basprice = int(day['price']['local_price_formatted'][1:])
                if basdate == basic_date:
                    basic_airbnb_price = basprice
                    basic_contract_price = ceil(basic_airbnb_price/1.10)
                    print (basic_date)
                    print ("Basic Contract Price: "+name+": "+str(basic_contract_price)+"\n")

# get airbnb prices and change it Lower in the next 7 days:
# it was named bnbpriceS, for now, it means the price i changed, not orgin airbnb priceS.
        pdates = []
        bnbprices = [] 
        for month in resp.json().get('calendar_months', []):
            for day in month.get('days', []):
                pdate = datetime.strptime(day['date'], '%Y-%m-%d')
                bnbprice = int(day['price']['local_price_formatted'][1:])
                if pdate > today:

# Start to Change Prices
                    if int((pdate - today).days) <= int(3):
                       bnbprice = int(int(int(int(basic_contract_price*0.7)*1.1/1.05/10)*10)+10+today_lastnum)
                    elif int((pdate - today).days) <= int(7):
                       bnbprice = int(int(int(int(basic_contract_price*0.9)*1.1/1.05/10)*10)+10+today_lastnum)
                    else:
                       bnbprice = int(int(int(int(bnbprice)/0.97/10)*10)+10+today_lastnum)

                    pdates.append(pdate)
                    bnbprices.append(bnbprice)
# pdates and bnbprices gen-ed
       
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
                 
        
 
                  for ie in range(0, len(wakarooms)):
                       reqid = gen_reqid()
                       print ("reqid: "+reqid)
                       payload = {"new_price":pri+200,"dates":dates,"room_uuid":wakarooms[ie]}
                       querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":reqid,"user_id":user_id,"login_string":login_string}
                       response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
                       print(response.text[:80])                       
                       print ("pri: "+str(pri))
                       print ("dates: "+str(dates))
                       print ("waka sku: "+str(wakarooms[ie]))
                       print("Done!\n")
                      # break
                       time.sleep(66)
                
              ### End




#12345678912345678break
                 # break
                                
        time.sleep(10)
#2345678break - Must Break Here
       # break
