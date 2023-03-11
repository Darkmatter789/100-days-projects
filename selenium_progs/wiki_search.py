from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option("detach", True)
option.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/new_chrome.exe"
driver_path = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=driver_path, options=option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element(By.NAME, 'search')
search.send_keys("python")
search.send_keys(Keys.ENTER)
link = driver.find_element(By.LINK_TEXT, "Python (programming language)")
link.click()

new_search = driver.find_element(By.NAME, 'search')
new_search.send_keys("javascript")
new_search.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()