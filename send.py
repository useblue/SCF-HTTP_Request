# -*- coding: utf8 -*-
import requests
from meg import payload

url = " "

headers = {
  'Host': '  ',
  'Connection': '  ',
  'Content-Length': '  ',
  'Cookie': '  ',
  'User-Agent': '  ',
  'X-Tag': '  ',
  'content-type': '  ',
  'Referer': '  ',
  'Accept-Encoding': '  '
}

response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

print(response.text)
