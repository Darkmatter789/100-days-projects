import requests
from twilio.rest import Client

account_sid = ""
auth_token  = ""

MY_LAT = 0
MY_LONG = 0
API_KEY = ""

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

res = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=params)
res.raise_for_status()
data = res.json()

will_rain = False
daily_data = data["hourly"][:12]
weather_ids = [items["weather"][0]["id"] for items in daily_data]
for id in weather_ids:
    if int(id) < 600:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="", 
        from_="",
        body="Its going to rain today!"
        )
    print(message.status)