from selenium import webdriver
from selenium.webdriver.common.by import By

class autoReport:
    def __init__(self, url, login_userName, login_password) -> None:
        self.url = url
        self.login_username = login_userName
        self.login_password = login_password
        self.driver = webdriver.Edge("driver/MicrosoftWebDriver.exe")
        
        
    def report(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//input[@name=\'T1\']").click()
        self.driver.find_element(By.NAME, "T1").send_keys(self.login_username)
        self.driver.find_element(By.CSS_SELECTOR, "td tr:nth-child(3) > td").click()
        self.driver.find_element(By.NAME, "T2").click()
        self.driver.find_element(By.NAME, "T2").send_keys(self.login_password)
        self.driver.find_element(By.NAME, "B1").click()
        self.driver.find_element(By.NAME, "B21").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.NAME, "B1").click()
    
    def change_user(self, login_userName, login_password):
        self.login_username = login_userName
        self.login_password = login_password

    def web_close(self):
        self.driver.quit()
        

if __name__ == "__main__":
    
    user = autoReport("http://163.32.74.2/web_ap/student_allin/index.asp", "test", "test")
    user.report()