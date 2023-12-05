import datetime as datetime
import requests
import numpy as np
import smtplib
import time

LATITUDE = 24.774265
LONGITUDE = 46.738586
MINUS = 5.0
PLUS = 5.0

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

longtitude = float(data['iss_position']['longitude'])
lantitude = float(data['iss_position']['latitude'])

iss_position = (longtitude, lantitude)

parameters = {
    'lat':LATITUDE,
    'lng':LONGITUDE,
    'formatted': 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

time_now = datetime.datetime.now()


is_on = True
while is_on:
    if LATITUDE - 5 <= lantitude <= LATITUDE + 5 and LONGITUDE - 5 <= longtitude <= LONGITUDE + 5:  
        if time_now.hour >= sunrise and time_now.hour <= sunset:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                my_email = 'ejljaithra2002@gmail.com'
                my_password = 'ddwz nsmp kjid amqi'
                connection.login(my_email, my_password)
                connection.sendmail(my_email, 'ejljaithra2002@gmail.com' , 'Subject:Look Up!!\n\nWe in the sky!!!')
        else:
            print("It's not a sunny day!")
    time.sleep(60)

# if longtitude in np.arange(LONGITUDE-MINUS, LONGITUDE+PLUS) and lantitude in np.arange(LATITUDE-MINUS, LATITUDE + PLUS):