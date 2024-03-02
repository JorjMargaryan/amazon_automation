import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener

from testData_.data import mainPageUrl


class BaseTestWithoutLogin(unittest.TestCase):
    """
        Base test class for setting up and tearing down the test environment.
    """

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, CustomListener(self.simpleDriver))
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()
