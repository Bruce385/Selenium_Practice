from selenium import webdriver
from time import sleep

sleep(2)
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 移动浏览器观看展示
driver.set_window_size(width=500, height=500)  # , windowHandle="current")
driver.set_window_position(x=1000, y=100)  # , windowHandle='current')
sleep(2)

# 获取当前页面title并断言
title = driver.title
print("当前页面的title是：", title, "\n")
assert title == u"百度一下，你就知道", "页面title属性值错误！"
sleep(2)

# 获取当前页面的源码并断言
pageSource = driver.page_source

try:
    assert u"百度一下，你就不知道" in pageSource, "页面源码中未找到'百度一下，你就知道'关键字"
except:
    print("源码这里故意断言错误", "\n")
sleep(2)

# 获取当前页面url并断言
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)
assert currentPageUrl == "https://www.baidu.com/", "当前网页网址非预期！"

sleep(2)
driver.quit()
