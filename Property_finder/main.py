from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FORM_ADD = "Your google form"
LAND_ADD = "https://www.land.com/East-Central-Tennessee-Region/all-land/under-100000/over-10-acres/"
BROWSER_FILE_PATH = ""
DRIVER_PATH = ""

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option("detach", True)
option.binary_location = BROWSER_FILE_PATH
driver_path = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=driver_path, options=option)

driver.get(LAND_ADD)

data = driver.find_elements(By.CSS_SELECTOR, '._89607 a')
price_acre_data = driver.find_elements(By.CLASS_NAME, "_12a2b")
items = [items.text.split("•") for items in price_acre_data]

prices = [price[1] for price in items]
acres = [acres[0] for acres in items]
addresses = [address.text for address in driver.find_elements(By.CLASS_NAME, "df867")]
links = [link.get_attribute('href') for link in data]

driver.get(FORM_ADD)

for i in range(0, 24):
    acre_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    acre_input.click()
    acre_input.send_keys(acres[i])
    add_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_input.click()
    add_input.send_keys(addresses[i])
    cost_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cost_input.click()
    cost_input.send_keys(prices[i])
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(links[i])
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    new_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_page.click()
    time.sleep(2)
driver.close()
