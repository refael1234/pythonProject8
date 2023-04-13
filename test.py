import json
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Register_Page import RegisterPage
from Second_Page import SecondPage
from Third_Page import ThirdPage
from Fourth_Page import FourthPage

class Test_Buyme_Pages(TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(service=Service("C:\\Users\\Refael\\Downloads\\chromedriver_win32\\chromedriver.exe"))

        self.Register_Page = RegisterPage(self.driver)
        self.Second_Page = SecondPage(self.driver)
        self.Third_Page = ThirdPage(self.driver)
        self.Fourth_Page = FourthPage(self.driver)

    def test_register_box(self):
        #self.Register_Page.send_text()
        #self.Second_Page.send_text()
        self.Third_Page.send_text()
        #self.Fourth_Page.send_text()

    def tearDown(self):
        self.driver.quit()
