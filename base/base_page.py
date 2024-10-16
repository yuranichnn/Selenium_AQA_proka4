import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Переходим на страницу {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Открыта страница {self.PAGE_URL}"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def is_element_visible(self, name_locator, locator):
        """ Функция проверки видимости элемента """
        with allure.step(f"Элемент '{name_locator}' отображается"):
            element = self.wait.until(EC.visibility_of_element_located(locator))

    def make_screenshot_element(self, locator, screenshot_name):
        """ Функция скриншота веб элемента """
        with allure.step(f"Скриншот веб элемента '{locator}'"):
            file_path = f"./utils/elements_screenshots/{screenshot_name}.png"
            element = self.driver.find_element(*locator)
            element.screenshot(file_path)
            allure.attach.file(source=file_path,
                               name=screenshot_name,
                               attachment_type=allure.attachment_type.PNG
                               )