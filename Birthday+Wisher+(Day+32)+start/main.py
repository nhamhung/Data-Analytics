import smtplib
import datetime as dt
import random

my_email = "udemy.hung.testemail@gmail.com"
password = "hung2241998"
yahoo_app_password = "ltkiznvedostifqy"

current_day_of_week = dt.datetime.now().weekday()

if current_day_of_week == 4:
    with open("quotes.txt", encoding="utf8") as quote_file:
        data = quote_file.readlines()
        quote = random.choice(data)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # transport layer security for secure connection
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="udemy.hungtestemail@yahoo.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}".encode(encoding="utf8"))
