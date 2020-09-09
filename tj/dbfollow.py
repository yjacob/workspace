import requests

url = "https://www.douban.com/j/contact/addcontact"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"people\"\r\n\r\n43986760\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ck\"\r\n\r\nVVDD\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Cookie': "bid=9joY5ma_uW8; ll="108296"; __utmz=30149280.1566377496.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=uhV80R7yFV632Cnz05UWi6qBTKzGUhyM; push_noty_num=0; push_doumail_num=0; douban-fav-remind=1; ct=y; douban-profile-remind=1; __utmv=30149280.164; __gads=ID=329f567e13fd54d8:T=1566508842:S=ALNI_MazJw2clntxK50uGHsx5AVV4jXBvA; _pk_ses.100001.8cb4=*; __utma=30149280.161253520.1566377496.1566508814.1566761952.5; __utmc=30149280; ap_v=0,6.0; dbcl2="1647809:/MMuJraNUvs"; ck=VVDD; __utmt=1; _pk_id.100001.8cb4=b99715a0baedf9f6.1566377491.5.1566762711.1566509655.; __utmb=30149280.109.5.1566762727489,bid=Z5n3drcosSg",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f3113ffe-07b0-4768-9645-13340ee79c98,10610f87-782f-4cfb-a3c6-dbc8f15a47da",
    'Host': "www.douban.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "multipart/form-data; boundary=--------------------------862851115002528082063546",
    'Content-Length': "274",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
