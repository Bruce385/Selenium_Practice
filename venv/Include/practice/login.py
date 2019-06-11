from selenium import webdriver
from time import sleep

# 声明一个司机，司机是个Chrome类的对象
driver = webdriver.Chrome()

# 让司机加载一个网页
driver.get("http://demo.ranzhi.org")

driver.implicitly_wait(30)  # 隐性等待，最长等30秒
print(driver.current_url)
print(driver.get_cookies())
# 开始登录
# 1. 让司机找用户名的输入框
we_account = driver.find_element_by_css_selector('#account')
we_account.clear()
we_account.send_keys("demo")

# 2. 让司机找密码的输入框
we_password = driver.find_element_by_css_selector('#password')
we_password.clear()
we_password.send_keys("demo")

# 3. 让司机找 登录按钮 并 单击
driver.find_element_by_css_selector('#submit').click()

sleep(3)
print(driver.current_url)
print(driver.get_cookies())
