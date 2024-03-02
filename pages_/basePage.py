from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

from common_.utilities_ import customLogger


class BasePage:
    def __init__(self, driver):
        """
            Initialize the BasePage with a Selenium WebDriver instance.
        """
        self.driver = driver

    def _find_element(self, locator, timeout=10, condition=EC.visibility_of_element_located):
        """
            Find and return a web element based on the provided locator, waiting for a specified condition.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(condition(locator))
            return element
        except NoSuchElementException as e:
            customLogger.logger("ERROR", f"Error: An error occurred: {str(e)} - The element was not found on the page.")
            exit(2)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"Error: Timeout waiting for element: {str(e)}")
            exit(3)

    def _find_elements(self, locator, timeout=10, condition=EC.presence_of_all_elements_located):
        """
            Find and return a multiple elements on the web page using the provided locators and wait for their presence.
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(condition(locator))
            return elements
        except NoSuchElementException as e:
            customLogger.logger("ERROR", f"Error: An error occurred: {str(e)} - The element(s) was not found on the page.")
            exit(2)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"Error: Timeout waiting for element(s): {str(e)}")
            exit(3)

    def _is_element_visible(self, locator):
        """
            Check if an element identified by the given locator is visible within a specified time.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            customLogger.logger("WARNING", "Warning: Element was not visible within the specified time.")
            return False

    def _element_should_be_visible(self, locator):
        """
            Check if an element identified by the given locator is visible within a specified time.
            If the element is not visible, log an error and exit the script.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            customLogger.logger("ERROR", "Error: Element is not visible within the specified time, but should be")
            exit(3)
        except Exception as e:
            customLogger.logger("ERROR", f"Error: An unexpected error occurred: {str(e)}")
            exit(5)

    def _drag_and_drop_by_element(self, sourceElement, targetElement):
        """
            Perform a drag-and-drop action from a source element to a target element.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop(sourceElement, targetElement)
        action.perform()

    def _drag_and_drop_by_offset(self, sourceElement, x, y):
        """
            Perform a drag-and-drop action from a source element by a specified offset (x, y).
        """
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(sourceElement, x, y)
        action.perform()

    def _mouse_move_to_element(self, element):
        """
            Move the mouse cursor to a specified element on the web page.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def _mouse_move_by_offset(self, x, y):
        """
            Move the mouse cursor by a specified offset from its current position.
        """
        action = ActionChains(self.driver)
        action.move_by_offset(x, y)
        action.perform()

    def _get_title_(self):
        """
            Get the title of the current web page.
        """
        return self.driver.title

    def _fill_field(self, element, text):
        """
            Fill a text input field with the provided text after clearing its current content.
        """
        element.clear()
        element.send_keys(text)

    def _fill_field_and_apply(self, element, text, key):
        """
            Fill a form field with text and apply a key action.
        """
        self._fill_field(element, text)
        element.send_keys(key)

    def _get_element_text(self, element):
        """
            Get the text content of a web element.
        """
        return element.text

    def _click_to_element(self, element):
        """
            Perform a click on a web element after ensuring it is clickable(enabled and displayed).
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: element.is_enabled() and element.is_displayed()
            )
        except TimeoutException as e:
            customLogger.logger("ERROR", f"Error: Timeout waiting for the element to be clickable: {str(e)}")
            exit(3)
        except ElementClickInterceptedException as e:
            customLogger.logger("ERROR", f"Error: Element is not clickable due to interception: {str(e)}")
            exit(4)
        except Exception as e:
            customLogger.logger("ERROR", f"Error: An unexpected error occurred: {str(e)}")
            exit(5)
        element.click()

    def _double_click_to_element(self, element):
        """
            Perform a double click on a web element after ensuring it is clickable(enabled and displayed).
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: element.is_enabled() and element.is_displayed()
            )
        except TimeoutException as e:
            customLogger.logger("ERROR", f"Error: Timeout waiting for the element to be clickable: {str(e)}")
            exit(3)
        except ElementClickInterceptedException as e:
            customLogger.logger("ERROR", f"Error: Element is not clickable due to interception: {str(e)}")
            exit(4)
        except Exception as e:
            customLogger.logger("ERROR", f"Error: An unexpected error occurred: {str(e)}")
            exit(5)
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()
