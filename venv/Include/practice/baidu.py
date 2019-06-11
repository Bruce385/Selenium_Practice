from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
driver.get("http://m.baidu.com")

#访问百度首页
driver.maximize_window()
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

#访问新闻页面
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
driver.back()

#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()

driver.refresh() #刷新当前页面
