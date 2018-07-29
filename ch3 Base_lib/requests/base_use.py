import re

import requests

# r = requests.get('https://www.baidu.com')
# print(type(r))  # <class 'requests.models.Response'>
# print(r.status_code)  # 200
# print(type(r.text))  # <class 'str'>
# print(r.text)  # html代码
# print(r.CookiesPool)  # <Cookie BDORZ=27315 for .baidu.com/>

# json
# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json))

# params
# data = {
#     "username": 'zhcf',
#     "age": 20
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(r.text)

# 抓取网页
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=header)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
# r = requests.get('https://github.com/favicon.ico')
# # print(r.text)
# # print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# post
# data = {
#     'username':'zhcf',
#     'age':20
# }
# r = requests.post('http://httpbin.org/post',data=data)
# print(r.json())