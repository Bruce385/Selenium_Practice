from selenium import webdriver
from time import sleep
import unittest


# 创建TestBaidu类，继承unittest.TestCase;实现定位搜索，验证搜索，定位打开新页面
class TestBaidu(unittest.TestCase):
    # 用例执行前准备工作I
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.get("https://www.baidu.com")

    # 在TestBaidu类下构造test_baidu()方法
    def test_baidu(self):
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("百度")
        driver.find_element_by_id("su").click()  # 定位搜索
        sleep(5)

        # 设置断言，验证搜索结果当前页面对应的title内容
        title = driver.title
        self.assertEqual(title, "百度_百度搜索")
        sleep(5)
        # 定位打开百度网盘新页面
        driver.find_element_by_partial_link_text("百度首页").click()
        sleep(5)

    # 用例执行后的处理操作
    def tearDown(self):
        self.driver.quit()


# 调试TestBaidu测试类
if __name__ == '__main__':
    unittest.main()
