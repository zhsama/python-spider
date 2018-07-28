import redis
from random import choice
from Proxypool.proxypool.error import PoolEmptyError

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host:redis地址
        :param port: redis端口
        :param password: redis密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理
        :param proxy:代理
        :param score: 分数
        :return: 添加结果
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd((REDIS_KEY, score, proxy))

    def random(self):
        """
        随机获取有效代理 尝试获取分数最高代理 然后尝试排名获取 否则异常
        :return: 随即接过
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理失效 扣1分 分数低于0 移除代理
        :param proxy: 代理链接
        :return: 修改后代理分数
        """
        scroe = self.db.zscore(REDIS_KEY, proxy)
        if scroe and scroe > MIN_SCORE:
            print("代理", proxy, '当前分数', scroe, '减一')
            return self.db.zincrby(REDIS_KEY, proxy)
        else:
            print("代理", proxy, '当前分数', scroe, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exist(self, proxy):
        """
        判断代理是否存在
        :param proxy:代理
        :return:是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为最高分
        :param proxy: 代理
        :return: 设置结束
        """
        print("代理", proxy, '可用，设置为', MAX_SCORE, '移除')
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        计算代理数量
        :return: 代理数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)

if __name__ == '__main__':
    conn = RedisClient()
    result = conn.batch(680, 688)
    print(result)
