import requests

# url = 'http://httpbin.org/get'
# proxy = 'py:py@127.0.0.1:8888'
# proxies = {
#     'http': 'socks5://' + proxy,
#     'https': 'socks5://' + proxy,
# }
# try:
#     response = requests.get(url, proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print(e.args)

import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9999)
socket.socket = socks.socksocket

try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(e.args)
