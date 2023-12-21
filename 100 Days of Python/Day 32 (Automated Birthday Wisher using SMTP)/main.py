import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()

my_email = 'ejljaithra2002@gmail.com'
my_password = 'xxxxxxxxxxxxxxxx'


if day == 0:
    with open ('quotes.txt', 'r') as file:
        data = file.read()
        data_list = data.split('\n')
        random = random.choice(data_list)
        print(random)

  

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, 'ejljaithra2002@gmail.com' , f'Subject: Monday Motivation\n\n{random}')
