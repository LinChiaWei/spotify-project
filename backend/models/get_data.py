import spotipy
import spotipy.util as util
from models.get_token import get_token
import time
import requests as rq

def find_songs_name(items):
    last50songs = []
    for i in range(len(items)):
        data = []
        current_track = items[i]['track']
        time = items[i]['played_at']
        album = current_track['album']
        album_name = album['name']
        album_image_inf = album['images'][0]
        album_image_url = album_image_inf['url']
        artist_inf = album['artists']
        artist_name = artist_inf[0]['name']
        artist_uri = artist_inf[0]['uri'].split(":", 2)[2]

        t = trans_time(time)

        data.append(current_track['name'])
        data.append(artist_name)
        data.append(album_image_url)
        data.append(t)
        data.append(artist_uri)
        last50songs.append(data)

    return last50songs
    
def sort_song(list):
    return list[4]

def sort_artist(list):
    return list[2]

def trans_time(t):
    t = t.split('T')
    date = t[0]
    time = t[1].split('.')[0]
    return date+" "+time

def get_artist_info(artist_id,headers):
    URL = 'https://api.spotify.com/v1/artists/{}'.format(artist_id)
    output = rq.get(URL,headers=headers).json()
    return output


def get_data():
    token = get_token()
    headers = {"Authorization": "Bearer {}".format(token['access_token'])}

    sp = spotipy.client.Spotify(headers)
    data = sp.current_user_recently_played(50)

    items =  data['items']

    last50songs = find_songs_name(items)

    for song in last50songs[:]:
        info = get_artist_info(song[-1],headers)
        song[-1] = info['images'][0]['url']
        song.append(info['genres'])

    return last50songs

def count_song(data):
    song_count = {}
    song_list = []
    for song in data:
        # print(song)
        song_name = song[0]
        artist_name =  song[1]
        artist_img_url =  song[2]
        song_image_url = song[3]
        if song_name in song_count:
            continue
        else:
            song_count.setdefault(song_name,[])
            song_count[song_name].append(0)
            song_count[song_name].append(artist_name)
            song_count[song_name].append(artist_img_url)
            song_count[song_name].append(song_image_url)

    for song in data:
        song_name = song[0]
        song_count[song_name][0] +=1

    for item in song_count:
        dic = {}
        dic['SongName'] = item
        dic['Artist'] = song_count[item][1]
        dic['ArtistImg'] = song_count[item][2]
        dic['Cover'] = song_count[item][3]
        dic['Count'] = song_count[item][0]
        data = [item, song_count[item][1],song_count[item][2],song_count[item][3],song_count[item][0]]
        song_list.append(data)

    song_list.sort(key=sort_song, reverse=True)
    
    return song_list

def count_artist(data):
    artist_count = {}
    artist_list = []
    for song in data:
        artist_name = song[1]
        artist_img_url =  song[2]
        if artist_name in artist_count:
            continue
        else:
            artist_count.setdefault(artist_name,[])
            artist_count[artist_name].append(0)
            artist_count[artist_name].append(artist_img_url)

    for song in data:
        artist_name = song[1]
        artist_count[artist_name][0] +=1

    for item in artist_count:
        dic = {}
        dic['Artist'] = item
        dic['ArtistImg'] = artist_count[item][1]
        dic['Count'] = artist_count[item][0]
        data = [item, artist_count[item][1],artist_count[item][0]]
        artist_list.append(data)

    artist_list.sort(key=sort_artist,reverse=True)
    
    return artist_list

def get_user_info():
    token = get_token()
    headers = {"Authorization": "Bearer {}".format(token['access_token'])}
    sp = spotipy.client.Spotify(headers)
    user = sp.me()
    l = []
    l.append(user['display_name'])
    l.append(user['images'][0]['url'] )

    return l
    






    
