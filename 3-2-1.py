
import requests


s = requests.session()


# url = 'http://httpbin.org/get'
# headers = {'user-agent':'myPythonApp_1.0.0'}



# print(r.text)

s.close()

with requests.Session() as s:
    r = s.get('http://www.naver.com')
    print(r.text)

