import re
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

# 初始化对象
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)

# 节点选择器
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(soup.title.string)
# print(type(soup.title))
# print(soup.p)
# print(soup.head)
# 提取信息
# print(soup.title.attrs)  # 获取属性
# print(soup.title.name)  # 获取节点名
# print(soup.title.string)  # 获取节点内容

# 嵌套选择
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

# 关联选择
# with open('test.html', encoding='utf-8') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'lxml')
#  选取子节点
# print(soup.p.contents)  # 获取直接子节点
# print(soup.p.children)  # 获取子节点 返回生成器对象
# for i, item in enumerate(soup.p.children):
#     print(i, item)
# print(soup.p.descendants)  # 获取所有子孙节点 返回生成器对象
# for i, item in enumerate(soup.p.descendants):
#     print(i, item)
# 选取父节点
# print(soup.a.parent)  # 选取直接父节点
# print(soup.a.parents)  # 选取所有祖先节点
# for i, item in enumerate(soup.a.parents):
#     print(i, item)
# 兄弟节点
# print(soup.a.next_sibling)
# print(soup.a.previous_sibling)
# print(list(enumerate(soup.a.next_siblings)))
# print(list(enumerate(soup.a.previous_siblings)))

# 方法选择器
# name
# print(soup.find_all(name='p'))
# print(type(soup.find_all(name='p')))
# for p in soup.find_all(name='p'):  # 嵌套查找
#     print(p.find_all(name='a'))
# attrs
# print(soup.find_all(attrs={'class': 'sister'}))
# text
# print(soup.find_all(text=re.compile('.*?i')))

# CSS选择器
# print(soup.select('.sister'))
# print(soup.select('p a'))
# 嵌套选择
# for item in soup.select('p'):
#     print(item.select('a'))
# 获取属性
# for p in soup.select('p'):
#     print(p['class'])
#     print(p.attrs['class'])
# 获取文本
# for p in soup.select('p'):
#     print(p.string)
#     print(p.get_text)

