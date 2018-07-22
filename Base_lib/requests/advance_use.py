import logging
import requests
import urllib3

# 文件上传
# files = {
#     'file': open('favicon.ico', 'rb')
# }
# r = requests.post('https://httpbin.org/post', files=files)
# print(r.text)

# cookies
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,val in r.cookies.items():
#     print(key,val)

# __DAYU_PP=iyBIZeuvmzI2VQmQvZvn2d23b7cb8b93; _zap=474829c0-aa81-43a3-97bd-c94a02c8c634; __utma=51854390.1171665045.1525114953.1525114953.1525114953.1; __utmz=51854390.1525114953.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/274062916; __utmv=51854390.100-1|2=registration_date=20160613=1^3=entry_date=20160613=1; d_c0="ACCg6vZJiQ2PTs0h3JyW8V0M0j8rX4twslw=|1525331603"; q_c1=c3891c1f5874412bac9f34f2a77a0efe|1529561129000|1521464585000; _xsrf=7f9624de-5051-4a60-8a8e-1e161694fdbe; tgw_l7_route=156dfd931a77f9586c0da07030f2df36
# Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080

# headers = {
#     'host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080 ',
# 'Cookies': '__DAYU_PP=iyBIZeuvmzI2VQmQvZvn2d23b7cb8b93; '
#            '_zap=474829c0-aa81-43a3-97bd-c94a02c8c634; '
#            '__utma=51854390.1171665045.1525114953.1525114953.1525114953.1; '
#            '__utmz=51854390.1525114953.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/274062916; '
#            '__utmv=51854390.100-1|2=registration_date=20160613=1^3=entry_date=20160613=1; '
#            'd_c0="ACCg6vZJiQ2PTs0h3JyW8V0M0j8rX4twslw=|1525331603"; '
#            'q_c1=c3891c1f5874412bac9f34f2a77a0efe|1529561129000|1521464585000; '
#            '_xsrf=7f9624de-5051-4a60-8a8e-1e161694fdbe; '
#            'tgw_l7_route=156dfd931a77f9586c0da07030f2df36'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# cookies = '__DAYU_PP=iyBIZeuvmzI2VQmQvZvn2d23b7cb8b93; _zap=474829c0-aa81-43a3-97bd-c94a02c8c634; __utma=51854390.1171665045.1525114953.1525114953.1525114953.1; __utmz=51854390.1525114953.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/274062916; __utmv=51854390.100-1|2=registration_date=20160613=1^3=entry_date=20160613=1; d_c0="ACCg6vZJiQ2PTs0h3JyW8V0M0j8rX4twslw=|1525331603"; q_c1=c3891c1f5874412bac9f34f2a77a0efe|1529561129000|1521464585000; _xsrf=7f9624de-5051-4a60-8a8e-1e161694fdbe; tgw_l7_route=156dfd931a77f9586c0da07030f2df36'
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookies.split(';'):
#     key, val = cookie.split('=', 1)
#     jar.set(key, val)
# r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
# # print(r.text)
# for key, val in r.cookies.items():
#     print(key + val)

# 会话维持
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# ssl证书验证
# urllib3.disable_warnings()  # 忽略警告
# response = requests.get('https://www.zhsama.me:8888/login', verify=False)
# print(response.status_code)
# 捕获日志方式忽略警告
# logging.captureWarnings(True)
# response = requests.get('https://www.zhsama.me:8888/login', verify=False)
# print(response.status_code)

# 代理设置
# proxies = {
#     'http': 'http://8.8.8.8:8888',
#     'https': 'https://8.8.8.8:8888'
# }
# response = requests.get('https://www.baidu.com', proxies=proxies)

# 超时设置
# response = requests.get('http://www.baidu.com',timeout=(0.01,0.002))

# 身份认证
