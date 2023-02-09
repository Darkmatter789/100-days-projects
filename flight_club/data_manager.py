import requests

SHEETY_ENDPOINT = ""
SHEETY_CUST_ENDPOINT = ""
SHEETY_AUTH_TOKEN = "your token"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_sheet_data(self):
        header = {"Authorization": SHEETY_AUTH_TOKEN}
        res = requests.get(SHEETY_ENDPOINT, headers=header)
        res.raise_for_status()
        data = res.json()["prices"]
        return data

    def update_sheet_data(self, params):
        header = {"Authorization": SHEETY_AUTH_TOKEN}
        id = params["price"]["id"]
        endpoint = f"{SHEETY_ENDPOINT}/{id}"
        res= requests.put(endpoint, json=params, headers=header)
        res.raise_for_status()

    def add_customer(self, f_name, l_name, email):
        header = {"Authorization": SHEETY_AUTH_TOKEN}
        params = {
            "customer": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }  
        res = requests.post(SHEETY_CUST_ENDPOINT, json=params, headers=header)
        res.raise_for_status()