import json
from selenium.webdriver.common.by import By
from base_page import BasePage


class ThirdPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

# The tests of the third page
    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Price = data['Price']
        # Url = data['Turl']
        # self.driver.get(Url)
        self.driver.set_page_load_timeout(1)
        self.click_element(By.CSS_SELECTOR, "div[class=top]")
        self.driver.set_page_load_timeout(1)
        self.send_key(By.XPATH, "//input[@placeholder='הכנס סכום']",Price)
        self.click_element(By.CSS_SELECTOR, "button[type=submit]")

    def tearDown(self):
        self.driver.quit()
