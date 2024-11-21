import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        s = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def tearDown(self):
        self.driver.close()
