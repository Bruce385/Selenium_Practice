from calculator import Count
import unittest


class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')
        try:
            self.a = int(input('请输入整数a:'))
            self.b = int(input('请输入整数b:'))
        except ValueError:
            print('请输入准确的整数')

    def test_add(self):
        print('加法')
        try:
            self.assertEqual(Count(self.a, self.b).add(), 18, '求和不匹配')
            print('通过')
        except Exception as msg:
            print(msg)

    def test_sub(self):
        print('减法')
        try:
            self.assertEqual(Count(self.a, self.b).sub(), 8, '求差不匹配')
            print('通过')
        except AssertionError as msg:
            print(msg)
        except AttributeError as msg:
            print(msg)

    def tearDown(self):
        print('test end')
        pass


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(TestCount('test_add'))
    # suite.addTest(TestCount('test_sub'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    discover=unittest.defaultTestLoader.discover('./','testplus.py')
    unittest.TextTestRunner().run(discover)
