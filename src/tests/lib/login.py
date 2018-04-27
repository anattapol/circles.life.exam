import waitEC, time

class authenBox():
    def __init__(self, driver, baseURL, timeout=10):
        self.driver = driver
        self.baseURL = baseURL
        self.waitEC = waitEC.waitEC(driver, timeout)
    
    def signin(self, email="", password="", validlogin=False, errorMsg=""):
        """ Provide the username and password leave blank mean None
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.sendKey('xpath',"//*[@id='st-container']//form//input[@name='email']","")
            self.waitEC.sendKey('xpath',"//*[@id='st-container']//form//input[@name='password']","")
            self.waitEC.sendKey('xpath',"//*[@id='st-container']//form//input[@name='email']",email.strip())
            self.waitEC.sendKey('xpath',"//*[@id='st-container']//form//input[@name='password']",password)
            self.waitEC.click('xpath',"//*[@id='st-container']//form[@method='post']//button")
            if not validlogin:
                if (email.strip() == '') and (password.strip() == ''):
                    self.waitEC.elementContains('xpath',"//div[@class='s-alert-wrapper']/div[1]/div[1]","Please enter your email")
                    self.waitEC.elementContains('xpath',"//div[@class='s-alert-wrapper']/div[2]/div[1]","Please enter your password")
                elif (password.strip() == '') and (email.strip() != ''):
                    self.waitEC.elementContains('xpath',"//div[@class='s-alert-wrapper']/div[1]/div[1]","Please enter your password")
                elif (email.strip() == '') and (password.strip() != '') :
                    self.waitEC.elementContains('xpath',"//div[@class='s-alert-wrapper']/div[1]/div[1]","Please enter your email")
                else:
                    self.waitEC.elementContains('xpath',"//div[@class='s-alert-wrapper']/div[1]/div[1]","Invalid login credentials. Please try again.")
                result = {"status":0 , "message": "pass"}
            else: 
                time.sleep(5) #Wait for login page load
                if "https://shop.circles.life/plan" not in self.driver.current_url:
                    result = {"status":1 , "message": "fail"}
                else:
                    result = {"status":0 , "message": "pass"}
                    
            return result
        except:
            raise

    def signout(self):
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.click('xpath',"//*[@id='st-container']//div[@class='st-content-inner']//div[@class='hidden-md-down']/div/a[6]")
            time.sleep(5) #Wait for login page load
            if "https://shop.circles.life/login" not in self.driver.current_url:
                result = {"status":1 , "message": "fail"}
            else:
                result = {"status":0 , "message": "pass"}
            return result
        except:
            raise
