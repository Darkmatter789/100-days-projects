import smtplib
import datetime as dt
import random
import pandas

EMAIL = "youremail@email.com"
PWD = "password"
NOW = dt.datetime.now()

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
bdays = pandas.read_csv("birthdays.csv")
lines = bdays.iterrows()

def send_message(email, letter):
    with smtplib.SMTP("your_remote_host") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )

for index, line in lines:
    if line["month"] == NOW.month and line["day"] == NOW.day:
        with open(random.choice(letters), 'r') as file:
            letter = file.read()
            bday_letter = letter.replace("[NAME]", line["name"])
        send_message(line["email"], bday_letter)

