# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options

url = "https://login.m.taobao.com/msg_login.htm?spm=0.0.0.0"

# 设置成手机模式
mobile_emulation = {"deviceName": "iPhone 7"}
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_experimental_option("w3c", False)
driver = webdriver.Chrome(chrome_options=options)

driver.set_window_size(width=450, height=800)
driver.get(url)

driver.find_element_by_id("username").send_keys("悠悠我心")

# 触摸事件
el = driver.find_element_by_id('getCheckcode')
TouchActions(driver).tap(el).perform()

driver.get("http://d.dell.com")
