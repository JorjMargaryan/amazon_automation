from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        """
            Initialize the BasePage with a Selenium WebDriver instance.

            Args:
                driver (selenium.webdriver.remote.webdriver.WebDriver): The Selenium WebDriver instance used for web automation.
        """
        self.driver = driver

    def _find_element(self, locator, timeout=10, condition=EC.visibility_of_element_located):
        """
            Find and return a web element based on the provided locator, waiting for a specified condition.

            Args:
                locator (tuple): A tuple representing the locator strategy and value,
                    e.g., (By.ID, 'element_id').
                timeout (int, optional): The maximum time (in seconds) to wait for the element
                    to meet the specified condition. Default is 10 seconds.
                condition (function, optional): The expected condition to wait for before
                    returning the element. Default is EC.visibility_of_element_located.

            Returns:
                selenium.webdriver.remote.webelement.WebElement: The located web element.

            Raises:
                NoSuchElementException: If the element is not found within the specified timeout.
                TimeoutException: If the condition is not met within the specified timeout.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(condition(locator))
            return element
        except NoSuchElementException as e:
            print(f"Error: An error occurred: {str(e)} - The element was not found on the page.")
            exit(2)
        except TimeoutException as e:
            print(f"Error: Timeout waiting for element: {str(e)}")
            exit(3)

    def _find_elements(self, locator, timeout=10, condition=EC.presence_of_all_elements_located):
        """
            Find multiple elements on the web page using the provided locators and wait for their presence.

            Args:
                locator (tuple): A tuple containing the locator strategy and value
                    (e.g., (By.ID, 'element_id')).
                timeout (int, optional): The maximum time to wait for the elements to be present, in seconds.
                    Defaults to 10.
                condition (callable, optional): The expected condition to be met.
                    Defaults to EC.presence_of_all_elements_located.

            Returns:
                WebElement(s): The found web element(s) matching the specified locators.

            Raises:
                NoSuchElementException: If the element(s) specified by the locators is not found on the web page.
                TimeoutException: If the elements are not present within the specified timeout period.
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(condition(locator))
            return elements
        except NoSuchElementException as e:
            print(f"Error: An error occurred: {str(e)} - The element(s) was not found on the page.")
            exit(2)
        except TimeoutException as e:
            print(f"Error: Timeout waiting for element(s): {str(e)}")
            exit(3)

    def _is_element_visible(self, locator):
        """
            Check if an element identified by the given locator is visible within a specified time.

            Args:
                locator (tuple): A tuple representing the element locator strategy (By) and value.

            Returns:
                bool: True if the element is visible within the specified time, False otherwise.

            Note:
                - This method utilizes WebDriverWait and ExpectedConditions to check the visibility of the element.
                - If the element becomes visible within the timeout period (10 seconds in this case), the method returns True.
                - If the element does not become visible within the timeout, a warning message is logged and the method returns False.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            print("Warning: Element was not visible within the specified time.")
            return False

    def _element_should_be_visible(self, locator):
        """
            Check if an element identified by the given locator is visible within a specified time.
            If the element is not visible, log an error and exit the script.

            Args:
                locator (tuple): A tuple representing the element locator strategy (By) and value.

            Returns:
                None

            Raises:
                TimeoutException: If the element is not visible within the specified time.
                Exception: If any unexpected error occurs during the process.

            Note:
                - This method utilizes WebDriverWait and ExpectedConditions to check the visibility of the element.
                - If the element does not become visible within the timeout period (10 seconds in this case),
                an error message is logged and the script exits.
                - If any unexpected error occurs during the process, an error message is logged, and the script exits.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("Error: Element is not visible within the specified time, but should be")
            exit(3)
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")
            exit(5)

    def _drag_and_drop_by_element(self, sourceElement, targetElement):
        """
            Perform a drag-and-drop action from a source element to a target element.

            Args:
                sourceElement (selenium.webdriver.remote.webelement.WebElement): The element to drag.
                targetElement (selenium.webdriver.remote.webelement.WebElement): The element to drop onto.

            Returns:
                None

            Note:
                - This method uses ActionChains to perform the drag-and-drop action.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop(sourceElement, targetElement)
        action.perform()

    def _drag_and_drop_by_offset(self, sourceElement, x, y):
        """
            Perform a drag-and-drop action from a source element by a specified offset (x, y).

            Args:
                sourceElement (selenium.webdriver.remote.webelement.WebElement): The element to drag.
                x (int): The horizontal offset to move the element.
                y (int): The vertical offset to move the element.

            Returns:
                None

            Note:
                - This method uses ActionChains to perform the drag-and-drop action.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(sourceElement, x, y)
        action.perform()

    def _mouse_move_to_element(self, element):
        """
            Move the mouse cursor to a specified element on the web page.

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The element to move the mouse to.

            Returns:
                None

            Note:
                - This method uses ActionChains to perform the mouse movement action.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def _mouse_move_by_offset(self, x, y):
        """
            Move the mouse cursor by a specified offset from its current position.

            Args:
                x (int): The horizontal offset.
                y (int): The vertical offset.

            Returns:
                None

            Note:
                - This method uses ActionChains to perform the mouse movement action.
        """
        action = ActionChains(self.driver)
        action.move_by_offset(x, y)
        action.perform()

    def _get_title_(self):
        """
            Get the title of the current web page.

            Returns:
                str: The title of the web page.

            Note:
                - This method retrieves the title of the web page currently loaded in the WebDriver.
                - The title typically represents the title of the web page as seen in the browser's title bar.

            Example usage:
                pageTitle = _get_title_()
                print(f"Current page title: {page_title}")
        """
        return self.driver.title

    def _fill_field(self, element, text):
        """
            Fill a text input field with the provided text after clearing its current content.

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The input field element.
                text (str): The text to be entered into the input field.

            Returns:
                None

            Note:
                - This method clears any existing text in the input field and then enters the provided 'text'.
                - It is commonly used for form input fields.

            Example usage:
                _fill_field(username_input, "myusername")
        """
        element.clear()
        element.send_keys(text)

    def _fill_field_and_apply(self, element, text, key):
        """
            Fill a form field with text and apply a key action.

            Purpose:
                This method fills a form field with the provided text and applies a key action (e.g., Enter or Tab).
                It combines the actions of filling the field and sending a key to it.

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The input field element.
                text (str): The text to be entered into the input field.
                key: The key action to apply (e.g., Keys.ENTER or Keys.TAB).

            Returns:
                None

            Example Usage:
                # Locate the input field element
                    input_field = driver.find_element_by_id("input_field_id")

                # Input text and press Enter key using _fill_field_and_apply method
                    text_to_input = "Hello, World!"
                    _fill_field_and_apply(input_field, text_to_input, Keys.ENTER)
        """
        self._fill_field(element, text)
        element.send_keys(key)

    def _get_element_text(self, element):
        """
            Get the text content of a web element.

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The element whose text content is to be retrieved.

            Returns:
                str: The text content of the web element.
        """
        return element.text

    def _click_to_element(self, element):
        """
            Perform a click on a web element after ensuring its clickable.

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The element to be clicked.

            Returns:
                None

            Raises:
                TimeoutException: If the element is not clickable within the specified timeout.
                ElementClickInterceptedException: If the element is not clickable due to interception.
                Exception: For other unexpected errors.

            Note:
                - The method waits for the element to be both enabled and displayed before clicking it.
                - If the element becomes clickable within the timeout, it is clicked.
                - If the element remains unclickable after the timeout, a TimeoutException is raised.
                - If the element remains unclickable due to interception, an ElementClickInterceptedException is raised.
                - Other unexpected errors are caught and result in an exit code of 5.

            Example usage:
                _click_to_element(element)
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: element.is_enabled() and element.is_displayed()
            )
        except TimeoutException as e:
            print(f"Error: Timeout waiting for the element to be clickable: {str(e)}")
            exit(3)
        except ElementClickInterceptedException as e:
            print(f"Error: Element is not clickable due to interception: {str(e)}")
            exit(4)
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")
            exit(5)
        element.click()

    def _double_click_to_element(self, element):
        """
            Perform a double click on a web element after ensuring it is clickable(enabled and displayed).

            Args:
                element (selenium.webdriver.remote.webelement.WebElement): The element to double-click.

            Returns:
                None

            Raises:
                TimeoutException: If the element is not clickable within the specified timeout.
                ElementClickInterceptedException: If the element is not clickable due to interception.
                Exception: For other unexpected errors.

            Note:
                - This method uses ActionChains to perform the double click action.
                - The method waits for the element to be both enabled and displayed before performing the double click.
                - If the element becomes clickable within the timeout, a double click is performed.
                - If the element remains unclickable after the timeout, a TimeoutException is raised.
                - If the element remains unclickable due to interception, an ElementClickInterceptedException is raised.
                - Other unexpected errors are caught and result in an exit code of 5.

            Example usage:
                _double_click_to_element(element)
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: element.is_enabled() and element.is_displayed()
            )
        except TimeoutException as e:
            print(f"Error: Timeout waiting for the element to be clickable: {str(e)}")
            exit(3)
        except ElementClickInterceptedException as e:
            print(f"Error: Element is not clickable due to interception: {str(e)}")
            exit(4)
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")
            exit(5)
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()
