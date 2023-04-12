import json
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Second_Page import SecondPage
from Register_Page import RegisterPage

json_file = open('register.json', 'r')
data = json.load(json_file)
Url = data['Url']
class Test_Buyme_Pages(TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(service=Service("C:\\Users\\Refael\\Downloads\\chromedriver_win32\\chromedriver.exe"))
        self.driver.get(Url)
        self.Register_Page = RegisterPage(self.driver)

    def test_register_box(self):
        self.Register_Page.send_text()

    def second_page_box(self):
        self.Second_Page.sender_text()


    def tearDown(self):
        self.driver.quit()
