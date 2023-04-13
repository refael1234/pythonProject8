import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
from base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class ThirdPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Price = data['Price']
        Url = data['Turl']
        self.driver.get(Url)
        self.click_element(By.CSS_SELECTOR, "div[class=top]")
        time.sleep(3)
        self.send_key(By.XPATH, "//input[@placeholder='הכנס סכום']",Price)
        self.click_element(By.CSS_SELECTOR, "button[type=submit]")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.quit()
