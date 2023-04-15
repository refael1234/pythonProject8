import allure
from allure_commons.types import AttachmentType

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def clear_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).clear()

    def send_key(self,locator_type, locator_value, keys):
        self.driver.find_element(locator_type, locator_value).send_keys(keys)