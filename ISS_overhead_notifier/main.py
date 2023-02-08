import requests
from datetime import datetime
import smtplib
import math
import time

EMAIL = "youremail@email.com"
PWD = "password"
REMOTE_HOST = ""
MY_LAT = 0
MY_LONG = 0

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if math.isclose(MY_LAT, iss_latitude, rel_tol=.14) and math.isclose(MY_LONG, iss_longitude, rel_tol=.14):
        return True
    
def send_message():
    with smtplib.SMTP(REMOTE_HOST) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
            msg=f"Subject:look up!\n\nISS is passing by!"
        )
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = 5
    sunset = 18
    time_now = datetime.now()
    if int(time_now.hour) < sunrise or int(time_now.hour) > sunset:
        return True

while True:
    time.sleep(60)
    if is_close() and is_night():
        send_message()


