from urllib import robotparser, error

# rp = robotparser.RobotFileParser('https://www.jianshu.com/robot.txt')
# rp = robotparser.RobotFileParser()  # 创建RobotFileParser对象
# rp.set_url('https://www.jianshu.com/robot.txt')
# rp.read()
# print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&type=collections'))

# from urllib.request import urlopen
#
# rp = robotparser.RobotFileParser()
# try:
#     rp.parse(urlopen('http://www.jianshu.com/robot.txt').read().decode('utf-8').split('\n'))
# except error.HTTPError as e:
#     print(e.reason, e.code)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('time out')
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&type=collections'))
