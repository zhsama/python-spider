import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import pymongo

# request url：https://m.weibo.cn/api/container/getIndex?containerid=1005053275235775

base_url = "https://m.weibo.cn/api/container/getIndex?"
headers = {
    'host': 'm.weibo.cn',
    "Referer": 'https://m.weibo.cn/u/3275235775',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# 获取页面方法
def get_page(page):
    # 构造参数 params
    params = {
        'type': 'uid',
        'value': '3275235775',
        'containerid': '1076033275235775',
        'page': page
    }
    url = base_url + urlencode(params)  # urlencode把参数构造成url的请求参数
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # 将获取内容转化为json格式
    except requests.ConnectionError as e:
        print(e.args)


# 解析方法
def parse_page(json):
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        weibo = {}
        weibo['id'] = item.get('id')
        weibo['text'] = pq(item.get('text')).text()
        weibo['attitudes'] = item.get('attitudes_count')
        weibo['comments'] = item.get('comments_count')
        weibo['reposts'] = item.get('reposts_count')
        yield weibo


client = pymongo.MongoClient(host='localhost', port=27017)
weibo = client.weibo
weibo = weibo.weibo


# 写入MongoDB
def save_to_mongo(result):
    if weibo.insert(result):
        print('success')


if __name__ == '__main__':
    for page in range(1, 10):
        json = get_page(page)
        # print(json)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(results)
