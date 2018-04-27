import waitEC, time

class navbar():
    def __init__(self, driver, baseURL, timeout=10):
        self.driver = driver
        self.baseURL = baseURL
        self.waitEC = waitEC.waitEC(driver, timeout)
        