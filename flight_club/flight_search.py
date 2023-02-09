import requests
from flight_data import FlightData as fd

TEQUILA_ENDPOINT = ""
TEQUILA_API_KEY = "your api key"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
        
    def get_iata_code(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": TEQUILA_API_KEY}
        params = {"term": city, "location_types": "city",}
        res = requests.get(location_endpoint, params=params, headers=header)
        res.raise_for_status()
        code = res.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, dest_city_code, from_time, to_time, stop_overs=0):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        header = {"apikey": TEQUILA_API_KEY}
        params = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": stop_overs,
        }
        res = requests.get(search_endpoint, params=params, headers=header)
        res.raise_for_status()
        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No direct flights found for {dest_city_code}.")
            return None
        if params["max_stopovers"] > 0:
            flight_data = fd(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                via_city=data["route"][0]["cityTo"],
                dest_city=data["cityTo"],
                dest_airport=data["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=stop_overs,
                )
            print(f"{flight_data.dest_city}: ${flight_data.price} via {flight_data.via_city}")
            return flight_data
        else:
            flight_data = fd(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                dest_city=data["cityTo"],
                dest_airport=data["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=stop_overs,
                )
        
            print(f"{flight_data.dest_city}: ${flight_data.price}")
            return flight_data