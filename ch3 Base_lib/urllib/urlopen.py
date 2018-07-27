from urllib.request import Request
from urllib.request import urlopen
import socket
import urllib.parse
import urllib.error

# urlopen方法
# response = urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status)  # 获取HTTP状态
# print(response.getheaders())  # 获所有取响应头文件
# print(response.getheader('Content-Type'))  # 获取指定响应头文件

# data参数
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# timeout参数
# response = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())
# 通过timeout参数处理响应异常
# try:
#     response = urlopen('http://httpbin.org/get', timeout=float(0.1))
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("time out")


