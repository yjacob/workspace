import os
from math import ceil
import time
import random
import string
from datetime import datetime, timedelta

import requests


rooms = {
    # 1st One Before Break
    #

    # Mono
    'mono1br': '36898405',
   # 'monost1br': '36901129',

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
nowhour = now.hour

print (nowhour)


url = "https://www.airbnb.cn/api/v2/homes_pdp_availability_calendar"
currency = 'THB'
key = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'
count = 3

nginx_path = "/usr/share/nginx/html/waka"
#New coding by  Jacob -  Start
available_path = "/usr/share/nginx/html/available"
myprice_path = "/usr/share/nginx/html/jrate"
agent_path = "/usr/share/nginx/html/agent"

backup_path = "/usr/share/nginx/html/agentlog"
namelogdate = str(now.year)+str(now.month).zfill(2)+str(now.day).zfill(2)

jratelog_path = "/usr/share/nginx/html/jratelog"

#End

#
cur_month_2 = cur_month-1
count_2 = count+1
cur_day = now.day
cur_day_2 = cur_day+7
#print (cur_day_2)
#

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
        print("-----")
        print (resp)
        print (resp.json())
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
                       # timestamp=timestamp,
                        timestamp=datetime.now().strftime('%Y%m%dT%H%M%SZ'),
                        uid=gen_uid(),
                        start=start.strftime('%Y%m%d'),
                        end=(start + timedelta(days=ndays)).strftime('%Y%m%d')
                    )
                    units.append(unit)
                    start, ndays = dates[i], 1
            unit = fmt_unit.format(
              # timestamp=timestamp,
                timestamp=datetime.now().strftime('%Y%m%dT%H%M%SZ'),
                uid=gen_uid(),
                start=start.strftime('%Y%m%d'),
                end=(start + timedelta(days=ndays)).strftime('%Y%m%d')
            )
            units.append(unit)

        doc = fmt_ics.format(''.join(units)).strip()
        fpath = os.path.join(nginx_path, f"{name}.txt")
        with open(fpath, 'w') as fs:
            fs.write(doc)
        print(name+".txt waka generated")
        time.sleep(3)
###New coding by Jacob - Start

        fpath2 = os.path.join(available_path, f"{name}.txt")
        with open(fpath2, 'w') as fs:
            fs.write(doc)
        print(name+".txt available generated")
        time.sleep(3)

        foragents = ''
        formyselfs = ''
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        newline12 = ''
        newline34 = ''
        #for month in resp.json().get('calendar_months', []):
        pmonths =  resp.json().get('calendar_months', [])
        for month in pmonths:
            pdays = month['days']
            for day in pdays:
                    airbnbprice = int(day['price']['local_price_formatted'][1:])
                    p2 = p1
                    mycontractprice = ceil(airbnbprice/1.10)                    
                    p1 = mycontractprice
                    if p1 != p2:
                       newline12 = '\n'
                    else:
                       newline12 = ''
                    p4 = p3
                    
                    # int(1,5,12) means +2 = 3days,7days,14days.
                    # int(2,8,18) means +2 = 4days,10days,20days.

                    if int((date - today).days) <= int(2):
                      #agentprice = int(mycontractprice/1/10)*10+10
                       agentprice = int(mycontractprice/1/10)*10+10

                    elif int((date - today).days) <= int(8):
                      #agentprice = int(mycontractprice/1/10)*10+10
                       agentprice = int(mycontractprice/0.98/10)*10+10

                    elif int((date - today).days) <= int(18):
                      #agentprice = int(mycontractprice/1/10)*10+10
                       agentprice = int(mycontractprice/0.96/10)*10+10

                    else:
                      #agentprice = int(mycontractprice/0.94/10)*10+10
                       agentprice = int(mycontractprice/0.94/10)*10+10

                    p3 = agentprice
                    if p3 != p4:
                       if date > today:
                          newline34 = '\n'
                    else:
                       newline34 = ''
                    recommendedprice = int(agentprice/0.92/10)*10+10
                    agentprofit = int((recommendedprice*0.97-agentprice)/4.2742999965538)
                    my2ndsaleprice = int(airbnbprice/0.9)
                    avlb = str(day['available'])[0:1]
                    foragent = newline34+avlb+"_AP:"+str(agentprice).zfill(4)+"__"+str(day['date'])[2:]+"__RP:"+str(recommendedprice).zfill(4)+"__RMB:"+str(agentprofit)
                    foragents = foragents + foragent + "\n"
                    date = datetime.strptime(day['date'], '%Y-%m-%d')
                    if date < today:
                       foragents = '\n'
                    date = datetime.strptime(day['date'], '%Y-%m-%d')
                    todayline = ''
                    if date == today:
                       todayline = '\n||||||||||||||||||||||||||||||\n\n'
                    formyself = todayline+newline12+avlb+"_CTP:"+str(mycontractprice).zfill(4)+"__ABB:"+str(airbnbprice).zfill(4)+"__"+str(day['date'])[2:]+"___"+str(my2ndsaleprice).zfill(4)
                    formyselfs = formyselfs + formyself + "\n"
           #formyselfs = formyselfs+'\n'
        foragents = name+'\nGenerated on '+now.strftime('%Y-%m-%d %H:%M:%S')+'\n'+foragents
        formyselfs = name+'\nGenerated on '+now.strftime('%Y-%m-%d %H:%M:%S')+'\n'+formyselfs 
#
        agentpath = os.path.join(agent_path, f"{name}.txt")
        with open(agentpath, 'w') as fs:
           fs.write(foragents)
        print(name+"'s agent price list is ready")
        time.sleep(3)
        
        if nowhour == 2:
           backuppath = os.path.join(backup_path, f"{name}{namelogdate}.txt")
           with open(backuppath, 'w') as fs:
              fs.write(foragents)
           print(name+"'s agent price backup is ready")
           time.sleep(3)
#
        mypricepath = os.path.join(myprice_path, f"{name}.txt")
        with open(mypricepath, 'w') as fs:
           fs.write(formyselfs)
        print(name+"'s myself price list is ready")
        time.sleep(3)

        if nowhour == 2:
           jratelogpath = os.path.join(jratelog_path, f"{name}{namelogdate}.txt")
           with open(jratelogpath, 'w') as fs:
              fs.write(formyselfs)
           print(name+"'s jRate Log is ready")

###End
        time.sleep(50)
#2345678break
###        break

