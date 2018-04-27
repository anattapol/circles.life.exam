# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from lib import account,login


class pageMyAccount(unittest.TestCase):

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
        cls.loginURL = 'https://shop.circles.life/login'
        cls.driver.get(cls.loginURL)
        cls.login = login.authenBox(cls.driver,cls.loginURL)
        cls.login.signin('anattapol.limopasit.testing@gmail.com','testPassword',validlogin=True)
        cls.driver.get('https://shop.circles.life/my_profile')
        cls.myAccount = account.myAccount(cls.driver,'anattapol.limopasit.testing@gmail.com')

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
       
    def test_VerifyEmail(self):
        result = self.myAccount.getEmail()
        return result['status']

if __name__ == "__main__":
    unittest.main(verbosity=2)