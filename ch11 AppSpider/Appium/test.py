from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

server = 'http://127.0.0.1:4723/wd/hub'
desired_caps = {
	'platformName': 'Andriod',
	'deviceName': 'MI_5S',
	'appPackage': 'com.tencent.mm',
	'appActivity': '.ui.LauncherUI'
}

driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 30)
login = wait.until(ec.presence_of_element_located((By.ID, 'com.tencent.mm:id/cjk')))
login.click()
phone = wait.until(ec.presence_of_element_located((By.ID, 'com.tencent.mm:id/h2')))
phone.set_text('18378912738912')
