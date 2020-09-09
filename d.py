import sys
from bs4 import BeautifulSoup
import time
import io
import requests
import datetime
import os

url = 'https://www.douban.com/group/topic/147631093/'
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, "html.parser")

#print (soup)
#
#for i in range(2):

resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, "html.parser")

contents = soup.text

print (contents)

#for a in contents:
#    if a["href"] 
#	if 'topic' in str(a["href"]) = True:
#		print(a["href"])
#	links = str(a["href"])
#	group = links.find('group')
#	topic = links.find('topic')
#	if (group > 0) and (topic > 0):
#		start = topic+6
#		end = len(links)-1
#		print (links[start:end])

		


#a = soup.select('.title')
#print (tables)

#    time.sleep(3)
#
#out = 'Douban Test '+str(datetime.datetime.now()
#file = io.open("/usr/share/nginx/html/test/db.txt", "w", encoding='utf-8')
#print(out, file=file)
#f.close
#
#print ('Great Job!')
