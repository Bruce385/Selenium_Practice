from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

driver.get('http://www.bilibili.com')
first_window = driver.current_window_handle

try:
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/input').send_keys('测试')
    driver.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/button').click()
    sleep(1)
    all_windows = driver.window_handles
    for handle in all_windows:
        if handle != first_window:
            driver.switch_to.window(handle)
            driver.get_screenshot_as_file('D:\\successful.png')
except BaseException as msg:
    print(msg)
    driver.get_screenshot_as_file('D:\\failed.png')
finally:
    pass
    # driver.quit()
