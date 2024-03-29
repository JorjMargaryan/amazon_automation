from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the NavigationBar class.
        """
        super().__init__(driver)

        self.__usernameFromAccountsAndListsLocator = (By.ID, "nav-link-accountList-nav-line-1")
        self.__deliveryCountryLocator = (By.ID, "glow-ingress-line2")
        self.__homePageLogoLocator = (By.ID, "nav-logo-sprites")
        self.__updateLocationButtonLocator = (By.ID, "glow-ingress-block")
        self.__searchFiltersDropdownLocator = (By.ID, "searchDropdownBox")
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__languageChangeDropdownLocator = (By.ID, "icp-nav-flyout")
        self.__accountListsDropdownLocator = (By.ID, "nav-link-accountList")
        self.__returnAndOrdersButtonLocator = (By.ID, "nav-orders")
        self.__cartButtonLocator = (By.ID, "nav-cart")
        self.__cartButtonQuantityLocator = (By.ID, "nav-cart-count")
        self.__hamburgerMenuButtonLocator = (By.ID, "nav-hamburger-menu")

    def __get_nav_bar_element_text_(self, locator):
        """
            Gets the text of an element by the provided locator
        """
        self._element_should_be_visible(locator)
        element = self._find_element(locator)
        return self._get_element_text(element)

    def get_hello_username_text_from_accounts_and_lists(self):
        """
            Gets the "Hello {current_user_name}" text from the navigation bar's accounts and lists section.
        """
        return self.__get_nav_bar_element_text_(self.__usernameFromAccountsAndListsLocator)

    def get_delivery_country_text_from_location_change_button(self):
        """
            Gets the delivery country name from the navigation bar's 'deliver to' section.
        """
        return self.__get_nav_bar_element_text_(self.__deliveryCountryLocator)

    def click_home_page_logo(self):
        """
            Clicks on the Amazon logo(home page)
        """
        homePageLogoElement = self._find_element(self.__homePageLogoLocator)
        self._click_to_element(homePageLogoElement)

    def click_update_location_button(self):
        """
            Clicks on the update location(deliver to) button
        """
        updateLocationButtonElement = self._find_element(self.__updateLocationButtonLocator)
        self._click_to_element(updateLocationButtonElement)

    def is_update_location_button_visible(self):
        """
            Checks if the delivery location update popup is open.
        """
        if self._is_element_visible(self.__updateLocationButtonLocator):
            return True
        else:
            return False

    def click_search_filters_dropdown(self):
        """
            Clicks on the search categories(filter) dropdown button.
        """
        searchFiltersDropdownElement = self._find_element(self.__searchFiltersDropdownLocator)
        self._click_to_element(searchFiltersDropdownElement)

    def fill_search_field(self, searchText):
        """
            Fills the search field with the provided text
        """
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, searchText)

    def fill_search_field_and_apply(self, searchText):
        """
            Fills the search field with the provided text and applies it by pressing the ENTER key on the keyboard.
        """
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field_and_apply(searchFieldElement, searchText, Keys.ENTER)

    def click_search_button(self):
        """
            Clicks on the search button
        """
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_element(searchButtonElement)

    def click_language_change_dropdown(self):
        """
            Clicks on the languages dropdown.
        """
        languageChangeDropdownElement = self._find_element(self.__languageChangeDropdownLocator)
        self._click_to_element(languageChangeDropdownElement)

    def hover_over_language_change_dropdown(self):
        """
            Hovering over the language dropdown list.
        """
        languageChangeDropdownElement = self._find_element(self.__languageChangeDropdownLocator)
        self._mouse_move_to_element(languageChangeDropdownElement)

    def click_account_lists_dropdown(self):
        """
            Clicks on the Account & Lists dropdown.
        """
        accountListsDropdownElement = self._find_element(self.__accountListsDropdownLocator)
        self._click_to_element(accountListsDropdownElement)

    def hover_over_account_lists_dropdown(self):
        """
            Hovering over the Account & Lists dropdown list.
        """
        accountListsDropdownElement = self._find_element(self.__accountListsDropdownLocator)
        self._mouse_move_to_element(accountListsDropdownElement)

    def click_return_and_orders_button(self):
        """
            Clicks on the Returns & Orders button.
        """
        returnAndOrdersButtonElement = self._find_element(self.__returnAndOrdersButtonLocator)
        self._click_to_element(returnAndOrdersButtonElement)

    def click_cart_button(self):
        """
            Clicks on the Cart button.
        """
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def get_cart_products_quantity(self):
        """
            Gets the quantity from the Cart button.
        """
        productsQuantityElement = self._find_element(self.__cartButtonQuantityLocator)
        return int(self._get_element_text(productsQuantityElement))

    def click_hamburger_menu_button(self):
        """
            Clicks on the hamburger menu button.
        """
        hamburgerMenuButtonElement = self._find_element(self.__hamburgerMenuButtonLocator)
        self._click_to_element(hamburgerMenuButtonElement)
