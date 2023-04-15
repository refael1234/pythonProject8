import json
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from base_page import BasePage
import time

class ThirdPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Price = data['Price']
        # Url = data['Turl']
        # self.driver.get(Url)
        time.sleep(1)
        self.click_element(By.CSS_SELECTOR, "div[class=top]")
        time.sleep(1)
        self.send_key(By.XPATH, "//input[@placeholder='הכנס סכום']",Price)
        self.click_element(By.CSS_SELECTOR, "button[type=submit]")

    def tearDown(self):
        self.driver.quit()
