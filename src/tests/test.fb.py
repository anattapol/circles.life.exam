# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from lib import fb
import time


class facebook(unittest.TestCase):

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
        cls.baseURL = 'https://www.facebook.com'
        cls.driver.get(cls.baseURL)
        cls.fb = fb.facebook(cls.driver,cls.baseURL)
        cls.fb.signin('anattapol.limopasit.testing@gmail.com','testPassword')

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_postStatus(self):
        result = self.fb.postStatus('Test the posting message at ' + str(time.gmtime().tm_min))
        return result

if __name__ == "__main__":
    unittest.main(verbosity=2)