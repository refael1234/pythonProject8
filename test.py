from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Register_Page import RegisterPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_Buyme_Pages(TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(service=Service("C:\\Users\\Refael\\Downloads\\chromedriver_win32\\chromedriver.exe"))
        self.driver.get('https://buyme.co.il/')
        self.Register_Page = RegisterPage(self.driver)

    def test_register_box(self):
        self.Register_Page.send_text()


    def tearDown(self):
        self.driver.quit()
