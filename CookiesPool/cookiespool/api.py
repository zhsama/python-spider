from flask import Flask, g
from CookiesPool.cookiespool.config import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'CookiesPool pool'


def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('RedisClient' + '("CookiesPool","' + website + '")'))
        return g


@app.route('/<website>/random')
def random(website):
    """
    随机获取cookies
    :param website:查询网站给 如：weibo
    :return:随机获取的cookies
    """
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies
