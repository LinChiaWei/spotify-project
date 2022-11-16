from secrets import *
import spotipy
import spotipy.util as util


def find_songs_name(items):
    last50songs = []
    for i in range(len(items)):
        current_track = items[i]['track']
        last50songs.append(current_track['name'])
        album = current_track['album']
        album_name = album['name']
        artist_inf = album['artists']
        artist_name = artist_inf[0]['name']

    return last50songs

def get_data():
    song_count = {}
    username = 'kevin880407'
    scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']
    token = util.prompt_for_user_token(username,scope,
                            client_id='a5f4717d6cbe43fea2cc354da04490b6',
                            client_secret='4eaba7b3f548455dae6a2ac83d8e39e1',
                            redirect_uri='http://localhost:8888/callback')

    headers = {"Authorization": "Bearer {}".format(token)}


    sp = spotipy.client.Spotify(headers)

    data = sp.current_user_recently_played(50)
    items =  data['items']


    last50songs = find_songs_name(items)


    for song in last50songs:
        song_count[song] = 0

    for song in last50songs:
        song_count[song]+=1

    return song_count