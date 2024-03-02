from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class UpdateDeliveryLocationPopup(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.popupTitleLocator = (By.ID, "a-popover-header-1")
        self.zipCodeFieldLocator = (By.ID, "GLUXZipUpdateInput")
        self.applyButtonLocator = (By.XPATH, "//div[@class='a-column a-span4 a-span-last']/span/span/input")
        self.continueButtonLocator = (By.CSS_SELECTOR, ".a-popover-footer #GLUXConfirmClose")
        self.countryDropdownLocator = (By.ID, "GLUXCountryValue")
        self.countryItemLocator = (By.XPATH, "(//*[@class='a-dropdown-item'])[17]")
        self.doneButtonLocator = (By.NAME, "glowDoneButton")
        self.changeButtonLocator = (By.ID, "GLUXChangePostalCodeLink")
        self.signInToSeeAddressButtonLocator = (By.ID, "GLUXSignInButton")
        self.manageAddressBookButtonLocator = (By.ID, "GLUXManageAddressLink")

        self.countryDropdownPlaceholderLocator = (By.ID, "GLUXCountryValue")
        self.deliveryCountryNameLocator = (By.ID, "glow-ingress-line2")
        self.invalidZipCodeValidationAlertLocator = (By.ID, "GLUXZipError")

    def fill_zip_code_field(self, zipCode):
        zipCodeFieldElement = self._find_element(self.zipCodeFieldLocator)
        self._fill_field(zipCodeFieldElement, zipCode)

    def click_apply_button(self):
        applyButtonElement = self._find_element(self.applyButtonLocator)
        self._click_to_element(applyButtonElement)

    def click_continue_button(self):
        continueButtonElement = self._find_element(self.continueButtonLocator)
        self._click_to_element(continueButtonElement)

    def open_country_dropdown(self):
        popupTitleElement = self._find_element(self.popupTitleLocator)
        countryDropdownElement = self._find_element(self.countryDropdownLocator)
        self._click_to_element(popupTitleElement)
        self._click_to_element(countryDropdownElement)

    def select_country_from_dropdown(self):
        countryItemElement = self._find_element(self.countryItemLocator)
        self._click_to_element(countryItemElement)

    def click_done_button(self):
        doneButtonElement = self._find_element(self.doneButtonLocator)
        self._click_to_element(doneButtonElement)

    def click_change_button(self):
        popupTitleElement = self._find_element(self.popupTitleLocator)
        changeButtonElement = self._find_element(self.changeButtonLocator)
        self._click_to_element(popupTitleElement)
        self._click_to_element(changeButtonElement)

    def check_the_change_button_existence(self):
        if self._is_element_visible(self.changeButtonLocator):
            return True
        else:
            return False

    def click_sign_in_to_see_address_button(self):
        signInToSeeAddressButtonElement = self._find_element(self.signInToSeeAddressButtonLocator)
        self._click_to_element(signInToSeeAddressButtonElement)

    def click_manage_address_book_button(self):
        manageAddressBookButtonElement = self._find_element(self.manageAddressBookButtonLocator)
        self._click_to_element(manageAddressBookButtonElement)

    def get_country_dropdown_placeholder_text(self):
        countryDropdownPlaceholderElement = self._find_element(self.countryDropdownPlaceholderLocator)
        return self._get_element_text(countryDropdownPlaceholderElement)

    def get_delivery_country_name(self):
        deliveryCountryNameElement = self._find_element(self.deliveryCountryNameLocator)
        return self._get_element_text(deliveryCountryNameElement)

    def get_invalid_zip_code_validation_alert_text(self):
        invalidZipCodeValidationAlertElement = self._find_element(self.invalidZipCodeValidationAlertLocator)
        return self._get_element_text(invalidZipCodeValidationAlertElement)

