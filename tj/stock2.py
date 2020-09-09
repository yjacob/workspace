import requests

url = "http://waka.tujia.com/api/v5/sku_stocks"

querystring = {"locale":"zh-CN","app_id":"waka_web","request_id":"1566744823612","user_id":"194835a0-731f-4ea2-b0d0-1100ae354d2b","login_string":"5dffc19ce4c7ed2894cedebc7a5e463c8e2f50d3"}

payload = {"new_stock":1,"room_uuid":"5ad8be1c-3a69-4e6f-9561-fc110dd409e4","confirm_type":1,"dates":["2019-09-06","2019-09-07"]}
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

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
