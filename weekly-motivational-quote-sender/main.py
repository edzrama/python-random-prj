import smtplib
import os
import datetime as dt
from random import choice
from dotenv import load_dotenv

load_dotenv()

with open("quotes.txt") as quotes:
    quotes_list = quotes.read().splitlines()

subject = "Motivational Quote to start you day"
body = choice(quotes_list)
signature = "Regards,\nEdz\n"
email_to = '[Email Recipient]'

now = dt.datetime.now()
day_of_the_week = now.weekday()
# Will send every monday
if day_of_the_week == 5:
    # get value from ENV
    my_email = os.getenv("EMAIL_SENDER")
    my_password = os.getenv("EMAIL_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        try:
            connection.login(user=my_email, password=my_password)
        except smtplib.SMTPAuthenticationError as ser:
            print("Incorrect Credentials or not properly configured!")
        else:
            connection.sendmail(from_addr=my_email,
                            to_addrs=email_to,
                            msg=f"Subject: {subject}\n\n{body}\n\n{signature}")
            print("Greetings Sent")
