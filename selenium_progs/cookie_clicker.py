from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BROWSER_FILE_PATH = ""
DRIVER_PATH = ""

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option("detach", True)
option.binary_location = BROWSER_FILE_PATH
driver_path = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=driver_path, options=option)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

seconds = 0
miliseconds = 250
store = driver.find_element(By.XPATH, '//*[@id="store"]').text.splitlines()
item_pairs = [store[i].split("-") for i in range(0, len(store), 2)]
items = [item[0].strip(' ') for item in item_pairs]
prices = [int(item[1].replace(",", "")) for item in item_pairs]

done = False
while not done:

    print(seconds)
    cookie = driver.find_element(By.ID, 'cookie')
    cookie.click()
    miliseconds -= 1
    while miliseconds == 0:
        money = driver.find_element(By.ID, "money").text.replace(",", "")
        for value in reversed(prices):
            if value < int(money):
                item = driver.find_element(By.ID, f"buy{items[prices.index(value)]}")
                item.click()
                miliseconds = 250
                seconds += 1
                break
    if seconds >= 10:
        done = True
        break

cookies_per_sec = driver.find_element(By.ID, 'cps').text
print(cookies_per_sec)
driver.close()