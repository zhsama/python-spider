from lxml import etree

# HTML
# text = '''
#     <div>
#     <ul>
#     <li class="item-0"><a href="link1.html">first
#     </ul>
#     </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# parse
# html = etree.parse('test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# 所有节点
# html = etree.parse('test.html', etree.HTMLParser())
# result1 = html.xpath('//*')
# result2 = html.xpath('//li')
# print(result1)
# print(result2)

# 子节点
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

# 父节点
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="/2.mp3"]/parent::*/@data-view')
# print(result)

# 属性匹配
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="/2.mp3"]/parent::*/@data-view')
# print(result)

# 文本获取
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li[@data-view="5"]/a/text()')
# print(result)

# 属性获取
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

# 属性多值匹配
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li[contains(@class, "test")]/a/text()')
# print(result)

# 多属性匹配
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li[contains(@class, "test") and @data-view="4"]/a/text()')
# print(result)

#