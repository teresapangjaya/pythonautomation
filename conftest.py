import os
import pytest
import pathlib
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

# Instantiate the parser
def pytest_addoption(parser):
    parser.addoption("--browser", type=str, default="mozilla", help="Browser used for testing", required=0)

@pytest.fixture
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    chrome_driver = os.getenv("CHROME_DRIVER_VER")
    # Initialize ChromeDriver
    if (browser_name == 'mozilla'):
        driver = webdriver.Firefox(
            executable_path=str(pathlib.Path().absolute()) + '\\browser\\mozilla\\geckodriver.exe')
    elif (browser_name == 'chrome'):
        driver = webdriver.Chrome(
            executable_path=str(pathlib.Path().absolute()) + '\\browser\\chrome\\' + chrome_driver)
    else:
        raise SystemExit('Browser ' + browser_name + ' not supported')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(5)

    # Return the driver object at the end of setups
    yield driver

    # For cleanup, quit the driver
    driver.quit()
