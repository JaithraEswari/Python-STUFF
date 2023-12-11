import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

text = soup.find_all(name='h3',class_='title')

all_movies = []

for movies in text:
    all_movies.append(movies.get_text())

reverse = list(reversed(all_movies))

with open("Top 100 Movies.txt", "w", encoding='utf-8') as f:
    for movie in reverse:
        f.write(f'{movie}\n')