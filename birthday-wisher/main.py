import datetime as dt
import pandas
import smtplib
import os
from random import choice
from dotenv import load_dotenv

load_dotenv()

LETTER_PATH = "./letter_templates/"
now = dt.datetime.now()
current_day = now.day
current_month = now.month
SUBJECT = "Happy Birthday!"
SIGNATURE = "Regards,\n[Your Name]\n"
MY_EMAIL = os.getenv('EMAIL_SENDER')
# see App password setup.docx on how to set up your own password
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(email_to, subject=SUBJECT, body="", signature=""):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        try:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        except smtplib.SMTPAuthenticationError as ser:
            print("Incorrect Credentials or not properly configured!")
        else:
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email_to,
                                msg=f"Subject: {subject}\n\n{body}\n\n{signature}")
            print("Greetings Sent")


# letters list - letter templates
letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# birthdays.csv  - list of people you want to send a birthday wish
birth_file = pandas.read_csv("birthdays.csv", header=0)
count = 0
for index, row in birth_file.iterrows():
    if row['month'] == current_month and row["day"] == current_day:
        count += 1
        # randomly pick letter template to use for your birthday wisher
        with open(f"{LETTER_PATH}{choice(letters_list)}") as file:
            letter = file.read().replace('[NAME]', row["name"])
            send_email(body=letter, email_to=row["email"])
if count == 0:
    print("No birthdays found for today!")
