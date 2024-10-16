import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By

class AutomationTestingPractice(BasePage):
    PAGE_URL = Links.ATPPAGE

    WIKI_ICON = ("class name", "wikipedia-icon")
    WIKI_INPUT_FIELD = ("id", "Wikipedia1_wikipedia-search-input")
    WIKI_SEARCH_BUTTON = ("class name", "wikipedia-search-button")
    START_BUTTON = ("xpath", "//button[@name='start']")

    @allure.step("Показывается иконка Wikipedia")
    def check_visibility_wiki_icon(self):
        self.is_element_visible(name_locator="WIKI_ICON", locator=self.WIKI_ICON)
        self.make_screenshot_element(locator=self.WIKI_ICON, screenshot_name="wiki_icon")

    @allure.step("Показывается поле ввода Wikipedia")
    def check_visibility_wiki_input_field(self):
        self.is_element_visible(name_locator=" WIKI_INPUT_FIELD", locator=self.WIKI_INPUT_FIELD)
        self.make_screenshot_element(locator=self.WIKI_INPUT_FIELD, screenshot_name="wiki_input")

    @allure.step("Показывается кнопка поиска Wikipedia")
    def check_visibility_wiki_search_button(self):
        self.is_element_visible(name_locator="WIKI_SEARCH_BUTTON", locator=self.WIKI_SEARCH_BUTTON)
        self.make_screenshot_element(locator=self.WIKI_SEARCH_BUTTON, screenshot_name="wiki_search")

    @allure.step("Показывается кнопка START")
    def check_visibility_start_button(self):
        self.is_element_visible(name_locator="START_BUTTON", locator=self.START_BUTTON)
        self.make_screenshot_element(locator=self.START_BUTTON, screenshot_name="start_button")
