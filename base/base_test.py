
import pytest

from pages.Automation_Testing_Practice import AutomationTestingPractice


class BaseTest:
    AutomationTestingPractice_page: AutomationTestingPractice

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.AutomationTestingPractice_page = AutomationTestingPractice(driver)

