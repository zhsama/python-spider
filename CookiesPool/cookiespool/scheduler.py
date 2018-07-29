import time
from multiprocessing import Process
from CookiesPool.cookiespool.api import app
from CookiesPool.cookiespool.config import *


class Scheduler(object):
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print("cookies正在运行")
            try:
                for website, cls in TEST_URL_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print('cookies生成进程开始')
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls + '("' + website + '")')
                    generator.run()
                    print('cookies生成完成')
                    generator.close()
                time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def api():
        print('api接口开始运行')
        app.run()

    def run(self):
        if API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()

        if GENERATOR_PROCESS:
            generator_process = Process(target=Scheduler.generate_cookie)
            generator_process.start()

        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()
