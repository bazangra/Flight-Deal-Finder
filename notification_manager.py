import requests
from twilio.rest import Client

account_sid = []
auth_token = []

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.price = []

    def send_text(self, price, origin_airport, destination_airport, out_date, return_date):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+[]',
            body=f'Low price alert! Only £{price} to fly from {origin_airport} to {destination_airport}, on {out_date} until {return_date}.',
            to='whatsapp:+[]'
        )
