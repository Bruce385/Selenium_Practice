from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/video/av48236634")

video = driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[7]/video')
url = driver.execute_script('return arguments[0].currentSrc;', video)
print(url)

print('start')
driver.execute_script('return arguments[0].play();', video)

sleep(10)
print('stop')
driver.execute_script('return arguments[0].pause();', video)
#driver.get_screenshot_as_file("D:\\123.png")