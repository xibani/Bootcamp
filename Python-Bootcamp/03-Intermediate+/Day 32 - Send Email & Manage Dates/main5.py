# import smtplib
#
# my_email = "anderg8t@gmail.com"
# password = "abcd1234()"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
#
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="appbrewrytesting@yahoo.com",
#     msg="Hello")
# connection.close()

# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1993, month=2, day=8, hour=11)
# print(date_of_birth)
import random
import smtplib
import datetime as dt
import pandas as pd

my_email = "anderg8t@gmail.com"
password = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


