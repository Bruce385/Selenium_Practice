# 执行测试用例
import unittest

test_dir = "./TestCase"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)