from bs4 import BeautifulSoup
import requests
import smtplib

EMAIL = "youremail@email.com"
PWD = "password"
REMOTE_HOST = ""
URL = "http://www.amazon.com"

header = {
    "Accept-Language": "",
    "User-Agent": ""
}

def send_message(price):
    with smtplib.SMTP(REMOTE_HOST) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
            msg=f"\n\nPrice alert for the RAM you wanted on amazon! {price}\n{URL}"
        )

res = requests.get(url=URL, headers=header)
res.raise_for_status()
html = res.text

soup = BeautifulSoup(html, "html.parser")
current_price = soup.find_all('div', id='')
print(current_price)

target_price = 1.00

if current_price <= target_price:
    send_message(current_price)