##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import random
import pandas as pd

now = dt.datetime.now()
current_day = now.day
current_month = now.month
today = (current_month, current_day)


my_email = 'ejljaithra2002@gmail.com'
my_password = 'ddwz nsmp kjid amqi'


data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']):data_row  for (index,data_row) in data.iterrows()}


if today in birthdays_dict:
    letters = ['./letter_templates/letter_1.txt' ,'./letter_templates/letter_2.txt', './letter_templates/letter_3.txt']
    random_letter = random.choice(letters)
    birthday_person = birthdays_dict[today]
    with open(random_letter, 'r') as f:
        letter = f.read()
        letter = letter.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, birthday_person['email'] , f'Subject: Happy Birthday\n\n{letter}')
