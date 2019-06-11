from time import sleep
import unittest, random, sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit, function
from page_obj.loginPage import login


class loginTest(myunit.MyTest):
    '''用户登录测试'''

    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login0(self):
        '''正常登录'''
        self.user_login_verify('admin', '123456')
        sleep(1)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), 'admin')
        function.insert_img(self.driver, 'user_pawd_ture.png')

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        sleep(1)
        # po = login(self.driver)
        # self.assertEqual(po.login_error_hint(), '用户名不能为空')
        function.insert_img(self.driver, 'user_pawd_empty.png')

if __name__ == '__main__':
    unittest.main()
