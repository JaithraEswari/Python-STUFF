import datetime as dt
import requests

GENDER = 'Male'
WEIGHT_KG = '73'
HEIGHT_CM = '174'
AGE = '21'

NUTRIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY = 'https://api.sheety.co/603cda274a3d468f01c07d4658c44f67/copyOfMyWorkouts/workouts'

bearer_headers = {
    'Authorization' : 'Bearer mo+9V0#j&5P+D&I0gk6r'
} 

datetime = dt.datetime.now()

exercise_text = input("Tell me which exercises you did: ")

headers = {
'x-app-id' : '09926a66',
'x-app-key' : '00d6e9824aca59bd9084a3321607a540',
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NUTRIX_ENDPOINT,json=parameters, headers=headers)
response.raise_for_status()
data = response.json()


date = datetime.strftime('%d/%m/%Y') 
time = datetime.strftime('%H:%M:%S')
exercise = data['exercises'][0]['name'].title()
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

shetty = {
    'workout' : {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

exercise_response = requests.post(SHEETY,json=shetty, headers=bearer_headers)
exercise_response.raise_for_status()
print(exercise_response.text)

