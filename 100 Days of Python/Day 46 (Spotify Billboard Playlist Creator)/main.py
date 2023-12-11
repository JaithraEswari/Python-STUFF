import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from bs4 import BeautifulSoup


input = input(
    'Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

url = f'https://www.billboard.com/charts/hot-100/{input}/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

text = soup.select('div ul li ul li h3')

all_songs = []

for songs in text:
    all_songs.append(songs.get_text())

# print(all_songs)

song_names = []

for song in all_songs:
    song = song.replace('\n', '').replace('\t', '')
    song_names.append(song)


# print(new_list)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='xxxxx',
                                               client_secret='xxxxx',
                                               redirect_uri='https://example.com',
                                               scope='playlist-modify-private',
                                               show_dialog=True,
                                               username='Paff._.Non',
                                               cache_path='token.txt'))

user_id = sp.current_user()['id']


song_uris = []
year = input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)

create_playlist = sp.user_playlist_create(user=user_id, name=f'{input} Billboard 100', public=False)
# print(create_playlist)
playlist_id = create_playlist['id']
# print(playlist_id)


add_tracks = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
