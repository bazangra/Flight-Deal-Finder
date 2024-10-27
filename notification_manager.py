import requests
from twilio.rest import Client

account_sid = 'ACbbb8fba945900aa7f2a1f4116d1b4ab3'
auth_token = '3a82e7c3b683c8f2d3bd6f80ad1cc50c'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.price = []

    def send_text(self, price, origin_airport, destination_airport, out_date, return_date):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Low price alert! Only £{price} to fly from {origin_airport} to {destination_airport}, on {out_date} until {return_date}.',
            to='whatsapp:+447711259832'
        )