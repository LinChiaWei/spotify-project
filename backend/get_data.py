import spotipy
import spotipy.util as util
from secrets import *
from get_token import *



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

def take_second(list):
    return list[1]

def get_data():
    song_count = {}
    song_list = []
    token = get_token()
    headers = {"Authorization": "Bearer {}".format(token)}


    sp = spotipy.client.Spotify(headers)

    data = sp.current_user_recently_played(50)
    items =  data['items']


    last50songs = find_songs_name(items)


    for song in last50songs:
        song_count[song] = 0

    for song in last50songs:
        song_count[song] +=1

    for item in song_count:
        dic = {}
        dic['SongName'] = item
        dic['Count'] = song_count[item]
        data = [item, song_count[item]]
        song_list.append(data)

    song_list.sort(key=take_second,reverse=True)

    return song_list