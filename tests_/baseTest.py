import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener
from pages_.navigationBar_.navigationBar import NavigationBar

from testData_.data import mainPageUrl


class BaseTest(unittest.TestCase):
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
        # If the page was loaded incorrectly this logic will refresh the page
        navigationBarObj = NavigationBar(self.driver)
        if not navigationBarObj.is_update_location_button_visible():
            self.driver.refresh()

    def tearDown(self):
        self.driver.close()
