import json
from selenium.webdriver.common.by import By
from base_page import BasePage

class SecondPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

# The tests of the second page with screenshot
    def send_text(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        Gift = data['Gift']
        #Url = data['Url']
        #self.driver.get(Url)
        self.driver.set_page_load_timeout(2)
        self.driver.find_element(By.CLASS_NAME, "input-label-wrapper").screenshot('2.png')
        select_sum = self.driver.find_element(By.CLASS_NAME, "input-label-wrapper")
        select_sum.click()
        select_sum.find_element(By.CSS_SELECTOR, 'li[value="1"]').click()
        self.driver.set_page_load_timeout(1)
        select_place = self.driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[1]
        select_place.click()
        select_place.find_element(By.CSS_SELECTOR, 'li[value="11"]').click()
        self.driver.set_page_load_timeout(1)
        select_gift = self.driver.find_elements(By.CLASS_NAME, "input-label-wrapper")[2]
        select_gift.click()
        select_gift.find_element(By.CSS_SELECTOR, 'li[value="22"]').click()
        self.send_key(By.XPATH, "//input[@placeholder='איזו מתנה תרצו לחפש?']",Gift)
        self.click_element(By.CSS_SELECTOR, "a[rel=nofollow]")

    def tearDown(self):
        self.driver.quit()
