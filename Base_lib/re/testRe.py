import re

# match
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.span())
# print(result.group())
# 匹配目标
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group(1))
# print(result.group())
# print(result.span())
# 通用匹配
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$',content)
# print(result.span())
# print(result.group())
# print(result)
# 贪婪与费贪婪
# content = 'Hello 1234567 World_This is a Regex Demo'
# result1 = re.match('^Hello.*(\d+).*World', content)  # 贪婪
# result2 = re.match('^Hello.*?(\d+).*World', content)  # 非贪婪
# print(result1.group(1))
# print(result2.group(1))
# 修饰符
# content = 'Hello 1234567 World_This \
#              is a Regex Demo'
# result = re.match('^Hello.*?(\d+).*World', content, re.S)
# print(result.group(1))

# search
# content = 'Extra string Hello 1234567 World_This is a Regex Demo'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result.group())
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# print(html)
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
# if result:
#     print(result.group(1), result.group(2))

# findall
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result)
# print(type(result))
# for results in result:
#     print(results)
#     print(results[0], results[1], results[2])

# sub
# content = "54dfsdfsd64sdasdas74dfsdfsd8fa2"
# result = re.sub('\d+', ' ', content)
# print(result)

# compile
content1 = '2018-07-18 12:00'
content2 = '2018-07-22 12:00'
content3 = '2018-07-14 12:00'
pattern = re.compile('\d{2}:\d{2}')
res1 = re.sub(pattern, '', content1)
res2 = re.sub(pattern, '', content2)
res3 = re.sub(pattern, '', content3)
print(res1)
print(res2)
print(res3)
