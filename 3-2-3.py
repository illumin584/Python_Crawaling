from bs4 import BeautifulSoup
import requests, json


s = requests.Session()
r = s.get('https://httpbin.org/stream/20')

print(r.encoding)
# print(r.json())

# r = s.get('https://httpbin.org/')
# print(r.status_code)
# print(r.ok)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in  r.iter_lines(decode_unicode=True):
    # print(line)    
    b = json.loads(line)
    print(json.loads(line))  #dict
    for e in b.keys():
        print("key", e, "values:",b[e])