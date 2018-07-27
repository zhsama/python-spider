import time

import pymongo
from pyquery.pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote

# selenium config
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
key_word = '手撕面包'

# mongo config
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'shousimianbao'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

#
TOTAL_PAGE = 100


def get_page(page):
    print("正在爬取第", page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(key_word)
        browser.get(url)
        if page > 1:
            input = wait.until(
                ec.presence_of_element_located(
                    (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(ec.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page)))
        get_product()
    except TimeoutException:
        get_page(page)


def get_product():
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(product):
    try:
        if collection.insert(product):
            print('存入MongoDB成功')
    except Exception:
        print('存入MongoDB失败')


def main():
    for i in range(1, TOTAL_PAGE + 1):
        get_page(i)
        time.sleep(3)
    browser.close()


if __name__ == '__main__':
    main()
