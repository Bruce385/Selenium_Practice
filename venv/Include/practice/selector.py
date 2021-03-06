from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select

s1.select_by_index(1)  # 选择第二项选项：o1
sleep(2)
s1.select_by_value("o2")  # 选择value="o2"的项
sleep(2)
s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本
print(s1.first_selected_option.text)
# driver.quit()