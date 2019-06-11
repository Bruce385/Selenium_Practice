from selenium.webdriver import Remote
from time import sleep

lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://192.168.1.102:5555/wd/hub': 'chrome'}

for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host, desired_capabilities={'platform': 'ANY',
                                                                 'browserName': browser,
                                                                 'version': '',
                                                                 'javascriptEnabled': True})
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
