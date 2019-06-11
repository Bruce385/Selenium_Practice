from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains    #悬停的操作
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
driver.maximize_window()

#选中南京南
driver.find_element_by_css_selector("#fromStationText").click()
time.sleep(1)
driver.find_element_by_css_selector("#fromStationText").send_keys("南京南")
time.sleep(1)
driver.find_element_by_css_selector("#citem_0>.ralign:nth-child(1)").click()

#选中杭州东
driver.find_element_by_css_selector("#toStationText").click()
time.sleep(1)
driver.find_element_by_css_selector("#toStationText").send_keys("杭州东")
driver.find_element_by_css_selector("#citem_0>span:nth-child(1)").click()

#选择6-12点
driver.find_element_by_css_selector("#cc_start_time").click()

driver.find_element_by_css_selector('option[value*="06001200"]').click()
driver.find_element_by_css_selector("#cc_start_time").click()


#选择第二天
driver.find_element_by_css_selector("#sear-sel>div:nth-child(1)>ul>li:nth-child(2)").click()

time.sleep(4)         #网速不好，时间不长，不行

a = driver.find_element_by_css_selector("#queryLeftTable")
b = a.find_elements_by_css_selector("tr")         #选到里面所有的tr
alltrain = b[0:len(b):2]       #隔一个选一个，去掉没用的
for train in alltrain:
    c = train.find_element_by_css_selector("tr>td:nth-child(4)")           #找到票信息的元素
    if c.text !="无"and c.text !="--":
        d = train.find_element_by_css_selector("tbody>tr>td>div>div>div>a")        #找到车次信息的元素
        print(d.text)
