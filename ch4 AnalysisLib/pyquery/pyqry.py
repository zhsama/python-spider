from pyquery import PyQuery as pq

# with open('test.html', encoding='utf-8') as f:
#     html = f.read()

## 初始化
# 字符串初始化
# doc = pq(html)
# print(doc('a'))
# URL初始化
# doc = pq('https://github.com')
# print(doc('title'))
# 文件初始化
# doc = pq(filename='test.html')
# print(doc('p'))

## 基本css选择器
with open('test.html', encoding='utf-8') as f:
    html = f.read()
doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

## 查找节点

# 子节点
# find
# item = doc('.list')
# print(item)
# # print(type(item))
# lis = item.find('li')
# # print(type(lis))
# print(lis)
# children
# lst = item.children()
# print(lst)
# print(type(lst))
# item = doc('.list')
# print(item.children('.active'))

# 父节点
# parent
# items = doc('.list')
# print(type(items.parent()))
# print(items.parent())
# items = doc('.list')
# print(items.parents())
# print(items.parents('.test'))

# 兄弟节点
# items = doc('.list .item-0.active')
# print(items.siblings())
# print(items.siblings('.active'))

# # 遍历
# lst = doc('li').items()
# print(type(lst))
# for li in lst:
#     print(li)

# # 获取信息
# 获取属性
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)
# for item in a.items():
#     print(item.attr.href)
# 获取文本
# a = doc('.item-0.active a')
# print(a.text())
# print(a.html())
# print(type(a.text()))

# # 节点操作
# add_class&remove_class
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)
# attr&text&html
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'attr')
# print(li)
# li.text('change text')
# print(li)
# li.html('<p>change html</p>')
# print(li)
# remove
# li = doc('.item-1')
# print(li)
# print(li.text())
# li.find('id').remove()
# print(li.text())

# # 伪类选择器
# li = doc('li:first-child')
# print(li)
# li = doc('li:last-child')
# print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:contains(second)')
# print(li)
