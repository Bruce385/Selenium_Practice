from selenium import webdriver
from time import sleep
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
right_click =driver.find_element_by_name("tj_briicon")

# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
ActionChains(driver).context_click(right_click).perform()
