import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
from Second_Page import SecondPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class ThirdPage():
    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Price = data['Price']
        Url = data['Turl']
        self.driver.get(Url)
        self.driver.find_element(locate_with(By.CSS_SELECTOR, "div[class=top]")).click()
        time.sleep(3)
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='הכנס סכום']")).send_keys(Price)
        self.driver.find_element(locate_with(By.CSS_SELECTOR, "button[type=submit]")).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.quit()
