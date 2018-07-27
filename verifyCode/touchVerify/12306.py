from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from verifyCode.touchVerify import Chaojiying
from selenium.webdriver.support import expected_conditions as ec

# 铁路账户
email = '602693793@qq.com'
password = '19980315zqssama'

# 超级鹰账户
cjy_username = 'zhcf1ess'
cjy_password = '19980315zqs'
cjy_soft_id = 896940
cjy_kind = 896940


class Crack12306():
    def __init__(self):
        self.url = "https://kyfw.12306.cn/otn/login/init"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = email
        self.password = password
        self.cjy = Chaojiying(cjy_username, cjy_password, cjy_soft_id)

    def open(self):
        """
        打开网页 输入用户名密码
        :return:
        """
        self.browser.get(self.url)
        email = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'username')))
        password = self.wait.until(ec.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_12306_button(self):
        """

        :return:
        """
