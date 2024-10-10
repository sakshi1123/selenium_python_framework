import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as cService
from selenium.webdriver.common.by import By

class Login_test():


    def test_valid_login(self):
        eService = cService(executable_path="C:\\Users\\Deepanshu\\workspace_python\\learnselenium\\pythonProject\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=eService)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        time.sleep(10)
        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        time.sleep(10)

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@email.com")

        time.sleep(12)

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("abcabc")

        time.sleep(12)

        loginButton = driver.find_element(By.NAME, "commit")
        loginButton.click()

        time.sleep(2)

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")





eg = Login_test()
eg.test_valid_login()