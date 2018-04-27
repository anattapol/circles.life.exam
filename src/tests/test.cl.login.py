# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from lib import login


class pageLogin(unittest.TestCase):

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
        cls.baseURL = 'https://shop.circles.life/login'
        cls.driver.get(cls.baseURL)
        cls.login = login.authenBox(cls.driver,cls.baseURL)

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_InvalidBoth_EmailPassword(self):
        result = self.login.signin('invalid@email.com','invalidPassword')
        return result['status']
    
    def test_ValidEmail_InvalidPassword(self):
        result = self.login.signin('kojiro540@gmail.com','invalidPassword')
        return result['status']
    
    def test_InvalidEmail_ValidPassword(self):
        result = self.login.signin('invalid@email.com','invalidPassword')
        return result['status']
    
    def test_NoEmail_NoPassword(self):
        result = self.login.signin(email="",password="")
        return result['status']
    
    def test_NoEmail_ValidPassword(self):
        result = self.login.signin(email="", password='invalidPassword')
        return result['status']
    
    def test_NoEmail_InvalidPassword(self):
        result = self.login.signin(email="", password='invalidPassword')
        return result['status']
    
    def test_ValidEmail_NoPassword(self):
        result = self.login.signin('kojiro540@email.com',password="")
        return result['status']
    
    def test_InvalidEmail_NoPassword(self):
        result = self.login.signin('invalid@email.com','invalidPassword')
        return result['status']

    def test_spaceOutterValidEmail_ValidPassword(self):
        result = self.login.signin('  kojiro540@gmail.com  ','testPassword',validlogin=True)
        self.login.signout()
        return result['status']
    
    def test_ValidBoth_EmailPassword(self):
        result = self.login.signin('kojiro540@gmail.com','testPassword',validlogin=True)
        self.login.signout()
        return result['status']

if __name__ == "__main__":
    unittest.main(verbosity=2)