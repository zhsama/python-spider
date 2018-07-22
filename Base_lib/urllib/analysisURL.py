from urllib import parse, request

# urlparse
# result = parse.urlparse('http://www.baidu.com/index.html;ueser?id=5#comment')
# print(result, type(result))
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='ueser', query='id=5', fragment='comment')
# scheme参数
# result = parse.urlparse('www.baidu.com/index.html;ueser?id=5#comment', scheme='https')
# print(result, type(result))
# ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='ueser', query='id=5', fragment='comment')
# allow_fragments参数
# result = parse.urlparse('http://www.baidu.com/index.html;ueser?id=5#comment', allow_fragments=False)
# print(result, type(result))
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='ueser', query='id=5#comment', fragment='') fragment被聚合到query里
# ParseResult结果元组
# result = parse.urlparse('http://www.baidu.com/index.html;ueser?id=5#comment')
# print(result.scheme, result[0])

# urlunparse
# url = ['http', 'www.baidu.com', 'index.html', 'user', 'id=1', 'comment']
# response = request.urlopen(parse.urlunparse(url))
# print(response.read())

# urlsplit
# result = parse.urlsplit('http://www.baidu.com/index.html;ueser?id=5#comment')
# print(result, type(result))
# # 返回SplitResult元组
# print(result.scheme)

# urlunsplit
# url = ['http', 'www.baidu.com', 'index.html', 'user?id=1', 'comment']
# response = request.urlopen(parse.urlunsplit(url))
# print(response.read())

# urljion
# print(parse.urljion('https://www.baidu.com', 'fqa.html'))

# urlencode
# params = {
#     'name': 'zhsama',
#     'age': 20
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + parse.urlencode(params)
# print(url)
# http://www.baidu.com?name=zhsama&age=20

# parse_qs
# query = 'name=zhsama&age=20'
# print(parse.parse_qs(query))
# {'name': ['zhsama'], 'age': ['20']}

# parse_qsl
# query = 'name=zhsama&age=20'
# print(parse.parse_qsl(query))
# [('name', 'zhsama'), ('age', '20')]

# quote
# keyword = '谷歌'
# url = 'https://www.baidu.com/s?word=' + parse.quote(keyword)
# print(url)
# https://www.baidu.com/s?word=%E8%B0%B7%E6%AD%8C

# unquote
# url = 'https://www.baidu.com/s?word=%E8%B0%B7%E6%AD%8C'
# print(parse.unquote(url))
# https://www.baidu.com/s?word=谷歌
