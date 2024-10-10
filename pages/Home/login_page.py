from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver
class  LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _email_field = "email"
    _password_field = "pass"
    _login_button = "loginbutton"

    def email(self):
        return self.driver.find_element(By.ID, self._email_field)
    def passwrd(self):
        return self.driver.find_element(By.ID, self._password_field)
    def login_button(self):
        return self.driver.find_element(By.ID, self._login_button)

    def enterEmail(self, email):
        self.sendkeys(email, self._email_field)
    def enterPassword(self, password):
        self.sendkeys(password, self._password_field)

    def clickLogin(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()

    def verifyLoginSuccessful(self):
        elementPresent =  self.isElementPresent("//div[contains(text(), 'email address')]", locatorType="xpath")
        return elementPresent

