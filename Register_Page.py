from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        self.driver.find_element(locate_with(By.CLASS_NAME, "notSigned")).click()
        time.sleep(3)
        self.driver.find_element(locate_with(By.XPATH, "//span[@class='text-link theme']")).click()
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='שם פרטי']")).send_keys('refael')
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='מייל']")).send_keys('TTJsahl5T@gmail.com')
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='סיסמה']")).send_keys('Re123456')
        self.driver.find_element(locate_with(By.XPATH, "//input[@placeholder='אימות סיסמה']")).send_keys('Re123456')
        self.driver.find_element(locate_with(By.CLASS_NAME, "fill")).click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
