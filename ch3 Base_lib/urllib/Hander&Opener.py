# 验证场景
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = ''
# pwd = ''
# url = 'http://localhost:80'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, pwd)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# 代理场景
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler(
#     {
#         'http': 'http://46.101.61.204:4937',
#         'https': 'https://46.101.61.204:4937'
#     }
# )
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open("https://www.baidu.com")
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# cookies
import http.cookiejar
import urllib.request

# CookieJar
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)

# MozillaCookieJar
# cookieFile = 'cookie1.txt'
# cookie = http.cookiejar.MozillaCookieJar(cookieFile)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# LWPCookieJar
# cookieFile = 'cookie2.txt'
# cookie = http.cookiejar.LWPCookieJar(cookieFile)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# load()读取cookies文件
# cookie = http.cookiejar.LWPCookieJar()
# cookie = http.cookiejar.MozillaCookieJar()
# # cookie.load('cookie2.txt', ignore_expires=True, ignore_discard=True)
# cookie.load('cookie1.txt', ignore_expires=True, ignore_discard=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))
