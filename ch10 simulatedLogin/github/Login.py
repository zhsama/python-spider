import requests
from lxml import etree


class Login():
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        """
        获取登录后的session和authenticity_token
        :return: authenticity_token
        """
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        return token

    def dynamics(self, html):
        """
        获取follower的news
        :param html:登录后的页面源码
        :return:
        """
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class,"news")]//div[contains(@class,"alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        """
        输出个人信息
        :param html: 获取到的页面源码
        :return:
        """
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)

    def login(self, email, password):
        """
        模拟登陆过程
        :param email: 用户名
        :param password: 密码
        :return:输出个人信息
        """
        post_data = {
            'commit': 'Sign in',
            'utf-8': '√',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        # response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        # if response.status_code == 200:
        #     self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            # self.profile(response.text)
            print(response.text)


if __name__ == "__main__":
    login = Login()
    login.login(email='939020488@qq.com', password='19980315zqs')
