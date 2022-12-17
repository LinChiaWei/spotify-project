from secrets import *
import spotipy
import spotipy.util as util
from get_token import *


def find_songs_name(items):
    last50songs = []
    for i in range(len(items)):
        data = []
        current_track = items[i]['track']
        album = current_track['album']
        album_name = album['name']
        album_image_inf = album['images'][1]
        album_image_url = album_image_inf['url']
        artist_inf = album['artists']
        artist_name = artist_inf[0]['name']
        data.append(current_track['name'])
        data.append(album_image_url)
        last50songs.append(data)

    return last50songs
    
def take_second(list):
    return list[2]

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
        # print(song)
        song_name = song[0]
        song_image_url = song[1]
        if song_name in song_count:
            continue
        else:
            song_count.setdefault(song_name,[])
            song_count[song_name].append(0)
            song_count[song_name].append(song_image_url)


    for song in last50songs:
        song_name = song[0]
        song_count[song_name][0] +=1

    for item in song_count:
        dic = {}
        dic['SongName'] = item
        dic['Cover'] = song_count[item][1]
        dic['Count'] = song_count[item][0]
        data = [item, song_count[item][1] ,song_count[item][0]]
        song_list.append(data)

    song_list.sort(key=take_second,reverse=True)

    return song_list