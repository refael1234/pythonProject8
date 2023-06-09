import json
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Register_Page import RegisterPage
from Second_Page import SecondPage
from Third_Page import ThirdPage
from Fourth_Page import FourthPage

class Test_Buyme_Pages(TestCase):
# first function to run
    def setUp(self):
        json_file = open('register.json', 'r')
        data = json.load(json_file)
        driver = data['driver']
        self.driver = webdriver.Chrome(service=Service(driver))
        self.Register_Page = RegisterPage(self.driver)
        self.Second_Page = SecondPage(self.driver)
        self.Third_Page = ThirdPage(self.driver)
        self.Fourth_Page = FourthPage(self.driver)
# second function to run
# call to the tests
    def test_register_box(self):
        self.Register_Page.send_text()
        self.Second_Page.send_text()
        self.Third_Page.send_text()
        self.Fourth_Page.send_text()
# third function to run
    def tearDown(self):
        self.driver.quit()
