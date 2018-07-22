import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchFrameException

# 初始化浏览器对象
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(ec.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# 访问页面
# browser.get('https://www.douban.com')
# print(browser.page_source)
# browser.close()

# 查找节点
# 单个节点
# browser.get('https://www.douban.com')
# input_first = browser.find_element_by_id('key')
# input_second = browser.find_element_by_class_name('text')
# input_third = browser.find_element_by_xpath('//*[@id="key"]')
# print(input_first, input_second, input_third)
# input_first = browser.find_element(By.NAME, 'q')
# input_second = browser.find_element(By.CLASS_NAME, 'key')
# print(input_first)
# browser.close()
# 多个节点
# browser.get('https://www.jd.com')
# lst = browser.find_elements_by_css_selector('.cate_menu_lk')
# print(lst)
# browser.close()
# lst = browser.find_elements(By.CSS_SELECTOR, '.cate_menu_lk')
# print(lst)
# browser.close()

# 节点交互
# browser.get('https://book.douban.com/')
# input = browser.find_element(By.NAME, 'search_text')
# input.send_keys('python')
# button = browser.find_element(By.CLASS_NAME, 'inp-btn')
# button.click()

# 动作链
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 模拟js
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 获取节点信息
# 获取属性
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# 获取文本值
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# inputs = browser.find_elements_by_class_name('question_link')
# for input in inputs:
#     print(input.text)
# 获取id 位置 标签名和大小
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-search-button')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# 切换frame
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to_frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchFrameException:
#     print('no logo')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 延时等待
# 隐式等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('euwioqueiowq')
# print(input)
# 显示等待
# browser = webdriver.Chrome()
# browser.get('https://www.jd.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(ec.presence_of_element_located((By.ID, 'q')))
# button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 前进后退
# browser = webdriver.Chrome()
# browser.get('https://www.jd.com')
# browser.get('https://www.douban.com')
# browser.get('https://www.baidu.com')
# browser.back()
# time.sleep(2)
# browser.forward()

# cookies
# browser = webdriver.Chrome()
# url = 'https://www.baidu.com'
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# time.sleep(2)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')
