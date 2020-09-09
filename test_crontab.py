# 每间隔2小时的第18分钟，自动执行一次

import datetime
import string
import sys
import time
import os

content = datetime.datetime.now()

fi = open("/usr/share/nginx/html/test/crontab.txt", "a")

# Only Works with Python2
# print>>fi,content

# Only Works with Python3 
print(content, file=fi)

fi.close
