##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas as pd
import random
import smtplib

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row['month'], row['day']):row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    random_index = random.randint(1, 3)
    with open(f'./letter_templates/letter_{random_index}.txt') as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", f"{data['name'][0]}")
        print(letter_content)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    my_email = "udemy.hung.testemail@gmail.com"
    password = "hung2241998"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="udemy.hungtestemail@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{letter_content}")

# 4. Send the letter generated in step 3 to that person's email address.




