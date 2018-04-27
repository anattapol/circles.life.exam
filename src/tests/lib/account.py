import waitEC, time

class myAccount():
    def __init__(self, driver,email, timeout=10):
        self.driver = driver
        self.email = email
        self.waitEC = waitEC.waitEC(driver, timeout)
    
    def getEmail(self):
        """ Provide the username and password leave blank mean None
        """
        try:
            result = {"status":0 , "message": ""}
            email = self.driver.find_element_by_xpath("//*[@id='st-container']/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/form/div[3]/div/input").get_attribute("value")
            if email == self.email:
                result = {"status":0 , "message": "pass"}
            else:
                result = {"status":1 , "message": "fail - email is not "+self.email}
            print email
            return result
        except:
            raise
