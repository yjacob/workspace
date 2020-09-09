import requests
from pprint import pprint

url = "http://waka.tujia.com/api/v4/date_prices"

querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":"1566759904712","user_id":"194835a0-731f-4ea2-b0d0-1100ae354d2b","login_string":"5dffc19ce4c7ed2894cedebc7a5e463c8e2f50d3"}

# lpn1br : 490395d6-6f4d-4a27-9e3f-b10689c81532

payload = {"new_price":"1208","dates":["2019-09-11","2019-09-12","2019-09-13"],"room_uuid":"490395d6-6f4d-4a27-9e3f-b10689c81532"}

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

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

pprint(response.text)
print("Success")
