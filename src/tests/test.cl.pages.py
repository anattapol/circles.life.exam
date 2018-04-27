# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from lib import navbar, body, footer


class pagesCL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'Configuring web driver'
        cls.firefoxdriver_path = "src\\tests\\webdriver\\geckodriver"
        cls.firefox_binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        cls.ff_profile = webdriver.FirefoxProfile()
        cls.ff_profile.set_preference("dom.webnotifications.enabled", False) ## Disable web push notification
        cls.driver = webdriver.Firefox(executable_path=cls.firefoxdriver_path \
            , firefox_binary=cls.firefox_binary,firefox_profile=cls.ff_profile)
        cls.driver.set_window_size(1280, 960)
        cls.baseURL = 'https://pages.circles.life'
        cls.driver.get(cls.baseURL)
        cls.navbar = navbar.navbar(cls.driver,cls.baseURL)

    def setUp(self):
        self.driver.get(self.baseURL)

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_clickApplyCode(self):
    #     result = self.navbar.clickApplyCode('signup?referral=SAVENOW20')
    #     return result['status']
    
    def test_clickCirclesLifeLogo(self):
        result = self.navbar.clickCirclesLifeLogo()
        return result['status']

    def test_clickPlanOnly(self):
        result = self.navbar.clickPlanOnly()
        return result['status']

    def test_clickPlanWithPhone(self):
        result = self.navbar.clickPlanWithPhone()
        return result['status']

    def test_clickRoaming(self):
        result = self.navbar.clickRoaming()
        return result['status']

    def test_clickPorting(self):
        result = self.navbar.clickPorting()
        return result['status']

    def test_clickWhyUs(self):
        result = self.navbar.clickWhyUs()
        return result['status']

    def test_clickHelp(self):
        result = self.navbar.clickHelp()
        return result['status']

if __name__ == "__main__":
    unittest.main(verbosity=2)