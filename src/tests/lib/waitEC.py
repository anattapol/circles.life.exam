import time, re
from selenium.webdriver.support.ui import Select, WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import sys, os

class waitEC():

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout

    def getAttributeValue(self, elementType, elementName):
        """Retrieved attribute_value from element.
        """
        try :
            time.sleep(1)
            errmsg = "Timeout click type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, elementName)), errmsg)
            return self.driver.find_element(by=by,value=elementName).get_attribute("value")
        except :
            raise

    def getText(self, elementType, elementName):
        """Get text from element
        """
        try :
            time.sleep(1)
            errmsg = "Timeout click type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, elementName)), errmsg)
            return self.driver.find_element(by=by,value=elementName).text
        except :
            raise
    
    def getElement(self, elementType, elementName):
        """Get text from element
        """
        try :
            time.sleep(1)
            errmsg = "Timeout click type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, elementName)), errmsg)
            return self.driver.find_element(by=by,value=elementName)
        except :
            raise

    def click(self, elementType, elementName):
        """
        Wait Until and element is clickable
        """
        try :
            time.sleep(1)
            errmsg = "Timeout click type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, elementName)), errmsg)
            self.driver.find_element(by=by,value=elementName).click()
        except :
            raise

    def sendKey(self, elementType, elementName, keyword):
        """
        Wait Until an element ready then send_keys
        """
        try :
            time.sleep(1)
            errmsg = "Timeout sendKey type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by, elementName)), errmsg)
            self.driver.find_element(by, elementName).clear()
            self.driver.find_element(by, elementName).send_keys(keyword)
        except :
            raise

    def titleContains(self, titleList) :
        """
        Wait Until that all words present in title
        """
        try:
            time.sleep(1)
            errmsg = "Timeout title: " 
            for title in titleList:
                WebDriverWait(self.driver, self.timeout).until(EC.title_contains(title), str(errmsg) + str(title))
        except :
            raise

    def elementContains(self, elementType, elementName, text) :
        """
        Wait Until that text present in element
        """
        try:
            time.sleep(1)
            errmsg = "Timeout : " + text + "isn't in type: " + elementType + " : " + elementName 
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element((by, elementName), text), errmsg)
        except :
            raise

    def select(self, elementType, elementName, text):
        """
        Wait Until that element can be selected
        """
        try :
            time.sleep(1)
            errmsg = "Timeout select type: "+ elementType + " : "+elementName
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by, elementName)), errmsg)
            Select(self.driver.find_element(by, elementName)).select_by_visible_text(text)
        except :
            raise

    def elementExist(self,elementType, elementName):
        """Wait until that element is visible by visibility_of_element_located
        """
        try:
            time.sleep(1)
            if elementType == "id": by = By.ID
            elif elementType.lower() == "linktext": by = By.LINK_TEXT
            elif elementType.lower() == "partiallinktext": by = By.PARTIAL_LINK_TEXT
            elif elementType.lower() == "name": by = By.NAME
            elif elementType.lower() == "tagname": by = By.TAG_NAME
            elif elementType.lower() == "xpath": by = By.XPATH
            elif elementType.lower() == "classname": by = By.CLASS_NAME
            elif elementType.lower() == "cssselector": by = By.CSS_SELECTOR
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by,elementName)),"Timeout By " + elementType + " For " + elementName)
        except :
            raise