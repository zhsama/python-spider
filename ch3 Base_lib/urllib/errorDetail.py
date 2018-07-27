import socket
from urllib import error, request

# URLError
# try:
#     request.urlopen('http://www.chidabianbani.com')
# except error.URLError as e:
#     print(e.reason)

# HTTPError
# try:
#     response = request.urlopen('https://www.nichidabianma.com/index.jsp')
# except error.HTTPError as e:
#     print(e.reason, e.headers, e.code)

# 先捕获子类HTTPError的异常 后捕获父类URLError的异常
# try:
#     request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.code, e.reason, e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('time out')

# e.reason返回对象
# try:
#     response = request.urlopen('https://www.baidu.com', timeout=0.01)
# except error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print("time out")
