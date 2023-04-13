import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Url = data['Url']
        username = data['username']
        email = data['email']
        password = data['password']
        self.driver.get(Url)
        self.driver.find_element(locate_with(By.CLASS_NAME, "notSigned")).click()
        time.sleep(3)
        self.driver.find_element(locate_with(By.XPATH, "//span[@class='text-link theme']")).click()
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='שם פרטי']")).send_keys(username)
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='מייל']")).send_keys(email)
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='סיסמה']")).send_keys(password)
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='אימות סיסמה']")).send_keys(password)
        self.driver.find_element(locate_with(By.CLASS_NAME, "fill")).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.driver.find_element(locate_with(By.CSS_SELECTOR, "span[class=label]")).click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
