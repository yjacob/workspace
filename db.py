import sys
from bs4 import BeautifulSoup
import time
import io
import requests
import datetime
import os

url = 'https://www.douban.com/group/explore/travel'
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, "html.parser")

for i in range(2):
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    a = soup.select('.title')
    print (a)
    time.sleep(3)





#
out = 'Douban Test '+str(datetime.datetime.now()
file = io.open("/usr/share/nginx/html/test/db.txt", "w", encoding='utf-8')
print(out, file=file)
f.close
#
print ('Great Job!')
