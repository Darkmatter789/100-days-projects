import requests
from datetime import datetime as dt

AUTH_TOKEN = ""
APP_ID = ""
API_KEY = ""
DATE = dt.now()
FORMATTED_DATE = DATE.strftime("%m/%d/%Y")
FORMATTED_TIME = DATE.strftime("%I:%M:%S") 

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": "95",
    "height_cm": "175",
    "age": "35",
}

res = requests.post(exercise_endpoint, json=exercise_params, headers=header)
res.raise_for_status()
data = res.json()

for items in data["exercises"]:
    exe = items["name"].title()
    dur = round(items["duration_min"])
    cal = round(items["nf_calories"])
    sheet_update = {
        "workout": {
            "date": FORMATTED_DATE,
            "time": FORMATTED_TIME,
            "exercise": exe,
            "duration": dur,
            "calories": cal
        }
    }

    header = {
        "Authorization": AUTH_TOKEN
    }
    update_endpoint = "https://api.sheety.co/"
    update_res = requests.post(url=update_endpoint, json=sheet_update, headers=header)
    update_res.raise_for_status()
    print(update_res.text)