import urllib
from urllib.request import Request
from urllib.request import urlopen

# Request方法
# request = Request('https://python.org')
# response = urlopen(request)
# print(response.read().decode('utf-8'))

# 参数
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'zhcf'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
req = Request(url=url, data=data, headers=headers, method='POST')
response = urlopen(req)
print(response.read())
