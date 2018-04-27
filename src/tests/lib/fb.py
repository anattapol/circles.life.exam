import waitEC, time

class facebook():
    def __init__(self, driver, baseURL, timeout=10):
        self.driver = driver
        self.baseURL = baseURL
        self.waitEC = waitEC.waitEC(driver, timeout)
    
    def signin(self, email="", password="", validlogin=False, errorMsg=""):
        """ Provide the username and password leave blank mean None
        """
        try:
            result = {"status":0 , "message": ""}
            self.waitEC.sendKey('id',"email",email.strip())
            self.waitEC.sendKey('id',"pass",password)
            self.waitEC.click('id','loginbutton')
            return result
        except:
            raise

    def postStatus(self,message=""):
        """ Provide the username and password leave blank mean None
        """
        try:
            result = {"status":0 , "message": ""}
            self.driver.get(self.baseURL+'/circle.lifetest.7')
            self.waitEC.click('xpath',"//div[@data-testid='react-composer-root']/div[2]/div/div[1]/div/div/div[2]")
            time.sleep(1) #wait for composer post box
            self.waitEC.sendKey('xpath',"//div[@contenteditable='true']",message)
            self.waitEC.click('xpath',"//div[@data-testid='react-composer-root']//button[@data-testid='react-composer-post-button']")
            # time.sleep(10) #wait for status post
            status = self.waitEC.getText('xpath',"//div[@id='timeline_composer_container']/div[2]//div[contains(@class,'userContentWrapper')]//div[contains(@class,'userContent')]/div/p")
            if str(message) == str(status):
                result = {"status":1 , "message": "Found the post"}
            else:
                result = {"status":1 , "message": "Post not found, something wrong"}
            return result
        except:
            raise

