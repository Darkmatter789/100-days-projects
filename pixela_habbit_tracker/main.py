import requests
from datetime import datetime as dt

DATE = dt.now()
FORMATTED_DATE = DATE.strftime("%Y%m%d")
USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora",
    "timezone": "America/Chicago"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

graph_update = {
    "date": FORMATTED_DATE,
    "quantity": "120",
}

pixel_update_endpoint = f"{graph_update_endpoint}/{FORMATTED_DATE}"

pixel_update = {
    "quantity": "90"
}

res = requests.delete(url=pixel_update_endpoint, json=pixel_update, headers=headers)
print(res.text)