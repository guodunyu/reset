
from appium import webdriver


class Testcase():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()


    def teardown(self):
        self.driver.quit()
