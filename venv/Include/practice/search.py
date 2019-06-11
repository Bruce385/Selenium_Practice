from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
sleep(1)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(1)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('20')  # 显示20条

driver.find_element_by_class_name("prefpanelgo").click()
#driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]')
sleep(1)
driver.switch_to.alert.accept()