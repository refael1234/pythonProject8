import json
from selenium.webdriver.common.by import By
from base_page import BasePage
import time

class RegisterPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)


    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Url = data['Url']
        username = data['username']
        email = data['email']
        password = data['password']
        self.driver.get(Url)
        self.click_element(By.CLASS_NAME, "notSigned")
        time.sleep(3)
        self.click_element(By.XPATH, "//span[@class='text-link theme']")
        self.send_key(By.XPATH, "//input[@placeholder='שם פרטי']",username)
        self.send_key(By.XPATH, "//input[@placeholder='מייל']",email)
        self.send_key(By.XPATH, "//input[@placeholder='סיסמה']",password)
        self.send_key(By.XPATH, "//input[@placeholder='אימות סיסמה']",password)
        self.click_element(By.CLASS_NAME, "fill")
        self.click_element(By.CSS_SELECTOR, "span[class=label]")
        self.driver.find_element(By.CSS_SELECTOR, "span[class=label]")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
