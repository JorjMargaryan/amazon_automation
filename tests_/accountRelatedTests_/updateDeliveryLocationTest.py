import time

from tests_.baseTest import BaseTest
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.updateDeliveryLocationPopup import UpdateDeliveryLocationPopup
from testData_.data import zipCodeData


class UpdateDeliveryLocationTest(BaseTest):
    def test_update_location_by_valid_zip_code(self):
        """
            Test Case: Update the delivery location by entering a valid zip code
        """
        # Pre-conditions
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_update_location_button()
        # Act
        updateDeliveryLocationPopupObj = UpdateDeliveryLocationPopup(self.driver)
        updateDeliveryLocationPopupObj.fill_zip_code_field(zipCodeData["validZipCode"])
        updateDeliveryLocationPopupObj.click_apply_button()
        updateDeliveryLocationPopupObj.click_continue_button()
        # todo improve logic for wait until the content will be updated to get rid of time sleep
        time.sleep(2)
        # Assertion
        deliveryCountryName = updateDeliveryLocationPopupObj.get_delivery_country_name()
        self.assertIn(str(zipCodeData["validZipCode"]), deliveryCountryName,
                      "AssertionError: The given valid zip code has not been updated")

    def test_update_location_by_country_selection(self):
        """
            Test Case: Update the delivery location by selecting country from the list
        """
        # Pre-Conditions
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_update_location_button()
        # Act
        updateDeliveryLocationPopupObj = UpdateDeliveryLocationPopup(self.driver)
        updateDeliveryLocationPopupObj.open_country_dropdown()
        updateDeliveryLocationPopupObj.select_country_from_dropdown()
        countryDropdownPlaceholder = updateDeliveryLocationPopupObj.get_country_dropdown_placeholder_text()
        updateDeliveryLocationPopupObj.click_done_button()

        # todo improve logic for wait until the content will be updated to get rid of time sleep
        time.sleep(2)
        # Assertion
        deliveryCountryName = updateDeliveryLocationPopupObj.get_delivery_country_name()
        self.assertEqual(countryDropdownPlaceholder, deliveryCountryName,
                         "AssertionError: The delivery country has not been updated.")

    def test_negative_update_location_by_invalid_zip_code(self):
        """
            Test Case: Trying to update the delivery location by entering some invalid zip code
        """
        # Pre-Conditions
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_update_location_button()
        # Act
        updateDeliveryLocationPopupObj = UpdateDeliveryLocationPopup(self.driver)
        updateDeliveryLocationPopupObj.fill_zip_code_field(zipCodeData["invalidZipCode"])
        updateDeliveryLocationPopupObj.click_apply_button()
        # Assertion
        invalidZipCodeAlertText = updateDeliveryLocationPopupObj.get_invalid_zip_code_validation_alert_text()
        self.assertEqual(invalidZipCodeAlertText, "Please enter a valid US zip code",
                         "AssertionError: Validation message for invalid zip code was not displayed")
