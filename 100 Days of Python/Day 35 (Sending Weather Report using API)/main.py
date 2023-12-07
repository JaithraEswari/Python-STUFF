import requests
import smtplib

weather_param = {
    'lat': '13.082680',
    'lon': '80.270721',
    'appid': '0b6ad8ad52d9c469ca37e08f73686ea8',
    'cnt': '4'
}

FORECAST = 'https://api.openweathermap.org/data/2.5/forecast'

response = requests.get(FORECAST, weather_param)               
response.raise_for_status()
weather_data = response.json()

my_email = 'ejljaithra2002@gmail.com'
my_password = 'ddwz nsmp kjid amqi'

idlist = []

for i in weather_data['list']:
    id = i['weather'][0]['id']
    idlist.append(id)

if all(i < 700 for i in idlist):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, 'ejljaithra2002@gmail.com' , f'Subject: ALERT\n\nUmbrella Needed!!')