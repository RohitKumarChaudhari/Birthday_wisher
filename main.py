import os
import random
import pandas as pd
import datetime as dt
import smtplib



data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

now = dt.datetime.now()

today_day =now.day
today_month =now.month

my_mail = "mobo07600@gmail.com"
password = "jbje zuwo iprp mbvi"

for person in birthdays:

    if today_month == person["month"] and today_day == person["day"]:

        random_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

        with open(random_file_path) as txt_file:
            content = txt_file.read()
            content = content.replace("[NAME]", person["name"])

        recipient_email = person["email"]

        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=recipient_email,
                                       msg=f"Subject:Happy Birthday!\n\n{content}")


