#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import time

data_manager = DataManager()
sheet_data = data_manager.getrequest()
flight_search = FlightSearch()
notification_manager = NotificationManager()

departure_date = (datetime.datetime.now() + datetime.timedelta(hours=24)).strftime("%Y-%m-%d")
return_date = ((datetime.datetime.now() + datetime.timedelta(hours=(24 * 180))).strftime("%Y-%m-%d"))

for each in sheet_data:
    if each["iataCode"] == "":
        each["iataCode"] = flight_search.function1(each["city"])
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")
data_manager.sheet_data1 = sheet_data
data_manager.putrequest()


for each in sheet_data:
    print(f"Getting flights for {each["city"]}...")
    data = flight_search.get_flights(each["iataCode"], departure_date, return_date)
    cheapest_flight = FlightData(each["lowestPrice"], "LON", each["iataCode"], departure_date, return_date).get_prices(data)
    print(f"{each["city"]}: £{cheapest_flight.price}")
    if cheapest_flight.price < each["lowestPrice"]:
        notification_manager.send_text(cheapest_flight.price, cheapest_flight.origin_airport, cheapest_flight.destination_airport, cheapest_flight.out_date, cheapest_flight.return_date)
    time.sleep(2)
