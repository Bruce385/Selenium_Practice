from selenium import webdriver
from .driver import browser
import unittest, os


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # def testOpen(self):
    #     self.driver.get('https://www.hfpark.cn')


if __name__ == '__main__':
    unittest.main()
