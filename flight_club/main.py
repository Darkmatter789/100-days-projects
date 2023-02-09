#This file uses the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

ORIGIN_CITY_CODE = "ATL"

DATE_FROM = datetime.now() + timedelta(days=1)
DATE_TO = DATE_FROM + timedelta(days=180)

formatted_from = DATE_FROM.strftime("%d/%m/%Y")
formatted_to = DATE_TO.strftime("%d/%m/%Y")

sheet_data = dm.get_sheet_data()

for place in sheet_data:
    if place["iataCode"] == '':
        place["iataCode"] = fs.get_iata_code(place["city"])
        params = {
            "price": place
        }
        dm.update_sheet_data(params)
        
for dest in sheet_data:
    flight = fs.check_flights(
        ORIGIN_CITY_CODE,
        dest["iataCode"],
        formatted_from,
        formatted_to
    )
    if flight == None:
        flight = fs.check_flights(
            ORIGIN_CITY_CODE,
            dest["iataCode"],
            formatted_from,
            formatted_to,
            stop_overs=1
        )
    
    if flight.price < dest["lowestPrice"]:
        nm.update_user(flight.price, 
        flight.origin_city, 
        flight.origin_airport, 
        flight.dest_city, 
        flight.dest_airport, 
        flight.out_date, 
        flight.return_date,
        flight.stop_overs,
        flight.via_city

    )

