import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from testData_.data import mainPageUrl


class BaseTest(unittest.TestCase):
    """
        Base test class for setting up and tearing down the test environment.

        This class defines common setup and teardown methods for test cases.
        The `setUp` method initializes a Chrome WebDriver instance with common settings,
        and the `tearDown` method closes the WebDriver instance after each test case.

        Attributes:
            driver (webdriver.Chrome): The WebDriver instance for running tests.

        Usage:
            Subclasses of this base class can inherit these setup and teardown methods
            to configure the test environment for their specific test cases.
    """

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self) -> None:
        self.driver.close()
