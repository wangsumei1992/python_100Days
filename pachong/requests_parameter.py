import requests

r = requests.get("http://www.baidu.com")
c = r.headers
m = r.headers['Content-Type']
print(m)