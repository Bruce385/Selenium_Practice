from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

sreach_windows = driver.current_window_handle

# driver.find_element_by_link_text("更多产品").click()
# driver.find_element_by_link_text("糯米").click()
driver.find_element_by_link_text("登录").click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
driver.find_element_by_link_text("立即注册").click()

#获得当前所有打开窗口的句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print("now in register window!")
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys('cyc')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__phone"]').send_keys('18965135110')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys('password')
        time.sleep(2)

for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.window(handle)
        print("now in sreach window!")
        # driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys("2297711680@qq.com")
        # driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('lyhgez')
        # driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        time.sleep(2)
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)