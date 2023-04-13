import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
from base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class FourthPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Url = data['Furl']
        text1 = data['text1']
        text2 = data['text2']
        picture = data['picture']
        self.driver.get(Url)
        self.send_key(By.XPATH, "//input[@maxlength='25']",text1)
        time.sleep(1)
        blessing = self.driver.find_element(By.CLASS_NAME, "input-label-wrapper")
        blessing.click()
        birthday = blessing.find_element(By.CSS_SELECTOR, 'li[value="10"]')
        birthday.click()
        self.clear_element(By.XPATH, "//textarea[@rows='4']")
        self.send_key(By.XPATH, "//textarea[@rows='4']",text2)
        self.send_key(By.NAME, "logo",picture)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.click_element(By.XPATH, "//button[@gtm='המשך']")
        time.sleep(1)
        # sasi = self.driver.find_elements(By.CLASS_NAME, "icon")[1]
        # sasi[1].click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
