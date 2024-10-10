import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

@pytest.fixture(scope="function")
def setUp(request):
    print("Running setup for each test")
    yield
    print("Running teardown for each test")

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser to use for testing")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
