import allure
from base.base_test import BaseTest

@allure.feature("Selenium_lesson2")
class TestSearchElement(BaseTest):

    def test_search_elements(self):
        self.AutomationTestingPractice_page.open()
        self.AutomationTestingPractice_page.is_opened()
        self.AutomationTestingPractice_page.check_visibility_wiki_icon()
        self.AutomationTestingPractice_page.check_visibility_wiki_input_field()
        self.AutomationTestingPractice_page.check_visibility_wiki_search_button()
        self.AutomationTestingPractice_page.check_visibility_start_button()
