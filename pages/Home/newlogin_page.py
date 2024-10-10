from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver



class  LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #locators
    _email_field = "username"
    _password_field = "password"
    _login_button = "//i[@class='fa fa-2x fa-sign-in']"

    def enterEmail(self, email):
        self.sendkeys(email, self._email_field)
    def enterPassword(self, password):
        self.sendkeys(password, self._password_field)

    def clickLogin(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email='', password=''):
        self.clearfiled()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()

    def verifyLoginSuccessful(self):
        elementPresent = self.isElementPresent("//div[@class = 'flash success']", locatorType="xpath")
        return elementPresent

    def verifyinvalidlogin(self):
        result = self.isElementPresent("//div[@class = 'flash error']", locatorType="xpath")
        return result

    def clearfiled(self):
        email = self.getElement(locator=self._email_field)
        email.clear()
        password = self.getElement(locator=self._password_field)
        password.clear()