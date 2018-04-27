import waitEC, time

class navbar():
    def __init__(self, driver, baseURL, timeout=10):
        self.driver = driver
        self.driver.find_element_by_id('site-navigation')
        self.baseURL = baseURL
        self.waitEC = waitEC.waitEC(self.driver, timeout)
    
    # def clickApplyCode(self,expectURL):
    #     """THe apply code is in the top bar
    #         expect the URL that need to be a parameter.
    #     """
    #     try:
    #         result = {"status":0 , "message": ""}
    #         self.waitEC.click('cssselector','div.insBanner')
    #         self.waitEC.titleContains(["Unlimit your telco. Now."])
    #         if expectURL  not in self.driver.current_url:
    #             result = {"status":1 , "message": "URL is not expected"}
    #         else:
    #             result = {"status":0 , "message": "Click Apply Code successfully"}
    #         return result
    #     except:
    #         raise
    
    def clickCirclesLifeLogo(self):
        """The circleslife logo is at the most left of the menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('xpath',"//*a[@title='Home']")
            time.sleep(5) ##wait for page started loading
            if self.baseURL != self.driver.current_url:
                result = {"status":1 , "message": "page loading slowly or something wrong"}
            else:
                result = {"status":0 , "message": "Click logo successfully"}
            return result
        except:
            raise
        
    def clickPlanOnly(self):
        """Click Plan only in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Plan Only')
            self.waitEC.titleContains(["No-Contract Plan"])
            result = {"status":0 , "message": "Plan Only works properly"}
            return result
        except:
            raise
    
    def clickPlanWithPhone(self):
        """Click Plan with phone in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Plan with phone')
            self.waitEC.titleContains(["No-Contract Plan"])
            result = {"status":0 , "message": "Plan with Phone works properly"}
            return result
        except:
            raise
    
    def clickRoaming(self):
        """Click Roaming in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Roaming')
            self.waitEC.titleContains(["Roaming"])
            result = {"status":0 , "message": "Roaming works properly"}
            return result
        except:
            raise
    
    def clickPorting(self):
        """Click Porting in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Porting')
            self.waitEC.titleContains(["Porting"])
            result = {"status":0 , "message": "Porting works properly"}
            return result
        except:
            raise
    
    def clickWhyUs(self):
        """Click Why us in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Why us')
            self.waitEC.titleContains(["About Us"])
            result = {"status":0 , "message": "Why us works properly"}
            return result
        except:
            raise
    
    def clickHelp(self):
        """Click Why us in menu bar
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('linktext','Help')
            self.waitEC.titleContains(["We're here to help"])
            result = {"status":0 , "message": "Help works properly"}
            return result
        except:
            raise