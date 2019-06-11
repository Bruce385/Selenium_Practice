from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    '''用户登录页面'''

    url = '/login'
    login_username_loc = (By.NAME, 'username')
    login_password_loc = (By.NAME, 'password')
    login_checkcode_loc = (By.NAME, 'code')
    login_button_loc = (By.XPATH, '/html/body/div[1]/form/input[3]')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_checkcode(self, checkcode):
        self.find_element(*self.login_checkcode_loc).send_keys(checkcode)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username='admin', password='123456', checkcode=''):
        '''用户登录测试'''
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_checkcode(checkcode)
        self.login_button()
        sleep(1)

    user_login_success_loc = (By.XPATH, '/html/body/div/div[1]/ul/li[2]/a')
    login_error_hint_loc = (By.XPATH, '/html/body/div[3]')

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text
