from twilio.rest import Client
import smtplib

EMAIL = "youremail@email.com"
PWD = "your password"
REMOTE_HOST = ""

ACCOUNT_SID = ""
AUTH_TOKEN  = ""

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def update_user(self, price, origin_city, origin_airport, dest_city, dest_airport, out_date, return_date, stop_overs=0, via_city=''):
        if stop_overs == 0:
            message = f"Low price alert! Only ${price} to fly from {origin_city}-{origin_airport} to {dest_city}-{dest_airport}, from {out_date} to {return_date}."
        else:
            message += f"\nFlight has {stop_overs} stop overs, via {via_city}."
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
        to="", 
        from_="",
        body=message
        )
        print(message.status)

    def send_emails(self, price, origin_city, origin_airport, dest_city, dest_airport, out_date, return_date, stop_overs=0, via_city=''):
        if stop_overs == 0:
            message = f"Low price alert! Only ${price} to fly from {origin_city}-{origin_airport} to {dest_city}-{dest_airport}, from {out_date} to {return_date}."
        else:
            message += f"\nFlight has {stop_overs} stop overs, via {via_city}."
        with smtplib.SMTP(REMOTE_HOST) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PWD)
            connection.sendmail(
                from_addr=EMAIL, 
                to_addrs=EMAIL, 
                msg=message
        )