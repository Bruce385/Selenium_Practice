import unittest
import time
from selenium import webdriver


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://www.baidu.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys('python')
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        products = self.driver.find_elements_by_xpath('//h3[@class="t"]/a')
        for product in products:
            print(product.text)
        print("products.len = " + str(products.__len__()))
        self.assertEqual(9, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("kw")
        self.submit_field = self.driver.find_element_by_id("su")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys('路飞')
        self.search_field.submit()
        # time.sleep(2)
        self.submit_field.click()
        time.sleep(1)
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath('//h3[@class="t"]/a')
        for product in products:
            print(product.text)
        print("products.len = " + str(products.__len__()))
        self.assertEqual(6, len(products))

    # 代码清理
    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.refresh()
        pass


if __name__ == '__main__':
    unittest.main()  # unittest.main(verbosity=2)
