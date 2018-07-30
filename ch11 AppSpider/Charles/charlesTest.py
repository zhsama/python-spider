import requests
from selenium import webdriver

url = 'https://www.baidu.com'
browser = webdriver.Chrome()

browser.get(url=url)