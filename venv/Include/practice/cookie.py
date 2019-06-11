from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests

userName = 'magic111'
passWord = '121314'

driver = webdriver.Chrome()
driver.get('https://aso100.com/account/signin')
# 等待20秒直到访问成功
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@name="username"]')))
user_name = driver.find_element_by_xpath('//*[@name="username"]')
user_name.send_keys(userName)
pass_word = driver.find_element_by_xpath('//*[@name="password"]')
pass_word.send_keys(passWord)
submit = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/form/div[4]/div/button')
submit.click()
# 等待20秒直到访问成功
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div[1]/div[3]/div[1]/input')))

# 获取cookies
cookie_list = driver.get_cookies()
print(cookie_list)
driver.close()
driver.quit()

driver = webdriver.Chrome()
# 要先访问一次这个域名
driver.get('https://aso100.com')

for item in cookie_list:
    driver.add_cookie({
        'domain': '.aso100.com',
        'name': item['name'],
        'value': item['value'],
        'path': '/',
        'expires': None
    })

driver.get('https://aso100.com/account/setting/type/dataCenter')
# input('是否有效')
# driver.close()
# driver.quit()

cookies = ";".join([item["name"] + "=" + item["value"] + "" for item in cookie_list])
print(cookies)
session = requests.Session()
# cookie要放到headers里
headers = {'Cookie': cookies}
html = session.get(url='https://aso100.com/account/setting/type/dataCenter', headers=headers).content.decode()
print(html)
