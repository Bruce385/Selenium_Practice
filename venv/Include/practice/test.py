from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

driver.find_element_by_id("kw").send_keys("selenium")
#driver.find_element_by_id("kw").clear()
driver.find_element_by_id("su").click()
sleep(3)

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("jmeter")
driver.find_element_by_id("su").click()
sleep(3)
driver.back()
#driver.back()