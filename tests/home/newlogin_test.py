import pytest
import unittest
from pages.Home.newlogin_page import LoginPage
from ddt import ddt, data, unpack
from utilities.readdata import get_CSV_Data

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    # def test_valid_login(self):
    #     self.lp.login("tomsmith", "SuperSecretPassword!")
    #     result = self.lp.verifyLoginSuccessful()
    #     assert result == True

    @pytest.mark.run(order=1)
    @data(*get_CSV_Data("C:\\Users\\Deepanshu\\workspace_python\\Framework_automation\\testdata.csv"))
    @unpack
    def test_invalid_login(self, user1, pass1):
        self.driver.get("http://the-internet.herokuapp.com/login")
        self.lp.login(user1, pass1)
        result = self.lp.verifyinvalidlogin()
        assert result == False
