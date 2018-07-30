from appium import webdriver

server = 'http://127.0.0.1:4723/wd/hub'
desired_caps = {
	'platformName': 'Andriod',
	'deviceName': 'MI_5S',
	'appPackage': 'com.tencent.mm',
	'appActivity': '.ui.LauncherUI'
}
driver = webdriver.Remote(server, desired_caps)
el = driver.find_element_by_id('com.tencent.mm:id/cjk')
