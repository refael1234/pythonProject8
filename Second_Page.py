import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
from base_page import BasePage
import time

class SecondPage():
    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Gift = data['Gift']
        Url = data['Url']
        self.driver.get(Url)
        rar = self.driver.find_element(By.CLASS_NAME, "input-label-wrapper")
        rar.click()
        rar1 = rar.find_element(By.CSS_SELECTOR, 'li[value="1"]')
        rar1.click()
        time.sleep(3)
        rar2 = self.driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[1]
        rar2.click()
        time.sleep(3)
        rar3 = rar.find_element(By.CSS_SELECTOR, 'li[value="11"]')
        rar3.click()
        rar4 = self.driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[2]
        rar4.click()
        rar5 = rar.find_element(By.CSS_SELECTOR, 'li[value="22"]')
        rar5.click()
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='איזו מתנה תרצו לחפש?']")).send_keys(Gift)
        self.driver.find_element(locate_with(By.CSS_SELECTOR, "a[rel=nofollow]")).click()
        time.sleep(4)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def tearDown(self):
        self.driver.quit()
