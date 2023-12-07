import requests
import datetime as dt

pixela = 'https://pixe.la/v1/users'

TOKEN = '9q3vfhm7l33rus21toc8fndupq76itje'
USERNAME = 'jaithra'

today = dt.date.today()
date = today.strftime('%Y%m%d')

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(pixela, json=user_params)
# print(response.text)

graph = f'{pixela}/{USERNAME}/graphs'

graph_params = {
    'id': 'graph1',
    'name': 'Workout Graph',
    'unit': 'commit',
    'type': 'float',
    'color': 'ajisai',

}

headers = {
    'X-USER-TOKEN' : TOKEN,
}

# response = requests.post(url=graph, json=graph_params, headers=headers)
# print(response.text)

post_value = f'{pixela}/{USERNAME}/graphs/graph1'

post_value_params = {
    'date': date,
    'quantity': '1',

}

response = requests.post(post_value, json=post_value_params, headers=headers)
print(response.text)

update_value = f'{pixela}/{USERNAME}/graphs/graph1/{date}'

update_value_params = {
    'quantity': '1',

}

# response = requests.put(update_value, json=update_value_params, headers=headers)
# print(response.text)

delete_value = f'{pixela}/{USERNAME}/graphs/graph1/{date}'

# response = requests.delete(delete_value, headers=headers)

# print(response.text)