import requests
from twilio.rest import Client
from datetime import datetime as dt

STOCK = "GME"
COMPANY_NAME = "Gamestop Corp"
ALPHA_KEY = ""
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_KEY = ""
NEWS_URL = "https://newsapi.org/v2/everything" 
ACCOUNT_SID = ""
AUTH_TOKEN  = ""

date = dt.now()
day_of_week = date.weekday()
todays_date = date.date()
day = date.day
month = date.month
year = date.year

alpha_params = {
    "function": "TIME_SERIES_INTRAday",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": ALPHA_KEY,
}

news_params = {
    "q": COMPANY_NAME,
    "from": todays_date,
    "sortBy": "popularity",
    "apiKey": NEWS_KEY,
}

day_1 = day - 1
day_2 = day - 2
if day_of_week == 6:
    day_1 = day - 2
    day_2 = day - 3

alpha_r = requests.get(ALPHA_URL, alpha_params)
alpha_r.raise_for_status()
alpha_data = alpha_r.json()
day_1_close = float(alpha_data["Time Series (60min)"][f'{year}-{month}-{day_1} 20:00:00']["4. close"])
day_2_close = float(alpha_data["Time Series (60min)"][f'{year}-{month}-{day_2} 20:00:00']["4. close"])
diff = abs(day_1_close - day_2_close)
percentage = (diff / day_1_close) * 100

if percentage > 4:
    news_r = requests.get(NEWS_URL, news_params)
    news_r.raise_for_status()
    news_data = news_r.json()
    news_slice = news_data["articles"][:3]
    for articles in news_slice:
        title = articles["title"]
        brief = articles["description"]
       
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            to="", 
            from_="",
            body=f"{STOCK}: {percentage}%\nHeadline: {title}\nBrief: {brief}")
        print(message.status)


