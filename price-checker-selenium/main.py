from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib

EMAIL = "TheHand87@outlook.com"
PWD = "Fr33YourMind"
URL = "https://www.udemy.com/course/the-python-mega-course/"
header = {
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def send_message(price):
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
            msg=f"\n\nPrice alert for the RAM you wanted on amazon! {price}\n{URL}"
        )


option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option("detach", True)
option.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=driver_path, options=option)

driver.get("https://www.udemy.com/course/the-python-pro-course/#instructor-1")

price = driver.find_element(By.XPATH, '//*[@id="u9-tabs--29-content-0"]/div/div[3]/div[1]/div/div[2]/div/div/div/span[1]')

print(price)

driver.close()